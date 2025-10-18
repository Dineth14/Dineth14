"""
Different kernel/filter types for wavelet transforms.
Includes Haar, Daubechies, and custom kernels.
"""

import numpy as np
from typing import Tuple, Optional


class KernelGenerator:
    """
    Generates various types of kernels/filters for wavelet transforms.
    """
    
    @staticmethod
    def haar_kernel(size: int = 2) -> Tuple[np.ndarray, np.ndarray]:
        """
        Generate Haar wavelet kernels.
        
        Args:
            size: Kernel size
            
        Returns:
            Tuple of (low_pass_filter, high_pass_filter)
        """
        scaling_factor = 1.0 / np.sqrt(size)
        
        # Low-pass filter (averaging)
        low_pass = np.ones(size) * scaling_factor
        
        # High-pass filter (differencing)
        high_pass = np.ones(size) * scaling_factor
        high_pass[size // 2:] *= -1
        
        return low_pass, high_pass
    
    @staticmethod
    def db2_kernel() -> Tuple[np.ndarray, np.ndarray]:
        """
        Generate Daubechies-2 (db2) wavelet kernels.
        
        Returns:
            Tuple of (low_pass_filter, high_pass_filter)
        """
        # Daubechies-2 coefficients
        h0 = (1 + np.sqrt(3)) / (4 * np.sqrt(2))
        h1 = (3 + np.sqrt(3)) / (4 * np.sqrt(2))
        h2 = (3 - np.sqrt(3)) / (4 * np.sqrt(2))
        h3 = (1 - np.sqrt(3)) / (4 * np.sqrt(2))
        
        low_pass = np.array([h0, h1, h2, h3])
        
        # High-pass filter derived from low-pass
        high_pass = np.array([h3, -h2, h1, -h0])
        
        return low_pass, high_pass
    
    @staticmethod
    def db4_kernel() -> Tuple[np.ndarray, np.ndarray]:
        """
        Generate Daubechies-4 (db4) wavelet kernels.
        
        Returns:
            Tuple of (low_pass_filter, high_pass_filter)
        """
        # Daubechies-4 coefficients (8 coefficients)
        c0 = 0.23037781330885523
        c1 = 0.71484657055254153
        c2 = 0.63088076792985890
        c3 = -0.02798376941685985
        c4 = -0.18703481171909309
        c5 = 0.03084138183598697
        c6 = 0.03288301166688519
        c7 = -0.01059740178506903
        
        low_pass = np.array([c0, c1, c2, c3, c4, c5, c6, c7])
        
        # High-pass filter derived from low-pass
        high_pass = np.array([c7, -c6, c5, -c4, c3, -c2, c1, -c0])
        
        return low_pass, high_pass
    
    @staticmethod
    def smoothing_kernel(size: int = 2, sigma: Optional[float] = None) -> np.ndarray:
        """
        Generate a Gaussian smoothing kernel.
        
        Args:
            size: Kernel size
            sigma: Standard deviation (if None, auto-calculated)
            
        Returns:
            2D smoothing kernel
        """
        if sigma is None:
            sigma = size / 6.0
        
        kernel_1d = np.zeros(size)
        center = size // 2
        
        for i in range(size):
            x = i - center
            kernel_1d[i] = np.exp(-x**2 / (2 * sigma**2))
        
        # Normalize
        kernel_1d /= np.sum(kernel_1d)
        
        # Create 2D kernel
        kernel_2d = np.outer(kernel_1d, kernel_1d)
        
        return kernel_2d
    
    @staticmethod
    def edge_detection_kernel(kernel_type: str = 'sobel') -> Tuple[np.ndarray, np.ndarray]:
        """
        Generate edge detection kernels.
        
        Args:
            kernel_type: Type of edge detector ('sobel', 'prewitt', 'scharr')
            
        Returns:
            Tuple of (horizontal_kernel, vertical_kernel)
        """
        if kernel_type == 'sobel':
            horizontal = np.array([
                [-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]
            ]) / 8.0
            
            vertical = np.array([
                [-1, -2, -1],
                [0, 0, 0],
                [1, 2, 1]
            ]) / 8.0
            
        elif kernel_type == 'prewitt':
            horizontal = np.array([
                [-1, 0, 1],
                [-1, 0, 1],
                [-1, 0, 1]
            ]) / 6.0
            
            vertical = np.array([
                [-1, -1, -1],
                [0, 0, 0],
                [1, 1, 1]
            ]) / 6.0
            
        elif kernel_type == 'scharr':
            horizontal = np.array([
                [-3, 0, 3],
                [-10, 0, 10],
                [-3, 0, 3]
            ]) / 32.0
            
            vertical = np.array([
                [-3, -10, -3],
                [0, 0, 0],
                [3, 10, 3]
            ]) / 32.0
            
        else:
            raise ValueError(f"Unknown edge detector type: {kernel_type}")
        
        return horizontal, vertical
    
    @staticmethod
    def custom_kernel(size: int, kernel_type: str = 'uniform') -> np.ndarray:
        """
        Generate custom kernels for specific purposes.
        
        Args:
            size: Kernel size
            kernel_type: Type of kernel ('uniform', 'center_weighted', 'edge_weighted')
            
        Returns:
            2D kernel
        """
        if kernel_type == 'uniform':
            kernel = np.ones((size, size)) / (size * size)
            
        elif kernel_type == 'center_weighted':
            kernel = np.zeros((size, size))
            center = size // 2
            
            for i in range(size):
                for j in range(size):
                    dist = np.sqrt((i - center)**2 + (j - center)**2)
                    kernel[i, j] = np.exp(-dist**2 / (size / 2.0)**2)
            
            kernel /= np.sum(kernel)
            
        elif kernel_type == 'edge_weighted':
            kernel = np.ones((size, size))
            center = size // 2
            
            for i in range(size):
                for j in range(size):
                    dist = np.sqrt((i - center)**2 + (j - center)**2)
                    kernel[i, j] = dist + 1
            
            kernel /= np.sum(kernel)
            
        else:
            raise ValueError(f"Unknown custom kernel type: {kernel_type}")
        
        return kernel
    
    @staticmethod
    def get_2d_wavelet_kernels(kernel_type: str = 'haar', 
                               size: int = 2) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Generate 2D wavelet transform kernels (LL, LH, HL, HH).
        
        Args:
            kernel_type: Type of wavelet ('haar', 'db2', 'db4')
            size: Kernel size (for Haar only)
            
        Returns:
            Tuple of (LL_kernel, LH_kernel, HL_kernel, HH_kernel)
        """
        if kernel_type == 'haar':
            low_pass, high_pass = KernelGenerator.haar_kernel(size)
        elif kernel_type == 'db2':
            low_pass, high_pass = KernelGenerator.db2_kernel()
        elif kernel_type == 'db4':
            low_pass, high_pass = KernelGenerator.db4_kernel()
        else:
            raise ValueError(f"Unknown wavelet kernel type: {kernel_type}")
        
        # Create 2D kernels
        LL = np.outer(low_pass, low_pass)
        LH = np.outer(low_pass, high_pass)
        HL = np.outer(high_pass, low_pass)
        HH = np.outer(high_pass, high_pass)
        
        return LL, LH, HL, HH


def apply_kernel_to_image(image: np.ndarray, 
                         kernel: np.ndarray,
                         stride: Optional[int] = None) -> np.ndarray:
    """
    Apply a kernel to an image with specified stride.
    
    Args:
        image: Input image
        kernel: Convolution kernel
        stride: Stride for convolution (if None, uses kernel size)
        
    Returns:
        Convolved image
    """
    kernel_size = kernel.shape[0]
    if stride is None:
        stride = kernel_size
    
    # Pad image if necessary
    pad_h = (stride - image.shape[0] % stride) % stride
    pad_w = (stride - image.shape[1] % stride) % stride
    
    if pad_h > 0 or pad_w > 0:
        image = np.pad(image, ((0, pad_h), (0, pad_w)), mode='reflect')
    
    height, width = image.shape
    output_height = (height - kernel_size) // stride + 1
    output_width = (width - kernel_size) // stride + 1
    output = np.zeros((output_height, output_width))
    
    for i in range(output_height):
        for j in range(output_width):
            patch = image[i*stride:i*stride+kernel_size, j*stride:j*stride+kernel_size]
            output[i, j] = np.sum(patch * kernel)
    
    return output


def compare_kernels(image: np.ndarray, 
                   kernel_types: list = ['haar', 'db2', 'db4'],
                   size: int = 2) -> dict:
    """
    Compare different kernel types on the same image.
    
    Args:
        image: Input image
        kernel_types: List of kernel types to compare
        size: Kernel size (for applicable kernels)
        
    Returns:
        Dictionary with results for each kernel type
    """
    results = {}
    
    for kernel_type in kernel_types:
        try:
            LL, LH, HL, HH = KernelGenerator.get_2d_wavelet_kernels(kernel_type, size)
            
            LL_result = apply_kernel_to_image(image, LL)
            LH_result = apply_kernel_to_image(image, LH)
            HL_result = apply_kernel_to_image(image, HL)
            HH_result = apply_kernel_to_image(image, HH)
            
            results[kernel_type] = {
                'LL': LL_result,
                'LH': LH_result,
                'HL': HL_result,
                'HH': HH_result
            }
        except Exception as e:
            print(f"Error processing kernel type {kernel_type}: {e}")
    
    return results
