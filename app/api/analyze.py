# app/api/analyze.py

from pathlib import Path
from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.schemas.plan_analysis import PlanStructure
from app.services.multi_phase_analyzer import analyze_multi_phase

router = APIRouter(prefix="/api/analyze", tags=["Analyzer"])


@router.get("/{plan_id}", response_model=PlanStructure)
async def analyze_uploaded_plan(plan_id: UUID):
    file_path = Path("uploaded_plans") / f"{plan_id}.md"

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Plan file not found")

    markdown_text = file_path.read_text()

    result = await analyze_multi_phase(markdown_text)  # 👈 cambio aquí
    return PlanStructure(**result)
