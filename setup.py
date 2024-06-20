from setuptools import setup, find_packages

setup(
    name='img-tinker',
    version='0.1',
    description='A tool for resizing images to multiple sizes and formats.',
    url='https://github.com/fidacura/img-tinker',
    author='fidacura',
    author_email='hello@fidacura.xyz',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'img-tinker=scripts.process_images:main',
        ],
    },
    install_requires=[
        'Pillow',
        'tqdm',
    ],
    python_requires='>=3.6',
)
