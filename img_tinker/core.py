import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from PIL import Image
from tqdm import tqdm
from .helpers import setup_logger

# Determine system's CPU count
max_workers = os.cpu_count() or 4

# Setup logger
logger = setup_logger('img_tinker')

def resize_image(input_path, output_path, sizes, format='WEBP'):
    """
    Resizes an image into multiple sizes and saves them in a specified format.

    Args:
        input_path (Path): Path to the input image file.
        output_path (Path): Directory where the resized images will be saved.
        sizes (list): List of sizes to resize the images to.
        format (str): Format of the output images.

    Raises:
        IOError: If the image cannot be opened or saved.
        Exception: For any other exceptions that occur during processing.
    """
    try:
        with Image.open(input_path) as img:
            for size in sizes:
                img_resized = img.resize((size, int(img.height * size / img.width)), Image.Resampling.LANCZOS)
                output_file = output_path / f"{input_path.stem}_{size}.{format.lower()}"
                img_resized.save(output_file, format=format)
                logger.info(f"Saved resized image: {output_file}")
    except IOError as e:
        logger.error(f"Cannot open/save file {input_path}: {e}")
        raise
    except Exception as e:
        logger.error(f"Error processing image {input_path}: {e}")
        raise

def process_directory(input_dir, output_dir, sizes, format='JPEG'):
    """
    Processes all images in a directory, resizing them into multiple sizes and saving them in a specified format.

    Args:
        input_dir (str): Directory containing images to process.
        output_dir (str): Directory to save processed images.
        sizes (list): List of sizes to resize the images to.
        format (str): Format of the output images.

    Raises:
        Exception: For any exceptions that occur during processing.
    """
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    image_files = list(input_dir.rglob('*'))
    image_files = [file for file in image_files if file.is_file() and file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.webp']]

    with ThreadPoolExecutor(max_workers=max_workers) as executor, tqdm(total=len(image_files), desc="Processing Images", unit="img") as progress:
        futures = {}
        for input_path in image_files:
            relative_path = input_path.relative_to(input_dir)
            output_path = output_dir / relative_path.parent
            output_path.mkdir(parents=True, exist_ok=True)
            future = executor.submit(resize_image, input_path, output_path, sizes, format)
            futures[future] = input_path

        for future in futures:
            try:
                future.result()  # Wait for the thread to complete and retrieve result
            except Exception as e:
                logger.error(f"A threading error occurred for {futures[future]}: {e}")
            finally:
                progress.update(1)
