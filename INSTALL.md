# ALIKED Installation Guide

This document explains how to install ALIKED as a pip package.

## Installation

### Option 1: Install from local directory (recommended for development)

From the ALIKED repository root:

```bash
pip install -e .
```

This installs ALIKED in "editable" mode, meaning changes to the source code are immediately reflected without reinstalling.

### Option 2: Install from local directory (standard)

```bash
pip install .
```

This installs ALIKED as a regular package.

### Option 3: Install from git repository

```bash
pip install git+https://github.com/Shiaoming/ALIKED.git
```

## Dependencies

ALIKED only requires:
- `torch>=1.9.0`
- `torchvision>=0.10.0`

These are minimal dependencies that are already present in the Summertime project. No additional dependencies are added beyond what's already in Summertime's requirements.

## Verification

After installation, verify that ALIKED works correctly:

```python
from nets.aliked import ALIKED
import torch

# Create model without pretrained weights
model = ALIKED(model_name='aliked-n32', device='cpu', load_pretrained=False)

# Create model with pretrained weights
model = ALIKED(model_name='aliked-n32', device='cpu', load_pretrained=True)

# Test with a dummy image
test_image = torch.randn(1, 3, 480, 640)
with torch.no_grad():
    outputs = model(test_image)
    print(f"Detected {len(outputs['keypoints'][0])} keypoints")
```

## Available Models

- `aliked-t16` - Tiny model with 16 channels
- `aliked-n16` - Normal model with 16 channels
- `aliked-n16rot` - Normal model with rotation augmentation
- `aliked-n32` - Normal model with 32 channels (recommended)

## Package Structure

After installation, the package includes:
- `nets/` - Core ALIKED modules
  - `aliked.py` - Main ALIKED model
  - `soft_detect.py` - DKD (Differentiable Keypoint Detection)
  - `blocks.py` - Neural network building blocks
  - `padder.py` - Input padding utilities
- `models/` - Pretrained model weights (*.pth files)
