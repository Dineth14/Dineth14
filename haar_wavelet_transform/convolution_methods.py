"""
Different convolution traversal methods for wavelet transforms.
Implements standard and custom traversal patterns.
"""

import numpy as np
from typing import List, Tuple, Callable, Generator


class ConvolutionTraversal:
    """
    Implements various convolution traversal patterns.
    """
    
    def __init__(self, image_shape: Tuple[int, int], kernel_size: int):
        """
        Initialize convolution traversal.
        
        Args:
            image_shape: Shape of the image (height, width)
            kernel_size: Size of the kernel
        """
        self.height, self.width = image_shape
        self.kernel_size = kernel_size
        
    def left_to_right_order(self) -> List[Tuple[int, int]]:
        """
        Generate left-to-right (row-major) traversal order.
        Standard convolution order.
        
        Returns:
            List of (row, col) tuples representing traversal order
        """
        order = []
        for i in range(0, self.height, self.kernel_size):
            for j in range(0, self.width, self.kernel_size):
                order.append((i, j))
        return order
    
    def up_down_order(self) -> List[Tuple[int, int]]:
        """
        Generate up-down (column-major) traversal order.
        Vertical traversal.
        
        Returns:
            List of (row, col) tuples representing traversal order
        """
        order = []
        for j in range(0, self.width, self.kernel_size):
            for i in range(0, self.height, self.kernel_size):
                order.append((i, j))
        return order
    
    def zigzag_order(self) -> List[Tuple[int, int]]:
        """
        Generate zigzag (diagonal) traversal order.
        Similar to JPEG encoding pattern.
        
        Returns:
            List of (row, col) tuples representing traversal order
        """
        order = []
        max_sum = (self.height // self.kernel_size - 1) + (self.width // self.kernel_size - 1)
        
        for s in range(max_sum + 1):
            # Determine if we're going up or down
            if s % 2 == 0:
                # Going down-left
                for i in range(min(s, self.height // self.kernel_size - 1), -1, -1):
                    j = s - i
                    if j < self.width // self.kernel_size:
                        order.append((i * self.kernel_size, j * self.kernel_size))
            else:
                # Going up-right
                for j in range(min(s, self.width // self.kernel_size - 1), -1, -1):
                    i = s - j
                    if i < self.height // self.kernel_size:
                        order.append((i * self.kernel_size, j * self.kernel_size))
        
        return order
    
    def custom_block_order(self) -> List[Tuple[int, int]]:
        """
        Generate custom block traversal order with repeating pattern:
        1. Move down through the block
        2. Move diagonally up (up-right direction)
        3. Move horizontally (left to right)
        4. Move diagonally down (down-right direction)
        5. Repeat
        
        Returns:
            List of (row, col) tuples representing traversal order
        """
        order = []
        visited = set()
        
        # Start from top-left
        i, j = 0, 0
        pattern_step = 0  # Track which step in the pattern we're at
        
        while len(visited) < (self.height // self.kernel_size) * (self.width // self.kernel_size):
            pos = (i * self.kernel_size, j * self.kernel_size)
            
            if (i, j) not in visited and 0 <= i < self.height // self.kernel_size and 0 <= j < self.width // self.kernel_size:
                order.append(pos)
                visited.add((i, j))
            
            # Follow the pattern
            if pattern_step == 0:  # Move down
                next_i, next_j = i + 1, j
                if (next_i, next_j) not in visited and next_i < self.height // self.kernel_size:
                    i, j = next_i, next_j
                else:
                    pattern_step = 1
                    
            elif pattern_step == 1:  # Move diagonally up-right
                next_i, next_j = i - 1, j + 1
                if (next_i, next_j) not in visited and next_i >= 0 and next_j < self.width // self.kernel_size:
                    i, j = next_i, next_j
                else:
                    pattern_step = 2
                    
            elif pattern_step == 2:  # Move horizontally right
                next_i, next_j = i, j + 1
                if (next_i, next_j) not in visited and next_j < self.width // self.kernel_size:
                    i, j = next_i, next_j
                else:
                    pattern_step = 3
                    
            elif pattern_step == 3:  # Move diagonally down-right
                next_i, next_j = i + 1, j + 1
                if (next_i, next_j) not in visited and next_i < self.height // self.kernel_size and next_j < self.width // self.kernel_size:
                    i, j = next_i, next_j
                else:
                    pattern_step = 0
                    
            # If stuck, find next unvisited position
            if (i, j) in visited:
                found = False
                for ii in range(self.height // self.kernel_size):
                    for jj in range(self.width // self.kernel_size):
                        if (ii, jj) not in visited:
                            i, j = ii, jj
                            pattern_step = 0
                            found = True
                            break
                    if found:
                        break
                if not found:
                    break
        
        return order


def apply_convolution_with_traversal(image: np.ndarray, 
                                     kernel: np.ndarray,
                                     traversal_method: str = 'left_to_right') -> np.ndarray:
    """
    Apply convolution using a specific traversal method.
    
    Args:
        image: Input image
        kernel: Convolution kernel
        traversal_method: One of 'left_to_right', 'up_down', 'zigzag', 'custom_block'
        
    Returns:
        Convolved image
    """
    kernel_size = kernel.shape[0]
    
    # Pad image if necessary
    pad_h = (kernel_size - image.shape[0] % kernel_size) % kernel_size
    pad_w = (kernel_size - image.shape[1] % kernel_size) % kernel_size
    
    if pad_h > 0 or pad_w > 0:
        image = np.pad(image, ((0, pad_h), (0, pad_w)), mode='reflect')
    
    height, width = image.shape
    output_height = height // kernel_size
    output_width = width // kernel_size
    output = np.zeros((output_height, output_width))
    
    # Get traversal order
    traversal = ConvolutionTraversal((height, width), kernel_size)
    
    if traversal_method == 'left_to_right':
        order = traversal.left_to_right_order()
    elif traversal_method == 'up_down':
        order = traversal.up_down_order()
    elif traversal_method == 'zigzag':
        order = traversal.zigzag_order()
    elif traversal_method == 'custom_block':
        order = traversal.custom_block_order()
    else:
        raise ValueError(f"Unknown traversal method: {traversal_method}")
    
    # Apply convolution in the specified order
    for idx, (i, j) in enumerate(order):
        # Extract patch
        patch = image[i:i+kernel_size, j:j+kernel_size]
        
        # Apply kernel
        result = np.sum(patch * kernel) / (kernel_size * kernel_size)
        
        # Store in output
        out_i = i // kernel_size
        out_j = j // kernel_size
        output[out_i, out_j] = result
    
    return output


def wavelet_transform_with_traversal(image: np.ndarray,
                                     kernel_size: int = 2,
                                     traversal_method: str = 'left_to_right') -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Perform wavelet transform using a specific traversal method.
    
    Args:
        image: Input image
        kernel_size: Size of the wavelet kernel
        traversal_method: Traversal pattern to use
        
    Returns:
        Tuple of (LL, LH, HL, HH) subbands
    """
    # Create Haar filters
    scaling_factor = 1.0 / np.sqrt(kernel_size)
    
    low_kernel_1d = np.ones(kernel_size) * scaling_factor
    high_kernel_1d = np.ones(kernel_size) * scaling_factor
    high_kernel_1d[kernel_size // 2:] *= -1
    
    # Create 2D kernels
    LL_kernel = np.outer(low_kernel_1d, low_kernel_1d)
    LH_kernel = np.outer(low_kernel_1d, high_kernel_1d)
    HL_kernel = np.outer(high_kernel_1d, low_kernel_1d)
    HH_kernel = np.outer(high_kernel_1d, high_kernel_1d)
    
    # Apply convolution with specified traversal
    LL = apply_convolution_with_traversal(image, LL_kernel, traversal_method)
    LH = apply_convolution_with_traversal(image, LH_kernel, traversal_method)
    HL = apply_convolution_with_traversal(image, HL_kernel, traversal_method)
    HH = apply_convolution_with_traversal(image, HH_kernel, traversal_method)
    
    return LL, LH, HL, HH


def get_traversal_visualization(image_shape: Tuple[int, int], 
                                kernel_size: int,
                                traversal_method: str) -> np.ndarray:
    """
    Create a visualization of the traversal order.
    
    Args:
        image_shape: Shape of the image (height, width)
        kernel_size: Size of the kernel
        traversal_method: Traversal pattern to visualize
        
    Returns:
        Array where values represent the order of traversal
    """
    height, width = image_shape
    visualization = np.zeros((height // kernel_size, width // kernel_size))
    
    traversal = ConvolutionTraversal(image_shape, kernel_size)
    
    if traversal_method == 'left_to_right':
        order = traversal.left_to_right_order()
    elif traversal_method == 'up_down':
        order = traversal.up_down_order()
    elif traversal_method == 'zigzag':
        order = traversal.zigzag_order()
    elif traversal_method == 'custom_block':
        order = traversal.custom_block_order()
    else:
        raise ValueError(f"Unknown traversal method: {traversal_method}")
    
    for idx, (i, j) in enumerate(order):
        visualization[i // kernel_size, j // kernel_size] = idx
    
    return visualization
