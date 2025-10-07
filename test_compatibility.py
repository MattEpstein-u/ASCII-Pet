#!/usr/bin/env python3
"""
Compatibility test for ASCII Desktop Pet
Check if your system can run the ASCII desktop pet
"""

import platform
import sys

def test_python_version():
    """Test if Python version is sufficient"""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 6:
        print("✓ Python version is compatible")
        return True
    else:
        print("✗ Python 3.6+ required")
        return False

def test_platform_detection():
    """Test platform detection"""
    system = platform.system()
    print(f"Operating system: {system}")
    
    if system in ["Darwin", "Windows", "Linux"]:
        print("✓ Supported operating system")
        return True
    else:
        print("! Untested operating system (may still work)")
        return True

def test_tkinter():
    """Test if tkinter is available"""
    try:
        import tkinter as tk
        print("✓ Tkinter is available")
        
        # Test basic functionality
        root = tk.Tk()
        root.withdraw()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.destroy()
        
        print(f"  Screen resolution: {screen_width}x{screen_height}")
        return True
    except ImportError:
        print("✗ Tkinter not available - install python3-tk")
        return False
    except Exception as e:
        print(f"! Tkinter test failed: {e}")
        return False

def test_ascii_art():
    """Test ASCII art rendering"""
    try:
        from ascii_pet_designs import ASCII_PET_SPRITES, ASCII_ANIMATIONS
        print("✓ ASCII art designs loaded")
        
        # Test a sample sprite
        sample_sprite = ASCII_PET_SPRITES.get('idle1')
        if sample_sprite:
            print("  Sample ASCII art:")
            for line in sample_sprite:
                print(f"    {line}")
        return True
    except ImportError:
        print("✗ ASCII art designs not found")
        return False
    except Exception as e:
        print(f"! ASCII art test failed: {e}")
        return False

def test_windows_integration():
    """Test Windows-specific features"""
    if platform.system() != "Windows":
        print("ℹ Windows integration test skipped (not on Windows)")
        return True
        
    try:
        import win32gui
        import win32con
        print("✓ Windows integration (pywin32) available")
        return True
    except ImportError:
        print("! Windows integration not available (install pywin32 for better desktop positioning)")
        return True

def main():
    """Run all tests"""
    print("=== ASCII Desktop Pet Compatibility Test ===")
    print()
    
    tests = [
        ("Python Version", test_python_version),
        ("Platform Detection", test_platform_detection),
        ("Tkinter Availability", test_tkinter),
        ("ASCII Art", test_ascii_art),
        ("Windows Integration", test_windows_integration),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"Testing {test_name}...")
        result = test_func()
        results.append(result)
        print()
    
    print("=== Test Summary ===")
    all_passed = all(results)
    
    if all_passed:
        print("✓ All tests passed! Your ASCII desktop pet should work perfectly.")
    else:
        print("! Some tests failed, but the pet might still work.")
    
    print()
    print("To test the pet interactively:")
    print("  python3 test_interactive.py")
    print()
    print("To install the desktop pet:")
    if platform.system() == "Windows":
        print("  Windows: install_windows.bat")
    else:
        print("  macOS/Linux: ./install.sh")
    
    return all_passed

if __name__ == "__main__":
    main()