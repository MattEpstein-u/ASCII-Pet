#!/usr/bin/env python3
"""
ASCII Underwater Kraken Environment
Collection of ASCII art for underwater kraken animations
"""

# ===== CONFIGURATION =====
# Master density control - adjust this to change overall ASCII character density
# Higher values = more characters visible, smaller individual characters
# Lower values = fewer characters visible, larger individual characters
ASCII_DENSITY_CONFIG = {
    'font_size': 10,  # Base font size (lower = more density, higher = less density)
    'line_spacing': 2,  # Spacing between lines (lower = more density)
    'char_spacing': 1.0,  # Character width multiplier (affects horizontal density)
}

# Kraken appearance configuration
KRAKEN_CONFIG = {
    'color': '#E0C6FF',  # Kraken sprite color (change this to update all kraken sprites)
}

# Boat configuration
BOAT_CONFIG = {
    'speed': 1,
    'color': '#FFFFFF',
    'update_interval': 3  # Update every N frames to slow down movement
}

# Debug grid overlay configuration
DEBUG_CONFIG = {
    'show_grid': True,  # Set to True to show debugging grid
    'grid_size': 50,     # Size of grid cells in pixels
    'grid_color': '#444444',  # Grid line color (dark gray)
    'show_coordinates': True,  # Show coordinate labels
    'show_boundaries': True,   # Show water level and boundaries
}

# Boat ASCII art - Left to Right (6 lines tall, rectangularized)
# Each line is exactly 16 characters wide
BOAT_SPRITE_LR = [
    "     |    |     ",  # Line 0: Masts
    "    )_)  )_)    ",  # Line 1: Sails
    "   )___))___)   ",  # Line 2: Sails lower
    "  )____)_____)  ",  # Line 3: Hull top
    "_____|____|_____",  # Line 4: Hull middle
    "\\______________/",  # Line 5: Hull bottom (overwrites top wave)
]

# Boat ASCII art - Right to Left (6 lines tall, rectangularized)
# Each line is exactly 16 characters wide
BOAT_SPRITE_RL = [
    "     |    |     ",  # Line 0: Masts
    "    (_(  (_(    ",  # Line 1: Sails
    "   (___((___(   ",  # Line 2: Sails lower
    "  (_____(____(  ",  # Line 3: Hull top
    "_____|____|_____",  # Line 4: Hull middle
    "\\______________/",  # Line 5: Hull bottom (overwrites top wave)
]

def get_density_font_size():
    """Get the configured font size for ASCII density"""
    return ASCII_DENSITY_CONFIG['font_size']

def get_density_line_height():
    """Get the calculated line height based on density config"""
    return ASCII_DENSITY_CONFIG['font_size'] + ASCII_DENSITY_CONFIG['line_spacing']

def get_kraken_color():
    """Get the configured kraken color"""
    return KRAKEN_CONFIG['color']

def get_boat_sprite(direction='lr'):
    """Get the boat ASCII art sprite
    
    Args:
        direction: 'lr' for left-to-right, 'rl' for right-to-left
    """
    if direction == 'rl':
        return BOAT_SPRITE_RL
    return BOAT_SPRITE_LR

def get_boat_speed():
    """Get the configured boat speed"""
    return BOAT_CONFIG['speed']

def get_boat_color():
    """Get the configured boat color"""
    return BOAT_CONFIG['color']

def get_boat_width():
    """Get the width of the boat sprite in characters"""
    if BOAT_SPRITE_LR:
        return len(BOAT_SPRITE_LR[0])
    return 0

def get_boat_update_interval():
    """Get the configured boat update interval (frames between position updates)"""
    return BOAT_CONFIG['update_interval']

