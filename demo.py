#!/usr/bin/env python3
"""
Demo script to show what the ASCII underwater kraken looks like
"""

import time
import random
from ascii_pet_designs import ASCII_PET_SPRITES, ASCII_ANIMATIONS, UNDERWATER_ENVIRONMENT

def demo_ascii_kraken():
    """Show a simple text-based demo of the ASCII kraken animations"""
    
    print("=== ASCII Underwater Kraken Animation Demo ===")
    print()
    print("🌊 Welcome to the underwater world! 🌊")
    print("Here's what your ASCII kraken will look like:")
    print()
    
    # Show water surface first
    print("--- UNDERWATER ENVIRONMENT ---")
    print("Water Surface:")
    for line in UNDERWATER_ENVIRONMENT['water_surface'][:2]:
        print(f"  {line[:60]}")
    print()
    
    states = ['idle', 'swimming', 'attack', 'sleep']
    
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
                print("    " + "─" * 20)
                
                time.sleep(1.0 if state == 'sleep' else 0.7)
        
        print()  # New line after each animation
        time.sleep(0.5)
    
    # Show environment elements
    print("--- UNDERWATER DECORATIONS ---")
    print("Seaweed Forest:")
    for line in UNDERWATER_ENVIRONMENT['seaweed_center'][:6]:
        print(f"    {line}")
    
    print("\nOcean Floor:")
    for line in UNDERWATER_ENVIRONMENT['ocean_floor'][:2]:
        print(f"  {line[:50]}...")
    
    print(f"\nFloating Bubbles: {' '.join(UNDERWATER_ENVIRONMENT['bubbles_small'] + UNDERWATER_ENVIRONMENT['bubbles_medium'] + UNDERWATER_ENVIRONMENT['bubbles_large'])}")
    
    print()
    print("🐙 Interactive Features:")
    print("• Lives in a detailed underwater environment in desktop corner")
    print("• Can ONLY move in water areas - kraken can't go on land!")
    print("• Click and drag to move the kraken through the water")
    print("• Double-click to make it attack with aggressive tentacles!")
    print("• Kraken follows your cursor when you're in the water")
    print("• Randomly swims around its underwater domain")
    print("• Beautiful detailed ASCII art with tentacle animations")
    print("• Floating bubbles and seaweed create a living ocean")
    print("• Multiple kraken states: idle, swimming, attacking, sleeping")
    print("• Only visible when desktop is showing (no apps on top)")
    print()
    print("Ready to install your ASCII underwater kraken! 🐙")
    print()
    print("💡 Want to try it first? Run: python3 test_interactive.py")
    print("   This opens a test window where you can interact with the kraken!")

if __name__ == "__main__":
    demo_ascii_kraken()