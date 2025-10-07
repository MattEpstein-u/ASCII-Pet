# 🐛 Debug Grid Overlay Guide

## Quick Start

### Enable Debug Grid

Edit `designs.py` and change:

```python
DEBUG_CONFIG = {
    'show_grid': True,  # Change False to True
    'grid_size': 50,
    'grid_color': '#444444',
    'show_coordinates': True,
    'show_boundaries': True,
}
```

Then run:
```bash
python3 pet.py
```

## Debug Features

### 1. **Grid Lines** (Dashed)
- Vertical and horizontal lines every `grid_size` pixels
- Default: 50px grid
- Color: Dark gray (`#444444`)
- Helps with: Positioning, measuring distances

### 2. **Coordinate Labels** (Gray Numbers)
- Shows X coordinates at top
- Shows Y coordinates at left
- Helps with: Debugging click positions, sprite locations

### 3. **Boundary Lines** (Colored Solid Lines)

| Color | Line | Description |
|-------|------|-------------|
| **Cyan** | Water Level | Top of ocean surface waves |
| **Green** | Underwater Start | Where interactive area begins (below 2-line waves) |
| **Orange** | Ocean Floor | Bottom boundary (50px from bottom) |
| **Magenta** | Kraken Top Limit | Minimum Y position for kraken center |

## Configuration Options

### Grid Size
```python
'grid_size': 50,  # Change to 25 for finer grid, 100 for coarser
```

### Grid Color
```python
'grid_color': '#444444',  # Dark gray
'grid_color': '#666666',  # Lighter gray
'grid_color': '#FF0000',  # Red (high contrast)
```

### Show/Hide Elements
```python
'show_coordinates': True,   # Set to False to hide numbers
'show_boundaries': True,    # Set to False to hide colored lines
```

## Using the Debug Grid

### **Debugging Shrimp Placement**
1. Enable grid
2. Click to drop shrimp
3. Check console: `🦐 Shrimp dropped at (x, y)`
4. Verify position is below **Green line** (Underwater Start)

### **Debugging Kraken Movement**
1. Watch kraken position relative to grid
2. Check it stays between:
   - **Magenta line** (top limit)
   - **Orange line** (bottom limit)

### **Debugging Bubble Spawning**
1. Bubbles should spawn between:
   - **Green line** (underwater start)
   - **Orange line** (ocean floor)
2. Bubbles should disappear at **Green line**

### **Debugging Wave Surface**
1. **Cyan line** = top of wave area
2. Wave text should render at Cyan line + small offset
3. 2-line wave surface ends at **Green line**

## Common Issues & Solutions

### ❌ "Shrimp placed above water"
- **Check:** Click position vs Green line
- **Fix:** Ensure `is_in_water()` uses correct `surface_height`

### ❌ "Kraken goes above surface"
- **Check:** Kraken top vs Magenta line
- **Fix:** Adjust `min_y` calculation in `move_kraken_to()`

### ❌ "Bubbles appear above water"
- **Check:** Bubble spawn Y vs Green line
- **Fix:** Verify `spawn_bubble()` uses `underwater_start` correctly

### ❌ "Grid covers sprites"
- **Symptom:** Can't see kraken/shrimp through grid
- **Fix:** Grid is automatically lowered in z-order - if issue persists, adjust colors

## Performance Note

The debug grid adds minimal overhead:
- ~100-200 canvas items (depending on window size)
- Redrawn only when environment updates (every 1 second)
- Negligible performance impact

## Disabling for Production

Before releasing/installing, set:
```python
'show_grid': False,
```

## Example Debug Session

```bash
# 1. Enable debug grid
# Edit designs.py, set show_grid = True

# 2. Run desktop pet
python3 pet.py

# 3. Observe output:
🐙 Starting ASCII Underwater Kraken...
📏 Density: Font Size=10, Line Height=12
🐛 Debug Grid: ENABLED (Grid Size: 50px)
🦐 Click underwater to drop shrimp and feed your kraken!

# 4. Click to test
🦐 Shrimp dropped at (245, 320). Queue size: 1

# 5. Verify position:
# - Is 320 > Green line Y? ✓ Yes → Valid underwater position
# - Is 245 between side margins? ✓ Yes → Valid X position
```

## Visual Legend

When debug grid is enabled, you'll see:

```
Top of window
│
├─ Cyan line ══════════════ Water Level (top of waves)
│  ~≈~≈~≈~ (Wave line 1)
│  ≈~≈~≈~≈ (Wave line 2)
├─ Green line ═════════════ Underwater Start (clicks work here)
│
│  🐙 Kraken swims here
│  🦐 Shrimp placed here
│  ○ ○ Bubbles spawn & rise here
│
├─ Magenta line ═══════════ Kraken Top Limit (dashed)
│
│
├─ Orange line ════════════ Ocean Floor
│
Bottom of window
```

---

Happy debugging! 🐙🔍
