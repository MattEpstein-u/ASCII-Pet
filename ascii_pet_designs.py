#!/usr/bin/env python3
"""
ASCII Underwater Kraken Environment
Collection of ASCII art for underwater scenes and kraken animations
"""

# ASCII art for the kraken in different states
# Each state has multiple frames for animation
# Using smaller characters for more detail

ASCII_PET_SPRITES = {
    # Idle kraken states - tentacles gently swaying
    'idle1': [
        "    .-'''-.",
        "   /  o   o \\",
        "  |     ^     |",
        "   \\  \\___/  /",
        "    '-.___.-'",
        "   ~)  ) (  (~",
        "  ~)  ) ( (  (~",
        " ~)  ) ( ( (  (~"
    ],
    
    'idle2': [
        "    .-'''-.",
        "   /  -   - \\",
        "  |     ~     |",
        "   \\  \\___/  /",
        "    '-.___.-'",
        "  (~  ) (  )~",
        " (~  ) ( (  )~",
        "(~  ) ( ( (  )~"
    ],
    
    'idle3': [
        "    .-'''-.",
        "   /  ^   ^ \\",
        "  |     o     |",
        "   \\  \\___/  /",
        "    '-.___.-'",
        "   )~  ) (  ~)",
        "  )~  ) ( (  ~)",
        " )~  ) ( ( (  ~)"
    ],
    
    # Swimming kraken - tentacles propelling through water
    'swim1': [
        "    .-'''-.",
        "   /  o   o \\",
        "  |     ^     |",
        "   \\  \\___/  /",
        "    '-.___.-'",
        "  ))  ) (  ((",
        " ))  ) ( (  ((",
        "))  ) ( ( (  (("
    ],
    
    'swim2': [
        "    .-'''-.",
        "   /  o   o \\",
        "  |     ^     |",
        "   \\  \\___/  /",
        "    '-.___.-'",
        "   ~)  ) (  (~",
        "  ~))  ) ( ((~",
        " ~)))  ) ( (((~"
    ],
    
    'swim3': [
        "    .-'''-.",
        "   /  o   o \\",
        "  |     ^     |",
        "   \\  \\___/  /",
        "    '-.___.-'",
        "  ((  ) (  ))",
        " (((  ) ( (((",
        "((((  ) ( (((("
    ],
    
    # Sleeping kraken - curled up with tentacles tucked
    'sleep1': [
        "    zzz",
        "   .-'''-.",
        "  /  -   - \\",
        " |     _     |",
        "  \\  \\___/  /",
        "   '-.___.-'",
        "    \\   /",
        "     ) ("
    ],
    
    'sleep2': [
        "   zzz zzz",
        "   .-'''-.",
        "  /  .   . \\",
        " |     _     |",
        "  \\  \\___/  /",
        "   '-.___.-'",
        "    \\   /",
        "     ) ("
    ],
    
    # Attacking kraken - aggressive tentacle spread
    'attack1': [
        "    .-'''-.",
        "   /  O   O \\",
        "  |     !     |",
        "   \\  \\___/  /",
        "    '-.___.-'",
        " )))  ) (  (((",
        "))))  ) ( ((((",
        ")))) ) ( ( ((((",
        " ))) ) ( ( ((("
    ],
    
    'attack2': [
        "    .-'''-.",
        "   /  @   @ \\",
        "  |     !!!   |",
        "   \\  \\___/  /",
        "    '-.___.-'",
        "((((  ) (  ))))",
        "(((( ) ( ( ))))",
        "((( ) ( ( ( )))",
        " (( ) ( ( ( ))"
    ],
    
    'attack3': [
        "    .-'''-.",
        "   /  X   X \\",
        "  |    ><    |",
        "   \\  \\___/  /",
        "    '-.___.-'",
        " ~))  ) (  ((~",
        "~)))  ) ( (((~",
        "~))) ) ( ( (((~",
        " ~)) ) ( ( ((~"
    ],
    
    # Happy playful kraken
    'happy1': [
        "    .-'''-.",
        "   /  ^   ^ \\",
        "  |     ω     |",
        "   \\  \\___/  /",
        "    '-.___.-'",
        "  \\)  ) (  (/",
        " \\))  ) ( ((/",
        "\\)))  ) ( (((/",
    ],
    
    'happy2': [
        "    .-'''-.",
        "   /  ◕   ◕ \\",
        "  |     ‿     |",
        "   \\  \\___/  /",
        "    '-.___.-'",
        "  /)  ) (  (\\",
        " /))  ) ( ((\\",
        "/)))  ) ( (((\\",
    ]
}

# Animation sequences for different kraken states
ASCII_ANIMATIONS = {
    'idle': ['idle1', 'idle2', 'idle1', 'idle3', 'idle1'],
    'swimming': ['swim1', 'swim2', 'swim3', 'swim2'],
    'sleep': ['sleep1', 'sleep2', 'sleep1', 'sleep2'],
    'attack': ['attack1', 'attack2', 'attack3', 'attack2', 'attack1'],
    'happy': ['happy1', 'happy2', 'happy1']
}

