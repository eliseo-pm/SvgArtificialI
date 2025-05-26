from datasets import load_dataset
from transformers import AutoTokenizer
import os

def main():
    # Carga tu dataset .jsonl
    dataset = load_dataset(
        "json",
        data_files="training_data.jsonl",
        split="train"
    )

    # Imprime un ejemplo para verificar las claves disponibles
    print(f"Ejemplo del dataset: {dataset[0]}")

    # Elige el tokenizer (puedes cambiar a otro modelo como "EleutherAI/gpt-neo-125M" si prefieres)
    tokenizer = AutoTokenizer.from_pretrained("gpt2")

    # Asegúrate de que tiene un token de padding
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Función para tokenizar
    def tokenize_function(example):
        # Cambia "text" por la clave correcta basada en la estructura del dataset
        return tokenizer(example["prompt"], truncation=True, padding="max_length", max_length=512)

    # Tokeniza el dataset
    try:
        tokenized_dataset = dataset.map(tokenize_function, batched=True)
    except KeyError as e:
        print(f"❌ Error: La clave '{e.args[0]}' no existe en el dataset. Verifica la estructura del dataset.")
        return

    # Guarda el dataset tokenizado en disco
    output_dir = "tokenized"
    os.makedirs(output_dir, exist_ok=True)
    tokenized_dataset.save_to_disk(output_dir)
    print(f"✅ Dataset tokenizado guardado en: {output_dir}")

if __name__ == "__main__":
    main()
