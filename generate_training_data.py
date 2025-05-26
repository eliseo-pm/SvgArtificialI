import json
import os

INPUT_FILE = "dataset.json"
OUTPUT_FILE = "training_data.jsonl"

def create_svg_string(paths):
    svg_header = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 256 256'>"
    path_elements = "".join([f"<path d='{d}'/>" for d in paths])
    svg_footer = "</svg>"
    return svg_header + path_elements + svg_footer

def main():
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        processed_count = 0
        skipped_count = 0
        
        with open(OUTPUT_FILE, "w", encoding="utf-8") as out_file:
            for item in data:
                try:
                    # Verificar que existan las claves necesarias
                    if "paths" not in item:
                        print(f"⚠️ Advertencia: Elemento sin 'paths' - {item.get('file_name', 'desconocido')}")
                        skipped_count += 1
                        continue
                    
                    # Usar tags si existen, sino usar file_name o valor por defecto
                    tags = item.get("tags", [])
                    if not tags:
                        tags = [item.get("file_name", "icon").replace(".svg", "").replace("_", " ")]
                    
                    prompt = " ".join(tags)
                    svg_code = create_svg_string(item["paths"])
                    
                    record = {
                        "prompt": prompt,
                        "completion": svg_code
                    }
                    out_file.write(json.dumps(record) + "\n")
                    processed_count += 1
                
                except Exception as e:
                    print(f"❌ Error procesando elemento: {str(e)}")
                    skipped_count += 1
                    continue
        
        print(f"✅ Proceso completado. Generados {processed_count} ejemplos, omitidos {skipped_count}")
    
    except Exception as e:
        print(f"❌ Error crítico: {str(e)}")
        raise

if __name__ == "__main__":
    main()
