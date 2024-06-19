import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from PIL import Image
from tqdm import tqdm
from .helpers import setup_logger

# Determine the number of max_workers based on the system's CPU count
# max_workers = os.cpu_count() or 4

# logger = setup_logger('img_tinker')

# def resize_image(input_path, output_path, sizes, format='JPEG'):

# def process_directory(input_dir, output_dir, sizes, format='JPEG'):
