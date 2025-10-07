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
                    get_density_font_size, get_density_line_height, DEBUG_CONFIG)

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
        margin = 0  # Remove right margin to touch edge
        self.container_x = screen_width - self.container_width - margin
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
        
        # Render the underwater environment with animation
        self.water_level = render_underwater_environment(self.canvas, self.container_width, 
                                                         self.container_height, self.wave_animation_frame)
        
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
        
        # Bubble system initialized (bubbles will spawn over time)
        # No initial bubbles needed - they'll appear naturally
        
        # Bind mouse click to drop shrimp
        self.canvas.bind('<Button-1>', self.on_click)
    
    def render_kraken(self):
        """Render the current ASCII kraken sprite"""
        sprite_lines = ASCII_PET_SPRITES.get(self.current_sprite, ASCII_PET_SPRITES['idle1'])
        
        # Get current kraken position or use default
        coords = self.canvas.coords("kraken")
        if coords:
            x, y = coords[0], coords[1]
        else:
            x, y = self.kraken_start_x, self.kraken_start_y
        
        # Render the ASCII art with lavender coloring
        # Use consistent font size for all kraken sprites
        render_ascii_art(sprite_lines, x, y, self.canvas, tag="kraken", color="#E6E6FA", font_size=self.kraken_font_size)
    
    def setup_animations(self):
        """Setup animation sequences"""
        self.animations = ASCII_ANIMATIONS
    
    def on_click(self, event):
        """Handle clicks: drop shrimp in water (only underwater area)"""
        if is_in_water(event.x, event.y, self.water_level, self.container_height):
            self.drop_shrimp(event.x, event.y)
        else:
            # Click was above water or below ocean floor - ignore silently
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
        
        # Render kraken at validated position with lavender color
        # No need to check is_in_water() since we've already validated boundaries above
        sprite_lines = ASCII_PET_SPRITES.get(self.current_sprite, ASCII_PET_SPRITES['idle1'])
        render_ascii_art(sprite_lines, x, y, self.canvas, tag="kraken", color="#E6E6FA", font_size=self.kraken_font_size)
        return True
    
    def drop_shrimp(self, x, y):
        """Drop a shrimp at the specified underwater position"""
        # Strict validation: shrimp must be below the 2-line surface
        surface_height = 20  # 2-line surface
        underwater_start = self.water_level + surface_height
        ocean_floor = self.container_height - 50
        
        # First check: y must be in valid underwater range
        if y < underwater_start:
            print(f"⚠️ Click rejected: y={y} is above underwater start {underwater_start} (water_level={self.water_level})")
            return
        
        if y > ocean_floor:
            print(f"⚠️ Click rejected: y={y} is below ocean floor {ocean_floor}")
            return
        
        # Second check: use is_in_water validation
        if not is_in_water(x, y, self.water_level, self.container_height):
            print(f"⚠️ Click rejected by is_in_water: ({x}, {y})")
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
            print(f"🐙 Om nom nom! Shrimp eaten. Remaining: {len(self.shrimp_queue)}")
    
    def get_next_shrimp_target(self):
        """Get the next shrimp from the queue"""
        if self.shrimp_queue and not self.current_shrimp_target:
            self.current_shrimp_target = self.shrimp_queue[0]
            self.eating_shrimp = True
            x, y, tag = self.current_shrimp_target
            print(f"🐙 Kraken targeting shrimp at ({x}, {y})")


    
    def update_position(self):
        """Smoothly move kraken towards shrimp target"""
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
            
            kraken_coords = self.canvas.coords("kraken")
            if kraken_coords:
                current_kraken_x, current_kraken_y = kraken_coords[0], kraken_coords[1]
                
                # Move towards target
                dx = self.target_x - current_kraken_x
                dy = self.target_y - current_kraken_y
                distance = math.sqrt(dx**2 + dy**2)
                
                if distance > 5:
                    # Swimming to shrimp
                    self.state = "swimming"
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
                    # Reached target - start eating animation
                    if self.current_shrimp_target:
                        self.state = "eating"
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
        if self.wave_animation_frame % 10 == 0:
            render_underwater_environment(self.canvas, self.container_width, 
                                         self.container_height, self.wave_animation_frame // 10)
        self.wave_animation_frame += 1
        
        # Update bubble physics every frame (spawn, rise, remove at surface)
        update_bubbles(self.bubble_list, self.canvas, self.container_width, 
                      self.water_level, self.container_height, spawn_chance=0.05)
        
        # Update position (shrimp hunting)
        self.update_position()
        
        # Schedule next behavior update
        self.root.after(100, self.update_behavior)

    
    def animate(self):
        """Animate the kraken sprite"""
        # Get animation sequence based on current state
        current_animation = self.animations.get(self.state, self.animations['idle'])
        
        # Update animation frame
        sprite_name = current_animation[self.animation_frame % len(current_animation)]
        self.current_sprite = sprite_name
        
        # Render the updated sprite
        self.render_kraken()
        
        # Advance animation frame
        self.animation_frame += 1
        
        # Faster animation for eating
        delay = 300 if self.state == "eating" else 500
        
        # Schedule next frame
        self.root.after(delay, self.animate)
    
    def run(self):
        """Start the kraken application"""
        print("Starting ASCII Underwater Kraken...")
        print("• Lives in underwater environment in desktop corner")
        print("• Click anywhere underwater to drop shrimp")
        print("• Kraken will hunt and eat the shrimp")
        print("• Press Ctrl+C in terminal to stop")
        
        # Position container (already calculated in __init__)
        geometry = f"{self.container_width}x{self.container_height}+{self.container_x}+{self.container_y}"
        self.root.geometry(geometry)
        
        # Start the main loop
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\nPet is going to sleep... 😴")
            self.root.quit()

if __name__ == "__main__":
    try:
        print("🐙 Starting ASCII Underwater Kraken...")
        print(f"📏 Density: Font Size={get_density_font_size()}, Line Height={get_density_line_height()}")
        if DEBUG_CONFIG['show_grid']:
            print(f"🐛 Debug Grid: ENABLED (Grid Size: {DEBUG_CONFIG['grid_size']}px)")
        print("🦐 Click underwater to drop shrimp and feed your kraken!")
        print()
        
        kraken = ASCIIUnderwaterKraken()
        kraken.run()
    except Exception as e:
        print(f"Error starting ASCII kraken: {e}")
        print("Make sure you have a display available (not in headless mode)")
        sys.exit(1)