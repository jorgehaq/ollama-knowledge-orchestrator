#!/bin/bash

echo "🛑 Buscando proceso de desarrollo (uvicorn)..."
PID=$(ps aux | grep 'uvicorn app.main:app' | grep -v grep | awk '{print $2}')

if [ -z "$PID" ]; then
  echo "⚠️  No se encontró un proceso activo de uvicorn."
else
  echo "🔪 Matando proceso uvicorn (PID $PID)..."
  kill $PID
  echo "✅ Servidor detenido."
fi
