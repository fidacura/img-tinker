# img-tinker

`img-tinker` is a simple Python CLI tool designed to efficiently process and resize images within a directory; it supports multiple image sizes and formats, with a focus on simplicity and performance.

## Features

- Batch process entire directories of images.
- Resize images to multiple specified sizes.
- Convert images to different formats.

## Installation

To use `img-tinker`, follow these steps:

1. Clone this repository:

```bash
   git clone https://github.com/yourusername/img-tinker.git
```

2. Navigate to project directory

```bash
    cd img-tinker
```

3. Install the required dependencies:

```bash
    pip install -r requirements.txt
```

3. Install img-tinker as a package:

```bash
    pip install .
```

## Usage

To run `img-tinker`, you need to specify the input and output directories (if the output directory doesn't exist, it will be created), the sizes to resize the images to, and optionally the image format (with a default option of WEBP for optimized performance).

### Basic Command Structure

```bash
    img-tinker input_dir output_dir --sizes 320 480 640 --format WEBP
```

### Examples

#### Resize and Convert to Default Format (WEBP)

Resize images in the photos directory to widths of 320px, 480px, and 640px and save them in the resized_photos directory. Since no format is specified, images will be converted to WEBP by default.

```bash
    img-tinker photos resized_photos --sizes 320 480 640
```

#### Resize and Specify Format

Resize images in the photos directory to widths of 800px and 1200px, convert them to JPEG, and save in the resized_photos directory.

```bash
    img-tinker photos resized_photos --sizes 800 1200 --format JPEG
```
