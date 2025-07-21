# app/services/ai_analyzer.py

import json

import httpx
from fastapi import HTTPException

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"  # Cambia si deseas otro modelo

PROMPT_TEMPLATE = """
You are a backend engineering assistant.

Your task is to extract a learning roadmap from the following markdown plan.
Follow this exact structure (JSON only):

{{
  "phases": [
    {{
      "name": "Fase 1",
      "sprints": [
        {{
          "title": "Sprint 1",
          "goals": [
            "Write goal 1",
            "Write goal 2"
          ]
        }}
      ]
    }}
  ]
}}

Rules:
- Use each markdown H2 (##) as a new phase name.
- Use each bullet point (-) as an individual goal.
- Group goals into logical sprints of 2–3 goals each.
- Use the bullet point text directly as-is.

ONLY RETURN JSON. No comments. No markdown. No explanations.

### MARKDOWN PLAN:
{plan_content}
"""


async def analyze_prompt(prompt: str) -> dict:
    payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}

    print("📤 Sending request to Ollama with payload:")
    print(payload)

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()

        raw_response = result.get("response", "").strip()
        print("📥 Raw response:")
        print(raw_response[:300])

        return json.loads(raw_response)

    except Exception as e:
        print("ERROR:")
        print(str(e))
        raise HTTPException(status_code=500, detail=f"AI analysis failed: {str(e)}")


async def analyze_plan(markdown_text: str) -> dict:
    prompt = PROMPT_TEMPLATE.format(plan_content=markdown_text)
    return await analyze_prompt(prompt)
