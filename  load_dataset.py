from datasets import load_dataset

def main():
    dataset = load_dataset(
        "json",
        data_files="training_data.jsonl",
        split="train"
    )

print(f"✅ Dataset cargado: {len(dataset)} ejemplos")
print(dataset[0])  # muestra el primer ejemplo
if name == "main":
    main()
