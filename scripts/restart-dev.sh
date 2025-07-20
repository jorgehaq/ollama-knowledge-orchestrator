#!/bin/bash

echo "🔄 Reiniciando entorno de desarrollo..."

# Paso 1: Detener proceso anterior
PID=$(ps aux | grep 'uvicorn app.main:app' | grep -v grep | awk '{print $2}')

if [ -n "$PID" ]; then
  echo "🛑 Deteniendo proceso anterior (PID $PID)..."
  kill $PID
else
  echo "⚠️  No hay proceso uvicorn activo."
fi

# Paso 2: Activar entorno y reiniciar servidor
echo "🚀 Iniciando servidor..."
source .venv/bin/activate
uvicorn app.main:app --reload
