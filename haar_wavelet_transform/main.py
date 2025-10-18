"""
Main execution script for Haar wavelet transform demonstration.
Provides user-friendly interface and comprehensive examples.
"""

import numpy as np
import argparse
import os
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None

from wavelet_transform import HaarWaveletTransform, process_color_image, reconstruct_color_image
from convolution_methods import wavelet_transform_with_traversal, get_traversal_visualization
from kernel_types import KernelGenerator, compare_kernels
from comparison_analysis import WaveletMetrics, MethodComparison, benchmark_performance
from visualization import WaveletVisualizer, create_test_image


def load_image(image_path: str) -> np.ndarray:
    """
    Load an image from file path.
    
    Args:
        image_path: Path to image file
        
    Returns:
        Image as numpy array
    """
    if Image is None:
        raise ImportError("PIL is required to load images. Install with: pip install Pillow")
    
    img = Image.open(image_path)
    
    # Convert to grayscale if needed
    if img.mode != 'L' and img.mode != 'RGB':
        img = img.convert('L')
    
    return np.array(img)


def save_image(image: np.ndarray, path: str):
    """
    Save an image to file.
    
    Args:
        image: Image array
        path: Output path
    """
    if Image is None:
        raise ImportError("PIL is required to save images. Install with: pip install Pillow")
    
    # Normalize to [0, 255]
    img_normalized = ((image - image.min()) / (image.max() - image.min()) * 255).astype(np.uint8)
    
    img = Image.fromarray(img_normalized)
    img.save(path)


def demo_basic_wavelet_transform(kernel_size: int = 2):
    """
    Demonstrate basic wavelet transform.
    
    Args:
        kernel_size: Size of the wavelet kernel
    """
    print("\n" + "="*80)
    print(f"BASIC WAVELET TRANSFORM DEMO (Kernel Size: {kernel_size}x{kernel_size})")
    print("="*80)
    
    # Create test image
    print("\nCreating test image...")
    image = create_test_image(256, 'checkerboard')
    
    # Perform wavelet transform
    print(f"\nPerforming {kernel_size}x{kernel_size} Haar wavelet transform...")
    transformer = HaarWaveletTransform(kernel_size)
    LL, LH, HL, HH = transformer.dwt_2d(image)
    
    print(f"Original image shape: {image.shape}")
    print(f"LL subband shape: {LL.shape}")
    print(f"LH subband shape: {LH.shape}")
    print(f"HL subband shape: {HL.shape}")
    print(f"HH subband shape: {HH.shape}")
    
    # Calculate energy preservation
    energy = WaveletMetrics.energy_preservation(image, LL, LH, HL, HH)
    print(f"\nEnergy preservation: {energy:.6f}")
    
    # Reconstruct image
    print("\nReconstructing image...")
    reconstructed = transformer.idwt_2d(LL, LH, HL, HH)
    
    # Calculate metrics
    mse = WaveletMetrics.mse(image, reconstructed)
    psnr = WaveletMetrics.psnr(image, reconstructed)
    
    print(f"Reconstruction MSE: {mse:.6f}")
    print(f"Reconstruction PSNR: {psnr:.2f} dB")
    
    # Visualize
    print("\nGenerating visualization...")
    WaveletVisualizer.plot_subbands(LL, LH, HL, HH, 
                                   title=f"Haar Wavelet Decomposition ({kernel_size}x{kernel_size})")
    WaveletVisualizer.plot_reconstruction_comparison(image, reconstructed,
                                                    title="Reconstruction Quality")


def demo_kernel_size_comparison():
    """Demonstrate comparison of different kernel sizes."""
    print("\n" + "="*80)
    print("KERNEL SIZE COMPARISON DEMO")
    print("="*80)
    
    # Create test image
    print("\nCreating test image...")
    image = create_test_image(256, 'circles')
    
    # Compare kernel sizes
    kernel_sizes = [2, 4, 8, 16]
    print(f"\nComparing kernel sizes: {kernel_sizes}")
    
    comparison = MethodComparison()
    
    def transform_func(img, size):
        transformer = HaarWaveletTransform(size)
        return transformer.dwt_2d(img)
    
    results = comparison.compare_kernel_sizes(image, kernel_sizes, transform_func)
    
    # Print comparison table
    print("\n" + comparison.generate_comparison_table(results))
    
    # Visualize
    print("\nGenerating visualization...")
    WaveletVisualizer.plot_kernel_size_comparison(results, 
                                                  title="Kernel Size Comparison")


