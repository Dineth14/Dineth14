"""
Comparison and analysis tools for wavelet transforms.
Includes metrics calculation and statistical analysis.
"""

import numpy as np
import time
from typing import Dict, Tuple, Optional, List


class WaveletMetrics:
    """
    Calculates various metrics for wavelet transform analysis.
    """
    
    @staticmethod
    def mse(original: np.ndarray, reconstructed: np.ndarray) -> float:
        """
        Calculate Mean Squared Error.
        
        Args:
            original: Original image
            reconstructed: Reconstructed image
            
        Returns:
            MSE value
        """
        # Ensure same shape
        min_h = min(original.shape[0], reconstructed.shape[0])
        min_w = min(original.shape[1], reconstructed.shape[1])
        
        original = original[:min_h, :min_w]
        reconstructed = reconstructed[:min_h, :min_w]
        
        return np.mean((original - reconstructed) ** 2)
    
    @staticmethod
    def psnr(original: np.ndarray, reconstructed: np.ndarray, max_value: float = 255.0) -> float:
        """
        Calculate Peak Signal-to-Noise Ratio.
        
        Args:
            original: Original image
            reconstructed: Reconstructed image
            max_value: Maximum possible pixel value
            
        Returns:
            PSNR value in dB
        """
        mse_value = WaveletMetrics.mse(original, reconstructed)
        
        if mse_value == 0:
            return float('inf')
        
        return 10 * np.log10((max_value ** 2) / mse_value)
    
    @staticmethod
    def compression_ratio(original_size: int, compressed_size: int) -> float:
        """
        Calculate compression ratio.
        
        Args:
            original_size: Size of original data
            compressed_size: Size of compressed data
            
        Returns:
            Compression ratio
        """
        return original_size / compressed_size if compressed_size > 0 else 0
    
    @staticmethod
    def energy_preservation(original: np.ndarray, 
                           LL: np.ndarray, LH: np.ndarray,
                           HL: np.ndarray, HH: np.ndarray) -> float:
        """
        Calculate energy preservation ratio.
        
        Args:
            original: Original image
            LL, LH, HL, HH: Wavelet subbands
            
        Returns:
            Energy preservation ratio (should be close to 1.0)
        """
        original_energy = np.sum(original ** 2)
        subband_energy = np.sum(LL ** 2) + np.sum(LH ** 2) + np.sum(HL ** 2) + np.sum(HH ** 2)
        
        return subband_energy / original_energy if original_energy > 0 else 0
    
    @staticmethod
    def entropy(image: np.ndarray) -> float:
        """
        Calculate Shannon entropy of an image.
        
        Args:
            image: Input image
            
        Returns:
            Entropy value
        """
        # Normalize to [0, 255] and convert to integer
        img_normalized = ((image - image.min()) / (image.max() - image.min()) * 255).astype(int)
        
        # Calculate histogram
        hist, _ = np.histogram(img_normalized, bins=256, range=(0, 256))
        
        # Calculate probabilities
        probs = hist / np.sum(hist)
        
        # Remove zeros
        probs = probs[probs > 0]
        
        # Calculate entropy
        return -np.sum(probs * np.log2(probs))
    
    @staticmethod
    def snr(original: np.ndarray, reconstructed: np.ndarray) -> float:
        """
        Calculate Signal-to-Noise Ratio.
        
        Args:
            original: Original image
            reconstructed: Reconstructed image
            
        Returns:
            SNR value in dB
        """
        # Ensure same shape
        min_h = min(original.shape[0], reconstructed.shape[0])
        min_w = min(original.shape[1], reconstructed.shape[1])
        
        original = original[:min_h, :min_w]
        reconstructed = reconstructed[:min_h, :min_w]
        
        signal_power = np.sum(original ** 2)
        noise_power = np.sum((original - reconstructed) ** 2)
        
        if noise_power == 0:
            return float('inf')
        
        return 10 * np.log10(signal_power / noise_power)


