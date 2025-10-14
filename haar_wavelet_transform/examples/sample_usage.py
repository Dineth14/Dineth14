#!/usr/bin/env python3
"""
Sample usage examples for the Haar wavelet transform implementation.
This script demonstrates all major features with clear examples.
"""

import sys
sys.path.append('..')

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt

from wavelet_transform import HaarWaveletTransform, process_color_image, reconstruct_color_image
from convolution_methods import wavelet_transform_with_traversal, get_traversal_visualization
from kernel_types import KernelGenerator, compare_kernels
from comparison_analysis import WaveletMetrics, MethodComparison, benchmark_performance
from visualization import WaveletVisualizer, create_test_image


def example_1_basic_transform():
    """Example 1: Basic wavelet transform and reconstruction."""
    print("\n" + "="*80)
    print("EXAMPLE 1: Basic Wavelet Transform")
    print("="*80)
    
    # Create test image
    image = create_test_image(256, 'checkerboard')
    print(f"Created test image: {image.shape}")
    
    # Perform transform
    transformer = HaarWaveletTransform(kernel_size=2)
    LL, LH, HL, HH = transformer.dwt_2d(image)
    
    print(f"Wavelet subbands:")
    print(f"  LL (approximation): {LL.shape}")
    print(f"  LH (horizontal):    {LH.shape}")
    print(f"  HL (vertical):      {HL.shape}")
    print(f"  HH (diagonal):      {HH.shape}")
    
    # Reconstruct
    reconstructed = transformer.idwt_2d(LL, LH, HL, HH)
    
    # Calculate metrics
    mse = WaveletMetrics.mse(image, reconstructed)
    psnr = WaveletMetrics.psnr(image, reconstructed)
    energy = WaveletMetrics.energy_preservation(image, LL, LH, HL, HH)
    
    print(f"\nReconstruction quality:")
    print(f"  MSE:                {mse:.10f}")
    print(f"  PSNR:               {psnr:.2f} dB")
    print(f"  Energy preservation: {energy:.6f}")
    
    # Save visualization (would normally display)
    WaveletVisualizer.plot_subbands(LL, LH, HL, HH, 
                                   title="Basic Wavelet Decomposition",
                                   save_path="example1_subbands.png")
    print("\n✓ Saved visualization to example1_subbands.png")


def example_2_kernel_sizes():
    """Example 2: Compare different kernel sizes."""
    print("\n" + "="*80)
    print("EXAMPLE 2: Comparing Kernel Sizes")
    print("="*80)
    
    image = create_test_image(256, 'circles')
    
    # Test different kernel sizes
    kernel_sizes = [2, 4, 8, 16]
    print(f"Testing kernel sizes: {kernel_sizes}")
    
    comparison = MethodComparison()
    
    def transform_func(img, size):
        transformer = HaarWaveletTransform(size)
        return transformer.dwt_2d(img)
    
    results = comparison.compare_kernel_sizes(image, kernel_sizes, transform_func)
    
    # Print comparison
    print("\nComparison results:")
    for name, data in results.items():
        if 'error' not in data:
            print(f"  {name}:")
            print(f"    Energy preservation: {data['energy_preservation']:.6f}")
            print(f"    Processing time:     {data['processing_time']:.4f} s")
    
    print("\n✓ Kernel size comparison complete")


def example_3_traversal_methods():
    """Example 3: Different traversal patterns."""
    print("\n" + "="*80)
    print("EXAMPLE 3: Traversal Patterns")
    print("="*80)
    
    image = create_test_image(128, 'gradient')
    
    traversal_methods = ['left_to_right', 'up_down', 'zigzag', 'custom_block']
    kernel_size = 4
    
    print(f"Testing traversal methods: {traversal_methods}")
    print(f"Kernel size: {kernel_size}x{kernel_size}")
    
    for method in traversal_methods:
        LL, LH, HL, HH = wavelet_transform_with_traversal(
            image, kernel_size, method
        )
        energy = WaveletMetrics.energy_preservation(image, LL, LH, HL, HH)
        print(f"  {method}: energy preservation = {energy:.6f}")
    
    print("\n✓ All traversal methods tested successfully")


