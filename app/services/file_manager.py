from pathlib import Path

from fastapi import UploadFile

UPLOAD_DIR = Path("uploaded_plans")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


async def save_plan_file(file: UploadFile, plan_id: str):
    file_path = UPLOAD_DIR / f"{plan_id}.md"
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
