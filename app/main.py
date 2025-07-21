# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import analyze, plans

app = FastAPI(title="AI Knowledge Orchestrator")

# CORS para desarrollo local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze.router)
app.include_router(plans.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