def demo_traversal_methods():
    """Demonstrate different convolution traversal methods."""
    print("\n" + "="*80)
    print("TRAVERSAL METHODS COMPARISON DEMO")
    print("="*80)
    
    # Create test image
    print("\nCreating test image...")
    image = create_test_image(128, 'gradient')
    
    # Compare traversal methods
    traversal_methods = ['left_to_right', 'up_down', 'zigzag', 'custom_block']
    kernel_size = 4
    
    print(f"\nComparing traversal methods: {traversal_methods}")
    print(f"Kernel size: {kernel_size}x{kernel_size}")
    
    comparison = MethodComparison()
    results = comparison.compare_traversal_methods(image, kernel_size, 
                                                   traversal_methods,
                                                   wavelet_transform_with_traversal)
    
    # Print comparison table
    print("\n" + comparison.generate_comparison_table(results))
    
    # Visualize traversal orders
    print("\nVisualizing traversal orders...")
    for method in traversal_methods:
        order = get_traversal_visualization(image.shape, kernel_size, method)
        WaveletVisualizer.plot_traversal_order(order, 
                                              title=f"Traversal Order: {method}")
    
    # Visualize results
    print("\nGenerating comparison visualization...")
    WaveletVisualizer.plot_traversal_comparison(results,
                                               title="Traversal Method Comparison")


def demo_kernel_types():
    """Demonstrate different kernel types."""
    print("\n" + "="*80)
    print("KERNEL TYPES COMPARISON DEMO")
    print("="*80)
    
    # Create test image
    print("\nCreating test image...")
    image = create_test_image(128, 'checkerboard')
    
    # Compare kernel types
    kernel_types = ['haar', 'db2', 'db4']
    print(f"\nComparing kernel types: {kernel_types}")
    
    results = compare_kernels(image, kernel_types, size=2)
    
    # Visualize
    print("\nGenerating visualization...")
    WaveletVisualizer.plot_kernel_size_comparison(results,
                                                  title="Kernel Types Comparison")


def demo_multilevel_decomposition(levels: int = 3):
    """
    Demonstrate multi-level wavelet decomposition.
    
    Args:
        levels: Number of decomposition levels
    """
    print("\n" + "="*80)
    print(f"MULTI-LEVEL DECOMPOSITION DEMO ({levels} levels)")
    print("="*80)
    
    # Create test image
    print("\nCreating test image...")
    image = create_test_image(256, 'circles')
    
    # Perform multi-level decomposition
    print(f"\nPerforming {levels}-level wavelet decomposition...")
    transformer = HaarWaveletTransform(kernel_size=2)
    decomposition = transformer.multilevel_dwt_2d(image, levels=levels)
    
    # Visualize
    print("\nGenerating visualization...")
    WaveletVisualizer.plot_multilevel_decomposition(decomposition,
                                                    title=f"{levels}-Level Wavelet Decomposition")
    
    # Reconstruct
    print("\nReconstructing image...")
    reconstructed = transformer.multilevel_idwt_2d(decomposition)
    
    # Calculate metrics
    mse = WaveletMetrics.mse(image, reconstructed)
    psnr = WaveletMetrics.psnr(image, reconstructed)
    
    print(f"\nReconstruction MSE: {mse:.6f}")
    print(f"Reconstruction PSNR: {psnr:.2f} dB")


def demo_color_image():
    """Demonstrate wavelet transform on color images."""
    print("\n" + "="*80)
    print("COLOR IMAGE PROCESSING DEMO")
    print("="*80)
    
    # Create color test image
    print("\nCreating color test image...")
    size = 128
    color_image = np.zeros((size, size, 3))
    
    # Red channel - checkerboard
    color_image[:, :, 0] = create_test_image(size, 'checkerboard')
    # Green channel - gradient
    color_image[:, :, 1] = create_test_image(size, 'gradient')
    # Blue channel - circles
    color_image[:, :, 2] = create_test_image(size, 'circles')
    
    print(f"Color image shape: {color_image.shape}")
    
    # Process color image
    print("\nProcessing color image...")
    decomposition = process_color_image(color_image, kernel_size=2, levels=1)
    
    # Reconstruct
    print("\nReconstructing color image...")
    reconstructed = reconstruct_color_image(decomposition, kernel_size=2)
    
    print(f"Reconstructed image shape: {reconstructed.shape}")
    
    # Calculate metrics per channel
    print("\nMetrics per channel:")
    for i in range(3):
        channel_names = ['Red', 'Green', 'Blue']
        mse = WaveletMetrics.mse(color_image[:, :, i], reconstructed[:, :, i])
        psnr = WaveletMetrics.psnr(color_image[:, :, i], reconstructed[:, :, i])
        print(f"{channel_names[i]}: MSE={mse:.6f}, PSNR={psnr:.2f} dB")


