import os
from typing import Optional

MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

TEXT_EXTENSIONS = {
    ".py", ".js", ".ts", ".java", ".c", ".cpp",
    ".cs", ".go", ".rs", ".rb", ".php",
    ".html", ".css", ".json", ".yml", ".yaml",
    ".md", ".txt", ".sql"
}


def is_binary_file(filepath: str) -> bool:
    try:
        with open(filepath, "rb") as f:
            chunk = f.read(1024)
            return b"\0" in chunk
    except Exception:
        return True


def is_large_file(filepath: str) -> bool:
    return os.path.getsize(filepath) > MAX_FILE_SIZE_BYTES


def is_text_file(filepath: str) -> bool:
    _, ext = os.path.splitext(filepath.lower())
    return ext in TEXT_EXTENSIONS


def safe_read_text(filepath: str) -> Optional[str]:
    for encoding in ("utf-8", "ascii", "latin-1"):
        try:
            with open(filepath, "r", encoding=encoding) as f:
                return f.read()
        except Exception:
            continue
    return None


def is_git_submodule(dir_path: str) -> bool:
    return os.path.exists(os.path.join(dir_path, ".git"))