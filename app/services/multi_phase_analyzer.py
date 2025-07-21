# app/services/multi_phase_analyzer.py

import json
import re
import unicodedata
from pathlib import Path

from fastapi import HTTPException

from app.services.ai_analyzer import (
    MODEL_NAME,
    OLLAMA_URL,
    PROMPT_TEMPLATE,
    analyze_prompt,
)

DEBUG_FOLDER = Path(".debug_ollama")
DEBUG_FOLDER.mkdir(exist_ok=True)


def normalize_filename(name: str) -> str:
    # Reemplaza espacios y acentos para crear nombres seguros de archivo
    return (
        unicodedata.normalize("NFKD", name)
        .encode("ascii", "ignore")
        .decode("utf-8")
        .replace(" ", "_")
    )


async def analyze_multi_phase(markdown_plan: str) -> dict:
    fases = re.split(r"^##\s+Fase\s+\d+.*", markdown_plan, flags=re.MULTILINE)
    titulos = re.findall(r"^##\s+(Fase\s+\d+.*)", markdown_plan, flags=re.MULTILINE)

    if len(fases) <= 1:
        raise ValueError(
            "❌ No se detectaron fases en el markdown. Asegúrate de usar ## Fase X"
        )

    phases_result = []

    for i, (titulo, contenido) in enumerate(zip(titulos, fases[1:]), 1):
        print(f"\n📂 Analizando {titulo}...")

        prompt = PROMPT_TEMPLATE.format(plan_content=contenido)

        debug_filename = DEBUG_FOLDER / f"{normalize_filename(titulo)}.txt"
        debug_filename.write_text(prompt)

        try:
            parsed = await analyze_prompt(prompt)
            if "phases" in parsed:
                for phase in parsed["phases"]:
                    phase.setdefault("name", titulo)
                    phases_result.append(phase)
        except Exception as e:
            print(f"❌ Error en {titulo}: {str(e)}")
            raise HTTPException(
                status_code=500, detail=f"AI analysis failed for {titulo}: {str(e)}"
            )

    return {"phases": phases_result}