def integrate_boat_into_waves(wave_line, boat_line, boat_char_position):
    """Integrate a boat line into a wave line at the specified character position
    
    Args:
        wave_line: The wave pattern string (repeating)
        boat_line: A line from the boat sprite
        boat_char_position: Character position where boat starts (can be negative)
    
    Returns:
        Modified wave line with boat integrated
    """
    if boat_char_position >= len(wave_line) or boat_char_position + len(boat_line) < 0:
        # Boat completely off screen
        return wave_line
    
    # Convert to list for modification
    wave_chars = list(wave_line)
    
    # Calculate which part of the boat is visible
    boat_start = max(0, -boat_char_position)
    boat_end = min(len(boat_line), len(wave_line) - boat_char_position)
    
    wave_start = max(0, boat_char_position)
    
    # Overlay boat onto wave (only non-space characters)
    for i in range(boat_start, boat_end):
        if boat_line[i] != ' ':
            wave_chars[wave_start + (i - boat_start)] = boat_line[i]
    
    return ''.join(wave_chars)

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
    
    # Upside-down swimming sprites (for swimming to intercept boats)
    'swim_flip1': [
        "     _/         `---   ",
        "  /    ___/  \\__       ",
        "   ,-.___/ || \\__,-._  ",
        "   \\____/ |||| \\____/ `",
        "  _ \\___/||||||\\___/ _ ",
        "   (    \\      /    |  ",
        "    )  @        @   ?  ",
        "       |        |      ",
        "       \\        /      ",
        "        \\______/       ",
        "                       ",
    ],
    
    'swim_flip2': [
        "     _/         `---   ",
        "  /    ___/  \\__       ",
        "   ,-.___/ || \\__,-._  ",
        "   \\____/ |||| \\____/ `",
        "  _ \\___/||||||\\___/ _ ",
        "   (    \\  ^   /    |  ",
        "    )  O        O   ?  ",
        "       |        |      ",
        "       \\        /      ",
        "        \\______/       ",
        "                       ",
    ],
    
    'swim_flip3': [
        "     _/         `---   ",
        "  /    ___/  \\__       ",
        "   ,-.___/ || \\__,-._  ",
        "   \\____/ |||| \\____/ `",
        "  _ \\___/||||||\\___/ _ ",
        "   (    \\  >   /    |  ",
        "    )  @        @   ?  ",
        "       |        |      ",
        "       \\        /      ",
        "        \\______/       ",
        "                       ",
    ],
    
    # Upside-down attack sprites (for attacking boats)
    'attack1': [
        "     _/         `---   ",
        "  /    ___/  \\__       ",
        "   ,-.___/ || \\__,-._  ",
        "   \\____/ |||| \\____/ `",
        "  _ \\___/||||||\\___/ _ ",
        "   (    \\  ><  /    |  ",
        "    )  @        @   ?  ",
        "       |        |      ",
        "       \\        /      ",
        "        \\______/       ",
        "                       ",
    ],
    
    'attack2': [
        "     _/         `---   ",
        "  /    ___/  \\__       ",
        "   ,-.___/ || \\__,-._  ",
        "   \\____/ |||| \\____/ `",
        "  _ \\___/||||||\\___/ _ ",
        "   (    \\ >XX< /    |  ",
        "    )  X        X   ?  ",
        "       |        |      ",
        "       \\        /      ",
        "        \\______/       ",
        "                       ",
    ],
    
    'attack3': [
        "     _/         `---   ",
        "  /    ___/  \\__       ",
        "   ,-.___/ || \\__,-._  ",
        "   \\____/ |||| \\____/ `",
        "  _ \\___/||||||\\___/ _ ",
        "   (    \\ <**> /    |  ",
        "    )  *        *   ?  ",
        "       |        |      ",
        "       \\        /      ",
        "        \\______/       ",
        "                       ",
    ],
}

# Animation sequences for different kraken states
ASCII_ANIMATIONS = {
    'idle': ['idle1', 'idle2'],
    'swimming': ['swim1', 'swim2', 'swim3'],
    'eating': ['eat1', 'eat2', 'eat3'],
    'swimming_flip': ['swim_flip1', 'swim_flip2', 'swim_flip3'],
    'attacking': ['attack1', 'attack2', 'attack3']
}

