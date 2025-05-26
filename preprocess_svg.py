import os
import json
from bs4 import BeautifulSoup

svg_folder = "icons"  # carpeta donde están los SVG descomprimidos
output_file = "cleaned_data.json"
metadata_file = "metadata.json"

def clean_svg(svg_content):
    soup = BeautifulSoup(svg_content, "xml")
    # Eliminar metadatos innecesarios
    for tag in soup.find_all(["metadata", "desc", "title"]):
        tag.decompose()
    return str(soup.svg)

data = []

with open(metadata_file, "r") as f:
    metadata = json.load(f)

for item in metadata:
    file_path = os.path.join(svg_folder, item["file_name"])
    if os.path.exists(file_path):
        with open(file_path, "r") as svg_file:
            raw_svg = svg_file.read()
            cleaned_svg = clean_svg(raw_svg)
            data.append({
                "svg": cleaned_svg,
                "tags": item["tags"],
                "style": item["style"],
                "author": item["author"]
            })

with open(output_file, "w") as out:
    json.dump(data, out, indent=2)

print(f"Procesados {len(data)} SVGs en {output_file}")

