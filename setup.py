from setuptools import setup, find_packages

setup(
    name='img-tinker',
    version='0.1.0',
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
