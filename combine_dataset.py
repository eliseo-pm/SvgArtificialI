import os
import json

INPUT_DIR = "cleaned"
output = []

for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".json"):
        with open(os.path.join(INPUT_DIR, filename), "r", encoding="utf-8") as f:
            data = json.load(f)
            output.append(data)

with open("dataset.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)

print("✅ Dataset combinado creado en dataset.json")

