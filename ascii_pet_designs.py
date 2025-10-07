#!/usr/bin/env python3
"""
ASCII Pet Art Designs
Collection of ASCII art for different pet states and animations
"""

# ASCII art for different pet states
# Each state has multiple frames for animation

ASCII_PET_SPRITES = {
    # Idle state - peaceful sitting cat
    'idle1': [
        "   /\\_/\\  ",
        "  ( o.o ) ",
        "   > ^ <  "
    ],
    
    'idle2': [
        "   /\\_/\\  ",
        "  ( -.-)  ",
        "   > ^ <  "
    ],
    
    'idle3': [
        "   /\\_/\\  ",
        "  ( ^.^ ) ",
        "   > ^ <  "
    ],
    
    # Walking state - cat in motion
    'walk1': [
        "   /\\_/\\  ",
        "  ( o.o ) ",
        "   > ^ <  ",
        "    / \\   "
    ],
    
    'walk2': [
        "   /\\_/\\  ",
        "  ( o.o ) ",
        "   > ^ <  ",
        "   \\ /    "
    ],
    
    'walk3': [
        "   /\\_/\\  ",
        "  ( o.o ) ",
        "   > ^ <  ",
        "  ~/ \\~   "
    ],
    
    # Sleeping state - cat curled up
    'sleep1': [
        "  /\\_/\\   ",
        " ( -.- )  ",
        "  \\___/   "
    ],
    
    'sleep2': [
        "  /\\_/\\   ",
        " ( ... )  ",
        "  \\___/   "
    ],
    
    # Playing state - excited cat
    'play1': [
        "   /\\_/\\  ",
        "  ( ^o^ ) ",
        "   >***<  ",
        "    !!!   "
    ],
    
    'play2': [
        "   /\\_/\\  ",
        "  ( *^* ) ",
        "   >^^^<  ",
        "   \\o/    "
    ],
    
    'play3': [
        "   /\\_/\\  ",
        "  ( >w< ) ",
        "   >~~~<  ",
        "   ~~~    "
    ],
    
    # Happy states
    'happy1': [
        "   /\\_/\\  ",
        "  ( ^_^ ) ",
        "   > ω <  "
    ],
    
    'happy2': [
        "   /\\_/\\  ",
        "  ( ◕‿◕ ) ",
        "   > ^ <  "
    ]
}

# Animation sequences for different states
ASCII_ANIMATIONS = {
    'idle': ['idle1', 'idle2', 'idle1', 'idle3', 'idle1'],
    'walking': ['walk1', 'walk2', 'walk3', 'walk2'],
    'sleep': ['sleep1', 'sleep2', 'sleep1', 'sleep2'],
    'play': ['play1', 'play2', 'play3', 'play2', 'play1'],
    'happy': ['happy1', 'happy2', 'happy1']
}

def get_ascii_pet(sprite_name):
    """Get ASCII art for a specific sprite"""
    return ASCII_PET_SPRITES.get(sprite_name, ASCII_PET_SPRITES['idle1'])

def get_animation_frames(state):
    """Get animation sequence for a specific state"""
    return ASCII_ANIMATIONS.get(state, ASCII_ANIMATIONS['idle'])

def render_ascii_art(lines, x, y, canvas, tag="pet", color="#333333"):
    """Render ASCII art on a tkinter canvas"""
    canvas.delete(tag)  # Clear previous art
    
    line_height = 12
    for i, line in enumerate(lines):
        canvas.create_text(
            x, y + (i * line_height), 
            text=line, 
            font=('Courier', 9, 'bold'), 
            anchor='center',
            fill=color,
            tags=tag
        )

def demo_ascii_art():
    """Demo function to preview all ASCII art"""
    print("=== ASCII Pet Art Demo ===\n")
    
    for state, frames in ASCII_ANIMATIONS.items():
        print(f"--- {state.upper()} Animation Frames ---")
        for frame_name in frames:
            lines = ASCII_PET_SPRITES[frame_name]
            print(f"\nFrame: {frame_name}")
            for line in lines:
                print(f"  {line}")
        print("\n" + "─" * 40 + "\n")

if __name__ == "__main__":
    demo_ascii_art()