def example_4_multilevel():
    """Example 4: Multi-level decomposition."""
    print("\n" + "="*80)
    print("EXAMPLE 4: Multi-level Decomposition")
    print("="*80)
    
    image = create_test_image(256, 'circles')
    
    # Perform 3-level decomposition
    levels = 3
    print(f"Performing {levels}-level decomposition...")
    
    transformer = HaarWaveletTransform(kernel_size=2)
    decomposition = transformer.multilevel_dwt_2d(image, levels=levels)
    
    # Show subband sizes at each level
    for level in range(1, levels + 1):
        level_data = decomposition[f'level_{level}']
        print(f"  Level {level}: {level_data['LL'].shape}")
    
    # Reconstruct
    reconstructed = transformer.multilevel_idwt_2d(decomposition)
    
    mse = WaveletMetrics.mse(image, reconstructed)
    psnr = WaveletMetrics.psnr(image, reconstructed)
    
    print(f"\nReconstruction quality:")
    print(f"  MSE:  {mse:.10f}")
    print(f"  PSNR: {psnr:.2f} dB")
    
    print("\n✓ Multi-level decomposition successful")


def example_5_color_image():
    """Example 5: Color image processing."""
    print("\n" + "="*80)
    print("EXAMPLE 5: Color Image Processing")
    print("="*80)
    
    # Create synthetic color image
    size = 128
    color_image = np.zeros((size, size, 3))
    color_image[:, :, 0] = create_test_image(size, 'checkerboard')
    color_image[:, :, 1] = create_test_image(size, 'gradient')
    color_image[:, :, 2] = create_test_image(size, 'circles')
    
    print(f"Color image shape: {color_image.shape}")
    
    # Process each channel
    decomposition = process_color_image(color_image, kernel_size=2, levels=1)
    reconstructed = reconstruct_color_image(decomposition, kernel_size=2)
    
    print(f"Reconstructed shape: {reconstructed.shape}")
    
    # Metrics per channel
    print("\nPer-channel metrics:")
    channel_names = ['Red', 'Green', 'Blue']
    for i in range(3):
        mse = WaveletMetrics.mse(color_image[:, :, i], reconstructed[:, :, i])
        psnr = WaveletMetrics.psnr(color_image[:, :, i], reconstructed[:, :, i])
        print(f"  {channel_names[i]}: PSNR = {psnr:.2f} dB")
    
    print("\n✓ Color image processing successful")


def example_6_kernel_types():
    """Example 6: Different kernel types."""
    print("\n" + "="*80)
    print("EXAMPLE 6: Different Kernel Types")
    print("="*80)
    
    image = create_test_image(128, 'checkerboard')
    
    kernel_types = ['haar', 'db2', 'db4']
    print(f"Comparing kernel types: {kernel_types}")
    
    results = compare_kernels(image, kernel_types, size=2)
    
    print("\nKernel comparison:")
    for kernel_type in kernel_types:
        if kernel_type in results:
            LL = results[kernel_type]['LL']
            print(f"  {kernel_type}: subband shape = {LL.shape}")
    
    print("\n✓ Kernel type comparison complete")


def example_7_performance():
    """Example 7: Performance benchmarking."""
    print("\n" + "="*80)
    print("EXAMPLE 7: Performance Benchmark")
    print("="*80)
    
    image = create_test_image(256, 'checkerboard')
    
    print("Benchmarking kernel sizes (10 iterations each)...")
    
    for kernel_size in [2, 4, 8]:
        def transform_func(img):
            transformer = HaarWaveletTransform(kernel_size)
            return transformer.dwt_2d(img)
        
        results = benchmark_performance(image, transform_func, iterations=10)
        
        print(f"\n  Kernel {kernel_size}x{kernel_size}:")
        print(f"    Mean time: {results['mean_time']:.4f} s")
        print(f"    Std dev:   {results['std_time']:.4f} s")
    
    print("\n✓ Performance benchmark complete")


def main():
    """Run all examples."""
    print("\n" + "="*80)
    print("HAAR WAVELET TRANSFORM - SAMPLE USAGE EXAMPLES")
    print("="*80)
    
    try:
        example_1_basic_transform()
        example_2_kernel_sizes()
        example_3_traversal_methods()
        example_4_multilevel()
        example_5_color_image()
        example_6_kernel_types()
        example_7_performance()
        
        print("\n" + "="*80)
        print("ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("="*80)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
