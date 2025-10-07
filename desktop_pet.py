#!/usr/bin/env python3
"""
ASCII Underwater Kraken - Cross-platform Desktop Companion
A majestic ASCII art kraken that lives in an underwater environment on your desktop.
Only visible when all applications are minimized to desktop.

Transformed from a simple pet into an underwater kraken in a detailed ASCII ocean.
"""

import tkinter as tk
import random
import math
import platform
import sys
from ascii_pet_designs import (ASCII_PET_SPRITES, ASCII_ANIMATIONS, render_ascii_art,
                              render_underwater_environment, is_in_water, add_floating_bubbles)

class ASCIIUnderwaterKraken:
    def __init__(self):
        self.root = tk.Tk()
        self.calculate_container_size()
        self.setup_window()
        self.setup_pet()
        self.setup_animations()
        
        # Kraken state
        self.target_x = self.container_width // 2
        self.target_y = (self.container_height * 2) // 3  # Start in underwater area
        self.current_x = self.container_width // 2
        self.current_y = (self.container_height * 2) // 3
        self.is_dragging = False
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.animation_frame = 0
        self.idle_counter = 0
        self.state = "idle"  # idle, swimming, sleeping, attack
        
        # Kraken properties
        self.kraken_width = 60  # Smaller for detailed ASCII art
        self.kraken_height = 50
        self.kraken_radius = 30  # For collision detection
        self.water_level = 0  # Will be set when environment is rendered
        
        # Bubble effects
        self.bubble_timer = 0
        
        # Start the main loops
        self.animate()
        self.update_behavior()
    
    def calculate_container_size(self):
        """Calculate container size as 1/8 of screen area"""
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate 1/8 of screen area (approximately square container)
        total_area = screen_width * screen_height
        container_area = total_area // 8
        
        # Make container roughly square, but constrain to reasonable dimensions
        container_side = int(container_area ** 0.5)
        
        # Constrain to reasonable limits (larger for underwater environment)
        self.container_width = max(400, min(container_side, 800))
        self.container_height = max(350, min(container_side, 600))
        
        # Position container in bottom-right corner with some margin
        margin = 50
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
        self.root.configure(bg='#f5f5f5')
        
        # Add a subtle border to define the container area
        self.root.configure(highlightbackground='#d5d5d5', highlightcolor='#d5d5d5', highlightthickness=1)
    
    def setup_pet(self):
        """Create the underwater kraken display"""
        # Create canvas that fills the container
        self.canvas = tk.Canvas(self.root, width=self.container_width, height=self.container_height, 
                               bg='#0F1419', highlightthickness=0)  # Dark ocean background
        self.canvas.pack(fill='both', expand=True)
        
        # Render the underwater environment
        self.water_level = render_underwater_environment(self.canvas, self.container_width, self.container_height)
        
        # Store kraken starting position (in underwater area)
        self.kraken_start_x = self.container_width // 2
        self.kraken_start_y = self.water_level + 100  # Well below water surface
        
        # Ensure starting position is in water
        if not is_in_water(self.kraken_start_x, self.kraken_start_y, self.water_level, self.container_height):
            self.kraken_start_y = self.water_level + 50
        
        # Create the initial ASCII kraken art
        self.current_sprite = 'idle1'
        self.render_kraken()
        
        # Add initial bubbles
        add_floating_bubbles(self.canvas, self.container_width, self.water_level, self.container_height)
        
        # Bind mouse events to the entire canvas
        self.canvas.bind('<Button-1>', self.start_drag)
        self.canvas.bind('<B1-Motion>', self.drag_kraken)
        self.canvas.bind('<ButtonRelease-1>', self.end_drag)
        self.canvas.bind('<Double-Button-1>', self.kraken_interaction)
    
    def render_kraken(self):
        """Render the current ASCII kraken sprite"""
        sprite_lines = ASCII_PET_SPRITES.get(self.current_sprite, ASCII_PET_SPRITES['idle1'])
        
        # Get current kraken position or use default
        coords = self.canvas.coords("kraken")
        if coords:
            x, y = coords[0], coords[1]
        else:
            x, y = self.kraken_start_x, self.kraken_start_y
        
        # Render the ASCII art with underwater coloring
        render_ascii_art(sprite_lines, x, y, self.canvas, tag="kraken", color="#FF6B35", font_size=6)
    
    def setup_animations(self):
        """Setup animation sequences"""
        self.animations = ASCII_ANIMATIONS
    
    def start_drag(self, event):
        """Start dragging the kraken"""
        # Check if click is near the kraken
        kraken_coords = self.canvas.coords("kraken")
        if kraken_coords:
            kraken_x, kraken_y = kraken_coords[0], kraken_coords[1]
            distance = ((event.x - kraken_x)**2 + (event.y - kraken_y)**2)**0.5
            
            if distance <= self.kraken_radius + 15:  # Allow some margin for clicking
                self.is_dragging = True
                self.drag_start_x = event.x
                self.drag_start_y = event.y
    
    def drag_kraken(self, event):
        """Handle kraken dragging (only in water)"""
        if self.is_dragging:
            # Calculate new kraken position within container
            dx = event.x - self.drag_start_x
            dy = event.y - self.drag_start_y
            
            kraken_coords = self.canvas.coords("kraken")
            if kraken_coords:
                new_x = kraken_coords[0] + dx
                new_y = kraken_coords[1] + dy
                
                # Keep kraken within container bounds and in water
                margin = self.kraken_radius + 10
                new_x = max(margin, min(new_x, self.container_width - margin))
                
                # Only allow movement in water areas
                if is_in_water(new_x, new_y, self.water_level, self.container_height):
                    # Move the kraken by re-rendering at new position
                    if self.move_kraken_to(new_x, new_y):
                        # Update drag start position for smooth dragging
                        self.drag_start_x = event.x
                        self.drag_start_y = event.y
    
    def move_kraken_to(self, x, y):
        """Move kraken to specific coordinates (only in water)"""
        # Ensure the kraken stays in water
        if is_in_water(x, y, self.water_level, self.container_height):
            sprite_lines = ASCII_PET_SPRITES.get(self.current_sprite, ASCII_PET_SPRITES['idle1'])
            render_ascii_art(sprite_lines, x, y, self.canvas, tag="kraken", color="#FF6B35", font_size=6)
            return True
        return False
    
    def end_drag(self, event):
        """End dragging"""
        self.is_dragging = False
    
    def kraken_interaction(self, event):
        """Handle double-click interaction with kraken"""
        # Check if double-click is near the kraken
        kraken_coords = self.canvas.coords("kraken")
        if kraken_coords:
            kraken_x, kraken_y = kraken_coords[0], kraken_coords[1]
            distance = ((event.x - kraken_x)**2 + (event.y - kraken_y)**2)**0.5
            
            if distance <= self.kraken_radius + 20:  # Allow some margin
                self.state = "attack"  # Kraken gets aggressive when poked!
                self.idle_counter = 0
    
    def get_cursor_position(self):
        """Get mouse cursor position"""
        try:
            x = self.root.winfo_pointerx()
            y = self.root.winfo_pointery()
            return x, y
        except:
            return self.target_x, self.target_y
    
    def ensure_desktop_level(self):
        """Ensure the window stays at desktop level (platform-specific)"""
        try:
            if self.os_type == "Darwin":  # macOS
                # Periodically ensure we stay at desktop level
                self.root.call('wm', 'attributes', '.', '-level', 'desktop')
            elif self.os_type == "Windows":  # Windows
                try:
                    import win32gui
                    import win32con
                    hwnd = int(self.root.wm_frame(), 16)
                    win32gui.SetWindowPos(hwnd, win32con.HWND_BOTTOM, 0, 0, 0, 0, 
                                        win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_NOACTIVATE)
                except ImportError:
                    pass
        except:
            pass
    
    def follow_cursor(self):
        """Make kraken follow cursor when idle (only in water)"""
        if self.is_dragging or self.state != "idle":
            return
            
        # Get cursor position relative to container
        try:
            cursor_screen_x, cursor_screen_y = self.get_cursor_position()
            # Convert to container-relative coordinates
            cursor_x = cursor_screen_x - self.container_x
            cursor_y = cursor_screen_y - self.container_y
            
            # Only follow if cursor is within or near the container and in water
            if (-50 <= cursor_x <= self.container_width + 50 and 
                is_in_water(cursor_x, cursor_y, self.water_level, self.container_height)):
                
                kraken_coords = self.canvas.coords("kraken")
                if kraken_coords:
                    kraken_x, kraken_y = kraken_coords[0], kraken_coords[1]
                    
                    # Calculate distance to cursor
                    distance = math.sqrt((cursor_x - kraken_x)**2 + (cursor_y - kraken_y)**2)
                    
                    # Follow if cursor is close but not too close
                    if 40 < distance < 150:
                        # Set target within water bounds
                        margin = self.kraken_radius + 15
                        target_x = max(margin, min(cursor_x, self.container_width - margin))
                        if is_in_water(target_x, cursor_y, self.water_level, self.container_height):
                            self.target_x = target_x
                            self.target_y = cursor_y
                            self.state = "swimming"
        except:
            pass
    
    def update_position(self):
        """Smoothly move kraken towards target (only in water)"""
        if self.state == "swimming" and not self.is_dragging:
            kraken_coords = self.canvas.coords("kraken")
            if kraken_coords:
                current_kraken_x, current_kraken_y = kraken_coords[0], kraken_coords[1]
                
                # Move towards target
                dx = self.target_x - current_kraken_x
                dy = self.target_y - current_kraken_y
                distance = math.sqrt(dx**2 + dy**2)
                
                if distance > 5:
                    # Move step by step
                    step_size = min(2.5, distance / 8)  # Kraken swims faster
                    new_x = current_kraken_x + (dx / distance) * step_size
                    new_y = current_kraken_y + (dy / distance) * step_size
                    
                    # Keep within water bounds
                    margin = self.kraken_radius + 10
                    new_x = max(margin, min(new_x, self.container_width - margin))
                    
                    # Only move if destination is in water
                    if is_in_water(new_x, new_y, self.water_level, self.container_height):
                        self.move_kraken_to(new_x, new_y)
                    else:
                        self.state = "idle"  # Stop if hit water boundary
                else:
                    self.state = "idle"
    
    def update_behavior(self):
        """Update kraken behavior and state"""
        self.idle_counter += 1
        self.bubble_timer += 1
        
        # Ensure we stay at desktop level every few cycles
        if self.idle_counter % 50 == 0:  # Every 5 seconds
            self.ensure_desktop_level()
        
        # Add floating bubbles periodically
        if self.bubble_timer % 30 == 0:  # Every 3 seconds
            add_floating_bubbles(self.canvas, self.container_width, self.water_level, self.container_height)
        
        # Random behavior changes
        if self.idle_counter > 80:  # About 8 seconds
            if self.state == "idle":
                # Occasionally do something random
                rand = random.random()
                if rand < 0.15:
                    self.state = random.choice(["sleep", "attack"])
                elif rand < 0.35:  # Random swimming
                    self.swim_randomly()
            elif self.state in ["sleep", "attack"]:
                # Return to idle after a while
                if random.random() < 0.2:
                    self.state = "idle"
            self.idle_counter = 0
            
        # Follow cursor behavior
        self.follow_cursor()
        
        # Update position
        self.update_position()
        
        # Schedule next behavior update
        self.root.after(100, self.update_behavior)
    
    def swim_randomly(self):
        """Make kraken swim to a random spot in the water"""
        if not self.is_dragging:
            margin = self.kraken_radius + 25
            attempts = 0
            while attempts < 10:  # Try to find a valid water position
                target_x = random.randint(margin, self.container_width - margin)
                target_y = random.randint(self.water_level + 30, self.container_height - 40)
                if is_in_water(target_x, target_y, self.water_level, self.container_height):
                    self.target_x = target_x
                    self.target_y = target_y
                    self.state = "swimming"
                    break
                attempts += 1
    
    def animate(self):
        """Animate the kraken sprite"""
        # Get current animation sequence
        current_animation = self.animations.get(self.state, self.animations['idle'])
        
        # Update animation frame
        sprite_name = current_animation[self.animation_frame % len(current_animation)]
        self.current_sprite = sprite_name
        
        # Render the updated sprite
        self.render_kraken()
        
        # Add a subtle sway effect when swimming
        if self.state == "swimming" and self.animation_frame % 6 < 3:
            # Slight horizontal sway for swimming motion
            kraken_coords = self.canvas.coords("kraken")
            if kraken_coords and len(kraken_coords) >= 2:
                sway_offset = 2 if self.animation_frame % 6 == 0 else -2
                current_x, current_y = kraken_coords[0], kraken_coords[1]
                if is_in_water(current_x + sway_offset, current_y, self.water_level, self.container_height):
                    self.move_kraken_to(current_x + sway_offset, current_y)
        
        # Advance animation frame
        self.animation_frame += 1
        
        # Schedule next frame (different speeds for different states)
        if self.state == "sleep":
            delay = 1200
        elif self.state == "attack":
            delay = 300  # Fast aggressive animation
        else:
            delay = 500
        self.root.after(delay, self.animate)
    
    def run(self):
        """Start the kraken application"""
        print("Starting ASCII Underwater Kraken...")
        print("• Lives in underwater environment in desktop corner")
        print("• Click and drag to move within water areas only") 
        print("• Double-click to make it attack (aggressive!)")
        print("• Follows your cursor when nearby (in water)")
        print("• Swims randomly through the underwater world")
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
        kraken = ASCIIUnderwaterKraken()
        kraken.run()
    except Exception as e:
        print(f"Error starting ASCII kraken: {e}")
        print("Make sure you have a display available (not in headless mode)")
        sys.exit(1)