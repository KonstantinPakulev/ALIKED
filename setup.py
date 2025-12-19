from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="aliked",
    version="1.0.0",
    author="Xiaoming Zhao",
    description="ALIKED: A Lighter Keypoint and Descriptor Extraction Network via Deformable Transformation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shiaoming/ALIKED",
    packages=find_packages(include=["nets", "nets.*"]),
    package_data={
        "nets": ["../models/*.pth"],  # Include pretrained model weights
    },
    include_package_data=True,
    data_files=[
        ("models", ["models/aliked-n16.pth", "models/aliked-n16rot.pth", 
                    "models/aliked-n32.pth", "models/aliked-t16.pth"]),
    ],
    python_requires=">=3.8",
    install_requires=[
        "torch>=1.9.0",
        "torchvision>=0.10.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
