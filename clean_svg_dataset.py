import os
import json
from bs4 import BeautifulSoup
from xml.dom import minidom

INPUT_DIR = "icons"
OUTPUT_DIR = "cleaned"

def extract_paths(svg_content):
    soup = BeautifulSoup(svg_content, "xml")
    paths = soup.find_all("path")
    path_data = []
    for path in paths:
        d = path.get("d")
        if d:
            path_data.append(d)
    return path_data

def normalize_viewbox(svg_content):
    soup = BeautifulSoup(svg_content, "xml")
    svg_tag = soup.find("svg")
    if not svg_tag:
        return svg_content
    svg_tag["viewBox"] = "0 0 256 256"
    svg_tag["width"] = "256"
    svg_tag["height"] = "256"
    return str(soup)

def clean_svg_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        svg_content = f.read()
    
    # Normalize viewBox
    svg_content = normalize_viewbox(svg_content)

    # Extract path data
    path_commands = extract_paths(svg_content)

    # Save to JSON
    json_output = {
        "file_name": os.path.basename(input_path),
        "paths": path_commands
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(json_output, f, indent=2)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".svg"):
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, filename.replace(".svg", ".json"))
            clean_svg_file(input_path, output_path)
            print(f"✔️ Procesado: {filename}")

if __name__ == "__main__":
    main()