class MethodComparison:
    """
    Compares different wavelet transform methods.
    """
    
    def __init__(self):
        """Initialize comparison framework."""
        self.results = {}
    
    def compare_kernel_sizes(self, image: np.ndarray, 
                            kernel_sizes: List[int],
                            transform_func) -> Dict:
        """
        Compare different kernel sizes.
        
        Args:
            image: Input image
            kernel_sizes: List of kernel sizes to compare
            transform_func: Function to perform transform
            
        Returns:
            Dictionary with comparison results
        """
        results = {}
        
        for size in kernel_sizes:
            start_time = time.time()
            
            try:
                # Perform transform
                LL, LH, HL, HH = transform_func(image, size)
                
                # Calculate metrics
                energy = WaveletMetrics.energy_preservation(image, LL, LH, HL, HH)
                
                elapsed_time = time.time() - start_time
                
                results[f'kernel_{size}x{size}'] = {
                    'LL': LL,
                    'LH': LH,
                    'HL': HL,
                    'HH': HH,
                    'energy_preservation': energy,
                    'processing_time': elapsed_time,
                    'original_shape': image.shape,
                    'subband_shapes': {
                        'LL': LL.shape,
                        'LH': LH.shape,
                        'HL': HL.shape,
                        'HH': HH.shape
                    }
                }
            except Exception as e:
                print(f"Error processing kernel size {size}: {e}")
                results[f'kernel_{size}x{size}'] = {'error': str(e)}
        
        return results
    
    def compare_traversal_methods(self, image: np.ndarray,
                                  kernel_size: int,
                                  traversal_methods: List[str],
                                  transform_func) -> Dict:
        """
        Compare different traversal methods.
        
        Args:
            image: Input image
            kernel_size: Kernel size to use
            traversal_methods: List of traversal methods
            transform_func: Function to perform transform with traversal
            
        Returns:
            Dictionary with comparison results
        """
        results = {}
        
        for method in traversal_methods:
            start_time = time.time()
            
            try:
                # Perform transform with specific traversal
                LL, LH, HL, HH = transform_func(image, kernel_size, method)
                
                # Calculate metrics
                energy = WaveletMetrics.energy_preservation(image, LL, LH, HL, HH)
                
                elapsed_time = time.time() - start_time
                
                results[method] = {
                    'LL': LL,
                    'LH': LH,
                    'HL': HL,
                    'HH': HH,
                    'energy_preservation': energy,
                    'processing_time': elapsed_time
                }
            except Exception as e:
                print(f"Error processing traversal method {method}: {e}")
                results[method] = {'error': str(e)}
        
        return results
    
    def compare_with_reconstruction(self, image: np.ndarray,
                                   transform_func,
                                   inverse_func,
                                   **kwargs) -> Dict:
        """
        Compare transform and reconstruction quality.
        
        Args:
            image: Input image
            transform_func: Forward transform function
            inverse_func: Inverse transform function
            **kwargs: Additional arguments for transform
            
        Returns:
            Dictionary with comparison results
        """
        start_time = time.time()
        
        # Forward transform
        LL, LH, HL, HH = transform_func(image, **kwargs)
        transform_time = time.time() - start_time
        
        # Inverse transform
        start_time = time.time()
        reconstructed = inverse_func(LL, LH, HL, HH)
        inverse_time = time.time() - start_time
        
        # Calculate metrics
        mse = WaveletMetrics.mse(image, reconstructed)
        psnr = WaveletMetrics.psnr(image, reconstructed, max_value=image.max())
        snr = WaveletMetrics.snr(image, reconstructed)
        energy = WaveletMetrics.energy_preservation(image, LL, LH, HL, HH)
        
        return {
            'original': image,
            'reconstructed': reconstructed,
            'subbands': {'LL': LL, 'LH': LH, 'HL': HL, 'HH': HH},
            'metrics': {
                'mse': mse,
                'psnr': psnr,
                'snr': snr,
                'energy_preservation': energy,
                'transform_time': transform_time,
                'inverse_time': inverse_time,
                'total_time': transform_time + inverse_time
            }
        }
    
    def generate_comparison_table(self, comparisons: Dict) -> str:
        """
        Generate a formatted comparison table.
        
        Args:
            comparisons: Dictionary with comparison results
            
        Returns:
            Formatted string table
        """
        table = []
        table.append("=" * 80)
        table.append("Wavelet Transform Comparison Results")
        table.append("=" * 80)
        
        for name, data in comparisons.items():
            table.append(f"\n{name}:")
            table.append("-" * 80)
            
            if 'error' in data:
                table.append(f"  Error: {data['error']}")
                continue
            
            if 'metrics' in data:
                metrics = data['metrics']
                table.append(f"  MSE:                  {metrics.get('mse', 'N/A'):.6f}")
                table.append(f"  PSNR:                 {metrics.get('psnr', 'N/A'):.2f} dB")
                table.append(f"  SNR:                  {metrics.get('snr', 'N/A'):.2f} dB")
                table.append(f"  Energy Preservation:  {metrics.get('energy_preservation', 'N/A'):.6f}")
                table.append(f"  Transform Time:       {metrics.get('transform_time', 'N/A'):.4f} s")
                table.append(f"  Inverse Time:         {metrics.get('inverse_time', 'N/A'):.4f} s")
                table.append(f"  Total Time:           {metrics.get('total_time', 'N/A'):.4f} s")
            else:
                if 'energy_preservation' in data:
                    table.append(f"  Energy Preservation:  {data['energy_preservation']:.6f}")
                if 'processing_time' in data:
                    table.append(f"  Processing Time:      {data['processing_time']:.4f} s")
                if 'subband_shapes' in data:
                    table.append(f"  Subband Shapes:")
                    for sb, shape in data['subband_shapes'].items():
                        table.append(f"    {sb}: {shape}")
        
        table.append("=" * 80)
        return "\n".join(table)


def benchmark_performance(image: np.ndarray,
                         transform_func,
                         iterations: int = 10,
                         **kwargs) -> Dict:
    """
    Benchmark performance of a transform function.
    
    Args:
        image: Input image
        transform_func: Transform function to benchmark
        iterations: Number of iterations
        **kwargs: Additional arguments for transform
        
    Returns:
        Dictionary with benchmark results
    """
    times = []
    
    for _ in range(iterations):
        start_time = time.time()
        _ = transform_func(image, **kwargs)
        elapsed = time.time() - start_time
        times.append(elapsed)
    
    return {
        'mean_time': np.mean(times),
        'std_time': np.std(times),
        'min_time': np.min(times),
        'max_time': np.max(times),
        'iterations': iterations
    }
