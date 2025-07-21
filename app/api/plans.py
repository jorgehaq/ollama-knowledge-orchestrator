# app/api/plans.py

from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.file_manager import save_plan_file

router = APIRouter(prefix="/api/plans", tags=["Plans"])


@router.post("/")
async def upload_plan(file: UploadFile = File(...)):
    if not file.filename.endswith(".md"):
        raise HTTPException(status_code=400, detail="Only .md files are allowed")

    plan_id = str(uuid4())
    try:
        await save_plan_file(file, plan_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"plan_id": plan_id, "filename": file.filename}
