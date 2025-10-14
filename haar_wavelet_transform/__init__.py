"""
Haar Wavelet Transform Package

A comprehensive implementation of Haar wavelet transform for images.
"""

__version__ = "1.0.0"
__author__ = "Dineth Perera"

from .wavelet_transform import (
    HaarWaveletTransform,
    process_color_image,
    reconstruct_color_image
)

from .convolution_methods import (
    ConvolutionTraversal,
    wavelet_transform_with_traversal,
    get_traversal_visualization
)

from .kernel_types import (
    KernelGenerator,
    compare_kernels
)

from .comparison_analysis import (
    WaveletMetrics,
    MethodComparison,
    benchmark_performance
)

from .visualization import (
    WaveletVisualizer,
    create_test_image
)

__all__ = [
    'HaarWaveletTransform',
    'process_color_image',
    'reconstruct_color_image',
    'ConvolutionTraversal',
    'wavelet_transform_with_traversal',
    'get_traversal_visualization',
    'KernelGenerator',
    'compare_kernels',
    'WaveletMetrics',
    'MethodComparison',
    'benchmark_performance',
    'WaveletVisualizer',
    'create_test_image',
]
