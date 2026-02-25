#!/bin/bash

echo "Starting Ollama server..."
ollama serve &

# Wait for Ollama server to be ready
echo "Waiting for Ollama server to start..."
while ! ollama list > /dev/null 2>&1; do
    sleep 1
done

echo "Ollama is ready, creating the model..."
ollama pull ${LOCAL_OLLAMA_MODEL}

echo "Model pulled successfully. Keeping server running..."
# Bring ollama serve to foreground or keep script alive
wait
