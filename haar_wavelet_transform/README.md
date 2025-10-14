# Haar Wavelet Transform Implementation

A comprehensive implementation of Haar wavelet transform for images with support for multiple kernel sizes, different convolution traversal patterns, and extensive comparison visualizations.

## Features

- ✨ **Multiple Kernel Sizes**: Support for 2x2, 4x4, 8x8, 16x16, and custom kernel sizes
- 🎯 **Various Kernel Types**: Haar, Daubechies (db2, db4), and custom kernels
- 🔄 **Multiple Traversal Patterns**: Left-to-right, up-down, zigzag, and custom block traversal
- 📊 **Comprehensive Analysis**: PSNR, MSE, energy preservation, and performance metrics
- 🎨 **Rich Visualizations**: Subband plots, comparison charts, and traversal visualizations
- 🖼️ **Color Image Support**: Process RGB images channel-by-channel
- 🔢 **Multi-level Decomposition**: Support for multiple decomposition levels
- ⚡ **Performance Benchmarking**: Compare execution times across methods

## Installation

```bash
# Clone or download this repository
cd haar_wavelet_transform

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

### Basic Usage

```python
from wavelet_transform import HaarWaveletTransform
from visualization import WaveletVisualizer, create_test_image

# Create a test image
image = create_test_image(256, 'checkerboard')

# Perform wavelet transform
transformer = HaarWaveletTransform(kernel_size=2)
LL, LH, HL, HH = transformer.dwt_2d(image)

# Visualize results
WaveletVisualizer.plot_subbands(LL, LH, HL, HH, title="Haar Wavelet Decomposition")

# Reconstruct image
reconstructed = transformer.idwt_2d(LL, LH, HL, HH)
```

### Command-Line Interface

```bash
# Run all demonstrations
python main.py --demo all

# Run specific demo with custom kernel size
python main.py --demo basic --kernel-size 4

# Compare traversal methods
python main.py --demo traversal

# Compare kernel sizes
python main.py --demo kernel_size

# Multi-level decomposition
python main.py --demo multilevel --levels 3

# Process custom image
python main.py --image path/to/your/image.jpg --kernel-size 4
```

## Module Documentation

### 1. wavelet_transform.py

Core Haar wavelet transform implementation.

**Key Classes:**
- `HaarWaveletTransform`: Main wavelet transform class

**Key Functions:**
- `dwt_1d()`: 1D discrete wavelet transform
- `idwt_1d()`: Inverse 1D DWT
- `dwt_2d()`: 2D discrete wavelet transform
- `idwt_2d()`: Inverse 2D DWT
- `multilevel_dwt_2d()`: Multi-level decomposition
- `process_color_image()`: Process RGB images

**Example:**
```python
from wavelet_transform import HaarWaveletTransform

# Initialize with kernel size
transformer = HaarWaveletTransform(kernel_size=4)

# Perform 2D transform
LL, LH, HL, HH = transformer.dwt_2d(image)

# Multi-level decomposition
decomposition = transformer.multilevel_dwt_2d(image, levels=3)
```

### 2. convolution_methods.py

Different convolution traversal patterns.

**Key Classes:**
- `ConvolutionTraversal`: Generates traversal patterns

**Traversal Methods:**
- **Left-to-Right**: Standard row-major order
- **Up-Down**: Column-major vertical traversal
- **Zigzag**: Diagonal zigzag pattern (JPEG-like)
- **Custom Block**: Custom pattern (down → diagonal up → horizontal → diagonal down)

**Example:**
```python
from convolution_methods import wavelet_transform_with_traversal

# Use zigzag traversal
LL, LH, HL, HH = wavelet_transform_with_traversal(
    image, 
    kernel_size=4, 
    traversal_method='zigzag'
)
```

### 3. kernel_types.py

Various kernel/filter implementations.

**Key Classes:**
- `KernelGenerator`: Generates different kernel types

**Kernel Types:**
- **Haar**: Standard Haar wavelet
- **Daubechies db2**: 4-coefficient Daubechies wavelet
- **Daubechies db4**: 8-coefficient Daubechies wavelet
- **Smoothing**: Gaussian smoothing kernels
- **Edge Detection**: Sobel, Prewitt, Scharr filters

**Example:**
```python
from kernel_types import KernelGenerator

