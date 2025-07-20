# 🧠 AI Knowledge Orchestrator

An intelligent backend automation system that transforms markdown-based master plans into structured, study-ready content using local AI models. Built with FastAPI, modular architecture, and optimized for cloud deployment.

---

## 🚀 Project Goals

- Automate personal learning material generation using AI
- Showcase a modern backend architecture with FastAPI
- Enable cloud-native deployment with clean DevOps
- Serve as a public portfolio project for international technical interviews

---

## 🧱 Tech Stack

| Layer         | Tools                      |
|---------------|-----------------------------|
| Backend       | Python, FastAPI, Uvicorn    |
| AI Local      | Ollama (planned in Sprint 2)|
| Storage       | FileSystem, PostgreSQL (later) |
| DevOps        | Docker, GitHub Actions (planned) |
| Cloud         | GCP Cloud Run + Cloud SQL (Sprint 4) |
| Code Quality  | Pre-commit (Black, Flake8, Isort) |

---

## ⚙️ Local Development

```bash
# Clone the repo
git clone https://github.com/your_user/ai-knowledge-orchestrator.git
cd ai-knowledge-orchestrator

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Activate pre-commit (once)
pre-commit install

# Start server
./start-dev.sh

---

## 📂 Project Structure

```bash
app/
├── main.py            # FastAPI entrypoint
├── api/               # Routers (e.g., plans, health)
├── services/          # File storage logic
├── schemas/           # (coming soon)
├── core/              # Config and utilities
tests/
├── api/               # Endpoint tests
├── services/          # Internal logic tests
docs/
├── sprints/           # Sprint-based documentation
```

---

## ✅ Completed Milestones

-  Sprint 1 – FastAPI backend foundation

-  Sprint 2 – AI Analyzer (Ollama integration)

-  Sprint 3 – WebSocket + Web UI

-  Sprint 4 – GCP Cloud Deployment

-  Sprint 5 – Interview Content Generator


---

## 🧑‍💻 Author

**Jorge H.A.Q.**
Senior Backend Engineer | AI Automation Enthusiast
_Transitioning to international remote roles with FastAPI + GCP + AI integration_
📍 Colombia 🇨🇴

---

## 📜 License

MIT

```

---
