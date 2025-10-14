"""
Visualization tools for wavelet transforms.
Includes plotting functions for subbands, comparisons, and analysis.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from typing import Dict, List, Optional, Tuple


class WaveletVisualizer:
    """
    Visualizes wavelet transform results and comparisons.
    """
    
    @staticmethod
    def plot_subbands(LL: np.ndarray, LH: np.ndarray, 
                     HL: np.ndarray, HH: np.ndarray,
                     title: str = "Wavelet Decomposition",
                     figsize: Tuple[int, int] = (12, 10),
                     save_path: Optional[str] = None):
        """
        Plot the four wavelet subbands.
        
        Args:
            LL: Low-Low subband (approximation)
            LH: Low-High subband (horizontal details)
            HL: High-Low subband (vertical details)
            HH: High-High subband (diagonal details)
            title: Plot title
            figsize: Figure size
            save_path: Path to save the figure (optional)
        """
        fig, axes = plt.subplots(2, 2, figsize=figsize)
        
        # LL subband
        im1 = axes[0, 0].imshow(LL, cmap='gray')
        axes[0, 0].set_title('LL (Approximation)')
        axes[0, 0].axis('off')
        plt.colorbar(im1, ax=axes[0, 0], fraction=0.046)
        
        # LH subband
        im2 = axes[0, 1].imshow(LH, cmap='gray')
        axes[0, 1].set_title('LH (Horizontal Details)')
        axes[0, 1].axis('off')
        plt.colorbar(im2, ax=axes[0, 1], fraction=0.046)
        
        # HL subband
        im3 = axes[1, 0].imshow(HL, cmap='gray')
        axes[1, 0].set_title('HL (Vertical Details)')
        axes[1, 0].axis('off')
        plt.colorbar(im3, ax=axes[1, 0], fraction=0.046)
        
        # HH subband
        im4 = axes[1, 1].imshow(HH, cmap='gray')
        axes[1, 1].set_title('HH (Diagonal Details)')
        axes[1, 1].axis('off')
        plt.colorbar(im4, ax=axes[1, 1], fraction=0.046)
        
        fig.suptitle(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    @staticmethod
    def plot_reconstruction_comparison(original: np.ndarray,
                                       reconstructed: np.ndarray,
                                       difference: Optional[np.ndarray] = None,
                                       title: str = "Reconstruction Comparison",
                                       figsize: Tuple[int, int] = (15, 5),
                                       save_path: Optional[str] = None):
        """
        Plot original, reconstructed, and difference images.
        
        Args:
            original: Original image
            reconstructed: Reconstructed image
            difference: Difference image (optional, will be calculated if not provided)
            title: Plot title
            figsize: Figure size
            save_path: Path to save the figure (optional)
        """
        if difference is None:
            # Ensure same shape
            min_h = min(original.shape[0], reconstructed.shape[0])
            min_w = min(original.shape[1], reconstructed.shape[1])
            original_crop = original[:min_h, :min_w]
            reconstructed_crop = reconstructed[:min_h, :min_w]
            difference = np.abs(original_crop - reconstructed_crop)
        
        fig, axes = plt.subplots(1, 3, figsize=figsize)
        
        # Original
        axes[0].imshow(original, cmap='gray')
        axes[0].set_title('Original')
        axes[0].axis('off')
        
        # Reconstructed
        axes[1].imshow(reconstructed, cmap='gray')
        axes[1].set_title('Reconstructed')
        axes[1].axis('off')
        
        # Difference
        im = axes[2].imshow(difference, cmap='hot')
        axes[2].set_title('Difference (Amplified)')
        axes[2].axis('off')
        plt.colorbar(im, ax=axes[2], fraction=0.046)
        
        fig.suptitle(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    @staticmethod
    def plot_kernel_size_comparison(results: Dict,
                                    title: str = "Kernel Size Comparison",
                                    figsize: Tuple[int, int] = (20, 12),
                                    save_path: Optional[str] = None):
        """
        Plot comparison of different kernel sizes.
        
        Args:
            results: Dictionary with results for different kernel sizes
            title: Plot title
            figsize: Figure size
            save_path: Path to save the figure (optional)
        """
        n_kernels = len(results)
        fig = plt.figure(figsize=figsize)
        gs = GridSpec(n_kernels, 4, figure=fig)
        
        for idx, (kernel_name, data) in enumerate(results.items()):
            if 'error' in data:
                continue
            
            # LL
            ax = fig.add_subplot(gs[idx, 0])
            ax.imshow(data['LL'], cmap='gray')
            ax.set_title(f'{kernel_name} - LL')
            ax.axis('off')
            
            # LH
            ax = fig.add_subplot(gs[idx, 1])
            ax.imshow(data['LH'], cmap='gray')
            ax.set_title(f'{kernel_name} - LH')
            ax.axis('off')
            
            # HL
            ax = fig.add_subplot(gs[idx, 2])
            ax.imshow(data['HL'], cmap='gray')
            ax.set_title(f'{kernel_name} - HL')
            ax.axis('off')
            
            # HH
            ax = fig.add_subplot(gs[idx, 3])
            ax.imshow(data['HH'], cmap='gray')
            ax.set_title(f'{kernel_name} - HH')
            ax.axis('off')
        
        fig.suptitle(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    @staticmethod
    def plot_traversal_comparison(results: Dict,
                                  title: str = "Traversal Method Comparison",
                                  figsize: Tuple[int, int] = (20, 12),
                                  save_path: Optional[str] = None):
        """
        Plot comparison of different traversal methods.
        
        Args:
            results: Dictionary with results for different traversal methods
            title: Plot title
            figsize: Figure size
            save_path: Path to save the figure (optional)
        """
        n_methods = len(results)
        fig = plt.figure(figsize=figsize)
        gs = GridSpec(n_methods, 4, figure=fig)
        
        for idx, (method_name, data) in enumerate(results.items()):
            if 'error' in data:
                continue
            
            # LL
            ax = fig.add_subplot(gs[idx, 0])
            ax.imshow(data['LL'], cmap='gray')
            ax.set_title(f'{method_name} - LL')
            ax.axis('off')
            
            # LH
            ax = fig.add_subplot(gs[idx, 1])
            ax.imshow(data['LH'], cmap='gray')
            ax.set_title(f'{method_name} - LH')
            ax.axis('off')
            
            # HL
            ax = fig.add_subplot(gs[idx, 2])
            ax.imshow(data['HL'], cmap='gray')
            ax.set_title(f'{method_name} - HL')
            ax.axis('off')
            
            # HH
            ax = fig.add_subplot(gs[idx, 3])
            ax.imshow(data['HH'], cmap='gray')
            ax.set_title(f'{method_name} - HH')
            ax.axis('off')
        
        fig.suptitle(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    @staticmethod
    def plot_metrics_comparison(comparisons: Dict,
                               metric_names: List[str] = ['psnr', 'mse', 'energy_preservation'],
                               title: str = "Metrics Comparison",
                               figsize: Tuple[int, int] = (15, 5),
                               save_path: Optional[str] = None):
        """
        Plot bar charts comparing metrics across different methods.
        
        Args:
            comparisons: Dictionary with comparison results
            metric_names: List of metrics to plot
            title: Plot title
            figsize: Figure size
            save_path: Path to save the figure (optional)
        """
        n_metrics = len(metric_names)
        fig, axes = plt.subplots(1, n_metrics, figsize=figsize)
        
        if n_metrics == 1:
            axes = [axes]
        
        for idx, metric in enumerate(metric_names):
            methods = []
            values = []
            
            for method_name, data in comparisons.items():
                if 'error' in data:
                    continue
                
                if 'metrics' in data and metric in data['metrics']:
                    methods.append(method_name)
                    values.append(data['metrics'][metric])
                elif metric in data:
                    methods.append(method_name)
                    values.append(data[metric])
            
            if methods:
                axes[idx].bar(range(len(methods)), values)
                axes[idx].set_xticks(range(len(methods)))
                axes[idx].set_xticklabels(methods, rotation=45, ha='right')
                axes[idx].set_title(metric.upper())
                axes[idx].set_ylabel('Value')
                axes[idx].grid(True, alpha=0.3)
        
        fig.suptitle(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    @staticmethod
    def plot_traversal_order(traversal_order: np.ndarray,
                            title: str = "Traversal Order",
                            figsize: Tuple[int, int] = (10, 8),
                            save_path: Optional[str] = None):
        """
        Visualize the traversal order as a heatmap.
        
        Args:
            traversal_order: Array where values represent order of traversal
            title: Plot title
            figsize: Figure size
            save_path: Path to save the figure (optional)
        """
        fig, ax = plt.subplots(figsize=figsize)
        
        im = ax.imshow(traversal_order, cmap='viridis')
        ax.set_title(title, fontsize=16, fontweight='bold')
        ax.axis('off')
        
        # Add colorbar
        cbar = plt.colorbar(im, ax=ax, fraction=0.046)
        cbar.set_label('Traversal Order', rotation=270, labelpad=20)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    @staticmethod
    def plot_multilevel_decomposition(decomposition: dict,
                                      title: str = "Multi-level Wavelet Decomposition",
                                      figsize: Tuple[int, int] = (20, 15),
                                      save_path: Optional[str] = None):
        """
        Plot multi-level wavelet decomposition.
        
        Args:
            decomposition: Dictionary from multilevel_dwt_2d
            title: Plot title
            figsize: Figure size
            save_path: Path to save the figure (optional)
        """
        levels = len([k for k in decomposition.keys() if k.startswith('level_')])
        
        fig = plt.figure(figsize=figsize)
        gs = GridSpec(levels, 4, figure=fig)
        
        for level in range(1, levels + 1):
            level_data = decomposition[f'level_{level}']
            
            # LL
            ax = fig.add_subplot(gs[level-1, 0])
            ax.imshow(level_data['LL'], cmap='gray')
            ax.set_title(f'Level {level} - LL')
            ax.axis('off')
            
            # LH
            ax = fig.add_subplot(gs[level-1, 1])
            ax.imshow(level_data['LH'], cmap='gray')
            ax.set_title(f'Level {level} - LH')
            ax.axis('off')
            
            # HL
            ax = fig.add_subplot(gs[level-1, 2])
            ax.imshow(level_data['HL'], cmap='gray')
            ax.set_title(f'Level {level} - HL')
            ax.axis('off')
            
            # HH
            ax = fig.add_subplot(gs[level-1, 3])
            ax.imshow(level_data['HH'], cmap='gray')
            ax.set_title(f'Level {level} - HH')
            ax.axis('off')
        
        fig.suptitle(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()


def create_test_image(size: int = 256, pattern: str = 'checkerboard') -> np.ndarray:
    """
    Create a test image for demonstration.
    
    Args:
        size: Image size
        pattern: Pattern type ('checkerboard', 'gradient', 'circles')
        
    Returns:
        Test image
    """
    if pattern == 'checkerboard':
        # Create checkerboard pattern
        image = np.zeros((size, size))
        block_size = size // 8
        for i in range(0, size, block_size):
            for j in range(0, size, block_size):
                if ((i // block_size) + (j // block_size)) % 2 == 0:
                    image[i:i+block_size, j:j+block_size] = 255
    
    elif pattern == 'gradient':
        # Create gradient
        image = np.linspace(0, 255, size)
        image = np.tile(image, (size, 1))
    
    elif pattern == 'circles':
        # Create concentric circles
        center = size // 2
        y, x = np.ogrid[:size, :size]
        dist = np.sqrt((x - center)**2 + (y - center)**2)
        image = 255 * (np.sin(dist / 10) + 1) / 2
    
    else:
        raise ValueError(f"Unknown pattern type: {pattern}")
    
    return image
