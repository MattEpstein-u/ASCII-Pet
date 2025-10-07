#!/usr/bin/env python3
"""
ASCII Underwater Kraken Environment
Collection of ASCII art for underwater kraken animations
"""

# ASCII art for the kraken in different states
# Each state has multiple frames for animation
# All sprites are 11 lines tall and 23 characters wide (rectangular)

ASCII_PET_SPRITES = {
    # Idle - simple compact octopus design
    # Clean structure with clear tentacles
    'idle1': [
        "         ______        ",
        "        /      \\       ",
        "       /        \\      ",
        "       |        |      ",
        "    )  o        o   ?  ",
        "   (    \\      /    |  ",
        "  _ \\___/||||||\\___/ _ ",
        "   \\____/ |||| \\____/ `",
        "   ,-.___/ || \\__,-._  ",
        "  /    ___/  \\__       ",
        "     _/         `---   ",
    ],
    
    'idle2': [
        "         ______        ",
        "        /      \\       ",
        "       /        \\      ",
        "       |        |      ",
        "    )  O        O   ?  ",
        "   (    \\  __  /    |  ",
        "  _ \\___/||||||\\___/ _ ",
        "   \\____/ |||| \\____/ `",
        "   ,-.___/ || \\__,-._  ",
        "  /    ___/  \\__       ",
        "     _/         `---   ",
    ],
    
    # Swimming - tentacles actively moving
    'swim1': [
        "         ______        ",
        "        /      \\       ",
        "       /        \\      ",
        "       |        |      ",
        "    )  @        @   ?  ",
        "   (    \\  >   /    |  ",
        "  _ \\___/||||||\\___/ _ ",
        "   \\____/ |||| \\____/ `",
        "   ,-.___/ || \\__,-._  ",
        "  /    ___/  \\__       ",
        "     _/         `---   ",
    ],
    
    'swim2': [
        "         ______        ",
        "        /      \\       ",
        "       /        \\      ",
        "       |        |      ",
        "    )  O        O   ?  ",
        "   (    \\  ^   /    |  ",
        "  _ \\___/||||||\\___/ _ ",
        "   \\____/ |||| \\____/ `",
        "   ,-.___/ || \\__,-._  ",
        "  /    ___/  \\__       ",
        "     _/         `---   ",
    ],
    
    'swim3': [
        "         ______        ",
        "        /      \\       ",
        "       /        \\      ",
        "       |        |      ",
        "    )  @        @   ?  ",
        "   (    \\  >   /    |  ",
        "  _ \\___/||||||\\___/ _ ",
        "   \\____/ |||| \\____/ `",
        "   ,-.___/ || \\__,-._  ",
        "  /    ___/  \\__       ",
        "     _/         `---   ",
    ],
    
    # Eating - chewing animation (no tentacle wrapping)
    # Mouth is positioned over shrimp, then chews
    'eat1': [
        "         ______        ",
        "        /      \\       ",
        "       /        \\      ",
        "       |        |      ",
        "    )  X        X   ?  ",
        "   (    \\ /VV\\ /    |  ",
        "  _ \\___/||||||\\___/ _ ",
        "   \\____/ |||| \\____/ `",
        "   ,-.___/ || \\__,-._  ",
        "  /    ___/  \\__       ",
        "     _/         `---   ",
    ],
    
    'eat2': [
        "         ______        ",
        "        /      \\       ",
        "       /        \\      ",
        "       |        |      ",
        "    )  *        *   ?  ",
        "   (    \\ <WW> /    |  ",
        "  _ \\___/||||||\\___/ _ ",
        "   \\____/ |||| \\____/ `",
        "   ,-.___/ || \\__,-._  ",
        "  /    ___/  \\__       ",
        "     _/         `---   ",
    ],
    
    'eat3': [
        "         ______        ",
        "        /      \\       ",
        "       /        \\      ",
        "       |        |      ",
        "    )  ^        ^   ?  ",
        "   (    \\ /^^\\ /    |  ",
        "  _ \\___/||||||\\___/ _ ",
        "   \\____/ |||| \\____/ `",
        "   ,-.___/ || \\__,-._  ",
        "  /    ___/  \\__       ",
        "     _/         `---   ",
    ],
}

# Animation sequences for different kraken states
ASCII_ANIMATIONS = {
    'idle': ['idle1', 'idle2'],
    'swimming': ['swim1', 'swim2', 'swim3'],
    'eating': ['eat1', 'eat2', 'eat3']
}

