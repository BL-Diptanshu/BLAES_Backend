from app.config.logger import AppLogger
import boto3
from botocore.exceptions import ClientError
import os
import io
from dotenv import load_dotenv

logger = AppLogger.get_logger()

load_dotenv()

S3_BUCKET = os.getenv("AWS_BUCKET")
s3_client = boto3.client("s3")


def get_s3_client():
    return boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION")
    )

def upload_to_s3(bucket: str, key: str, content: str) -> str:
    s3 = get_s3_client()
    try:
        s3.put_object(Bucket=bucket, Key=key, Body=content.encode("utf-8"))
        return key
    except ClientError as e:
        raise Exception(f"Failed to upload to S3: {e}")


def create_s3_folders(bucket: str, folders: list[str]) -> None:
    s3 = get_s3_client()
    for folder in folders:
        if not folder.endswith("/"):
            folder += "/"
        s3.put_object(Bucket=bucket, Key=folder)


def upload_to_s3(payload: dict) -> list[dict]:
    """
    Upload EACH question-answer pair as a separate file to S3.
    Returns a list of objects:
    [
        {
            "question_id": "...",
            "user_id": "...",
            "url": "..."
        }
    ]
    """

    logger.info(f"S3_BUCKET --> {S3_BUCKET}")
    logger.info("Uploading multiple Q/A files to S3...")

    # -------------------------------
    # Build folder path (skip empty fields)
    # -------------------------------
    folder_parts = [
        "answers",
        payload.get("coe_name", "DEFAULT_COE"),
        payload.get("program_name", "DEFAULT_PROG"),
        payload.get("semester", "DEFAULT_SEM"),
        payload.get("user_id", "UNKNOWN_USER"),
        payload.get("module", "DEFAULT_MODULE")
    ]

    # Add subtopic only if valid
    topic_val = payload.get("submodule")
    if topic_val and isinstance(topic_val, str) and topic_val.strip():
        folder_parts.append(topic_val.strip())


    # Add question type as the last folder
    folder_parts.append(payload.get("question_type", "UNKNOWN_TYPE"))

    folder_path = "/".join(folder_parts)

    # -------------------------------
    # Create S3 folders if not exist
    # -------------------------------
    for i in range(1, len(folder_parts) + 1):
        prefix = "/".join(folder_parts[:i]) + "/"
        s3_client.put_object(Bucket=S3_BUCKET, Key=prefix)

    # -------------------------------
    # Upload each QA item
    # -------------------------------
    uploaded_responses = []
    content_list = payload.get("content", [])

    for index, qa in enumerate(content_list):

        question_id = qa.get("question_id", f"Q{index+1}")
        question_text = qa.get("question_text", "")
        answer_text = qa.get("answer_text", "")

        file_text = (
            f"QUESTION ID: {question_id}\n"
            f"QUESTION:\n{question_text}\n\n"
            f"ANSWER:\n{answer_text}\n"
        )
        file_obj = io.BytesIO(file_text.encode("utf-8"))

        file_name = f"{question_id}_{payload.get('question_type', 'UNK')}.txt"
        s3_key = f"{folder_path}/{file_name}"

        # Upload
        s3_client.upload_fileobj(file_obj, S3_BUCKET, s3_key)

        file_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{s3_key}"

        uploaded_responses.append({
            "question_id": question_id,
            "user_id": payload.get("user_id"),
            "url": file_url
        })

        logger.info(f"Uploaded: {question_id} → {file_url}")

    logger.info(f"Uploaded {len(uploaded_responses)} files")
    return uploaded_responses

