#!/usr/bin/env python3
"""
Interactive ASCII Underwater Kraken Test - Play with the kraken in a regular window!
This allows you to test all kraken behaviors without desktop-level positioning.
"""

import tkinter as tk
import random
import math
import platform
import sys
from ascii_pet_designs import (ASCII_PET_SPRITES, ASCII_ANIMATIONS, render_ascii_art,
                              render_underwater_environment, is_in_water, add_floating_bubbles)

class TestASCIIUnderwaterKraken:
    def __init__(self):
        self.root = tk.Tk()
        
        # Set container dimensions first (larger for underwater environment)
        self.container_width = 800
        self.container_height = 600
        
        self.setup_test_window()
        self.setup_kraken()
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
        self.kraken_width = 60
        self.kraken_height = 50
        self.kraken_radius = 30
        self.water_level = 0  # Will be set when environment is rendered
        
        # Bubble effects
        self.bubble_timer = 0
        
        # Test mode variables
        self.mouse_in_window = False
        self.last_cursor_x = 0
        self.last_cursor_y = 0
        
        # Start the main loops
        self.animate()
        self.update_behavior()
    
    def setup_test_window(self):
        """Configure the test window"""
        self.root.title("ASCII Underwater Kraken Test - Interactive Mode")
        self.root.geometry("850x700+100+100")  # Larger for underwater environment
        self.root.configure(bg='#0F1419')  # Dark ocean background
        
        # Add control panel at top
        control_frame = tk.Frame(self.root, bg='#1E3A5F', height=60)
        control_frame.pack(fill='x', padx=5, pady=5)
        control_frame.pack_propagate(False)
        
        # Control buttons
        tk.Label(control_frame, text="🐙 Kraken Controls:", bg='#1E3A5F', fg='white',
                font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(control_frame, text="� Sleep", command=self.trigger_sleep,
                 bg='#87CEEB', font=('Arial', 9)).pack(side='left', padx=2)
        
        tk.Button(control_frame, text="⚡ Attack", command=self.trigger_attack,
                 bg='#FF6B35', font=('Arial', 9)).pack(side='left', padx=2)
        
        tk.Button(control_frame, text="🌊 Swim", command=self.trigger_swim,
                 bg='#4A90E2', font=('Arial', 9)).pack(side='left', padx=2)
        
        tk.Button(control_frame, text="🎯 Random Swim", command=self.random_target,
                 bg='#2D5016', font=('Arial', 9)).pack(side='left', padx=2)
        
        # Status label
        self.status_label = tk.Label(control_frame, text="State: idle", 
                                   bg='#e0e0e0', font=('Arial', 9))
        self.status_label.pack(side='right', padx=5)
    
    def setup_kraken(self):
        """Create the underwater kraken display"""
        # Create canvas for the underwater area
        self.canvas = tk.Canvas(self.root, width=self.container_width, 
                               height=self.container_height, 
                               bg='#0F1419', highlightthickness=1,
                               highlightcolor='#4A90E2')
        self.canvas.pack(padx=5, pady=5)
        
        # Render the underwater environment
        self.water_level = render_underwater_environment(self.canvas, self.container_width, self.container_height)
        
        # Add environment info
        self.canvas.create_text(20, 20, 
                              text=f'🌊 Underwater World {self.container_width}x{self.container_height}',
                              font=('Arial', 8), anchor='nw', fill='#87CEEB')
        
        # Store kraken starting position (in underwater area)
        self.kraken_start_x = self.container_width // 2
        self.kraken_start_y = self.water_level + 100
        
        # Ensure starting position is in water
        if not is_in_water(self.kraken_start_x, self.kraken_start_y, self.water_level, self.container_height):
            self.kraken_start_y = self.water_level + 50
        
        # Create the initial ASCII kraken art
        self.current_sprite = 'idle1'
        self.render_kraken()
        
        # Add initial bubbles
        add_floating_bubbles(self.canvas, self.container_width, self.water_level, self.container_height)
        
        # Bind mouse events
        self.canvas.bind('<Button-1>', self.start_drag)
        self.canvas.bind('<B1-Motion>', self.drag_pet)
        self.canvas.bind('<ButtonRelease-1>', self.end_drag)
        self.canvas.bind('<Double-Button-1>', self.pet_interaction)
        
        # Track mouse movement for following behavior
        self.canvas.bind('<Motion>', self.track_mouse)
        self.canvas.bind('<Enter>', self.mouse_enter)
        self.canvas.bind('<Leave>', self.mouse_leave)
        
        # Add instructions
        instructions = """
🎮 How to interact with your ASCII pet:
• Click and drag the pet around the container
• Double-click the pet to make it play and get excited
• Move mouse near pet to make it follow your cursor
• Use buttons above for direct state control
• Pet will wander randomly when idle and bored
• ASCII art changes based on pet's current mood and activity
        """
        
        instruction_label = tk.Label(self.root, text=instructions, 
                                   justify='left', bg='#f0f0f0', 
                                   font=('Arial', 9), fg='#666')
        instruction_label.pack(pady=5)
    
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
    
    def move_kraken_to(self, x, y):
        """Move kraken to specific coordinates (only in water)"""
        if is_in_water(x, y, self.water_level, self.container_height):
            sprite_lines = ASCII_PET_SPRITES.get(self.current_sprite, ASCII_PET_SPRITES['idle1'])
            render_ascii_art(sprite_lines, x, y, self.canvas, tag="kraken", color="#FF6B35", font_size=6)
            return True
        return False
    
    def setup_animations(self):
        """Setup animation sequences"""
        self.animations = ASCII_ANIMATIONS
        
    def track_mouse(self, event):
        """Track mouse movement for following behavior"""
        self.mouse_in_window = True
        self.last_cursor_x = event.x
        self.last_cursor_y = event.y
        
    def mouse_enter(self, event):
        """Mouse entered the canvas"""
        self.mouse_in_window = True
        
    def mouse_leave(self, event):
        """Mouse left the canvas"""
        self.mouse_in_window = False
    
    def start_drag(self, event):
        """Start dragging the pet"""
        pet_coords = self.canvas.coords("pet")
        if pet_coords:
            pet_x, pet_y = pet_coords[0], pet_coords[1]
            distance = ((event.x - pet_x)**2 + (event.y - pet_y)**2)**0.5
            
            if distance <= self.pet_radius + 15:
                self.is_dragging = True
                self.drag_start_x = event.x
                self.drag_start_y = event.y
                self.state = "idle"  # Stop other behaviors while dragging
    
    def drag_pet(self, event):
        """Handle pet dragging"""
        if self.is_dragging:
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
                
                # Move the pet
                self.move_pet_to(new_x, new_y)
                
                # Update drag start position for smooth dragging
                self.drag_start_x = event.x
                self.drag_start_y = event.y
                
    def end_drag(self, event):
        """End dragging"""
        self.is_dragging = False
    
    def pet_interaction(self, event):
        """Handle double-click interaction"""
        pet_coords = self.canvas.coords("pet")
        if pet_coords:
            pet_x, pet_y = pet_coords[0], pet_coords[1]
            distance = ((event.x - pet_x)**2 + (event.y - pet_y)**2)**0.5
            
            if distance <= self.pet_radius + 20:
                self.trigger_play()
                
    def trigger_attack(self):
        """Trigger attack behavior"""
        self.state = "attack"
        self.animation_frame = 0
        self.idle_counter = 0
        print("⚡ Kraken is attacking!")
    
    def trigger_sleep(self):
        """Trigger sleep behavior"""
        self.state = "sleeping"
        self.animation_frame = 0
        self.idle_counter = 0
        print("😴 Kraken is resting on the ocean floor...")
    
    def trigger_swim(self):
        """Trigger swimming behavior"""
        self.state = "swimming"
        self.animation_frame = 0
        self.idle_counter = 0
        print("🌊 Kraken is swimming!")    def random_target(self):
        """Set random target within container"""
        margin = self.pet_radius + 25
        self.target_x = random.randint(margin, self.container_width - margin)
        self.target_y = random.randint(margin, self.container_height - margin)
        self.state = "walking"
        
    def set_target(self, x, y):
        """Set specific target coordinates"""
        margin = self.pet_radius + 15
        self.target_x = max(margin, min(x, self.container_width - margin))
        self.target_y = max(margin, min(y, self.container_height - margin))
        self.state = "walking"
    
    def follow_cursor(self):
        """Make pet follow cursor when idle"""
        if (self.is_dragging or self.state not in ["idle", "walking"] or 
            not self.mouse_in_window):
            return
            
        pet_coords = self.canvas.coords("pet")
        if pet_coords:
            pet_x, pet_y = pet_coords[0], pet_coords[1]
            cursor_x, cursor_y = self.last_cursor_x, self.last_cursor_y
            
            # Calculate distance to cursor
            distance = math.sqrt((cursor_x - pet_x)**2 + (cursor_y - pet_y)**2)
            
            # Follow if cursor is close but not too close
            if 40 < distance < 120:
                self.set_target(cursor_x, cursor_y)
    
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
                    step_size = min(2.5, distance / 6)
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
    
    def wander_randomly(self):
        """Make pet wander to a random spot in the container"""
        if not self.is_dragging:
            self.random_target()
    
    def update_behavior(self):
        """Update pet behavior and state"""
        self.idle_counter += 1
        
        # Update status
        self.status_label.config(text=f"State: {self.state}")
        
        # Random behavior changes
        if self.idle_counter > 80:  # About 8 seconds in test mode
            if self.state == "idle":
                rand = random.random()
                if rand < 0.15:
                    self.state = random.choice(["sleep", "play"])
                elif rand < 0.3:  # Random wandering
                    self.wander_randomly()
            elif self.state in ["sleep", "play"]:
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
            pet_coords = self.canvas.coords("pet")
            if pet_coords and len(pet_coords) >= 2:
                bounce_offset = 2 if self.animation_frame % 4 == 0 else -2
                current_x, current_y = pet_coords[0], pet_coords[1]
                self.move_pet_to(current_x, current_y + bounce_offset)
        
        # Advance animation frame
        self.animation_frame += 1
        
        # Schedule next frame (slower for sleep)
        delay = 1200 if self.state == "sleep" else 500
        self.root.after(delay, self.animate)
    
    def run(self):
        """Start the test application"""
        print("🎮 ASCII Desktop Pet Test Mode")
        print("• Window will open with interactive ASCII pet")
        print("• Try all the controls and interactions")
        print("• Close window when done testing")
        print()
        
        # Center window on screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
        # Start the main loop
        self.root.mainloop()

if __name__ == "__main__":
    print("Starting ASCII Underwater Kraken Interactive Test...")
    print("Controls:")
    print("  ⚡ Attack - Make kraken attack")
    print("  😴 Sleep - Make kraken rest on ocean floor")
    print("  🌊 Swim - Make kraken swim around")
    print("  🎯 Random Swim - Send kraken to random water location")
    print("  🔄 Drag - Click and drag the kraken (water areas only)")
    print("  👁️ Double-click - Make kraken attack")
    print()
    
    try:
        kraken = TestASCIIUnderwaterKraken()
        kraken.run()
    except KeyboardInterrupt:
        print("\n👋 Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()