# Ocean Cross-Section Environment ASCII Art
UNDERWATER_ENVIRONMENT = {
    # Ocean surface line (separates air from water at 1/5 from top)
    'ocean_surface': [
        "≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈"
    ],
    
    # Better seaweed designs using various ASCII techniques
    'kelp_forest_tall': [
        "    |    ",
        "   /|\\   ",
        "  / | \\  ",
        "    |    ",
        "   /|\\   ",
        "  / | \\  ",
        "    |    ",
        "   /|\\   ",
        "  / | \\  ",
        "    |    ",
        "   /|\\   ",
        "  / | \\  "
    ],
    
    'kelp_forest_medium': [
        "  | |  ",
        " /| |\\ ",
        "/ | | \\",
        "  | |  ",
        " /| |\\ ",
        "/ | | \\",
        "  | |  ",
        " /| |\\ "
    ],
    
    'sea_grass': [
        " | | | ",
        "|| | ||",
        " | | | ",
        "|| | ||",
        " | | | ",
        "|| | ||"
    ],
    
    'coral_formation': [
        " ∩∩∩ ",
        "∩   ∩",
        " ∩ ∩ ",
        "  |  ",
        "  |  ",
        " _|_ "
    ],
    
    # Ocean floor with texture and depth
    'ocean_floor_layers': [
        "▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀",
        "████████████████████████████████████████████████████████████████████████████████",
        "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
        "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
    ],
    
    # Rocks and underwater features
    'rock_formations': [
        "  ▲   ▲     ▲▲    ▲   ▲▲▲   ▲    ▲▲     ▲   ▲▲▲    ▲     ▲▲   ▲▲    ▲▲▲  ",
        " ▲▲▲ ▲▲▲   ▲▲▲▲  ▲▲▲ ▲▲▲▲  ▲▲▲  ▲▲▲▲   ▲▲▲ ▲▲▲▲   ▲▲▲   ▲▲▲▲ ▲▲▲▲  ▲▲▲▲ "
    ],
    
    # Surface area for future boat (top 1/5 of screen)
    'surface_area': [
        "                                                                                 ",
        "                     [ BOAT WILL SAIL HERE ]                                   ",
        "                                                                                 "
    ],
    
    # Bubbles for atmosphere
    'bubbles_small': ["○", "∘", "·", "°"],
    'bubbles_medium': ["●", "○", "◯"],
    'bubbles_large': ["⬤", "⭕", "◯"]
}

def get_ascii_pet(sprite_name):
    """Get ASCII art for a specific sprite"""
    return ASCII_PET_SPRITES.get(sprite_name, ASCII_PET_SPRITES['idle1'])

def get_animation_frames(state):
    """Get animation sequence for a specific state"""
    return ASCII_ANIMATIONS.get(state, ASCII_ANIMATIONS['idle'])

def render_ascii_art(lines, x, y, canvas, tag="pet", color="#333333", font_size=6):
    """Render ASCII art on a tkinter canvas with customizable font size"""
    canvas.delete(tag)  # Clear previous art
    
    line_height = font_size + 2
    for i, line in enumerate(lines):
        canvas.create_text(
            x, y + (i * line_height), 
            text=line, 
            font=('Courier', font_size, 'bold'), 
            anchor='center',
            fill=color,
            tags=tag
        )

