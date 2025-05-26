import json

path = "training_data.jsonl"
with open(path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        line = line.strip()
        if line:
            try:
                json.loads(line)
            except json.JSONDecodeError as e:
                print(f"Error en línea {i}: {e}")

