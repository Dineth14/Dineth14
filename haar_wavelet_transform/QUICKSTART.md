# Quick Start Guide

Get started with the Haar Wavelet Transform implementation in 5 minutes!

## Installation

1. **Clone or download the repository**

2. **Install dependencies**:
```bash
cd haar_wavelet_transform
pip install -r requirements.txt
```

3. **Verify installation**:
```bash
python test_installation.py
```

You should see: ✅ ALL TESTS PASSED!

## First Example - 30 Seconds

```python
from wavelet_transform import HaarWaveletTransform
from visualization import create_test_image, WaveletVisualizer

# Create a test image
image = create_test_image(256, 'checkerboard')

# Transform it
transformer = HaarWaveletTransform(kernel_size=2)
LL, LH, HL, HH = transformer.dwt_2d(image)

# Visualize (will display plots)
WaveletVisualizer.plot_subbands(LL, LH, HL, HH)
```

That's it! You've performed your first wavelet transform.

## Command-Line Quick Start

### Run all demos:
```bash
python main.py --demo all
```

### Run specific demo:
```bash
python main.py --demo basic --kernel-size 4
```

### Process your own image:
```bash
python main.py --image path/to/your/image.jpg
```

## Common Tasks

### Task 1: Transform and Reconstruct
```python
from wavelet_transform import HaarWaveletTransform
from visualization import create_test_image

image = create_test_image(128, 'circles')
transformer = HaarWaveletTransform(kernel_size=2)

# Forward transform
LL, LH, HL, HH = transformer.dwt_2d(image)

# Inverse transform
reconstructed = transformer.idwt_2d(LL, LH, HL, HH)

# Check quality
from comparison_analysis import WaveletMetrics
psnr = WaveletMetrics.psnr(image, reconstructed)
print(f"Reconstruction quality: {psnr:.2f} dB")
```

### Task 2: Compare Kernel Sizes
```python
from comparison_analysis import MethodComparison
from wavelet_transform import HaarWaveletTransform
from visualization import create_test_image

image = create_test_image(256, 'gradient')
comparison = MethodComparison()

def transform_func(img, size):
    transformer = HaarWaveletTransform(size)
    return transformer.dwt_2d(img)

results = comparison.compare_kernel_sizes(
    image, 
    kernel_sizes=[2, 4, 8, 16], 
    transform_func=transform_func
)

# Print results
print(comparison.generate_comparison_table(results))
```

### Task 3: Try Different Traversal Methods
```python
from convolution_methods import wavelet_transform_with_traversal
from visualization import create_test_image

image = create_test_image(128, 'checkerboard')

# Try zigzag traversal
LL, LH, HL, HH = wavelet_transform_with_traversal(
    image, 
    kernel_size=4, 
    traversal_method='zigzag'
)
```

### Task 4: Multi-level Decomposition
```python
from wavelet_transform import HaarWaveletTransform
from visualization import create_test_image

image = create_test_image(256, 'circles')
transformer = HaarWaveletTransform(kernel_size=2)

# 3-level decomposition
decomposition = transformer.multilevel_dwt_2d(image, levels=3)

# Reconstruct
reconstructed = transformer.multilevel_idwt_2d(decomposition)
```

### Task 5: Process Color Images
```python
import numpy as np
from wavelet_transform import process_color_image, reconstruct_color_image
from visualization import create_test_image

# Create color image
size = 128
color_image = np.zeros((size, size, 3))
color_image[:, :, 0] = create_test_image(size, 'checkerboard')
color_image[:, :, 1] = create_test_image(size, 'gradient')
color_image[:, :, 2] = create_test_image(size, 'circles')

# Process
decomposition = process_color_image(color_image, kernel_size=2)
reconstructed = reconstruct_color_image(decomposition, kernel_size=2)
```

## Interactive Examples

### Run the Jupyter Notebook:
```bash
jupyter notebook examples/demo_notebook.ipynb
```

### Run Sample Usage Script:
```bash
python examples/sample_usage.py
```

## Understanding the Output

### Wavelet Subbands

After transformation, you get 4 subbands:

- **LL**: Low-frequency approximation (blurred version)
- **LH**: Horizontal edges (left-right changes)
- **HL**: Vertical edges (up-down changes)
- **HH**: Diagonal edges (diagonal changes)

### Quality Metrics

- **PSNR > 40 dB**: Excellent quality
- **PSNR 30-40 dB**: Good quality
- **PSNR 20-30 dB**: Acceptable quality
- **PSNR < 20 dB**: Poor quality

- **MSE ≈ 0**: Perfect reconstruction
- **Energy ≈ 1.0**: Energy is conserved

## Next Steps

1. **Read the full documentation**: `README.md`
2. **Explore technical details**: `DOCUMENTATION.md`
3. **Try the examples**: `examples/sample_usage.py`
4. **Experiment with parameters**: kernel size, levels, methods

## Common Issues

### Issue: Import Error
**Solution**: Make sure you're in the correct directory and dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: Visualization doesn't show
**Solution**: If running in a script, use:
```python
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg'
```

### Issue: Image size error
**Solution**: Image dimensions should be divisible by kernel size, or will be automatically padded.

## Getting Help

- Check `README.md` for detailed examples
- Read `DOCUMENTATION.md` for technical details
- Review `examples/demo_notebook.ipynb` for interactive examples
- Run `python test_installation.py` to verify setup

## Tips

1. Start with 2×2 kernel for best quality
2. Use larger kernels (8×8, 16×16) for compression
3. Multi-level decomposition provides better frequency separation
4. Energy preservation ≈ 1.0 indicates correct implementation
5. PSNR > 300 dB means near-perfect reconstruction

## Performance

Typical processing times (256×256 image):
- 2×2 kernel: ~5 ms
- 4×4 kernel: ~3 ms
- 8×8 kernel: ~3 ms

Faster for larger kernels due to fewer operations.

---

**Ready to explore more?** Check out the full `README.md` and `DOCUMENTATION.md`!