def render_underwater_environment(canvas, width, height):
    """Render ocean cross-section: top 1/5 surface area, bottom 4/5 underwater"""
    canvas.delete("environment")  # Clear previous environment
    
    # Calculate water level (top 1/5 is surface, bottom 4/5 is underwater)
    water_level = height // 5
    underwater_height = height - water_level
    
    # ===== SURFACE AREA (Top 1/5) =====
    # Draw surface area background (deep blue, almost black)
    canvas.create_rectangle(
        0, 0, width, water_level,
        fill='#0A0F1C', outline='',
        tags="environment"
    )
    
    # ===== OCEAN SURFACE LINE =====
    # Draw the water surface line that separates air from water
    surface_lines = UNDERWATER_ENVIRONMENT['ocean_surface']
    for i, line in enumerate(surface_lines):
        # Create full-width surface line
        chars_needed = width // 10  # Adjust character density
        full_line = (line * (chars_needed // len(line) + 1))[:chars_needed]
        canvas.create_text(
            width // 2, water_level + (i * 5),
            text=full_line,
            font=('Courier', 8, 'bold'),
            fill='#FFFFFF',
            anchor='center',
            tags="environment"
        )
    
    # ===== UNDERWATER AREA (Bottom 4/5) =====
    # Draw underwater background (deep blue, almost black)
    canvas.create_rectangle(
        0, water_level + 15, width, height,
        fill='#0A0F1C', outline='',
        tags="environment"
    )
    
    return water_level  # Return water level for movement constraints

def is_in_water(x, y, water_level, canvas_height):
    """Check if coordinates are in the underwater area (bottom 4/5 of canvas)"""
    # Water starts after the surface line (water_level + surface line height)
    underwater_start = water_level + 15
    # Leave space above ocean floor
    underwater_end = canvas_height - 50
    return y >= underwater_start and y <= underwater_end

def spawn_bubble(bubble_list, width, water_level, height):
    """Spawn a new bubble at a random underwater position"""
    import random
    
    # Spawn in underwater area only (below surface line, above ocean floor)
    underwater_start = water_level + 20  # Below surface line
    underwater_end = height - 60  # Above ocean floor
    
    x = random.randint(80, width - 80)
    y = random.randint(underwater_start, underwater_end)
    
    # Bubble appearance
    bubble_char = random.choice(UNDERWATER_ENVIRONMENT['bubbles_small'] + 
                              UNDERWATER_ENVIRONMENT['bubbles_medium'] + 
                              UNDERWATER_ENVIRONMENT['bubbles_large'])
    bubble_size = random.choice([10, 12, 14, 16])
    bubble_color = random.choice(['#FFFFFF', '#F8F8FF', '#F0F8FF', '#E6E6FA', '#FFFAFA'])
    
    # Add to bubble list with all needed info
    bubble_list.append({
        'x': x,
        'y': y,
        'char': bubble_char,
        'size': bubble_size,
        'color': bubble_color,
        'canvas_id': None  # Will be set when rendered
    })


def update_bubbles(bubble_list, canvas, width, water_level, height, spawn_chance=0.05):
    """Update bubble physics: spawn new bubbles randomly, move existing bubbles upward, remove at surface
    
    Args:
        bubble_list: List of bubble dictionaries to update
        canvas: Tkinter canvas to render on
        width: Canvas width
        water_level: Y-coordinate of ocean surface
        height: Canvas height
        spawn_chance: Probability (0.0-1.0) of spawning a bubble each frame
    """
    import random
    
    # Randomly spawn new bubble
    if random.random() < spawn_chance:
        spawn_bubble(bubble_list, width, water_level, height)
    
    # Update existing bubbles
    bubbles_to_remove = []
    for i, bubble in enumerate(bubble_list):
        # Move bubble upward (rising physics)
        bubble['y'] -= 2  # Rise speed: 2 pixels per frame
        
        # Mark for removal if reached surface (one line below surface for visibility)
        if bubble['y'] <= water_level + 15:
            bubbles_to_remove.append(i)
    
    # Remove bubbles that reached surface (reverse order to preserve indices)
    for i in reversed(bubbles_to_remove):
        bubble_list.pop(i)
    
    # Render all bubbles
    render_bubbles(bubble_list, canvas)


def render_bubbles(bubble_list, canvas):
    """Render all bubbles on canvas"""
    # Clear existing bubble graphics
    canvas.delete("bubbles")
    
    # Render each bubble at its current position
    for bubble in bubble_list:
        canvas.create_text(
            bubble['x'], bubble['y'],
            text=bubble['char'],
            font=('Arial', bubble['size']),
            fill=bubble['color'],
            tags="bubbles"
        )

def demo_ascii_art():
    """Demo function to preview all kraken ASCII art"""
    print("=== ASCII Underwater Kraken Art Demo ===\n")
    
    for state, frames in ASCII_ANIMATIONS.items():
        print(f"--- {state.upper()} Animation Frames ---")
        for frame_name in frames:
            lines = ASCII_PET_SPRITES[frame_name]
            print(f"\nFrame: {frame_name}")
            for line in lines:
                print(f"  {line}")
        print("\n" + "─" * 50 + "\n")
    
    print("=== Underwater Environment Elements ===\n")
    
    print("Water Surface:")
    for line in UNDERWATER_ENVIRONMENT['ocean_surface'][:2]:
        print(f"  {line[:50]}...")
    
    print("\nKelp Forest:")
    for line in UNDERWATER_ENVIRONMENT['kelp_forest_tall'][:5]:
        print(f"  {line}")
    
    print("\nOcean Floor:")
    for line in UNDERWATER_ENVIRONMENT['ocean_floor_layers'][:1]:
        print(f"  {line[:50]}...")
    
    print(f"\nBubbles: {', '.join(UNDERWATER_ENVIRONMENT['bubbles_small'] + UNDERWATER_ENVIRONMENT['bubbles_medium'])}")
    print("\nYour kraken will swim in this underwater world! 🐙")

if __name__ == "__main__":
    demo_ascii_art()
