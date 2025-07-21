# app/schemas/plan_analysis.py

from typing import List

from pydantic import BaseModel


class Sprint(BaseModel):
    title: str
    goals: List[str]


class Phase(BaseModel):
    name: str
    sprints: List[Sprint]


class PlanStructure(BaseModel):
    phases: List[Phase]
