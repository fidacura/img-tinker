import argparse
from img_tinker.core import process_directory

def main():
    parser = argparse.ArgumentParser(description="Process images in a directory.")
    parser.add_argument('input_dir', type=str, help='Directory containing images to process')
    parser.add_argument('output_dir', type=str, help='Directory to save processed images')
    parser.add_argument('--sizes', nargs='+', type=int, help='List of sizes to resize images to, e.g. --sizes 320 480 640')
    parser.add_argument('--format', type=str, default='WEBP', help='Format of the output images')
    args = parser.parse_args()
    
    if not args.sizes:
        parser.error("The --sizes parameter requires at least one size.")
    
    process_directory(args.input_dir, args.output_dir, args.sizes, args.format)

if __name__ == '__main__':
    main()