# Underwater environment ASCII art
UNDERWATER_ENVIRONMENT = {
    # Water surface (top 1/3 of screen)
    'water_surface': [
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    ],
    
    # Underwater decorations
    'seaweed_left': [
        "  |",
        " /|",
        "/ |",
        "  |",
        " /|",
        "/ |",
        "  |",
        " /|",
        "/ |"
    ],
    
    'seaweed_right': [
        "|  ",
        "|\\ ",
        "| \\",
        "|  ",
        "|\\ ",
        "| \\",
        "|  ",
        "|\\ ",
        "| \\"
    ],
    
    'seaweed_center': [
        " | ",
        "/|\\",
        " | ",
        "\\|/",
        " | ",
        "/|\\",
        " | ",
        "\\|/",
        " | "
    ],
    
    # Ocean floor
    'ocean_floor': [
        "^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~",
        "~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^",
        "^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~"
    ],
    
    # Bubbles for atmosphere
    'bubbles_small': ["o", "°", "·"],
    'bubbles_medium': ["O", "o"],
    'bubbles_large': ["●", "○"]
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
    """Render the complete underwater environment"""
    canvas.delete("environment")  # Clear previous environment
    
    # Calculate water level (top 1/3 is surface, bottom 2/3 is underwater)
    water_level = height // 3
    underwater_height = height - water_level
    
    # Draw water surface
    surface_lines = UNDERWATER_ENVIRONMENT['water_surface']
    for i, line in enumerate(surface_lines):
        if i * 8 < water_level:
            # Repeat the line to fill width
            full_line = (line * (width // len(line) + 1))[:width//6]
            canvas.create_text(
                width // 2, i * 8,
                text=full_line,
                font=('Courier', 6),
                fill='#4A90E2',
                anchor='center',
                tags="environment"
            )
    
    # Draw underwater background (blue tint)
    canvas.create_rectangle(
        0, water_level, width, height,
        fill='#1E3A5F', outline='',
        tags="environment"
    )
    
    # Draw seaweed
    seaweed_positions = [
        (width * 0.1, height - 80, 'seaweed_left'),
        (width * 0.2, height - 70, 'seaweed_center'),
        (width * 0.8, height - 75, 'seaweed_right'),
        (width * 0.9, height - 85, 'seaweed_left')
    ]
    
    for x_pos, y_pos, seaweed_type in seaweed_positions:
        seaweed_lines = UNDERWATER_ENVIRONMENT[seaweed_type]
        for i, line in enumerate(seaweed_lines):
            canvas.create_text(
                x_pos, y_pos + (i * 8),
                text=line,
                font=('Courier', 6),
                fill='#2D5016',
                anchor='center',
                tags="environment"
            )
    
    # Draw ocean floor
    floor_lines = UNDERWATER_ENVIRONMENT['ocean_floor']
    floor_start = height - len(floor_lines) * 8
    for i, line in enumerate(floor_lines):
        full_line = (line * (width // len(line) + 1))[:width//6]
        canvas.create_text(
            width // 2, floor_start + (i * 8),
            text=full_line,
            font=('Courier', 6),
            fill='#8B4513',
            anchor='center',
            tags="environment"
        )
    
    return water_level  # Return water level for movement constraints

def is_in_water(x, y, water_level, canvas_height):
    """Check if coordinates are in the underwater area"""
    return y >= water_level and y <= (canvas_height - 30)  # Leave space above ocean floor

def add_floating_bubbles(canvas, width, water_level, canvas_height):
    """Add animated bubbles to the underwater scene"""
    import random
    canvas.delete("bubbles")
    
    # Add various sized bubbles
    num_bubbles = 15
    for _ in range(num_bubbles):
        x = random.randint(50, width - 50)
        y = random.randint(water_level + 20, canvas_height - 50)
        
        # Choose bubble type
        bubble_type = random.choice(['bubbles_small', 'bubbles_medium', 'bubbles_large'])
        bubble_char = random.choice(UNDERWATER_ENVIRONMENT[bubble_type])
        
        canvas.create_text(
            x, y,
            text=bubble_char,
            font=('Courier', random.randint(6, 10)),
            fill='#87CEEB',
            anchor='center',
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
    for line in UNDERWATER_ENVIRONMENT['water_surface'][:2]:
        print(f"  {line[:50]}...")
    
    print("\nSeaweed:")
    for line in UNDERWATER_ENVIRONMENT['seaweed_center'][:5]:
        print(f"  {line}")
    
    print("\nOcean Floor:")
    for line in UNDERWATER_ENVIRONMENT['ocean_floor'][:1]:
        print(f"  {line[:50]}...")
    
    print(f"\nBubbles: {', '.join(UNDERWATER_ENVIRONMENT['bubbles_small'] + UNDERWATER_ENVIRONMENT['bubbles_medium'])}")
    print("\nYour kraken will swim in this underwater world! 🐙")

if __name__ == "__main__":
    demo_ascii_art()