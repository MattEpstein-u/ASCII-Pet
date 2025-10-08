#!/usr/bin/env python3
"""
ASCII Underwater Kraken - Shrimp Hunter
A simple ASCII art kraken that hunts and eats shrimp you drop in the water.
Click anywhere underwater to drop shrimp!
"""

import tkinter as tk
import math
import platform
import sys
from designs import (ASCII_PET_SPRITES, ASCII_ANIMATIONS, render_ascii_art,
                    render_underwater_environment, is_in_water, update_bubbles,
                    get_density_font_size, get_density_line_height, get_kraken_color, 
                    get_boat_sprite, get_boat_speed, get_boat_color, get_boat_width, 
                    get_boat_update_interval, DEBUG_CONFIG)

class ASCIIUnderwaterKraken:
    def __init__(self):
        self.root = tk.Tk()
        self.calculate_container_size()
        self.setup_window()
        
        # Kraken state - MUST be initialized before setup_pet() and update_behavior()
        self.target_x = self.container_width // 2
        self.target_y = (self.container_height * 2) // 3
        self.animation_frame = 0
        self.state = "idle"
        self.wave_animation_frame = 0  # For ocean surface animation
        
        # Kraken rendering settings - use density config font size
        self.kraken_font_size = get_density_font_size()  # Use density config (10)
        self.kraken_sprite_lines = 11  # Kraken sprite is 11 lines tall
        
        # Calculate kraken dimensions based on density configuration
        self.kraken_line_height = get_density_line_height()  # Font size + line spacing from config
        self.kraken_total_height = self.kraken_sprite_lines * self.kraken_line_height
        self.kraken_radius = self.kraken_total_height // 2
        
        print(f"🐙 Kraken dimensions: line_height={self.kraken_line_height}, total_height={self.kraken_total_height}, radius={self.kraken_radius}")
        
        # Mouth offset (where kraken eats) - mouth is on line 6 (0-indexed line 5)
        self.mouth_offset_x = 0  # Centered horizontally
        self.mouth_offset_y = 5 * self.kraken_line_height  # 5 lines down from top
        
        # Shrimp eaten counter system (initialize before setup_pet)
        self.shrimp_eaten_count = 0  # How many shrimp the kraken has eaten (max 100)
        self.decay_timer = 0  # Frames since last decay (decays every 11 seconds = 110 frames at 10fps)
        self.counter_change_indicator = None  # "+1" or "-1" visual indicator
        self.counter_change_frames = 0  # How long to show the indicator
        
        # Boat destruction counter
        self.boats_destroyed = 0  # How many boats the kraken has destroyed
        self.show_boat_counter = False  # Only show after first boat is destroyed
        
        self.setup_pet()
        self.setup_animations()
        
        # Bubble physics system
        self.bubble_list = []  # List of active bubbles with positions
        
        # Shrimp feeding system
        self.shrimp_queue = []  # List of (x, y, tag) tuples
        self.current_shrimp_target = None
        self.eating_shrimp = False
        self.eating_frames = 0  # Counter for eating animation duration
        self.shrimp_counter = 0  # For unique shrimp tags
        self.stuck_frames = 0  # Counter for how long kraken has been stuck at boundary
        self.last_kraken_x = 0  # Track last position to detect if stuck
        self.last_kraken_y = 0
        
        # Boat system (spawns when clicking above water, can respawn after previous boat sails off)
        self.boat_active = False  # Whether a boat is currently on screen
        self.boat_char_pos = -get_boat_width()  # Current boat character position (starts off-screen left)
        self.boat_update_counter = 0  # Frame counter for slowing down boat movement
        self.boat_direction = 'lr'  # Direction: 'lr' = left-to-right, 'rl' = right-to-left
        self.boat_attacked = False  # Whether kraken has triggered attack on current boat
        
        # Kraken attack state
        self.attacking_boat = False  # Whether kraken is currently attacking a boat
        self.attack_phase = 'none'  # Attack phases: 'none', 'swimming', 'attacking', 'returning'
        self.attack_frames = 0  # Counter for attack animation duration
        self.pre_attack_state = None  # Store what kraken was doing before attack
        self.pre_attack_target = None  # Store shrimp target before attack
        self.boat_pending_destruction = False  # Flag to destroy boat at next sprite update
        
        # Start the main loops
        self.animate()
        self.update_behavior()
    
    def calculate_container_size(self):
        """Calculate container size as 1/5 of screen area"""
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate 1/5 of screen area (approximately square container)
        total_area = screen_width * screen_height
        container_area = total_area // 5
        
        # Make container roughly square, but constrain to reasonable dimensions
        container_side = int(container_area ** 0.5)
        
        # Constrain to reasonable limits (larger for underwater environment)
        self.container_width = max(400, min(container_side, 800))
        self.container_height = max(350, min(container_side, 600))
        
        # Position container in bottom-right corner with no margin
        margin = 50  # Remove right margin to touch edge
        self.container_x = screen_width - self.container_width
        self.container_y = screen_height - self.container_height - margin
        
        print(f"Screen: {screen_width}x{screen_height}")
        print(f"Container: {self.container_width}x{self.container_height} at ({self.container_x}, {self.container_y})")
    
    def setup_window(self):
        """Configure the main window"""
        self.root.title("ASCII Underwater Kraken")
        
        # Set window size and position using container dimensions
        geometry = f"{self.container_width}x{self.container_height}+{self.container_x}+{self.container_y}"
        self.root.geometry(geometry)
        
        # Get the operating system
        self.os_type = platform.system()
        
        # Configure window to stay on desktop background (below other apps)
        if self.os_type == "Darwin":  # macOS
            # On macOS, use level -1 to stay below normal windows
            self.root.attributes('-alpha', 0.90)  # Slight transparency for container
            self.root.overrideredirect(True)  # Remove window decorations
            # Set window level to desktop level (below normal windows)
            try:
                # This puts the window at desktop level on macOS
                self.root.call('wm', 'attributes', '.', '-topmost', False)
                self.root.call('wm', 'attributes', '.', '-level', 'desktop')
            except:
                # Fallback: just don't stay on top
                pass
                
        elif self.os_type == "Windows":  # Windows
            # On Windows, use specific attributes to stay on desktop
            self.root.overrideredirect(True)  # Remove window decorations
            self.root.attributes('-alpha', 0.90)  # Slight transparency for container
            # Try to set window to desktop level
            try:
                # Import Windows-specific modules if available
                import win32gui
                import win32con
                # Get window handle and set it below normal windows
                hwnd = int(self.root.wm_frame(), 16)
                win32gui.SetWindowPos(hwnd, win32con.HWND_BOTTOM, 0, 0, 0, 0, 
                                    win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_NOACTIVATE)
            except ImportError:
                # If win32gui not available, just don't stay on top
                print("Note: Install pywin32 for better Windows desktop integration")
                pass
        else:  # Linux and others
            self.root.overrideredirect(True)
            self.root.attributes('-alpha', 0.90)
            # Try to stay below other windows
            try:
                self.root.attributes('-type', 'desktop')
            except:
                pass
        
        # Set a subtle background for the container
        # Use a very light color that blends with most wallpapers
        self.root.configure(bg='#0A0F1C')  # Deep blue, almost black
        
        # Add a subtle border to define the container area
        self.root.configure(highlightbackground='#d5d5d5', highlightcolor='#d5d5d5', highlightthickness=1)
    
    def setup_pet(self):
        """Create the underwater kraken display"""
        # Create canvas that fills the container
        self.canvas = tk.Canvas(self.root, width=self.container_width, height=self.container_height, 
                               bg='#0A0F1C', highlightthickness=0)  # Deep blue, almost black background
        self.canvas.pack(fill='both', expand=True)
        
        # Render the underwater environment with animation (no boat initially)
        self.water_level = render_underwater_environment(
            self.canvas, self.container_width, self.container_height, 
            self.wave_animation_frame,
            boat_char_pos=None,
            boat_active=False
        )
        
        print(f"🌊 Water level initialized: {self.water_level}, Container height: {self.container_height}")
        print(f"🌊 Underwater starts at: {self.water_level + 20} (water_level + 20)")
        
        # Store kraken starting position (in underwater area)
        self.kraken_start_x = self.container_width // 2
        self.kraken_start_y = self.water_level + 100  # Well below water surface
        
        # Ensure starting position is in water
        if not is_in_water(self.kraken_start_x, self.kraken_start_y, self.water_level, self.container_height):
            self.kraken_start_y = self.water_level + 50
        
        # Create the initial ASCII kraken art
        self.current_sprite = 'idle1'
        self.render_kraken()
        
        # Initialize shrimp counter display
        self.update_counter_display()
        
        # Bubble system initialized (bubbles will spawn over time)
        # No initial bubbles needed - they'll appear naturally
        
        # Bind mouse clicks: left-click and right-click
        self.canvas.bind('<Button-1>', self.on_click)  # Left-click
        self.canvas.bind('<Button-3>', self.on_click)  # Right-click
    
    def render_kraken(self):
        """Render the current ASCII kraken sprite"""
        sprite_lines = ASCII_PET_SPRITES.get(self.current_sprite, ASCII_PET_SPRITES['idle1'])
        
        # Get current kraken position or use default
        coords = self.canvas.coords("kraken")
        if coords:
            x, y = coords[0], coords[1]
        else:
            x, y = self.kraken_start_x, self.kraken_start_y
        
        # Render the ASCII art with configured kraken color
        # Use consistent font size for all kraken sprites
        render_ascii_art(sprite_lines, x, y, self.canvas, tag="kraken", color=get_kraken_color(), font_size=self.kraken_font_size)
    
    def setup_animations(self):
        """Setup animation sequences"""
        self.animations = ASCII_ANIMATIONS
    
    def on_click(self, event):
        """Handle clicks: drop shrimp in water, spawn boat above water
        
        Left-click above water: spawn boat going right-to-left
        Right-click above water: spawn boat going left-to-right
        Any click in water: drop shrimp
        """
        if is_in_water(event.x, event.y, self.water_level, self.container_height):
            # Click underwater - drop shrimp
            self.drop_shrimp(event.x, event.y)
        elif event.y < self.water_level and not self.boat_active:
            # Click above water and no boat currently active - spawn boat
            # event.num: 1 = left-click, 3 = right-click
            if event.num == 3:  # Right-click: left-to-right
                self.spawn_boat(direction='lr')
            else:  # Left-click (or any other): right-to-left
                self.spawn_boat(direction='rl')
        else:
            # Click was above water but boat is active, or other invalid area
            pass

    
    def move_kraken_to(self, x, y):
        """Move kraken to specific coordinates (only in water, with strict boundaries)"""
        # Enforce strict boundaries - don't allow crossing surface or floor
        margin = self.kraken_radius + 10
        
        # Clamp to container sides
        x = max(margin, min(x, self.container_width - margin))
        
        # Clamp to underwater area (below surface, above floor)
        # TOP boundary: kraken's head (top) can reach the water_level
        # render_ascii_art renders line 0 at y, so y IS the top of the sprite
        min_y = self.water_level
        
        # BOTTOM boundary: kraken's legs (bottom) must stay above ocean floor
        # Ocean floor is at container_height - 50
        # Bottom of sprite = y + kraken_total_height
        # We want: y + kraken_total_height <= ocean_floor
        # Therefore: y <= ocean_floor - kraken_total_height
        ocean_floor = self.container_height - 50
        max_y = ocean_floor - self.kraken_total_height
        
        # Debug: show what boundaries are being calculated
        if y < min_y:
            print(f"🐙 Clamping y from {y} to min_y {min_y} (head at water surface)")
        if y > max_y:
            print(f"🐙 Clamping y from {y} to max_y {max_y} (legs at ocean floor)")
        
        y = max(min_y, min(y, max_y))
        
        # Render kraken at validated position with configured color
        # No need to check is_in_water() since we've already validated boundaries above
        sprite_lines = ASCII_PET_SPRITES.get(self.current_sprite, ASCII_PET_SPRITES['idle1'])
        render_ascii_art(sprite_lines, x, y, self.canvas, tag="kraken", color=get_kraken_color(), font_size=self.kraken_font_size)
        return True
    
    def drop_shrimp(self, x, y):
        """Drop a shrimp at the specified underwater position"""
        # First check: maximum queue size (20 shrimp)
        max_shrimp = 20
        if len(self.shrimp_queue) >= max_shrimp:
            print(f"⚠️ Click rejected: shrimp queue is full ({len(self.shrimp_queue)}/{max_shrimp}). Wait for kraken to eat some!")
            return
        
        # Strict validation: shrimp must be below the 2-line surface
        surface_height = 20  # 2-line surface
        underwater_start = self.water_level + surface_height
        ocean_floor = self.container_height - 50
        
        # Second check: y must be in valid underwater range
        if y < underwater_start:
            print(f"⚠️ Click rejected: y={y} is above underwater start {underwater_start} (water_level={self.water_level})")
            return
        
        if y > ocean_floor:
            print(f"⚠️ Click rejected: y={y} is below ocean floor {ocean_floor}")
            return
        
        # Third check: use is_in_water validation
        if not is_in_water(x, y, self.water_level, self.container_height):
            print(f"⚠️ Click rejected by is_in_water: ({x}, {y})")
            return
        
        # Fourth check: ensure new shrimp is at least 80 pixels from all existing shrimp
        min_distance = 80
        for existing_x, existing_y, _ in self.shrimp_queue:
            distance = math.sqrt((x - existing_x)**2 + (y - existing_y)**2)
            if distance < min_distance:
                print(f"⚠️ Click rejected: too close to existing shrimp (distance: {distance:.1f} < {min_distance})")
                return
        
        # All checks passed - add shrimp
        self.shrimp_counter += 1
        shrimp_tag = f"shrimp_{self.shrimp_counter}"
        self.shrimp_queue.append((x, y, shrimp_tag))
        # Render shrimp on canvas with same font size as kraken
        # Use Georgia font for a more curved, shrimp-like comma appearance
        shrimp_size = get_density_font_size()  # Same size as kraken
        self.canvas.create_text(x, y, text=",", font=("Georgia", shrimp_size, "bold"),
                               fill="#FFB6C1", tags=shrimp_tag)
        print(f"🦐 Shrimp dropped at ({x}, {y}). Queue size: {len(self.shrimp_queue)}")
    
    def eat_shrimp(self):
        """Kraken eats the current target shrimp"""
        if self.current_shrimp_target:
            # Remove shrimp from canvas using stored tag
            x, y, tag = self.current_shrimp_target
            self.canvas.delete(tag)
            # Remove from queue
            self.shrimp_queue.remove(self.current_shrimp_target)
            self.current_shrimp_target = None
            self.eating_shrimp = False
            self.eating_frames = 0  # Reset eating timer
            
            # Increment shrimp eaten counter (max 100)
            if self.shrimp_eaten_count < 100:
                self.shrimp_eaten_count += 1
                self.counter_change_indicator = "+1"
                self.counter_change_frames = 5  # Show indicator for 0.5 seconds (5 frames at 10fps)
                self.update_counter_display()
            
            print(f"🐙 Om nom nom! Shrimp eaten. Remaining: {len(self.shrimp_queue)}")
    
    def get_next_shrimp_target(self):
        """Get the closest shrimp from the queue"""
        if self.shrimp_queue and not self.current_shrimp_target:
            # Get current kraken position
            kraken_coords = self.canvas.coords("kraken")
            if not kraken_coords:
                # Kraken not yet rendered, just pick first shrimp
                self.current_shrimp_target = self.shrimp_queue[0]
            else:
                # Find the closest shrimp to current kraken position
                kraken_x, kraken_y = kraken_coords[0], kraken_coords[1]
                closest_shrimp = None
                closest_distance = float('inf')
                
                for shrimp in self.shrimp_queue:
                    shrimp_x, shrimp_y, _ = shrimp
                    distance = math.sqrt((shrimp_x - kraken_x)**2 + (shrimp_y - kraken_y)**2)
                    if distance < closest_distance:
                        closest_distance = distance
                        closest_shrimp = shrimp
                
                self.current_shrimp_target = closest_shrimp
            
            self.eating_shrimp = True
            x, y, tag = self.current_shrimp_target
            print(f"🐙 Kraken targeting shrimp at ({x}, {y})")
    
    def update_counter_display(self):
        """Update the shrimp eaten counter display at the top left of the window"""
        # Clear previous counter display
        self.canvas.delete("shrimp_counter")
        self.canvas.delete("counter_indicator")
        
        # Display shrimp counter at top left
        counter_x = 20
        counter_y = 15
        
        # Show the count in shrimp color (#FFB6C1) - smaller Consolas font
        self.canvas.create_text(counter_x, counter_y, 
                               text=str(self.shrimp_eaten_count),
                               font=("Consolas", 18, "bold"),
                               fill="#FFB6C1",
                               tags="shrimp_counter",
                               anchor="nw")
        
        # Show +1 or -1 indicator if active (to the right of the counter)
        if self.counter_change_indicator and self.counter_change_frames > 0:
            indicator_x = counter_x + 25
            self.canvas.create_text(indicator_x, counter_y,
                                   text=self.counter_change_indicator,
                                   font=("Consolas", 14, "bold"),
                                   fill="#FFB6C1",
                                   tags="counter_indicator",
                                   anchor="nw")
    
    def update_boat_counter_display(self):
        """Update the boat destruction counter display at the top right of the window"""
        # Clear previous boat counter display
        self.canvas.delete("boat_counter")
        
        # Only display if at least one boat has been destroyed
        if self.show_boat_counter:
            # Display boat counter at top right
            counter_x = self.container_width - 20
            counter_y = 15
            
            # Show "⛵: count" in white
            boat_text = f"⛵: {self.boats_destroyed}"
            self.canvas.create_text(counter_x, counter_y,
                                   text=boat_text,
                                   font=("Consolas", 18, "bold"),
                                   fill="#FFFFFF",
                                   tags="boat_counter",
                                   anchor="ne")

    
    def spawn_boat(self, direction='lr'):
        """Spawn a boat that moves across the water surface (can be called multiple times after previous boat sails off)
        
        Args:
            direction: 'lr' for left-to-right (right-click), 'rl' for right-to-left (left-click)
        """
        if not self.boat_active:
            self.boat_active = True
            self.boat_direction = direction
            self.boat_attacked = False  # Reset attack flag for new boat
            
            # Set starting position based on direction
            screen_width_chars = self.container_width // 8
            if direction == 'rl':
                # Start off-screen to the right for right-to-left
                self.boat_char_pos = screen_width_chars + 10
            else:
                # Start off-screen to the left for left-to-right
                self.boat_char_pos = -get_boat_width()
            
            self.boat_update_counter = 0  # Reset frame counter
            print(f"⛵")
    
    def update_boat(self):
        """Update boat character position based on direction"""
        if self.boat_active:
            # Check if boat has reached 1/4 of the way across screen
            screen_width_chars = self.container_width // 8
            one_quarter_position = screen_width_chars / 4
            
            if not self.boat_attacked:
                # Check if boat crossed 1/4 threshold
                if self.boat_direction == 'rl':
                    # Right-to-left: check if passed 3/4 mark (coming from right)
                    three_quarters_position = 3 * screen_width_chars / 4
                    if self.boat_char_pos <= three_quarters_position:
                        self.trigger_boat_attack()
                else:
                    # Left-to-right: check if passed 1/4 mark (coming from left)
                    if self.boat_char_pos >= one_quarter_position:
                        self.trigger_boat_attack()
            
            # Increment frame counter
            self.boat_update_counter += 1
            
            # Only update position every N frames to slow down movement
            if self.boat_update_counter >= get_boat_update_interval():
                # Move boat based on direction
                if self.boat_direction == 'rl':
                    # Right-to-left: subtract speed
                    self.boat_char_pos -= get_boat_speed()
                else:
                    # Left-to-right: add speed
                    self.boat_char_pos += get_boat_speed()
                self.boat_update_counter = 0
            
            # Check if boat has sailed completely off screen (either direction)
            if self.boat_direction == 'rl':
                # Right-to-left: check if sailed off left edge
                if self.boat_char_pos < -get_boat_width() - 10:
                    self.boat_active = False
                    print("⛵...")
            else:
                # Left-to-right: check if sailed off right edge
                if self.boat_char_pos > screen_width_chars + 10:
                    self.boat_active = False
                    print("⛵...")
    
    def trigger_boat_attack(self):
        """Trigger kraken attack on the boat - abandon everything and attack!"""
        import random
        
        self.boat_attacked = True
        self.attacking_boat = True
        self.attack_phase = 'swimming'  # Start with swimming phase (upside down)
        self.attack_frames = 0
        
        # Determine if this attack will destroy the boat based on shrimp counter
        # Success rate = (shrimp_eaten_count / 100) * 0.2
        #success_rate = (self.shrimp_eaten_count / 100) * 0.2
        success_rate = 1
        self.attack_will_destroy = random.random() < success_rate
        
        # Save current state to resume later
        self.pre_attack_state = self.state
        self.pre_attack_target = self.current_shrimp_target
        
        # Calculate boat position in pixels for kraken to intercept
        # Position slightly ahead of the boat based on direction
        boat_pixel_x = self.boat_char_pos * 8  # Approximate char width
        
        if self.boat_direction == 'rl':
            self.target_x = boat_pixel_x + 180
        else:
            self.target_x = boat_pixel_x + 300
        
        self.target_y = self.water_level - 20  # Just below the surface
        
        # DON'T clear shrimp targets - save them for later
        # But stop eating current shrimp and reset eating counter
        # This allows kraken to resume eating the same shrimp from scratch
        self.eating_shrimp = False
        self.eating_frames = 0
        
        print("🐙 ATTACK!")

    def update_position(self):
        """Smoothly move kraken towards target (shrimp or boat)"""
        # Get current kraken position from canvas
        kraken_coords = self.canvas.coords("kraken")
        if not kraken_coords:
            return  # Kraken not yet rendered
        
        current_kraken_x, current_kraken_y = kraken_coords[0], kraken_coords[1]
        
        # If attacking boat, handle multi-phase attack sequence
        if self.attacking_boat:
            self.attack_frames += 1
            
            # PHASE 1: Swimming upside-down to intercept (0-20 frames, 2 seconds)
            if self.attack_phase == 'swimming':
                # Update target to track boat movement (stay on the side of boat)
                boat_pixel_x = self.boat_char_pos * 8
                if self.boat_direction == 'rl':
                    self.target_x = boat_pixel_x + 20
                else:
                    self.target_x = boat_pixel_x + 30
                
                # Move quickly to intercept position
                dx = self.target_x - current_kraken_x
                dy = self.target_y - current_kraken_y
                
                # Fast movement during attack
                distance = math.sqrt(dx**2 + dy**2)
                if distance > 5:
                    step_size = min(8.0, distance / 2)
                    new_x = current_kraken_x + (dx / distance) * step_size
                    new_y = current_kraken_y + (dy / distance) * step_size
                    self.move_kraken_to(new_x, new_y)
                
                # Once reached position, start attacking
                if distance < 30:
                    self.attack_phase = 'attacking'
                    self.attack_frames = 0  # Reset for attack phase timing
            
            # PHASE 2: Attacking the boat
            elif self.attack_phase == 'attacking':
                # Track and move with the boat during attack
                boat_pixel_x = self.boat_char_pos * 8
                if self.boat_direction == 'rl':
                    self.target_x = boat_pixel_x + 20
                else:
                    self.target_x = boat_pixel_x + 30
                
                # Follow the boat smoothly
                dx = self.target_x - current_kraken_x
                distance_x = abs(dx)
                if distance_x > 5:
                    step_size = min(4.0, distance_x / 2)
                    new_x = current_kraken_x + (dx / distance_x) * step_size
                    self.move_kraken_to(new_x, current_kraken_y)
                
                # Attack duration: 30 frames (3 seconds) to determine outcome
                attack_should_end = False
                
                if self.attack_frames == 30:
                    # Exactly at frame 30, determine outcome (only happens once)
                    if self.attack_will_destroy:
                        # Successful attack: mark boat for destruction at next sprite update
                        # Don't end attack yet - wait for boat to disappear
                        self.boat_pending_destruction = True
                        print("💥 Boat destroyed!")
                        # Continue attacking until boat disappears from view
                    else:
                        # Unsuccessful attack: boat escapes, end immediately
                        print("⛵ Boat escaped!")
                        attack_should_end = True
                
                # Check if boat has been destroyed (removed at sprite update)
                if self.boat_pending_destruction and not self.boat_active:
                    # Boat is now gone from view, end attack
                    attack_should_end = True
                    self.boat_pending_destruction = False
                    # Increment boat destruction counter
                    self.boats_destroyed += 1
                    self.show_boat_counter = True
                    self.update_boat_counter_display()
                
                if attack_should_end:
                    # Start returning phase
                    self.attack_phase = 'returning'
                    self.attack_frames = 0
                    
                    # Don't target specific pre-attack shrimp anymore
                    # Just return to a central hunting position and find closest shrimp
                    if len(self.shrimp_queue) > 0:
                        # Return to center of ocean to hunt closest shrimp
                        self.target_x = self.container_width // 2
                        self.target_y = self.water_level + 150
                    else:
                        # No shrimp available, return to idle position
                        self.target_x = self.container_width // 2
                        self.target_y = self.water_level + 150
            
            # PHASE 3: Returning and flipping right-side up (swim back)
            elif self.attack_phase == 'returning':
                # Move back to resume position
                dx = self.target_x - current_kraken_x
                dy = self.target_y - current_kraken_y
                
                # Normal movement speed
                distance = math.sqrt(dx**2 + dy**2)
                if distance > 5:
                    step_size = min(6.0, distance / 3)
                    new_x = current_kraken_x + (dx / distance) * step_size
                    new_y = current_kraken_y + (dy / distance) * step_size
                    self.move_kraken_to(new_x, new_y)
                
                # Check if we're stuck at a boundary trying to reach an unreachable target
                # Define boundaries for stuck detection
                margin = self.kraken_radius + 10
                min_x = margin
                max_x = self.container_width - margin
                min_y = self.water_level
                ocean_floor = self.container_height - 50
                max_y = ocean_floor - self.kraken_total_height
                
                stuck_at_boundary_returning = (
                    (abs(current_kraken_y - min_y) < 1 and self.target_y < current_kraken_y) or
                    (abs(current_kraken_y - max_y) < 1 and self.target_y > current_kraken_y) or
                    (abs(current_kraken_x - min_x) < 1 and self.target_x < current_kraken_x) or
                    (abs(current_kraken_x - max_x) < 1 and self.target_x > current_kraken_x)
                )
                
                # Once back in position OR stuck at boundary, finish attack and flip right-side up
                if distance < 30 or stuck_at_boundary_returning:
                    self.attacking_boat = False
                    self.attack_phase = 'none'
                    self.attack_frames = 0
                    
                    # Resume hunting - clear current target so closest shrimp will be selected
                    self.current_shrimp_target = None
                    self.eating_shrimp = False
                    
                    if len(self.shrimp_queue) > 0:
                        print("🐙 Back to hunting...")
                    else:
                        print("🐙 Back to idle...")
                    
                    self.pre_attack_state = None
                    self.pre_attack_target = None
            
            return
        
        # Normal shrimp hunting behavior
        # Check if there's a shrimp to eat
        if not self.current_shrimp_target and len(self.shrimp_queue) > 0:
            self.get_next_shrimp_target()
        
        # If targeting shrimp, move towards it
        if self.current_shrimp_target:
            shrimp_x, shrimp_y, shrimp_tag = self.current_shrimp_target
            
            # Calculate where the sprite anchor should be so the mouth reaches the shrimp
            # Mouth is at (sprite_x + mouth_offset_x, sprite_y + mouth_offset_y)
            # So: sprite_x + mouth_offset_x = shrimp_x  =>  sprite_x = shrimp_x - mouth_offset_x
            target_sprite_x = shrimp_x - self.mouth_offset_x
            target_sprite_y = shrimp_y - self.mouth_offset_y
            
            # Safety check: ensure target position is valid (in water and within bounds)
            # If not, fall back to simple targeting to avoid bugs at boundaries
            margin = self.kraken_radius + 10
            min_x = margin
            max_x = self.container_width - margin
            
            # TOP boundary: kraken's head can reach water_level
            # Since render_ascii_art draws line 0 at y, y IS the top position
            min_y = self.water_level
            
            # BOTTOM boundary: kraken's legs must stay above ocean floor
            # Ocean floor at container_height - 50, bottom of sprite at y + kraken_total_height
            ocean_floor = self.container_height - 50
            max_y = ocean_floor - self.kraken_total_height
            
            # Clamp target to safe bounds
            target_sprite_x = max(min_x, min(target_sprite_x, max_x))
            target_sprite_y = max(min_y, min(target_sprite_y, max_y))
            
            # Use adjusted target
            self.target_x = target_sprite_x
            self.target_y = target_sprite_y
            
            # Move towards target (using kraken position already obtained at start of function)
            dx = self.target_x - current_kraken_x
            dy = self.target_y - current_kraken_y
            distance = math.sqrt(dx**2 + dy**2)
            
            # Calculate where the mouth actually is right now
            current_mouth_x = current_kraken_x + self.mouth_offset_x
            current_mouth_y = current_kraken_y + self.mouth_offset_y
            
            # Check if mouth can reach the shrimp (either perfectly or as close as boundaries allow)
            # The mouth should be within eating range of the shrimp
            mouth_to_shrimp_dx = shrimp_x - current_mouth_x
            mouth_to_shrimp_dy = shrimp_y - current_mouth_y
            mouth_distance = math.sqrt(mouth_to_shrimp_dx**2 + mouth_to_shrimp_dy**2)
            
            # Check if we can get the mouth closer by moving, or if we're boundary-blocked
            # If target was clamped, calculate what the mouth position would be at the clamped target
            ideal_mouth_x = target_sprite_x + self.mouth_offset_x
            ideal_mouth_y = target_sprite_y + self.mouth_offset_y
            ideal_mouth_distance = math.sqrt((shrimp_x - ideal_mouth_x)**2 + (shrimp_y - ideal_mouth_y)**2)
            
            # Check if kraken is stuck at a boundary (being actively clamped)
            # This happens when we're trying to reach a position but boundaries won't let us
            # Detect by checking if current position is AT the boundary and target is beyond it
            stuck_at_top = (abs(current_kraken_y - min_y) < 1 and target_sprite_y < current_kraken_y)
            stuck_at_bottom = (abs(current_kraken_y - max_y) < 1 and target_sprite_y > current_kraken_y)
            stuck_at_left = (abs(current_kraken_x - min_x) < 1 and target_sprite_x < current_kraken_x)
            stuck_at_right = (abs(current_kraken_x - max_x) < 1 and target_sprite_x > current_kraken_x)
            stuck_at_boundary = stuck_at_top or stuck_at_bottom or stuck_at_left or stuck_at_right
            
            # Check if kraken hasn't moved (is genuinely stuck)
            position_changed = (abs(current_kraken_x - self.last_kraken_x) > 0.5 or 
                              abs(current_kraken_y - self.last_kraken_y) > 0.5)
            
            # Update stuck counter
            if stuck_at_boundary and not position_changed:
                self.stuck_frames += 1
            else:
                self.stuck_frames = 0
            
            # Update last position for next frame
            self.last_kraken_x = current_kraken_x
            self.last_kraken_y = current_kraken_y
            
            # Only consider truly stuck if we've been stuck for at least 5 frames
            # AND we're within reasonable mouth distance (not too far from shrimp)
            truly_stuck_at_boundary = (self.stuck_frames >= 5 and stuck_at_boundary and mouth_distance < 50)
            
            if distance > 2 and not truly_stuck_at_boundary:
                # Still moving to shrimp - reset eating timer since we're not stationary
                self.state = "swimming"
                self.eating_shrimp = False
                self.eating_frames = 0
                
                # Move step by step
                step_size = min(8.0, distance / 3)
                new_x = current_kraken_x + (dx / distance) * step_size
                new_y = current_kraken_y + (dy / distance) * step_size
                
                # Keep within water bounds
                new_x = max(min_x, min(new_x, max_x))
                new_y = max(min_y, min(new_y, max_y))
                
                # Move kraken (already validated by boundary clamping above)
                self.move_kraken_to(new_x, new_y)
            else:
                # Stopped moving OR at boundary limit - now can start eating animation
                # Kraken is stationary with mouth as close as possible to shrimp
                if self.current_shrimp_target:
                    self.state = "eating"
                    self.eating_shrimp = True  # Set flag so animate() shows eating animation
                    self.eating_frames += 1
                    # Eat shrimp after 15 frames (~0.75 seconds at 20fps)
                    if self.eating_frames >= 15:
                        self.eat_shrimp()
        else:
            # No target, return to idle
            if self.state != "idle":
                self.state = "idle"
    
    def update_behavior(self):
        """Update kraken behavior and state"""
        # Update wave animation (slower cycle - every 10 frames)
        # Pass boat position for integration into wave rendering
        if self.wave_animation_frame % 10 == 0:
            # If boat is pending destruction, destroy it now at sprite update
            if self.boat_pending_destruction and self.boat_active:
                self.boat_active = False
                # boat_pending_destruction flag will be cleared in attack logic
            
            render_underwater_environment(
                self.canvas, self.container_width, self.container_height, 
                self.wave_animation_frame // 10,
                boat_char_pos=self.boat_char_pos if self.boat_active else None,
                boat_active=self.boat_active,
                boat_direction=self.boat_direction
            )
        self.wave_animation_frame += 1
        
        # Update bubble physics every frame (spawn, rise, remove at surface)
        update_bubbles(self.bubble_list, self.canvas, self.container_width, 
                      self.water_level, self.container_height, spawn_chance=0.05)
        
        # Update shrimp eaten counter decay (every 11 seconds = 110 frames at 10fps)
        self.decay_timer += 1
        if self.decay_timer >= 110:
            self.decay_timer = 0
            if self.shrimp_eaten_count > 0:
                self.shrimp_eaten_count -= 1
                self.counter_change_indicator = "-1"
                self.counter_change_frames = 5  # Show indicator for 0.5 seconds (5 frames at 10fps)
                self.update_counter_display()
        
        # Update counter change indicator
        if self.counter_change_frames > 0:
            self.counter_change_frames -= 1
            if self.counter_change_frames == 0:
                self.counter_change_indicator = None
                self.update_counter_display()
        
        # Update boat movement (boat rendering is integrated into wave rendering above)
        self.update_boat()
        
        # Update position (shrimp hunting)
        self.update_position()
        
        # Schedule next behavior update
        self.root.after(100, self.update_behavior)

    
    def animate(self):
        """Animate the kraken sprite"""
        # Determine state based on what kraken is doing
        if self.attacking_boat:
            # Show different upside-down sprites for swimming vs attacking
            if self.attack_phase == 'swimming':
                # Swimming upside-down to intercept boat
                self.state = "swimming_flip"
            elif self.attack_phase == 'attacking':
                # Attacking the boat (upside-down)
                self.state = "attacking"
            elif self.attack_phase == 'returning':
                # Flipped back right-side up, swimming back
                if self.pre_attack_target:
                    self.state = "swimming"  # Swimming back to shrimp
                else:
                    self.state = "swimming"  # Swimming back to idle position
        elif self.eating_shrimp:
            self.state = "eating"
        elif self.current_shrimp_target or len(self.shrimp_queue) > 0:
            self.state = "swimming"
        else:
            self.state = "idle"
        
        # Get animation sequence based on current state
        current_animation = self.animations.get(self.state, self.animations['idle'])
        
        # Update animation frame
        sprite_name = current_animation[self.animation_frame % len(current_animation)]
        self.current_sprite = sprite_name
        
        # Render the updated sprite
        self.render_kraken()
        
        # Advance animation frame
        self.animation_frame += 1
        
        # Faster animation for eating and attacking
        if self.state == "eating" or self.state == "attacking":
            delay = 200
        else:
            delay = 500
        
        # Schedule next frame
        self.root.after(delay, self.animate)
    
    def run(self):
        """Start the kraken application"""
        print("• Press Ctrl+C in terminal to stop")
        # Position container (already calculated in __init__)
        geometry = f"{self.container_width}x{self.container_height}+{self.container_x}+{self.container_y}"
        self.root.geometry(geometry)
        
        # Start the main loop
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\n...")
            self.root.quit()

if __name__ == "__main__":
    try:
        print("🐙 ...")
        print()
        
        kraken = ASCIIUnderwaterKraken()
        kraken.run()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)