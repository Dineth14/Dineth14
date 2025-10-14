"""
Core Haar Wavelet Transform Implementation
Supports multiple kernel sizes, decomposition levels, and color images.
"""

import numpy as np
from typing import Tuple, Optional


class HaarWaveletTransform:
    """
    Implements Haar wavelet transform for images with support for multiple kernel sizes.
    """
    
    def __init__(self, kernel_size: int = 2):
        """
        Initialize Haar wavelet transform.
        
        Args:
            kernel_size: Size of the wavelet kernel (2, 4, 8, 16, or custom)
        """
        self.kernel_size = kernel_size
        self.scaling_factor = 1.0 / np.sqrt(kernel_size)
        
    def _get_haar_filters(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Generate Haar low-pass and high-pass filters for the given kernel size.
        
        Returns:
            Tuple of (low_pass_filter, high_pass_filter)
        """
        # Low-pass filter (averaging)
        low_pass = np.ones(self.kernel_size) * self.scaling_factor
        
        # High-pass filter (differencing)
        high_pass = np.ones(self.kernel_size) * self.scaling_factor
        high_pass[self.kernel_size // 2:] *= -1
        
        return low_pass, high_pass
    
    def dwt_1d(self, signal: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Perform 1D discrete wavelet transform on a signal.
        
        Args:
            signal: Input 1D signal
            
        Returns:
            Tuple of (approximation_coefficients, detail_coefficients)
        """
        low_pass, high_pass = self._get_haar_filters()
        
        # Pad signal if necessary
        pad_length = (self.kernel_size - len(signal) % self.kernel_size) % self.kernel_size
        if pad_length > 0:
            signal = np.pad(signal, (0, pad_length), mode='reflect')
        
        # Reshape for convolution
        reshaped = signal.reshape(-1, self.kernel_size)
        
        # Apply filters
        approx = np.dot(reshaped, low_pass)
        detail = np.dot(reshaped, high_pass)
        
        return approx, detail
    
    def idwt_1d(self, approx: np.ndarray, detail: np.ndarray) -> np.ndarray:
        """
        Perform inverse 1D discrete wavelet transform.
        
        Args:
            approx: Approximation coefficients
            detail: Detail coefficients
            
        Returns:
            Reconstructed signal
        """
        low_pass, high_pass = self._get_haar_filters()
        
        # Reconstruction
        reconstructed = np.zeros(len(approx) * self.kernel_size)
        
        for i in range(len(approx)):
            start_idx = i * self.kernel_size
            end_idx = start_idx + self.kernel_size
            reconstructed[start_idx:end_idx] = (
                approx[i] * low_pass + detail[i] * high_pass
            )
        
        return reconstructed
    
    def dwt_2d(self, image: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Perform 2D discrete wavelet transform on an image.
        
        Args:
            image: Input 2D image array
            
        Returns:
            Tuple of (LL, LH, HL, HH) subbands
            - LL: Low-Low (approximation)
            - LH: Low-High (horizontal details)
            - HL: High-Low (vertical details)
            - HH: High-High (diagonal details)
        """
        height, width = image.shape
        
        # Pad image if necessary
        pad_h = (self.kernel_size - height % self.kernel_size) % self.kernel_size
        pad_w = (self.kernel_size - width % self.kernel_size) % self.kernel_size
        
        if pad_h > 0 or pad_w > 0:
            image = np.pad(image, ((0, pad_h), (0, pad_w)), mode='reflect')
        
        height, width = image.shape
        
        # Row-wise transform
        row_approx = np.zeros((height, width // self.kernel_size))
        row_detail = np.zeros((height, width // self.kernel_size))
        
        for i in range(height):
            row_approx[i, :], row_detail[i, :] = self.dwt_1d(image[i, :])
        
        # Column-wise transform on approximation
        LL = np.zeros((height // self.kernel_size, width // self.kernel_size))
        HL = np.zeros((height // self.kernel_size, width // self.kernel_size))
        
        for j in range(width // self.kernel_size):
            LL[:, j], HL[:, j] = self.dwt_1d(row_approx[:, j])
        
        # Column-wise transform on detail
        LH = np.zeros((height // self.kernel_size, width // self.kernel_size))
        HH = np.zeros((height // self.kernel_size, width // self.kernel_size))
        
        for j in range(width // self.kernel_size):
            LH[:, j], HH[:, j] = self.dwt_1d(row_detail[:, j])
        
        return LL, LH, HL, HH
    
    def idwt_2d(self, LL: np.ndarray, LH: np.ndarray, 
                HL: np.ndarray, HH: np.ndarray) -> np.ndarray:
        """
        Perform inverse 2D discrete wavelet transform.
        
        Args:
            LL: Low-Low subband (approximation)
            LH: Low-High subband (horizontal details)
            HL: High-Low subband (vertical details)
            HH: High-High subband (diagonal details)
            
        Returns:
            Reconstructed 2D image
        """
        height_sub, width_sub = LL.shape
        
        # Inverse column-wise transform
        row_approx = np.zeros((height_sub * self.kernel_size, width_sub))
        row_detail = np.zeros((height_sub * self.kernel_size, width_sub))
        
        for j in range(width_sub):
            row_approx[:, j] = self.idwt_1d(LL[:, j], HL[:, j])
            row_detail[:, j] = self.idwt_1d(LH[:, j], HH[:, j])
        
        # Inverse row-wise transform
        height = height_sub * self.kernel_size
        width = width_sub * self.kernel_size
        reconstructed = np.zeros((height, width))
        
        for i in range(height):
            reconstructed[i, :] = self.idwt_1d(row_approx[i, :], row_detail[i, :])
        
        return reconstructed
    
    def multilevel_dwt_2d(self, image: np.ndarray, levels: int = 1) -> dict:
        """
        Perform multi-level 2D discrete wavelet transform.
        
        Args:
            image: Input 2D image array
            levels: Number of decomposition levels
            
        Returns:
            Dictionary containing all subbands at each level
        """
        result = {'original_shape': image.shape}
        current_image = image.copy()
        
        for level in range(1, levels + 1):
            LL, LH, HL, HH = self.dwt_2d(current_image)
            result[f'level_{level}'] = {
                'LL': LL,
                'LH': LH,
                'HL': HL,
                'HH': HH
            }
            current_image = LL
        
        return result
    
    def multilevel_idwt_2d(self, decomposition: dict) -> np.ndarray:
        """
        Perform multi-level inverse 2D discrete wavelet transform.
        
        Args:
            decomposition: Dictionary from multilevel_dwt_2d
            
        Returns:
            Reconstructed image
        """
        levels = len([k for k in decomposition.keys() if k.startswith('level_')])
        
        # Start with the deepest level LL
        current_image = decomposition[f'level_{levels}']['LL']
        
        # Reconstruct level by level
        for level in range(levels, 0, -1):
            level_data = decomposition[f'level_{level}']
            current_image = self.idwt_2d(
                current_image,
                level_data['LH'],
                level_data['HL'],
                level_data['HH']
            )
        
        return current_image


def process_color_image(image: np.ndarray, kernel_size: int = 2, 
                        levels: int = 1) -> dict:
    """
    Process a color image by applying wavelet transform to each channel separately.
    
    Args:
        image: Input color image (H x W x C)
        kernel_size: Size of the wavelet kernel
        levels: Number of decomposition levels
        
    Returns:
        Dictionary containing decomposition for each channel
    """
    if len(image.shape) == 2:
        # Grayscale image
        transformer = HaarWaveletTransform(kernel_size)
        return {'channel_0': transformer.multilevel_dwt_2d(image, levels)}
    
    # Color image - process each channel
    result = {}
    transformer = HaarWaveletTransform(kernel_size)
    
    for channel in range(image.shape[2]):
        channel_data = image[:, :, channel]
        result[f'channel_{channel}'] = transformer.multilevel_dwt_2d(channel_data, levels)
    
    return result


def reconstruct_color_image(decomposition: dict, kernel_size: int = 2) -> np.ndarray:
    """
    Reconstruct a color image from wavelet decomposition.
    
    Args:
        decomposition: Dictionary from process_color_image
        kernel_size: Size of the wavelet kernel
        
    Returns:
        Reconstructed color image
    """
    transformer = HaarWaveletTransform(kernel_size)
    channels = []
    
    for key in sorted(decomposition.keys()):
        if key.startswith('channel_'):
            reconstructed = transformer.multilevel_idwt_2d(decomposition[key])
            channels.append(reconstructed)
    
    if len(channels) == 1:
        return channels[0]
    
    return np.stack(channels, axis=2)
