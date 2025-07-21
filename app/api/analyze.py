# app/api/analyze.py

from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.schemas.plan_analysis import PlanStructure
from app.services.ai_analyzer import analyze_plan

router = APIRouter(prefix="/api/analyze", tags=["Analyzer"])


@router.get("/{plan_id}", response_model=PlanStructure)
async def analyze_uploaded_plan(plan_id: str):
    file_path = Path("uploaded_plans") / f"{plan_id}.md"

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Plan file not found")

    markdown_text = file_path.read_text()

    result = await analyze_plan(markdown_text)
    return PlanStructure(**result)
