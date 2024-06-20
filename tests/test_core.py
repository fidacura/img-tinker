import sys
import os
import unittest
from pathlib import Path
from PIL import Image, UnidentifiedImageError
import tempfile
import shutil

# Ensure the root directory is in sys.path before importing img_tinker modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from img_tinker.core import resize_image, process_directory

class TestImageProcessing(unittest.TestCase):
    def setUp(self):
        # Setup a temporary directory
        self.test_dir = tempfile.mkdtemp()
        self.output_dir = tempfile.mkdtemp()
        # Create a test image file
        self.test_image_path = Path(self.test_dir) / "test_image.jpg"
        img = Image.new('RGB', (100, 100), color='red')
        img.save(self.test_image_path)

    def tearDown(self):
        # Remove temporary directory after test
        shutil.rmtree(self.test_dir)
        shutil.rmtree(self.output_dir)

    def test_resize_image(self):
        # Test the resize_image functionality
        resize_image(self.test_image_path, Path(self.output_dir), [50, 75], 'JPEG')
        resized_paths = list(Path(self.output_dir).glob('*'))
        self.assertEqual(len(resized_paths), 2)  # Check if two files are created

    def test_process_directory(self):
        # Test the process_directory functionality
        process_directory(self.test_dir, self.output_dir, [50], 'JPEG')
        processed_files = list(Path(self.output_dir).glob('**/*'))
        self.assertEqual(len(processed_files), 1)  # Should handle 1 image

    def test_error_handling(self):
        # Introduce an error scenario
        with open(self.test_image_path, 'wb') as corrupt_file:
            corrupt_file.write(b'notanimage')
        with self.assertRaises(UnidentifiedImageError):
            resize_image(self.test_image_path, Path(self.output_dir), [50], 'JPEG')

if __name__ == '__main__':
    unittest.main()
