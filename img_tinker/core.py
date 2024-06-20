from pathlib import Path
from PIL import Image
from tqdm import tqdm

def resize_image(input_path, output_path, sizes, format='WEBP'):
    with Image.open(input_path) as img:
        for size in sizes:
            img_resized = img.resize((size, int(img.height * size / img.width)), Image.Resampling.LANCZOS)
            output_file = output_path / f"{input_path.stem}_{size}.{format.lower()}"
            img_resized.save(output_file, format=format)


def process_directory(input_dir, output_dir, sizes, format='JPEG'):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    image_files = list(input_dir.rglob('*'))
    image_files = [file for file in image_files if file.is_file() and file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.webp']]