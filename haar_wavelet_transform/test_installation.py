#!/usr/bin/env python3
"""
Quick test script to verify the Haar wavelet transform installation.
Run this to ensure all components are working correctly.
"""

import sys
import traceback

def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    try:
        import numpy as np
        print("  ✓ numpy")
        
        import matplotlib
        print("  ✓ matplotlib")
        
        import matplotlib.pyplot as plt
        print("  ✓ matplotlib.pyplot")
        
        from PIL import Image
        print("  ✓ PIL")
        
        import scipy
        print("  ✓ scipy")
        
        # Test local imports
        from wavelet_transform import HaarWaveletTransform
        print("  ✓ wavelet_transform")
        
        from convolution_methods import ConvolutionTraversal
        print("  ✓ convolution_methods")
        
        from kernel_types import KernelGenerator
        print("  ✓ kernel_types")
        
        from comparison_analysis import WaveletMetrics
        print("  ✓ comparison_analysis")
        
        from visualization import WaveletVisualizer
        print("  ✓ visualization")
        
        return True
    except Exception as e:
        print(f"  ✗ Import failed: {e}")
        traceback.print_exc()
        return False


def test_basic_functionality():
    """Test basic wavelet transform functionality."""
    print("\nTesting basic functionality...")
    try:
        import numpy as np
        from wavelet_transform import HaarWaveletTransform
        from visualization import create_test_image
        from comparison_analysis import WaveletMetrics
        
        # Create test image
        image = create_test_image(64, 'checkerboard')
        print(f"  ✓ Created test image: {image.shape}")
        
        # Transform
        transformer = HaarWaveletTransform(kernel_size=2)
        LL, LH, HL, HH = transformer.dwt_2d(image)
        print(f"  ✓ Transform successful: LL={LL.shape}")
        
        # Reconstruct
        reconstructed = transformer.idwt_2d(LL, LH, HL, HH)
        print(f"  ✓ Reconstruction successful: {reconstructed.shape}")
        
        # Verify quality
        mse = WaveletMetrics.mse(image, reconstructed)
        energy = WaveletMetrics.energy_preservation(image, LL, LH, HL, HH)
        
        if mse < 1e-6 and abs(energy - 1.0) < 1e-6:
            print(f"  ✓ Quality verified: MSE={mse:.2e}, Energy={energy:.6f}")
            return True
        else:
            print(f"  ✗ Quality check failed: MSE={mse}, Energy={energy}")
            return False
            
    except Exception as e:
        print(f"  ✗ Functionality test failed: {e}")
        traceback.print_exc()
        return False


def test_advanced_features():
    """Test advanced features."""
    print("\nTesting advanced features...")
    try:
        import numpy as np
        from wavelet_transform import HaarWaveletTransform
        from convolution_methods import wavelet_transform_with_traversal
        from kernel_types import compare_kernels
        from visualization import create_test_image
        
        image = create_test_image(64, 'gradient')
        
        # Test multi-level decomposition
        transformer = HaarWaveletTransform(kernel_size=2)
        decomposition = transformer.multilevel_dwt_2d(image, levels=2)
        print("  ✓ Multi-level decomposition")
        
        # Test traversal methods
        LL, LH, HL, HH = wavelet_transform_with_traversal(
            image, kernel_size=4, traversal_method='zigzag'
        )
        print("  ✓ Traversal methods")
        
        # Test kernel types
        results = compare_kernels(image, ['haar', 'db2'], size=2)
        print("  ✓ Kernel types")
        
        # Test color processing
        from wavelet_transform import process_color_image
        color_image = np.random.rand(32, 32, 3) * 255
        decomposition = process_color_image(color_image, kernel_size=2)
        print("  ✓ Color image processing")
        
        return True
        
    except Exception as e:
        print(f"  ✗ Advanced features test failed: {e}")
        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("="*70)
    print("HAAR WAVELET TRANSFORM - INSTALLATION TEST")
    print("="*70)
    
    all_passed = True
    
    # Test imports
    if not test_imports():
        all_passed = False
        print("\n⚠ Warning: Some imports failed. Check dependencies.")
    
    # Test basic functionality
    if not test_basic_functionality():
        all_passed = False
        print("\n⚠ Warning: Basic functionality test failed.")
    
    # Test advanced features
    if not test_advanced_features():
        all_passed = False
        print("\n⚠ Warning: Advanced features test failed.")
    
    # Final result
    print("\n" + "="*70)
    if all_passed:
        print("✅ ALL TESTS PASSED!")
        print("The Haar wavelet transform implementation is ready to use.")
        print("\nNext steps:")
        print("  1. Run: python main.py --demo all")
        print("  2. Or: python examples/sample_usage.py")
        print("  3. Read: README.md for detailed documentation")
    else:
        print("❌ SOME TESTS FAILED")
        print("Please check the error messages above and:")
        print("  1. Ensure all dependencies are installed: pip install -r requirements.txt")
        print("  2. Check that you're in the correct directory")
        print("  3. Verify Python version (3.6+ required)")
    print("="*70)
    
    return 0 if all_passed else 1


if __name__ == '__main__':
    sys.exit(main())
