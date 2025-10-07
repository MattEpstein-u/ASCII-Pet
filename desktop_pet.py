#!/usr/bin/env python3
"""
ASCII Desktop Pet - Cross-platform Desktop Companion
A cute ASCII art pet that sits on your desktop background and provides companionship.
Only visible when all applications are minimized to desktop.

Based on the Mac-pet repository but using ASCII art instead of emoji sprites.
"""

import tkinter as tk
import random
import math
import platform
import sys
from ascii_pet_designs import ASCII_PET_SPRITES, ASCII_ANIMATIONS, render_ascii_art

class ASCIIDesktopPet:
    def __init__(self):
        self.root = tk.Tk()
        self.calculate_container_size()
        self.setup_window()
        self.setup_pet()
        self.setup_animations()
        
        # Pet state
        self.target_x = self.container_width // 2
        self.target_y = self.container_height // 2
        self.current_x = self.container_width // 2
        self.current_y = self.container_height // 2
        self.is_dragging = False
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.animation_frame = 0
        self.idle_counter = 0
        self.state = "idle"  # idle, walking, sleeping, playing
        
        # ASCII pet properties
        self.pet_width = 80  # Approximate width of ASCII art
        self.pet_height = 40  # Approximate height of ASCII art
        self.pet_radius = 40  # For collision detection
        
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
        
        # Constrain to reasonable limits (minimum 300x300 for ASCII art, maximum 700x500)
        self.container_width = max(300, min(container_side, 700))
        self.container_height = max(300, min(container_side, 500))
        
        # Position container in bottom-right corner with some margin
        margin = 50
        self.container_x = screen_width - self.container_width - margin
        self.container_y = screen_height - self.container_height - margin
        
        print(f"Screen: {screen_width}x{screen_height}")
        print(f"Container: {self.container_width}x{self.container_height} at ({self.container_x}, {self.container_y})")
    
    def setup_window(self):
        """Configure the main window"""
        self.root.title("ASCII Desktop Pet")
        
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
        """Create the pet display"""
        # Create canvas that fills the container
        self.canvas = tk.Canvas(self.root, width=self.container_width, height=self.container_height, 
                               bg='#f5f5f5', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        
        # Add a subtle container background with rounded corners effect
        self.canvas.create_rectangle(5, 5, self.container_width-5, self.container_height-5,
                                   fill='#fafafa', outline='#e5e5e5', width=1)
        
        # Add a small label in the corner to indicate this is the pet's home
        self.canvas.create_text(self.container_width-15, 15, text='🏠', 
                              font=('Arial', 10), anchor='ne', fill='#c0c0c0')
        
        # Store pet starting position (center of container)
        self.pet_start_x = self.container_width // 2
        self.pet_start_y = self.container_height // 2
        
        # Create the initial ASCII pet art
        self.current_sprite = 'idle1'
        self.render_pet()
        
        # Bind mouse events to the entire canvas
        self.canvas.bind('<Button-1>', self.start_drag)
        self.canvas.bind('<B1-Motion>', self.drag_pet)
        self.canvas.bind('<ButtonRelease-1>', self.end_drag)
        self.canvas.bind('<Double-Button-1>', self.pet_interaction)
    
    def render_pet(self):
        """Render the current ASCII pet sprite"""
        sprite_lines = ASCII_PET_SPRITES.get(self.current_sprite, ASCII_PET_SPRITES['idle1'])
        
        # Get current pet position or use default
        coords = self.canvas.coords("pet")
        if coords:
            x, y = coords[0], coords[1]
        else:
            x, y = self.pet_start_x, self.pet_start_y
        
        # Render the ASCII art
        render_ascii_art(sprite_lines, x, y, self.canvas, tag="pet", color="#2c3e50")
    
    def setup_animations(self):
        """Setup animation sequences"""
        self.animations = ASCII_ANIMATIONS
    
    def start_drag(self, event):
        """Start dragging the pet"""
        # Check if click is near the pet
        pet_coords = self.canvas.coords("pet")
        if pet_coords:
            pet_x, pet_y = pet_coords[0], pet_coords[1]
            distance = ((event.x - pet_x)**2 + (event.y - pet_y)**2)**0.5
            
            if distance <= self.pet_radius + 15:  # Allow some margin for clicking
                self.is_dragging = True
                self.drag_start_x = event.x
                self.drag_start_y = event.y
    
    def drag_pet(self, event):
        """Handle pet dragging"""
        if self.is_dragging:
            # Calculate new pet position within container
            dx = event.x - self.drag_start_x
            dy = event.y - self.drag_start_y
            
            pet_coords = self.canvas.coords("pet")
            if pet_coords:
                new_x = pet_coords[0] + dx
                new_y = pet_coords[1] + dy
                
                # Keep pet within container bounds
                margin = self.pet_radius + 10
                new_x = max(margin, min(new_x, self.container_width - margin))
                new_y = max(margin, min(new_y, self.container_height - margin))
                
                # Move the pet by re-rendering at new position
                self.move_pet_to(new_x, new_y)
                
                # Update drag start position for smooth dragging
                self.drag_start_x = event.x
                self.drag_start_y = event.y
    
    def move_pet_to(self, x, y):
        """Move pet to specific coordinates"""
        sprite_lines = ASCII_PET_SPRITES.get(self.current_sprite, ASCII_PET_SPRITES['idle1'])
        render_ascii_art(sprite_lines, x, y, self.canvas, tag="pet", color="#2c3e50")
    
    def end_drag(self, event):
        """End dragging"""
        self.is_dragging = False
    
    def pet_interaction(self, event):
        """Handle double-click interaction"""
        # Check if double-click is near the pet
        pet_coords = self.canvas.coords("pet")
        if pet_coords:
            pet_x, pet_y = pet_coords[0], pet_coords[1]
            distance = ((event.x - pet_x)**2 + (event.y - pet_y)**2)**0.5
            
            if distance <= self.pet_radius + 20:  # Allow some margin
                self.state = "play"
                self.idle_counter = 0
    
    def get_cursor_position(self):
        """Get mouse cursor position"""
        try:
            x = self.root.winfo_pointerx()
            y = self.root.winfo_pointery()
            return x, y
        except:
            return self.current_x, self.current_y
    
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
        """Make pet follow cursor when idle"""
        if self.is_dragging or self.state != "idle":
            return
            
        # Get cursor position relative to container
        try:
            cursor_screen_x, cursor_screen_y = self.get_cursor_position()
            # Convert to container-relative coordinates
            cursor_x = cursor_screen_x - self.container_x
            cursor_y = cursor_screen_y - self.container_y
            
            # Only follow if cursor is within or near the container
            if (-50 <= cursor_x <= self.container_width + 50 and 
                -50 <= cursor_y <= self.container_height + 50):
                
                pet_coords = self.canvas.coords("pet")
                if pet_coords:
                    pet_x, pet_y = pet_coords[0], pet_coords[1]
                    
                    # Calculate distance to cursor
                    distance = math.sqrt((cursor_x - pet_x)**2 + (cursor_y - pet_y)**2)
                    
                    # Follow if cursor is close but not too close
                    if 40 < distance < 150:
                        # Set target within container bounds
                        margin = self.pet_radius + 15
                        self.target_x = max(margin, min(cursor_x, self.container_width - margin))
                        self.target_y = max(margin, min(cursor_y, self.container_height - margin))
                        self.state = "walking"
        except:
            pass
    
    def update_position(self):
        """Smoothly move pet towards target"""
        if self.state == "walking" and not self.is_dragging:
            pet_coords = self.canvas.coords("pet")
            if pet_coords:
                current_pet_x, current_pet_y = pet_coords[0], pet_coords[1]
                
                # Move towards target
                dx = self.target_x - current_pet_x
                dy = self.target_y - current_pet_y
                distance = math.sqrt(dx**2 + dy**2)
                
                if distance > 5:
                    # Move step by step
                    step_size = min(2.0, distance / 8)
                    new_x = current_pet_x + (dx / distance) * step_size
                    new_y = current_pet_y + (dy / distance) * step_size
                    
                    # Keep within container bounds
                    margin = self.pet_radius + 10
                    new_x = max(margin, min(new_x, self.container_width - margin))
                    new_y = max(margin, min(new_y, self.container_height - margin))
                    
                    # Move the pet
                    self.move_pet_to(new_x, new_y)
                else:
                    self.state = "idle"
    
    def update_behavior(self):
        """Update pet behavior and state"""
        self.idle_counter += 1
        
        # Ensure we stay at desktop level every few cycles
        if self.idle_counter % 50 == 0:  # Every 5 seconds
            self.ensure_desktop_level()
        
        # Random behavior changes
        if self.idle_counter > 100:  # About 10 seconds
            if self.state == "idle":
                # Occasionally do something random
                rand = random.random()
                if rand < 0.2:
                    self.state = random.choice(["sleep", "play"])
                elif rand < 0.4:  # Random wandering
                    self.wander_randomly()
            elif self.state in ["sleep", "play"]:
                # Return to idle after a while
                if random.random() < 0.1:
                    self.state = "idle"
            self.idle_counter = 0
            
        # Follow cursor behavior
        self.follow_cursor()
        
        # Update position
        self.update_position()
        
        # Schedule next behavior update
        self.root.after(100, self.update_behavior)
    
    def wander_randomly(self):
        """Make pet wander to a random spot in the container"""
        if not self.is_dragging:
            margin = self.pet_radius + 25
            self.target_x = random.randint(margin, self.container_width - margin)
            self.target_y = random.randint(margin, self.container_height - margin)
            self.state = "walking"
    
    def animate(self):
        """Animate the pet sprite"""
        # Get current animation sequence
        current_animation = self.animations.get(self.state, self.animations['idle'])
        
        # Update animation frame
        sprite_name = current_animation[self.animation_frame % len(current_animation)]
        self.current_sprite = sprite_name
        
        # Render the updated sprite
        self.render_pet()
        
        # Add a subtle bounce effect when walking
        if self.state == "walking" and self.animation_frame % 4 < 2:
            # Slight vertical offset for bounce
            pet_coords = self.canvas.coords("pet")
            if pet_coords and len(pet_coords) >= 2:
                bounce_offset = 3 if self.animation_frame % 4 == 0 else -3
                current_x, current_y = pet_coords[0], pet_coords[1]
                self.move_pet_to(current_x, current_y + bounce_offset)
        
        # Advance animation frame
        self.animation_frame += 1
        
        # Schedule next frame (slower for sleep)
        delay = 1000 if self.state == "sleep" else 600
        self.root.after(delay, self.animate)
    
    def run(self):
        """Start the pet application"""
        print("Starting ASCII Desktop Pet...")
        print("• Lives in desktop corner container")
        print("• Click and drag to move within container") 
        print("• Double-click to make it play")
        print("• Follows your cursor when nearby")
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
        pet = ASCIIDesktopPet()
        pet.run()
    except Exception as e:
        print(f"Error starting ASCII pet: {e}")
        print("Make sure you have a display available (not in headless mode)")
        sys.exit(1)