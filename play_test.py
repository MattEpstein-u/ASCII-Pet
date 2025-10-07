#!/usr/bin/env python3
"""
Quick launcher for the interactive ASCII desktop pet test
"""

import sys
import os

def main():
    print("🎮 ASCII Desktop Pet Interactive Test Launcher")
    print("=" * 55)
    print()
    print("This will open a window where you can:")
    print("• Play with the ASCII pet using mouse and buttons")
    print("• Test all behaviors (following, wandering, sleeping)")  
    print("• See exactly how the pet will behave on your desktop")
    print("• Try different interactions without installation")
    print("• Experience beautiful ASCII art animations")
    print()
    
    try:
        # Import and run the interactive test
        import test_interactive
        
        print("Starting interactive ASCII pet test... (close window when done)")
        print()
        
        pet = test_interactive.TestASCIIDesktopPet()
        pet.run()
        
        print()
        print("✅ Interactive test completed!")
        print()
        print("Ready to install? Run:")
        print("• macOS/Linux: ./install.sh")
        print("• Windows: install_windows.bat")
        
    except ImportError as e:
        print(f"❌ Error: Could not import test_interactive: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error running test: {e}")
        print("Make sure you have a display available")
        sys.exit(1)

if __name__ == "__main__":
    main()