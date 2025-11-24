from PIL import Image, ImageOps
import os

# Obtener la ruta del directorio donde está el script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Configuración de rutas relativas
INPUT_FOLDER = os.path.join(BASE_DIR, "inicial")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "result")
# Asumimos que la marca de agua está en la carpeta watermark
WATERMARK_PATH = os.path.join(BASE_DIR, "watermark", "sample.png")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

watermark = Image.open(WATERMARK_PATH).convert("RGBA")

for filename in os.listdir(INPUT_FOLDER):
    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    img_path = os.path.join(INPUT_FOLDER, filename)

    img = Image.open(img_path)
    img = ImageOps.exif_transpose(img)
    img = img.convert("RGBA")

    if img.width > img.height:
        # Horizontal: 20% del ancho
        factor = img.width * 0.2 / watermark.width
    else:
        # Vertical: 50% del ancho
        factor = img.width * 0.5 / watermark.width

    new_size = (int(watermark.width * factor), int(watermark.height * factor))
    wm_resized = watermark.resize(new_size, Image.LANCZOS)

    # Centro abajo con 20px de margen
    margin_bottom = 20
    x = (img.width - wm_resized.width) // 2
    y = img.height - wm_resized.height - margin_bottom

    img_with_wm = img.copy()
    img_with_wm.alpha_composite(wm_resized, (x, y))

    output_path = os.path.join(OUTPUT_FOLDER, filename)
    img_rgb = img_with_wm.convert("RGB")
    img_rgb.save(output_path, quality=90)

    print(f"Procesado: {filename}")

print("Listo. Todas las imágenes fueron procesadas.")