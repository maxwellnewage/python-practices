"""
Pillow Image Converter
"""

from PIL import Image


def convert_webp_to_jpg(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            # Convierte a sRGB si es posible
            if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
                alpha = img.convert('RGBA').split()[-1]
                bg = Image.new("RGB", img.size, (255, 255, 255) + (255,))
                bg.paste(img, mask=alpha)
                img = bg
            else:
                img = img.convert("RGB")

            # Eliminar metadata
            img.info = {}

            # Guardar con calidad alta, ajusta según necesidades.
            img.save(output_path, "JPEG", quality=70)
    except IOError as e:
        print(f"Error al convertir la imagen: {e}")


if __name__ == "__main__":
    convert_webp_to_jpg('avatar.webp', 'avatar.jpg')
