from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

MODEL_DIR = "./svg-model/checkpoint-8150"
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForCausalLM.from_pretrained(MODEL_DIR)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_svg(prompt, max_tokens=512):
    output = generator(
        prompt,
        max_new_tokens=max_tokens,
        do_sample=True,
        temperature=0.9,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.2,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.eos_token_id,
    )
    svg_code = output[0]["generated_text"]
    return svg_code

if __name__ == "__main__":
    prompt = input("📝 Ingresa el prompt (por ejemplo: 'outline icon of a rocket'): ")
    svg = generate_svg(prompt)


print("\n🖼️ SVG generado:\n")
print(svg)

with open("output.svg", "w", encoding="utf-8") as f:
    f.write(svg)