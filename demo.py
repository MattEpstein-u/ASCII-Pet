#!/usr/bin/env python3
"""
Demo script to show what the ASCII desktop pet looks like
"""

import time
import random
from ascii_pet_designs import ASCII_PET_SPRITES, ASCII_ANIMATIONS

def demo_ascii_pet():
    """Show a simple text-based demo of the ASCII pet animations"""
    
    print("=== ASCII Desktop Pet Animation Demo ===")
    print()
    print("Here's what your ASCII desktop pet will look like:")
    print()
    
    states = ['idle', 'walking', 'play', 'sleep']
    
    for state in states:
        print(f"--- {state.upper()} animation ---")
        animation = ASCII_ANIMATIONS[state]
        
        for cycle in range(2):  # Show 2 full cycles
            for frame_name in animation:
                sprite_lines = ASCII_PET_SPRITES[frame_name]
                
                # Clear screen area and show new sprite
                print(f"\r{frame_name} - {state}:", end="")
                print()
                for line in sprite_lines:
                    print(f"    {line}")
                print("    " + "─" * 12)
                
                time.sleep(0.8 if state == 'sleep' else 0.6)
        
        print()  # New line after each animation
        time.sleep(0.5)
    
    print()
    print("🎮 Interactive Features:")
    print("• Lives in a small container (1/8 screen size) in corner of desktop")
    print("• Click and drag to move the pet within its container")
    print("• Double-click to trigger play animation")
    print("• Pet follows your cursor when you move near the container")
    print("• Randomly wanders around its container space")
    print("• Automatically changes between idle, sleep, and play")
    print("• Only visible when desktop is showing (no apps on top)")
    print("• Subtle, non-intrusive design that blends with wallpaper")
    print("• Beautiful ASCII art animations instead of simple emojis")
    print()
    print("Ready to install your ASCII desktop companion!")
    print()
    print("💡 Want to try it first? Run: python3 test_interactive.py")
    print("   This opens a test window where you can play with the ASCII pet!")

if __name__ == "__main__":
    demo_ascii_pet()