def demo_performance_benchmark():
    """Benchmark performance of different methods."""
    print("\n" + "="*80)
    print("PERFORMANCE BENCHMARK")
    print("="*80)
    
    # Create test image
    print("\nCreating test image...")
    image = create_test_image(256, 'checkerboard')
    
    # Benchmark different kernel sizes
    print("\nBenchmarking different kernel sizes...")
    kernel_sizes = [2, 4, 8]
    
    for size in kernel_sizes:
        def transform_func(img):
            transformer = HaarWaveletTransform(size)
            return transformer.dwt_2d(img)
        
        results = benchmark_performance(image, transform_func, iterations=10)
        print(f"\nKernel {size}x{size}:")
        print(f"  Mean time: {results['mean_time']:.4f} s")
        print(f"  Std dev:   {results['std_time']:.4f} s")
        print(f"  Min time:  {results['min_time']:.4f} s")
        print(f"  Max time:  {results['max_time']:.4f} s")


def main():
    """Main function with command-line interface."""
    parser = argparse.ArgumentParser(
        description='Haar Wavelet Transform Demonstration',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --demo all                    Run all demonstrations
  %(prog)s --demo basic --kernel-size 4  Run basic demo with 4x4 kernel
  %(prog)s --demo traversal              Compare traversal methods
  %(prog)s --image path/to/image.jpg     Process custom image
        """
    )
    
    parser.add_argument('--demo', type=str, 
                       choices=['all', 'basic', 'kernel_size', 'traversal', 
                               'kernel_types', 'multilevel', 'color', 'benchmark'],
                       default='all',
                       help='Demo to run')
    
    parser.add_argument('--kernel-size', type=int, default=2,
                       help='Kernel size for wavelet transform')
    
    parser.add_argument('--levels', type=int, default=3,
                       help='Number of decomposition levels for multilevel demo')
    
    parser.add_argument('--image', type=str,
                       help='Path to custom image to process')
    
    parser.add_argument('--output-dir', type=str, default='output',
                       help='Directory to save output images')
    
    args = parser.parse_args()
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    print("\n" + "="*80)
    print("HAAR WAVELET TRANSFORM DEMONSTRATION")
    print("="*80)
    
    # Process custom image if provided
    if args.image:
        print(f"\nProcessing custom image: {args.image}")
        try:
            image = load_image(args.image)
            print(f"Image loaded successfully: {image.shape}")
            
            # Convert to grayscale if color
            if len(image.shape) == 3:
                image = np.mean(image, axis=2)
                print(f"Converted to grayscale: {image.shape}")
            
            # Perform transform
            transformer = HaarWaveletTransform(args.kernel_size)
            LL, LH, HL, HH = transformer.dwt_2d(image)
            
            # Visualize
            WaveletVisualizer.plot_subbands(LL, LH, HL, HH,
                                           title=f"Wavelet Transform of {Path(args.image).name}")
            
        except Exception as e:
            print(f"Error processing image: {e}")
        
        return
    
    # Run demos
    if args.demo == 'all' or args.demo == 'basic':
        demo_basic_wavelet_transform(args.kernel_size)
    
    if args.demo == 'all' or args.demo == 'kernel_size':
        demo_kernel_size_comparison()
    
    if args.demo == 'all' or args.demo == 'traversal':
        demo_traversal_methods()
    
    if args.demo == 'all' or args.demo == 'kernel_types':
        demo_kernel_types()
    
    if args.demo == 'all' or args.demo == 'multilevel':
        demo_multilevel_decomposition(args.levels)
    
    if args.demo == 'all' or args.demo == 'color':
        demo_color_image()
    
    if args.demo == 'all' or args.demo == 'benchmark':
        demo_performance_benchmark()
    
    print("\n" + "="*80)
    print("DEMONSTRATION COMPLETE")
    print("="*80)


if __name__ == '__main__':
    main()
