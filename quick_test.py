#!/usr/bin/env python3
"""
Quick Test - Interactive ASCII Underwater Kraken
The one and only test script you need! Test everything in one place.
"""

import tkinter as tk
import random
import math
import sys
from ascii_pet_designs import (ASCII_PET_SPRITES, ASCII_ANIMATIONS, render_ascii_art,
                              render_underwater_environment, is_in_water, add_floating_bubbles)

class QuickTest:
    def __init__(self):
        self.root = tk.Tk()
        
        # Container dimensions for testing (800x800 for visibility)
        self.container_width = 800
        self.container_height = 800
        
        self.setup_window()
        self.setup_canvas()
        self.setup_controls()
        self.setup_status()
        self.init_kraken_state()
        
        # Start animation and behavior loops
        self.animate()
        self.update_behavior()
    
    def setup_window(self):
        """Setup test window"""
        self.root.title("🐙 ASCII Kraken Quick Test - Feed & Play!")
        self.root.configure(bg='#0A0F1C')
        self.root.geometry(f"{self.container_width}x{self.container_height + 100}")
    
    def setup_canvas(self):
        """Setup underwater canvas"""
        self.canvas = tk.Canvas(self.root, width=self.container_width, height=self.container_height,
                               bg='#0A0F1C', highlightthickness=1, highlightbackground='#FFFFFF')
        self.canvas.pack()
        
        # Render underwater environment
        self.water_level = render_underwater_environment(self.canvas, self.container_width, self.container_height)
        
        # Bind mouse events
        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.bind('<B1-Motion>', self.on_drag)
        self.canvas.bind('<ButtonRelease-1>', self.on_release)
        self.canvas.bind('<Double-Button-1>', self.on_double_click)
        self.canvas.bind('<Motion>', self.on_mouse_move)
    
    def setup_controls(self):
        """Setup control panel"""
        control_frame = tk.Frame(self.root, bg='#0A0F1C', height=60)
        control_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(control_frame, text="🐙 Controls:", bg='#0A0F1C', fg='white',
                font=('Arial', 11, 'bold')).grid(row=0, column=0, padx=5)
        
        tk.Button(control_frame, text="🏊 Swim Random", command=self.swim_random,
                 bg='#4a90e2', fg='white', font=('Arial', 9)).grid(row=0, column=1, padx=3)
        
        tk.Button(control_frame, text="⚡ Attack", command=lambda: setattr(self, 'state', 'attack'),
                 bg='#e74c3c', fg='white', font=('Arial', 9)).grid(row=0, column=2, padx=3)
        
        tk.Button(control_frame, text="😴 Sleep", command=self.prepare_sleep,
                 bg='#9b59b6', fg='white', font=('Arial', 9)).grid(row=0, column=3, padx=3)
        
        tk.Button(control_frame, text="🦐 Drop Shrimp", command=self.drop_random_shrimp,
                 bg='#FFB6C1', fg='black', font=('Arial', 9, 'bold')).grid(row=0, column=4, padx=3)
        
        tk.Button(control_frame, text="🫧 Bubbles", command=self.add_bubbles,
                 bg='#1abc9c', fg='white', font=('Arial', 9)).grid(row=0, column=5, padx=3)
    
    def setup_status(self):
        """Setup status display"""
        status_frame = tk.Frame(self.root, bg='#0A0F1C', height=40)
        status_frame.pack(fill='x', padx=10, pady=0)
        
        # Status labels
        self.state_label = tk.Label(status_frame, text="State: idle",
                                   bg='#0A0F1C', fg='white', font=('Arial', 9))
        self.state_label.grid(row=0, column=0, padx=10, sticky='w')
        
        self.pos_label = tk.Label(status_frame, text="Position: (400, 400)",
                                 bg='#0A0F1C', fg='#FFB6C1', font=('Arial', 9))
        self.pos_label.grid(row=0, column=1, padx=10, sticky='w')
        
        self.shrimp_label = tk.Label(status_frame, text="Shrimp: 0",
                                    bg='#0A0F1C', fg='#98FB98', font=('Arial', 9))
        self.shrimp_label.grid(row=0, column=2, padx=10, sticky='w')
    
    def init_kraken_state(self):
        """Initialize kraken state variables"""
        # Position
        self.target_x = self.container_width // 2
        self.target_y = (self.container_height * 3) // 5
        self.current_x = self.target_x
        self.current_y = self.target_y
        
        # State
        self.state = "idle"
        self.current_sprite = 'idle1'
        self.animation_frame = 0
        self.idle_counter = 0
        
        # Interaction
        self.is_dragging = False
        self.drag_start_x = 0
        self.drag_start_y = 0
        
        # Properties
        self.kraken_radius = 30
        
        # Shrimp feeding
        self.shrimp_queue = []
        self.current_shrimp_target = None
        self.eating_shrimp = False
        
        # Effects
        self.bubble_timer = 0
        
        # Render initial kraken
        self.render_kraken()
    
    def render_kraken(self):
        """Render kraken at current position"""
        coords = self.canvas.coords("kraken")
        if coords:
            x, y = coords[0], coords[1]
        else:
            x, y = self.current_x, self.current_y
        
        sprite_lines = ASCII_PET_SPRITES.get(self.current_sprite, ASCII_PET_SPRITES['idle1'])
        render_ascii_art(sprite_lines, x, y, self.canvas, tag="kraken", color="#FFB6C1", font_size=12)
        
        # Update status
        self.pos_label.config(text=f"Position: ({int(x)}, {int(y)})")
    
    def move_kraken_to(self, x, y):
        """Move kraken with boundary enforcement"""
        margin = self.kraken_radius + 10
        
        # Clamp to boundaries
        x = max(margin, min(x, self.container_width - margin))
        min_y = self.water_level + margin
        max_y = self.container_height - margin
        y = max(min_y, min(y, max_y))
        
        if is_in_water(x, y, self.water_level, self.container_height):
            sprite_lines = ASCII_PET_SPRITES.get(self.current_sprite, ASCII_PET_SPRITES['idle1'])
            render_ascii_art(sprite_lines, x, y, self.canvas, tag="kraken", color="#FFB6C1", font_size=12)
            self.current_x = x
            self.current_y = y
            self.pos_label.config(text=f"Position: ({int(x)}, {int(y)})")
            return True
        return False
    
    # === Mouse Event Handlers ===
    
    def on_click(self, event):
        """Handle mouse click - drag kraken or drop shrimp"""
        kraken_coords = self.canvas.coords("kraken")
        if kraken_coords:
            kraken_x, kraken_y = kraken_coords[0], kraken_coords[1]
            distance = ((event.x - kraken_x)**2 + (event.y - kraken_y)**2)**0.5
            
            if distance <= self.kraken_radius + 15:
                # Click on kraken - start dragging
                self.is_dragging = True
                self.drag_start_x = event.x
                self.drag_start_y = event.y
            elif is_in_water(event.x, event.y, self.water_level, self.container_height):
                # Click in water - drop shrimp
                self.drop_shrimp(event.x, event.y)
    
    def on_drag(self, event):
        """Handle dragging"""
        if self.is_dragging:
            dx = event.x - self.drag_start_x
            dy = event.y - self.drag_start_y
            
            kraken_coords = self.canvas.coords("kraken")
            if kraken_coords:
                new_x = kraken_coords[0] + dx
                new_y = kraken_coords[1] + dy
                
                if self.move_kraken_to(new_x, new_y):
                    self.drag_start_x = event.x
                    self.drag_start_y = event.y
    
    def on_release(self, event):
        """Handle mouse release"""
        self.is_dragging = False
    
    def on_double_click(self, event):
        """Handle double-click - attack mode"""
        self.state = "attack"
        self.idle_counter = 0
    
    def on_mouse_move(self, event):
        """Track mouse movement for cursor following"""
        self.last_cursor_x = event.x
        self.last_cursor_y = event.y
    
    # === Shrimp Feeding System ===
    
    def drop_shrimp(self, x, y):
        """Drop shrimp at position"""
        if is_in_water(x, y, self.water_level, self.container_height):
            self.shrimp_queue.append((x, y))
            shrimp_tag = f"shrimp_{len(self.shrimp_queue)}"
            self.canvas.create_text(x, y, text=",", font=("Courier", 16, "bold"),
                                   fill="#FFB6C1", tags=shrimp_tag)
            self.shrimp_label.config(text=f"Shrimp: {len(self.shrimp_queue)}")
            print(f"🦐 Shrimp dropped at ({x}, {y})")
    
    def drop_random_shrimp(self):
        """Drop shrimp at random underwater location"""
        margin = 50
        for _ in range(10):  # Try up to 10 times
            x = random.randint(margin, self.container_width - margin)
            y = random.randint(self.water_level + margin, self.container_height - margin)
            if is_in_water(x, y, self.water_level, self.container_height):
                self.drop_shrimp(x, y)
                break
    
    def get_next_shrimp(self):
        """Target next shrimp in queue"""
        if self.shrimp_queue and not self.current_shrimp_target:
            self.current_shrimp_target = self.shrimp_queue[0]
            self.eating_shrimp = True
            print(f"🐙 Targeting shrimp at {self.current_shrimp_target}")
    
    def eat_shrimp(self):
        """Eat current target shrimp"""
        if self.current_shrimp_target:
            idx = self.shrimp_queue.index(self.current_shrimp_target) + 1
            self.canvas.delete(f"shrimp_{idx}")
            self.shrimp_queue.remove(self.current_shrimp_target)
            self.current_shrimp_target = None
            self.eating_shrimp = False
            self.shrimp_label.config(text=f"Shrimp: {len(self.shrimp_queue)}")
            self.state = "attack"
            print(f"🐙 Om nom nom! {len(self.shrimp_queue)} shrimp remaining")
    
    # === Behavior Methods ===
    
    def swim_random(self):
        """Swim to random underwater location"""
        margin = self.kraken_radius + 25
        for _ in range(10):
            x = random.randint(margin, self.container_width - margin)
            y = random.randint(self.water_level + margin, self.container_height - margin)
            if is_in_water(x, y, self.water_level, self.container_height):
                self.target_x = x
                self.target_y = y
                self.state = "swimming"
                break
    
    def prepare_sleep(self):
        """Swim to ocean floor before sleeping"""
        margin = self.kraken_radius + 25
        x = random.randint(margin, self.container_width - margin)
        y = self.container_height - 60
        if is_in_water(x, y, self.water_level, self.container_height):
            self.target_x = x
            self.target_y = y
            self.state = "sleeping_prep"
    
    def add_bubbles(self):
        """Add bubble effects"""
        add_floating_bubbles(self.canvas, self.container_width, self.water_level, self.container_height)
    
    # === Animation & Movement ===
    
    def update_position(self):
        """Update kraken position towards target"""
        # Check for shrimp to eat
        if not self.current_shrimp_target and len(self.shrimp_queue) > 0:
            self.get_next_shrimp()
        
        # Override target if eating
        if self.current_shrimp_target and not self.is_dragging:
            self.target_x, self.target_y = self.current_shrimp_target
            if self.state == "idle":
                self.state = "swimming"
        
        # Move towards target
        if (self.state == "swimming" or self.state == "sleeping_prep") and not self.is_dragging:
            kraken_coords = self.canvas.coords("kraken")
            if kraken_coords:
                current_x, current_y = kraken_coords[0], kraken_coords[1]
                
                dx = self.target_x - current_x
                dy = self.target_y - current_y
                distance = math.sqrt(dx**2 + dy**2)
                
                if distance > 5:
                    # Move faster when hunting shrimp
                    speed = 8.0 if self.eating_shrimp else 2.5
                    step = min(speed, distance / 3)
                    new_x = current_x + (dx / distance) * step
                    new_y = current_y + (dy / distance) * step
                    
                    self.move_kraken_to(new_x, new_y)
                else:
                    # Reached target
                    if self.eating_shrimp and self.current_shrimp_target:
                        self.eat_shrimp()
                    elif self.state == "sleeping_prep":
                        self.state = "sleep"
                    else:
                        self.state = "idle"
    
    def animate(self):
        """Animate kraken sprite"""
        animation = ASCII_ANIMATIONS.get(self.state, ASCII_ANIMATIONS['idle'])
        sprite_name = animation[self.animation_frame % len(animation)]
        self.current_sprite = sprite_name
        
        self.render_kraken()
        self.animation_frame += 1
        
        # Update status
        self.state_label.config(text=f"State: {self.state}")
        
        # Schedule next frame
        delay = 1200 if self.state == "sleep" else 300 if self.state == "attack" else 500
        self.root.after(delay, self.animate)
    
    def update_behavior(self):
        """Update behaviors and random actions"""
        self.idle_counter += 1
        self.bubble_timer += 1
        
        # Add bubbles periodically
        if self.bubble_timer % 30 == 0:
            self.add_bubbles()
        
        # Random behaviors
        if self.idle_counter > 80 and self.state == "idle":
            rand = random.random()
            if rand < 0.15:
                self.state = random.choice(["sleep", "attack"])
            elif rand < 0.35:
                self.swim_random()
            self.idle_counter = 0
        
        # Return to idle from other states
        if self.state in ["sleep", "attack"] and self.idle_counter > 50:
            if random.random() < 0.3:
                self.state = "idle"
                self.idle_counter = 0
        
        # Update position
        self.update_position()
        
        # Schedule next update
        self.root.after(100, self.update_behavior)
    
    def run(self):
        """Run the test"""
        print("\n" + "="*60)
        print("🐙 ASCII Underwater Kraken - Quick Test")
        print("="*60)
        print("\n📋 Instructions:")
        print("  • Click in water to drop shrimp - kraken will hunt them!")
        print("  • Click & drag kraken to move it manually")
        print("  • Double-click for attack mode")
        print("  • Use buttons for quick actions")
        print("\n🎮 Features to test:")
        print("  ✓ Shrimp feeding & hunting (faster swimming!)")
        print("  ✓ Water boundary enforcement")
        print("  ✓ All animations (idle, swim, attack, sleep)")
        print("  ✓ Bubble effects and underwater environment")
        print("  ✓ Doubled ASCII character density (12pt font)")
        print("\n💡 Close window when done testing\n")
        
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\n✅ Test complete!")

if __name__ == "__main__":
    try:
        test = QuickTest()
        test.run()
        print("\n✅ Ready to install? Run:")
        print("  • macOS/Linux: ./install.sh")
        print("  • Windows: install_windows.bat\n")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure you have a display available")
        sys.exit(1)