# Generate Haar kernels
LL, LH, HL, HH = KernelGenerator.get_2d_wavelet_kernels('haar', size=2)

# Generate db2 kernels
LL, LH, HL, HH = KernelGenerator.get_2d_wavelet_kernels('db2')

# Compare different kernel types
results = compare_kernels(image, ['haar', 'db2', 'db4'], size=2)
```

### 4. comparison_analysis.py

Metrics calculation and comparison framework.

**Key Classes:**
- `WaveletMetrics`: Calculates quality metrics
- `MethodComparison`: Compares different methods

**Metrics:**
- **PSNR**: Peak Signal-to-Noise Ratio
- **MSE**: Mean Squared Error
- **SNR**: Signal-to-Noise Ratio
- **Energy Preservation**: Ensures energy conservation
- **Entropy**: Information content
- **Processing Time**: Execution time

**Example:**
```python
from comparison_analysis import WaveletMetrics, MethodComparison

# Calculate metrics
mse = WaveletMetrics.mse(original, reconstructed)
psnr = WaveletMetrics.psnr(original, reconstructed)
energy = WaveletMetrics.energy_preservation(original, LL, LH, HL, HH)

# Compare kernel sizes
comparison = MethodComparison()
results = comparison.compare_kernel_sizes(image, [2, 4, 8, 16], transform_func)
```

### 5. visualization.py

Visualization tools for wavelet transforms.

**Key Classes:**
- `WaveletVisualizer`: Creates various plots and visualizations

**Visualization Types:**
- Subband plots (LL, LH, HL, HH)
- Reconstruction comparisons
- Kernel size comparisons
- Traversal method comparisons
- Metrics bar charts
- Traversal order heatmaps
- Multi-level decomposition plots

**Example:**
```python
from visualization import WaveletVisualizer

# Plot subbands
WaveletVisualizer.plot_subbands(LL, LH, HL, HH, 
                               title="Wavelet Decomposition")

# Compare reconstructions
WaveletVisualizer.plot_reconstruction_comparison(
    original, reconstructed, 
    title="Reconstruction Quality"
)

# Visualize traversal order
WaveletVisualizer.plot_traversal_order(order, title="Zigzag Traversal")
```

## Understanding Wavelet Subbands

After performing a 2D wavelet transform, the image is decomposed into four subbands:

- **LL (Low-Low)**: Approximation coefficients - represents the low-frequency components (overall structure)
- **LH (Low-High)**: Horizontal detail coefficients - captures horizontal edges and features
- **HL (High-Low)**: Vertical detail coefficients - captures vertical edges and features
- **HH (High-High)**: Diagonal detail coefficients - captures diagonal edges and corners

## Traversal Patterns Explained

### 1. Left-to-Right (Row-Major)
Standard convolution order - processes blocks from left to right, top to bottom.

### 2. Up-Down (Column-Major)
Vertical traversal - processes blocks from top to bottom, left to right.

### 3. Zigzag
Diagonal traversal similar to JPEG encoding - follows a zigzag pattern through the image.

### 4. Custom Block Traversal
A unique pattern that repeats:
1. Move **down** through the current column
2. Move **diagonally up** (up-right direction)
3. Move **horizontally** (left to right)
4. Move **diagonally down** (down-right direction)

## Examples

### Example 1: Basic Transform and Reconstruction

```python
import numpy as np
from wavelet_transform import HaarWaveletTransform
from visualization import create_test_image, WaveletVisualizer

# Create test image
image = create_test_image(256, 'circles')

# Transform
transformer = HaarWaveletTransform(kernel_size=2)
LL, LH, HL, HH = transformer.dwt_2d(image)

# Reconstruct
reconstructed = transformer.idwt_2d(LL, LH, HL, HH)

# Visualize
WaveletVisualizer.plot_subbands(LL, LH, HL, HH)
WaveletVisualizer.plot_reconstruction_comparison(image, reconstructed)
```

### Example 2: Compare Kernel Sizes

```python
from comparison_analysis import MethodComparison

