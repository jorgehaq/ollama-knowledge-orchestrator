# app/services/ai_analyzer.py

import json

import httpx
from fastapi import HTTPException

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama2"  # O el modelo que tengas cargado en Ollama
MODEL_NAME = "mistral"  # O el modelo que tengas cargado en Ollama

PROMPT_TEMPLATE = """
You are an AI backend assistant.

Read the following markdown learning plan and return only a strict JSON like this:

{{
  "phases": [
    {{
      "name": "Fase 1",
      "sprints": [
        {{
          "title": "Sprint 1",
          "goals": [
            "Learn FastAPI"
          ]
        }}
      ]
    }}
  ]
}}

Return only valid JSON. No explanations. No Markdown. Just the JSON object.

### PLAN:
{{plan_content}}
"""


async def analyze_plan(markdown_text: str) -> dict:
    prompt = PROMPT_TEMPLATE.format(plan_content=markdown_text)

    payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}

    try:
        async with httpx.AsyncClient() as client:
            print("📤 Sending request to Ollama with payload:")
            print(payload)
            response = await client.post(OLLAMA_URL, json=payload, timeout=30)

        response.raise_for_status()

        if not response.text.strip():
            print("❌ Ollama returned an empty response.")
            raise HTTPException(
                status_code=500, detail="Ollama returned empty response"
            )

        print("📤 Raw HTTP response text:")
        print(response.text)
        result = response.json()

        raw_response = result.get("response", "").strip()

        print("📥 Raw response:")
        print(raw_response)  # para no imprimir todo

        try:
            parsed = json.loads(raw_response)

        except json.JSONDecodeError:
            print("❌ Failed to parse JSON from Ollama:")
            print(response.text)
            print("❌ Ollama returned non-JSON:")
            print(raw_response)
            raise HTTPException(status_code=500, detail="AI returned invalid JSON")

        return parsed

    except Exception as e:
        print("ERROR:", str(e))
        raise HTTPException(status_code=500, detail=f"AI analysis failed: {str(e)}")
