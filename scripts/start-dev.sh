#!/bin/bash

echo "🚀 Activando entorno virtual..."
source .venv/bin/activate

if [ ! -f requirements.txt ]; then
    echo "📦 Instalando dependencias..."
    pip install fastapi uvicorn python-multipart
    pip freeze > requirements.txt
else
    echo "📦 Verificando dependencias..."
    pip install -r requirements.txt
fi

echo "✅ Entorno listo. Iniciando servidor..."
uvicorn app.main:app --reload
