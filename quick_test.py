#!/usr/bin/env python3
"""
Quick Test - ASCII Underwater Kraken Shrimp Hunter
Simple test script - just click to drop shrimp and watch the kraken hunt!
"""

import tkinter as tk
import math
import sys
from ascii_pet_designs import (ASCII_PET_SPRITES, ASCII_ANIMATIONS, render_ascii_art,
                              render_underwater_environment, is_in_water, update_bubbles)

class QuickTest:
    def __init__(self):
        self.root = tk.Tk()
        
        # Container dimensions for testing (800x800 for visibility)
        self.container_width = 800
        self.container_height = 800
        
        self.setup_window()
        self.setup_canvas()
        self.init_kraken_state()
        
        # Start animation and behavior loops
        self.animate()
        self.update_behavior()
    
    def setup_window(self):
        """Setup test window"""
        self.root.title("🐙 ASCII Kraken Test - Click to Feed Shrimp!")
        self.root.configure(bg='#0A0F1C')
        self.root.geometry(f"{self.container_width}x{self.container_height}")
    
    def setup_canvas(self):
        """Setup underwater canvas"""
        self.canvas = tk.Canvas(self.root, width=self.container_width, height=self.container_height,
                               bg='#0A0F1C', highlightthickness=1, highlightbackground='#FFFFFF')
        self.canvas.pack()
        
        # Render underwater environment
        self.water_level = render_underwater_environment(self.canvas, self.container_width, self.container_height)
        
        # Bind mouse click to drop shrimp
        self.canvas.bind('<Button-1>', self.on_click)


    
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
        
        # Properties
        self.kraken_radius = 30
        
        # Mouth offset from sprite anchor (center bottom of head)
        # Line 5 of sprite × 14 pixels per line = 70 pixels
        mouth_offset_x = 0  # Center of sprite
        mouth_offset_y = 70  # Mouth is at line 5: 5 × (font_size + 2) = 5 × 14 = 70 pixels
        
        # Shrimp feeding
        self.shrimp_queue = []
        self.current_shrimp_target = None
        self.eating_shrimp = False
        
        # Bubble physics system
        self.bubble_list = []  # List of active bubbles
        
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
            return True
        return False
    
    # === Mouse Event Handlers ===
    
    def on_click(self, event):
        """Handle mouse click - drop shrimp in water"""
        if is_in_water(event.x, event.y, self.water_level, self.container_height):
            self.drop_shrimp(event.x, event.y)

    
    # === Shrimp Feeding System ===
    
    def drop_shrimp(self, x, y):
        """Drop shrimp at position"""
        if is_in_water(x, y, self.water_level, self.container_height):
            self.shrimp_queue.append((x, y))
            shrimp_tag = f"shrimp_{len(self.shrimp_queue)}"
            self.canvas.create_text(x, y, text=",", font=("Courier", 16, "bold"),
                                   fill="#FFB6C1", tags=shrimp_tag)
            print(f"🦐 Shrimp dropped at ({x}, {y})")

    
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
            print(f"🐙 Om nom nom! {len(self.shrimp_queue)} shrimp remaining")

    
    # === Animation & Movement ===
    
    def update_position(self):
        """Update kraken position towards shrimp target"""
        # Check for shrimp to eat
        if not self.current_shrimp_target and len(self.shrimp_queue) > 0:
            self.get_next_shrimp()
        
        # Move towards shrimp target
        if self.current_shrimp_target:
            shrimp_x, shrimp_y = self.current_shrimp_target
            
            # Calculate where the sprite anchor should be so the mouth reaches the shrimp
            target_sprite_x = shrimp_x - self.mouth_offset_x
            target_sprite_y = shrimp_y - self.mouth_offset_y
            
            # Safety check: ensure target position is valid
            margin = self.kraken_radius + 10
            min_x = margin
            max_x = self.container_width - margin
            min_y = self.water_level + margin
            max_y = self.container_height - margin
            
            # Clamp target to safe bounds
            target_sprite_x = max(min_x, min(target_sprite_x, max_x))
            target_sprite_y = max(min_y, min(target_sprite_y, max_y))
            
            # Use adjusted target
            self.target_x = target_sprite_x
            self.target_y = target_sprite_y
            
            kraken_coords = self.canvas.coords("kraken")
            if kraken_coords:
                current_x, current_y = kraken_coords[0], kraken_coords[1]
                
                dx = self.target_x - current_x
                dy = self.target_y - current_y
                distance = math.sqrt(dx**2 + dy**2)
                
                if distance > 5:
                    # Swimming to shrimp
                    self.state = "swimming"
                    # Move fast when hunting
                    step = min(8.0, distance / 3)
                    new_x = current_x + (dx / distance) * step
                    new_y = current_y + (dy / distance) * step
                    
                    # Keep within safe bounds
                    new_x = max(min_x, min(new_x, max_x))
                    new_y = max(min_y, min(new_y, max_y))
                    
                    self.move_kraken_to(new_x, new_y)
                else:
                    # Reached target - eat!
                    if self.current_shrimp_target:
                        self.state = "eating"
                        self.eat_shrimp()
        else:
            # No target, return to idle
            if self.state != "idle":
                self.state = "idle"
    
    def animate(self):
        """Animate kraken sprite"""
        # Get animation based on current state
        animation = ASCII_ANIMATIONS.get(self.state, ASCII_ANIMATIONS['idle'])
        sprite_name = animation[self.animation_frame % len(animation)]
        self.current_sprite = sprite_name
        
        self.render_kraken()
        self.animation_frame += 1
        
        # Faster animation for eating
        delay = 300 if self.state == "eating" else 500
        
        # Schedule next frame
        self.root.after(delay, self.animate)
    
    def update_behavior(self):
        """Update behaviors and bubble effects"""
        # Update bubble physics every frame (spawn, rise, remove at surface)
        update_bubbles(self.bubble_list, self.canvas, self.container_width,
                      self.water_level, self.container_height, spawn_chance=0.05)
        
        # Update position (shrimp hunting)
        self.update_position()
        
        # Schedule next update
        self.root.after(100, self.update_behavior)
    
    def run(self):
        """Run the test"""
        print("\n" + "="*60)
        print("🐙 ASCII Underwater Kraken - Quick Test")
        print("="*60)
        print("\n🎯 Instructions:")
        print("  • Click anywhere in the water to drop shrimp")
        print("  • Kraken will hunt and eat the shrimp")
        print("  • Close window when done testing")
        print("\n💡 Features:")
        print("  ✓ NEW: Larger kraken with 2 eyes & long tentacles!")
        print("  ✓ Idle animation (calm floating)")
        print("  ✓ Swimming animation (tentacles propelling)")
        print("  ✓ Eating animation (excited eyes, mouth open!)")
        print("  ✓ Shrimp feeding & hunting")
        print("  ✓ Water boundary enforcement")
        print("  ✓ Bubble effects and underwater environment\n")
        
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
