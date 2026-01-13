from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import tempfile
import os
import subprocess
import threading
import asyncio
from queue import Queue
from app.config.logger import AppLogger

logger = AppLogger.get_logger()
java_router = APIRouter()


@java_router.websocket("/ws/execute_java/")
async def execute_java(websocket: WebSocket):
    await websocket.accept()
    temp_dir = tempfile.mkdtemp()
    java_path = os.path.join(temp_dir, "Main.java")

    try:
        #1 Receive Java code
        data = await websocket.receive_json()
        code = data.get("code")
        if not code:
            await websocket.send_text("No code provided")
            return

        with open(java_path, "w") as f:
            f.write(code)

        logger.info("Java code received successfully")

        #2 Compile Java code
        compile_proc = subprocess.run(
            ["javac", java_path],
            cwd=temp_dir,
            capture_output=True,
            text=True
        )

        if compile_proc.returncode != 0:
            await websocket.send_text(f"Compilation Error:\n{compile_proc.stderr}")
            return
        logger.info("Code compiled successfully")

        #3 Run Java program using Popen
        process = subprocess.Popen(
            ["java", "Main"],
            cwd=temp_dir,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=1,
            text=True
        )

        logger.info("Java program started successfully")

        #4 Get main asyncio loop
        loop = asyncio.get_running_loop()

        # Queue to safely send input to Java process
        input_queue = Queue()

        def write_input():
            while True:
                line = input_queue.get()
                if line is None:
                    break
                process.stdin.write(line + "\n")
                process.stdin.flush()

        input_thread = threading.Thread(target=write_input)
        input_thread.start()

        #5 Stream stdout/stderr
        def stream_output(pipe, tag="", loop=None):
            try:
                for line in iter(pipe.readline, ''):
                    if loop:
                        asyncio.run_coroutine_threadsafe(
                            websocket.send_text(f"{tag}{line}"), loop
                        )
            except Exception as e:
                logger.exception(f"Error streaming {tag} output: {e}")

        stdout_thread = threading.Thread(target=stream_output, args=(process.stdout, "", loop))
        stderr_thread = threading.Thread(target=stream_output, args=(process.stderr, "ERR: ", loop))
        stdout_thread.start()
        stderr_thread.start()

        #6 Receive input from frontend
        try:
            while True:
                msg = await websocket.receive_text()
                if msg.lower() == "exit":
                    process.terminate()
                    await websocket.send_text("\nProgram terminated.\n")
                    break
                input_queue.put(msg)
        except WebSocketDisconnect:
            process.terminate()

        # 7 Clean up
        input_queue.put(None)
        process.wait()
        input_thread.join()
        stdout_thread.join()
        stderr_thread.join()
        await websocket.send_text(f"\nProgram exited with code {process.returncode}\n")

    except Exception as e:
        await websocket.send_text(f"Error: {e}")
        logger.exception("Error executing Java code")
    finally:
        await websocket.close()
        for f in os.listdir(temp_dir):
            os.remove(os.path.join(temp_dir, f))
        os.rmdir(temp_dir)
