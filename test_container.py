#!/usr/bin/env python3
"""
Container size and position preview for ASCII Desktop Pet
"""

import tkinter as tk
import platform
from ascii_pet_designs import ASCII_PET_SPRITES, render_ascii_art

def calculate_container_size():
    """Calculate container size as 1/8 of screen area"""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Calculate 1/8 of screen area (approximately square container)
    total_area = screen_width * screen_height
    container_area = total_area // 8
    
    # Make container roughly square, but constrain to reasonable dimensions
    container_side = int(container_area ** 0.5)
    
    # Constrain to reasonable limits (minimum 300x300 for ASCII art, maximum 700x500)
    container_width = max(300, min(container_side, 700))
    container_height = max(300, min(container_side, 500))
    
    # Position container in bottom-right corner with some margin
    margin = 50
    container_x = screen_width - container_width - margin
    container_y = screen_height - container_height - margin
    
    root.destroy()
    return container_width, container_height, container_x, container_y, screen_width, screen_height

def test_container_size():
    """Show a preview of the container size and position"""
    print("=== ASCII Pet Container Preview ===")
    print("Calculating optimal container size...")
    
    container_width, container_height, container_x, container_y, screen_width, screen_height = calculate_container_size()
    
    print(f"Screen size: {screen_width} x {screen_height}")
    print(f"Container size: {container_width} x {container_height}")
    print(f"Container position: ({container_x}, {container_y})")
    print()
    print("Opening preview window...")
    
    # Create preview window
    root = tk.Tk()
    root.title("ASCII Pet Container Preview")
    root.geometry(f"{container_width}x{container_height}+{container_x}+{container_y}")
    root.configure(bg='#f5f5f5')
    root.attributes('-alpha', 0.90)
    
    # Create canvas with preview
    canvas = tk.Canvas(root, width=container_width, height=container_height, 
                      bg='#f5f5f5', highlightthickness=0)
    canvas.pack()
    
    # Draw container background
    canvas.create_rectangle(5, 5, container_width-5, container_height-5,
                           fill='#fafafa', outline='#e5e5e5', width=1)
    
    # Add preview ASCII pet in center
    pet_x = container_width // 2
    pet_y = container_height // 2
    preview_sprite = ASCII_PET_SPRITES['idle1']
    render_ascii_art(preview_sprite, pet_x, pet_y, canvas, tag="preview_pet", color="#2c3e50")
    
    # Add labels
    canvas.create_text(container_width-15, 15, text='🏠', 
                      font=('Arial', 12), anchor='ne', fill='#c0c0c0')
    
    canvas.create_text(15, container_height-25, 
                      text=f'{container_width}x{container_height}',
                      font=('Arial', 10), anchor='w', fill='#888')
    
    canvas.create_text(container_width//2, 30, 
                      text='ASCII Desktop Pet Container Preview',
                      font=('Arial', 12, 'bold'), anchor='center', fill='#666')
    
    canvas.create_text(container_width//2, container_height-50, 
                      text='This is where your ASCII pet will live on your desktop',
                      font=('Arial', 10), anchor='center', fill='#888')
    
    print("Preview window opened!")
    print("This shows the size and position of your ASCII pet's container.")
    print("Close the preview window when you're done.")
    print()
    
    # Auto close after 15 seconds or user interaction
    def close_preview():
        print("Closing preview...")
        root.quit()
        root.destroy()
        
    root.bind('<Button-1>', lambda e: close_preview())
    root.bind('<Key>', lambda e: close_preview())
    root.focus_set()
    root.after(15000, close_preview)  # Auto-close after 15 seconds
    
    try:
        root.mainloop()
    except:
        pass
    
    print("Preview complete!")
    print()
    print("Ready to test your ASCII pet? Run:")
    print("  python3 test_interactive.py")

if __name__ == "__main__":
    test_container_size()