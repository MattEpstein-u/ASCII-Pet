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
        
        # Set container dimensions first (800x800 underwater world)
        self.container_width = 800
        self.container_height = 800
        
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
        
        # Mouse tracking
        self.mouse_in_window = False
        self.last_cursor_x = 0
        self.last_cursor_y = 0
        
        # Status display
        self.create_status_display()
        
        # Start animation loops
        self.update_animation()
        
    def setup_test_window(self):
        """Configure the test window"""
        self.root.title("ASCII Underwater Kraken Test - Interactive Mode")
        self.root.geometry("850x900+100+100")  # 800x800 world plus controls
        self.root.configure(bg='#2C3E50')  # Neutral background
        
        # Add control panel at top
        control_frame = tk.Frame(self.root, bg='#1E3A5F', height=60)
        control_frame.pack(fill='x', padx=5, pady=5)
        control_frame.pack_propagate(False)
        
        # Control buttons
        tk.Label(control_frame, text="🐙 Kraken Controls:", bg='#1E3A5F', fg='white',
                font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(control_frame, text="😴 Sleep", command=self.trigger_sleep,
                 bg='#87CEEB', font=('Arial', 9)).pack(side='left', padx=2)
        
        tk.Button(control_frame, text="⚡ Attack", command=self.trigger_attack,
                 bg='#FF6B35', font=('Arial', 9)).pack(side='left', padx=2)
        
        tk.Button(control_frame, text="🌊 Swim", command=self.trigger_swim,
                 bg='#4A90E2', font=('Arial', 9)).pack(side='left', padx=2)
        
        tk.Button(control_frame, text="🎯 Random Swim", command=self.random_target,
                 bg='#2D5016', font=('Arial', 9)).pack(side='left', padx=2)
    
    def setup_kraken(self):
        """Create the underwater kraken display"""
        # Create canvas for the ocean cross-section
        self.canvas = tk.Canvas(self.root, width=self.container_width, 
                               height=self.container_height, 
                               bg='#ECF0F1', highlightthickness=1,
                               highlightcolor='#34495E')
        self.canvas.pack(padx=5, pady=5)
        
        # Render the underwater environment
        self.water_level = render_underwater_environment(self.canvas, self.container_width, self.container_height)
        
        # Add environment info
        self.canvas.create_text(20, 20, 
                              text=f'🌊 Ocean Cross-Section {self.container_width}x{self.container_height}',
                              font=('Arial', 8), anchor='nw', fill='#34495E')
        
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
        
        # Mouse events for interaction
        self.canvas.tag_bind("kraken", "<Button-1>", self.on_kraken_click)
        self.canvas.tag_bind("kraken", "<Double-Button-1>", self.on_kraken_double_click)
        self.canvas.tag_bind("kraken", "<ButtonPress-1>", self.start_drag)
        self.canvas.tag_bind("kraken", "<B1-Motion>", self.do_drag)
        self.canvas.tag_bind("kraken", "<ButtonRelease-1>", self.end_drag)
        
        # Track mouse for following behavior
        self.canvas.bind("<Motion>", self.track_mouse)
        self.canvas.bind("<Enter>", self.mouse_enter)
        self.canvas.bind("<Leave>", self.mouse_leave)
    
    def create_status_display(self):
        """Create status information display"""
        status_frame = tk.Frame(self.root, bg='#1E3A5F', height=40)
        status_frame.pack(fill='x', padx=5, pady=(0, 5))
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(status_frame, text=f"State: {self.state}", 
                                   bg='#1E3A5F', fg='white', font=('Arial', 9))
        self.status_label.pack(side='left', padx=10, pady=8)
        
        coords_text = f"Position: ({int(self.current_x)}, {int(self.current_y)})"
        self.coords_label = tk.Label(status_frame, text=coords_text, 
                                   bg='#1E3A5F', fg='#87CEEB', font=('Arial', 9))
        self.coords_label.pack(side='left', padx=10, pady=8)
    
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
            self.current_x = x
            self.current_y = y
            # Update status display
            self.coords_label.config(text=f"Position: ({int(x)}, {int(y)})")
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
        print("🌊 Kraken is swimming!")

    def random_target(self):
        """Set a random target location in water"""
        # Keep trying until we find a water location
        max_attempts = 20
        for _ in range(max_attempts):
            padding = self.kraken_radius
            test_x = random.randint(padding, self.container_width - padding)
            test_y = random.randint(self.water_level + padding, self.container_height - padding)
            
            if is_in_water(test_x, test_y, self.water_level, self.container_height):
                self.target_x = test_x
                self.target_y = test_y
                self.state = "swimming"
                self.animation_frame = 0
                self.idle_counter = 0
                print(f"🌊 Kraken swimming to ({self.target_x}, {self.target_y})")
                return
        
        print("Could not find valid water location for kraken")

    def update_animation(self):
        """Update kraken animation based on current state"""
        # Handle different states
        if self.state == "idle":
            self.handle_idle_state()
        elif self.state == "swimming":
            self.handle_swimming_state()
        elif self.state == "sleeping":
            self.handle_sleeping_state()
        elif self.state == "attack":
            self.handle_attack_state()
        
        # Update animation frame
        self.animation_frame += 1
        if self.animation_frame >= 20:  # Reset every 20 frames
            self.animation_frame = 0
        
        # Add floating bubbles much more frequently
        self.bubble_timer += 1
        if self.bubble_timer >= 5:  # Every 1 second - much more frequent bubbles
            add_floating_bubbles(self.canvas, self.container_width, self.water_level, self.container_height)
            self.bubble_timer = 0
        
        # Update status display
        self.status_label.config(text=f"State: {self.state}")
        
        # Continue animation
        self.root.after(200, self.update_animation)

    def handle_idle_state(self):
        """Handle kraken idle behavior"""
        self.idle_counter += 1
        
        # Idle animation - gentle tentacle movement
        if self.animation_frame < 10:
            self.current_sprite = 'idle1'
        else:
            self.current_sprite = 'idle2'
        
        self.move_kraken_to(int(self.current_x), int(self.current_y))
        
        # Occasionally swim to a random spot when idle too long
        if self.idle_counter > 50:  # After 10 seconds of idle
            if random.random() < 0.3:  # 30% chance
                self.random_target()
            else:
                self.idle_counter = 0  # Reset counter
    
    def handle_swimming_state(self):
        """Handle kraken swimming behavior"""
        # Move towards target
        dx = self.target_x - self.current_x
        dy = self.target_y - self.current_y
        distance = math.sqrt(dx*dx + dy*dy)
        
        if distance > 5:  # Still moving
            # Move step by step - much faster swimming
            step_size = 8  # Much faster underwater movement
            if distance > 0:
                new_x = self.current_x + (dx / distance) * step_size
                new_y = self.current_y + (dy / distance) * step_size
                
                # Only move if the new position is in water
                if is_in_water(new_x, new_y, self.water_level, self.container_height):
                    self.current_x = new_x
                    self.current_y = new_y
                else:
                    # Hit boundary, stop swimming
                    self.state = "idle"
                    self.animation_frame = 0
                    return
            
            # Use swimming animation
            if self.animation_frame < 10:
                self.current_sprite = 'swim1'
            else:
                self.current_sprite = 'swim2'
            
            self.move_kraken_to(int(self.current_x), int(self.current_y))
        else:
            # Reached target, go back to idle
            self.state = "idle"
            self.animation_frame = 0
            self.idle_counter = 0
            print("🌊 Kraken reached destination")
    
    def handle_sleeping_state(self):
        """Handle kraken sleeping behavior"""
        # Sleeping animation (slower, resting on ocean floor)
        if self.animation_frame < 15:
            self.current_sprite = 'sleep1'
        else:
            self.current_sprite = 'sleep2'
        
        self.move_kraken_to(int(self.current_x), int(self.current_y))
        
        # Wake up after a while
        if self.animation_frame >= 19 and random.random() < 0.1:  # 10% chance to wake up
            self.state = "idle"
            self.animation_frame = 0
            self.idle_counter = 0
            print("🐙 Kraken awakened from the depths!")

    def handle_attack_state(self):
        """Handle kraken attack behavior"""
        # Attack behavior - tentacle thrashing
        if self.animation_frame < 3:
            self.current_sprite = 'attack1'
        elif self.animation_frame < 6:
            self.current_sprite = 'attack2'
        elif self.animation_frame < 9:
            self.current_sprite = 'attack3'
        elif self.animation_frame < 12:
            self.current_sprite = 'attack2'
        else:
            self.current_sprite = 'attack1'
        
        # Add some aggressive movement during attack
        if self.animation_frame % 3 == 0:
            offset_x = random.randint(-8, 8)
            offset_y = random.randint(-5, 5)
            new_x = max(self.kraken_radius, min(self.container_width - self.kraken_radius, 
                                              self.current_x + offset_x))
            new_y = max(self.water_level + self.kraken_radius, 
                       min(self.container_height - self.kraken_radius, self.current_y + offset_y))
            
            # Only move if still in water
            if is_in_water(new_x, new_y, self.water_level, self.container_height):
                self.current_x = new_x
                self.current_y = new_y
        
        self.move_kraken_to(int(self.current_x), int(self.current_y))
        
        # Stop attacking after a while
        if self.animation_frame >= 19:
            self.state = "idle"
            self.animation_frame = 0
            self.idle_counter = 0
            print("⚡ Kraken finished attacking")
    
    def on_kraken_click(self, event):
        """Handle clicks on the kraken"""
        self.trigger_swim()
    
    def on_kraken_double_click(self, event):
        """Handle double clicks on the kraken"""
        self.trigger_attack()

    def start_drag(self, event):
        """Start dragging the kraken"""
        self.is_dragging = True
        self.drag_start_x = event.x
        self.drag_start_y = event.y
        print("🐙 Started dragging kraken")
    
    def do_drag(self, event):
        """Handle kraken dragging"""
        if self.is_dragging:
            # Calculate new position
            new_x = self.current_x + (event.x - self.drag_start_x)
            new_y = self.current_y + (event.y - self.drag_start_y)
            
            # Only allow dragging within water areas
            if is_in_water(new_x, new_y, self.water_level, self.container_height):
                # Keep within bounds
                new_x = max(self.kraken_radius, min(self.container_width - self.kraken_radius, new_x))
                new_y = max(self.water_level + self.kraken_radius, 
                           min(self.container_height - self.kraken_radius, new_y))
                
                # Update position
                self.current_x = new_x
                self.current_y = new_y
                self.target_x = new_x
                self.target_y = new_y
                
                # Use swimming sprite while dragging
                self.current_sprite = 'swim1'
                self.move_kraken_to(int(self.current_x), int(self.current_y))
                
                # Update drag start for next movement
                self.drag_start_x = event.x
                self.drag_start_y = event.y
    
    def end_drag(self, event):
        """End kraken dragging"""
        if self.is_dragging:
            self.is_dragging = False
            self.state = "idle"
            self.animation_frame = 0
            self.idle_counter = 0
            print(f"🐙 Kraken released at ({int(self.current_x)}, {int(self.current_y)})")
    
    def run(self):
        """Start the test application"""
        print("🎮 ASCII Underwater Kraken Test Mode")
        print("• Window will open with interactive ASCII kraken")
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