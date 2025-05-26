# SVG AI Generator

Este proyecto entrena un modelo de lenguaje basado en Transformers (como GPT-2) para generar contenido SVG (íconos, logos, dibujos) a partir de un dataset personalizado. Utiliza Hugging Face Transformers y PyTorch.

---

## 🧠 Requisitos

- Python 3.10 o 3.11
- Linux o WSL (ideal)
- Entorno virtual (`venv`)
- Dataset en formato `.jsonl` (ej. `training_data.jsonl`)
- Internet (para descargar modelos preentrenados)

---

## 📦 Instalación

1. Clona este repositorio:

bash
git clone https://github.com/tuusuario/svgai.git
cd svgai
Crea y activa un entorno virtual:

bash
python3 -m venv venv
source venv/bin/activate
Instala dependencias:

bash
pip install -r requirements.txt
O si no tienes requirements.txt:

bash
pip install torch transformers datasets accelerate
⚠️ Para soporte de GPU con CUDA (opcional):

bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
📁 Estructura esperada
bash
svgai/
├── train_svg_model.py
├── training_data.jsonl
├── logs/              # Se crea automáticamente durante entrenamiento
├── svg-model/         # Se crea automáticamente durante entrenamiento
└── venv/              # Entorno virtual, lo creas tú
ℹ️ Los directorios venv/, logs/ y svg-model/ han sido eliminados del repositorio para ahorrar espacio. Se generarán automáticamente al correr el proyecto localmente.

🏋️ Entrenamiento
Ejecuta el script principal:

bash
python train_svg_model.py
Este iniciará el fine-tuning del modelo en tu dataset personalizado.

Argumentos usados en el Trainer:
output_dir="./svg-model"

overwrite_output_dir=True

num_train_epochs=50

per_device_train_batch_size=2

save_steps=500

save_total_limit=2

logging_steps=100

logging_dir="./logs"

fp16=True

report_to="none"

🔄 Reanudar desde Checkpoint
Si pausas el entrenamiento (ej. con Ctrl+C), puedes reanudarlo:

Edita el script:

python
trainer.train(resume_from_checkpoint=True)
Y vuelve a correr:

bash
python train_svg_model.py
📤 Exportar el modelo entrenado
Después del entrenamiento, el modelo se guarda en ./svg-model. Puedes usarlo así:

python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("./svg-model")
model = AutoModelForCausalLM.from_pretrained("./svg-model")
🛠 Dataset esperado
Archivo .jsonl con líneas como:

json
{"prompt": "<svg ...>...</svg>"}
Cada línea representa un SVG válido como texto.

✅ Recomendaciones
Usa batch size pequeño si no tienes GPU potente.

Usa fp16=True solo si tu GPU lo soporta.

Haz pruebas con 1–2 epochs antes de un entrenamiento largo.

🧑‍💻 Autor
Desarrollado por [Tu Nombre o Alias]

📄 Licencia
MIT
