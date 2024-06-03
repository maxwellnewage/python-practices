"""
PIL Demo
"""
from PIL import Image, ImageFilter


def process_image(filename):
    image = Image.open(f'media/{filename}')

    # Repeating the same task 10 times to increase the workload
    for _ in range(10):
        image = image.filter(ImageFilter.GaussianBlur(15))

    output_filename = f"processed_{filename}"
    image.save(f'media/{output_filename}')