# Compare different kernel sizes
comparison = MethodComparison()

def transform_func(img, size):
    transformer = HaarWaveletTransform(size)
    return transformer.dwt_2d(img)

results = comparison.compare_kernel_sizes(
    image, 
    kernel_sizes=[2, 4, 8, 16], 
    transform_func=transform_func
)

# Print comparison table
print(comparison.generate_comparison_table(results))

# Visualize
from visualization import WaveletVisualizer
WaveletVisualizer.plot_kernel_size_comparison(results)
```

### Example 3: Compare Traversal Methods

```python
from convolution_methods import wavelet_transform_with_traversal
from comparison_analysis import MethodComparison

# Compare traversal methods
comparison = MethodComparison()
methods = ['left_to_right', 'up_down', 'zigzag', 'custom_block']

results = comparison.compare_traversal_methods(
    image, 
    kernel_size=4,
    traversal_methods=methods,
    transform_func=wavelet_transform_with_traversal
)

# Visualize
WaveletVisualizer.plot_traversal_comparison(results)
```

### Example 4: Multi-level Decomposition

```python
# Perform 3-level decomposition
transformer = HaarWaveletTransform(kernel_size=2)
decomposition = transformer.multilevel_dwt_2d(image, levels=3)

# Visualize all levels
WaveletVisualizer.plot_multilevel_decomposition(decomposition)

# Reconstruct
reconstructed = transformer.multilevel_idwt_2d(decomposition)
```

### Example 5: Color Image Processing

```python
from wavelet_transform import process_color_image, reconstruct_color_image

# Process color image
decomposition = process_color_image(color_image, kernel_size=2, levels=1)

# Reconstruct
reconstructed = reconstruct_color_image(decomposition, kernel_size=2)

# Each channel is processed independently
```

## Performance Considerations

- **Kernel Size**: Larger kernels reduce computation but may lose detail
- **Traversal Method**: Different methods have similar performance but may affect cache locality
- **Image Size**: Processing time scales with image size
- **Decomposition Levels**: Each level reduces resolution by half

## Applications

- **Image Compression**: Discard high-frequency coefficients
- **Denoising**: Remove noise in detail subbands
- **Feature Extraction**: Use subbands for feature detection
- **Edge Detection**: LH, HL, HH contain edge information
- **Image Analysis**: Multi-resolution analysis
- **Watermarking**: Embed data in wavelet domain

## Technical Notes

- Uses NumPy for efficient array operations
- All operations preserve energy (Parseval's theorem)
- Supports reflection padding for boundary handling
- Type hints included for better code documentation
- Follows PEP 8 style guidelines

## File Structure

```
haar_wavelet_transform/
├── wavelet_transform.py      # Core wavelet transform
├── convolution_methods.py    # Traversal patterns
├── kernel_types.py           # Kernel/filter types
├── comparison_analysis.py    # Metrics and comparison
├── visualization.py          # Plotting functions
├── main.py                   # Main execution script
├── requirements.txt          # Dependencies
├── README.md                 # This file
└── examples/                 # Example notebooks and images
    ├── demo_notebook.ipynb
    └── sample_images/
```

## Testing

The implementation can be tested using:

```python
# Test basic transform
python main.py --demo basic

# Test with different parameters
python main.py --demo basic --kernel-size 8

# Run all tests
python main.py --demo all
```

## Contributing

Feel free to extend this implementation with:
- Additional wavelet types (Symlets, Coiflets)
- GPU acceleration
- More traversal patterns
- Additional metrics
- 3D wavelet transforms
- Lossy compression schemes

## License

This implementation is provided as-is for educational and research purposes.

## References

1. Haar, A. (1910). "Zur Theorie der orthogonalen Funktionensysteme"
2. Daubechies, I. (1992). "Ten Lectures on Wavelets"
3. Mallat, S. (1989). "A Theory for Multiresolution Signal Decomposition"

## Author

Developed as part of signal processing and image analysis demonstrations.

## Acknowledgments

Special thanks to the signal processing and computer vision communities for their foundational work on wavelet transforms.