# Ocean Cross-Section Environment ASCII Art
UNDERWATER_ENVIRONMENT = {

    
    # Animated wave patterns (cycle through these for animation)
    'ocean_surface_frame1': "~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈",
    'ocean_surface_frame2': "≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈~≈",
    'ocean_surface_frame3': "~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈",
    'ocean_surface_frame4': "≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈~~≈≈",
    
    # Bubbles for atmosphere
    'bubbles_small': ["○", "∘", "·", "°"],
    'bubbles_medium': ["●", "○"],
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

def render_underwater_environment(canvas, width, height, animation_frame=0, boat_char_pos=None, boat_active=False, boat_direction='lr'):
    """Render ocean cross-section: top 1/5 surface area, bottom 4/5 underwater
    
    Args:
        canvas: Tkinter canvas
        width: Canvas width
        height: Canvas height
        animation_frame: Current animation frame for wave animation
        boat_char_pos: Character position of boat (for integration into waves)
        boat_active: Whether boat is active and should be rendered
        boat_direction: Direction of boat ('lr' = left-to-right, 'rl' = right-to-left)
    """
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
    
    # ===== ANIMATED OCEAN SURFACE (7 LINES TALL: 5 blank + 2 waves) =====
    # Cycle through wave animation frames
    wave_frames = [
        UNDERWATER_ENVIRONMENT['ocean_surface_frame1'],
        UNDERWATER_ENVIRONMENT['ocean_surface_frame2'],
        UNDERWATER_ENVIRONMENT['ocean_surface_frame3'],
        UNDERWATER_ENVIRONMENT['ocean_surface_frame4']
    ]
    current_wave_top = wave_frames[animation_frame % 4]
    # Bottom line uses alternating frame for better wave effect
    current_wave_bottom = wave_frames[(animation_frame + 2) % 4]
    
    # Make surface lines span the ENTIRE width
    num_repeats = (width // 8) + 2  # Character width ~8 pixels, add extra for safety
    full_wave_line_top = current_wave_top * num_repeats
    full_wave_line_bottom = current_wave_bottom * num_repeats
    
    # Create 5 blank lines above waves
    blank_line = " " * (len(full_wave_line_top))
    
    # Integrate boat into surface if active (boat is 6 lines, overlaps top wave)
    if boat_active and boat_char_pos is not None:
        boat_sprite = get_boat_sprite(boat_direction)
        if len(boat_sprite) >= 6:
            # Boat line 5 (hull bottom) overwrites the top wave line
            full_wave_line_top = integrate_boat_into_waves(full_wave_line_top, boat_sprite[5], boat_char_pos)
    
    # Render 7-line surface: 5 blank lines + 2 wave lines
    line_height = 10
    surface_y_start = water_level - (5 * line_height)  # Start 5 lines above water_level
    
    # Draw 5 blank lines (or boat lines 1-5 if boat is present)
    for i in range(5):
        y_pos = surface_y_start + (i * line_height)
        
        if boat_active and boat_char_pos is not None and i < len(boat_sprite) - 1:
            # Render boat line i into this blank line
            boat_line_text = blank_line
            boat_line_text = integrate_boat_into_waves(boat_line_text, boat_sprite[i], boat_char_pos)
            canvas.create_text(
                0, y_pos,
                text=boat_line_text,
                font=('Courier', 8, 'bold'),
                fill='#FFFFFF',
                anchor='w',
                tags="environment"
            )
        else:
            # Just blank space
            canvas.create_text(
                0, y_pos,
                text=blank_line,
                font=('Courier', 8, 'bold'),
                fill='#FFFFFF',
                anchor='w',
                tags="environment"
            )
    
    # Draw FIRST animated wave line (line 6, with boat hull bottom overlapping if active)
    canvas.create_text(
        0, water_level,  # First wave line at water level
        text=full_wave_line_top,
        font=('Courier', 8, 'bold'),
        fill='#FFFFFF',
        anchor='w',  # Anchor to west (left) to ensure full coverage
        tags="environment"
    )
    
    # Draw SECOND animated wave line (line 7, bottom wave)
    canvas.create_text(
        0, water_level + 10,  # Second line below first
        text=full_wave_line_bottom,
        font=('Courier', 8, 'bold'),
        fill='#AAAAAA',  # Slightly darker to show depth
        anchor='w',
        tags="environment"
    )
    
    # ===== UNDERWATER AREA (Bottom 4/5) =====
    # Draw underwater background (deep blue, almost black)
    # Start below the 2-line surface (20 pixels for 2 lines)
    surface_height = 20  # Height of 2-line surface
    canvas.create_rectangle(
        0, water_level + surface_height, width, height,
        fill='#0A0F1C', outline='',
        tags="environment"
    )
    
    # CRITICAL: Lower environment to bottom of z-order so it doesn't cover kraken/shrimp/bubbles
    canvas.lower("environment")
    
    # Draw debug grid if enabled
    if DEBUG_CONFIG['show_grid']:
        render_debug_grid(canvas, width, height, water_level)
    
    return water_level  # Return water level for movement constraints

def render_debug_grid(canvas, width, height, water_level):
    """Render a debugging grid overlay to help with positioning and boundaries
    
    Args:
        canvas: Tkinter canvas
        width: Canvas width
        height: Canvas height
        water_level: Y-coordinate of water surface
    """
    grid_size = DEBUG_CONFIG['grid_size']
    grid_color = DEBUG_CONFIG['grid_color']
    
    # Clear previous debug elements
    canvas.delete("debug_grid")
    
    # Draw vertical grid lines
    for x in range(0, width, grid_size):
        canvas.create_line(
            x, 0, x, height,
            fill=grid_color,
            tags="debug_grid",
            dash=(2, 4)  # Dashed line
        )
        # Add x-coordinate labels
        if DEBUG_CONFIG['show_coordinates'] and x > 0:
            canvas.create_text(
                x, 10,
                text=str(x),
                fill='#888888',
                font=('Arial', 8),
                tags="debug_grid"
            )
    
    # Draw horizontal grid lines
    for y in range(0, height, grid_size):
        canvas.create_line(
            0, y, width, y,
            fill=grid_color,
            tags="debug_grid",
            dash=(2, 4)  # Dashed line
        )
        # Add y-coordinate labels
        if DEBUG_CONFIG['show_coordinates'] and y > 0:
            canvas.create_text(
                10, y,
                text=str(y),
                fill='#888888',
                font=('Arial', 8),
                tags="debug_grid"
            )
    
    # Show boundaries if enabled
    if DEBUG_CONFIG['show_boundaries']:
        # Calculate wave surface height
        wave_font_size = max(6, get_density_font_size() - 2)
        wave_line_height = wave_font_size + 2
        surface_height = wave_line_height * 2
        
        # Water level line (top of waves) - HIDDEN
        # canvas.create_line(
        #     0, water_level, width, water_level,
        #     fill='#00FFFF',  # Cyan
        #     width=2,
        #     tags="debug_grid"
        # )
        # canvas.create_text(
        #     width - 80, water_level - 10,
        #     text=f"Water Level: {water_level}",
        #     fill='#00FFFF',
        #     font=('Arial', 9, 'bold'),
        #     tags="debug_grid"
        # )
        
        # Underwater start (below waves) - HIDDEN
        # underwater_start = water_level + surface_height + 5
        # canvas.create_line(
        #     0, underwater_start, width, underwater_start,
        #     fill='#00FF00',  # Green
        #     width=2,
        #     tags="debug_grid"
        # )
        # canvas.create_text(
        #     width - 120, underwater_start + 15,
        #     text=f"Underwater Start: {underwater_start}",
        #     fill='#00FF00',
        #     font=('Arial', 9, 'bold'),
        #     tags="debug_grid"
        # )
        
        # Ocean floor boundary
        ocean_floor = height - 50
        canvas.create_line(
            0, ocean_floor, width, ocean_floor,
            fill='#FF8800',  # Orange
            width=2,
            tags="debug_grid"
        )
        canvas.create_text(
            width - 100, ocean_floor - 15,
            text=f"Ocean Floor: {ocean_floor}",
            fill='#FF8800',
            font=('Arial', 9, 'bold'),
            tags="debug_grid"
        )
    
    # Keep grid below other elements but above environment
    # Only lower if bubbles exist (to avoid "doesn't match any items" error)
    if canvas.find_withtag("bubbles"):
        canvas.tag_lower("debug_grid", "bubbles")

def is_in_water(x, y, water_level, canvas_height):
    """Check if coordinates are in the underwater area (bottom 4/5 of canvas)"""
    # Water starts after the 2-line surface (20 pixels total)
    surface_height = 20
    underwater_start = water_level + surface_height
    # Leave space above ocean floor
    underwater_end = canvas_height - 50
    return y >= underwater_start and y <= underwater_end

def spawn_bubble(bubble_list, width, water_level, height):
    """Spawn a new bubble at a random underwater position"""
    import random
    
    # Spawn in underwater area only (below 2-line surface, above ocean floor)
    surface_height = 20  # Height of 2-line surface
    underwater_start = water_level + surface_height + 10  # Below surface
    underwater_end = height - 60  # Above ocean floor
    
    # Spawn across entire width (no margin)
    x = random.randint(0, width)
    y = random.randint(underwater_start, underwater_end)
    
    # Bubble appearance
    bubble_char = random.choice(UNDERWATER_ENVIRONMENT['bubbles_small'] + 
                              UNDERWATER_ENVIRONMENT['bubbles_medium'])
    bubble_size = random.choice([10, 12, 14, 16])
    bubble_color = '#FFFFFF'
    
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
    # Surface is 2 lines tall: water_level to water_level + 10
    # Remove bubbles slightly before they reach the visible surface (for realism)
    bubble_removal_threshold = 15  # Remove 15 pixels before water_level
    for i, bubble in enumerate(bubble_list):
        # Move bubble upward (rising physics)
        bubble['y'] -= 2  # Rise speed: 2 pixels per frame
        
        # Mark for removal if approaching surface (slightly before water_level)
        if bubble['y'] <= water_level + bubble_removal_threshold:
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
    print(f"Current Density Config: Font Size={get_density_font_size()}, Line Height={get_density_line_height()}\n")
    print(f"Debug Grid: {'ENABLED' if DEBUG_CONFIG['show_grid'] else 'DISABLED'}")
    if DEBUG_CONFIG['show_grid']:
        print(f"  Grid Size: {DEBUG_CONFIG['grid_size']}px")
        print(f"  Show Coordinates: {DEBUG_CONFIG['show_coordinates']}")
        print(f"  Show Boundaries: {DEBUG_CONFIG['show_boundaries']}\n")
    
    for state, frames in ASCII_ANIMATIONS.items():
        print(f"--- {state.upper()} Animation Frames ---")
        for frame_name in frames:
            lines = ASCII_PET_SPRITES[frame_name]
            print(f"\nFrame: {frame_name}")
            for line in lines:
                print(f"  {line}")
        print("\n" + "─" * 50 + "\n")
    
    print("=== Underwater Environment Elements ===\n")
    
    print("Water Surface (2 lines - animated):")
    for line in UNDERWATER_ENVIRONMENT['ocean_surface_frame1']:
        print(f"  {line[:50]}...")
    
    print(f"\nBubbles: {', '.join(UNDERWATER_ENVIRONMENT['bubbles_small'] + UNDERWATER_ENVIRONMENT['bubbles_medium'])}")
    print("\nYour kraken will swim in this underwater world! 🐙")
    print(f"\n💡 Tip: Adjust ASCII_DENSITY_CONFIG at the top of this file to change character density:")
    print(f"   - Lower font_size = MORE density (more chars visible)")
    print(f"   - Higher font_size = LESS density (fewer chars visible)")
    print(f"\n🐛 Debug Grid: Set DEBUG_CONFIG['show_grid'] = True to enable grid overlay")

if __name__ == "__main__":
    demo_ascii_art()
