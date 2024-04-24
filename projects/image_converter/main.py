"""
Pillow Image Converter
"""

from PIL import Image


def convert_webp_to_jpg(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            img.convert("RGB").save(output_path, "JPEG")
        print(f"La imagen ha sido convertida y guardada como '{output_path}'")
    except IOError as e:
        print(f"Error al convertir la imagen: {e}")


if __name__ == "__main__":
    convert_webp_to_jpg('avatar.webp', 'avatar.jpg')
