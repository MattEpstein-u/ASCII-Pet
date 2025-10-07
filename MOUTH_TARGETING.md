# 🎯 Mouth Targeting Implementation

## Problem
Previously, when the kraken swam to eat shrimp, the **sprite anchor point** (top-left of the sprite) moved to the shrimp location. This meant the top of the kraken's head reached the shrimp, which looked unnatural.

## Solution
The kraken now moves so its **mouth** (center bottom of the head) reaches the shrimp location for realistic eating behavior.

## Implementation

### Mouth Position
The octopus mouth is located at:
- **Horizontal**: Center of sprite (offset_x = 0)
- **Vertical**: Line 7 of sprite (offset_y = 7) - bottom of head

### Target Calculation
When targeting a shrimp at `(shrimp_x, shrimp_y)`:

```python
# Calculate where sprite anchor should be so mouth reaches shrimp
target_sprite_x = shrimp_x - mouth_offset_x  # = shrimp_x - 0
target_sprite_y = shrimp_y - mouth_offset_y  # = shrimp_y - 7

# Safety: clamp to boundaries
margin = kraken_radius + 10
target_sprite_x = max(margin, min(target_sprite_x, container_width - margin))
target_sprite_y = max(min_y, min(target_sprite_y, max_y))
```

### Boundary Handling
**Simplest approach** to avoid bugs:
- Clamp all target coordinates to safe boundaries
- `min_x = margin`
- `max_x = container_width - margin`
- `min_y = water_level + margin`
- `max_y = container_height - margin`

No complex edge case logic needed - just clamp and go!

## Code Changes

### desktop_pet.py
1. **Added properties** in `__init__`:
   ```python
   self.mouth_offset_x = 0  # Centered horizontally
   self.mouth_offset_y = 7  # Bottom of head (line 7 of sprite)
   ```

2. **Updated `update_position()`**:
   - Calculate adjusted target based on mouth offset
   - Clamp to safe boundaries
   - Move towards adjusted target
   - Same eating logic when reached

### quick_test.py
Same changes for consistent behavior in test environment.

## Visual Explanation

### Before (Sprite Anchor Targeting)
```
  Kraken Sprite        
  (x, y) ← anchor      Shrimp 🦐
    ↓
    ___________
   /           \
  |  (@)  (@)  |
  |            |
   \____/\____/
       |  |
     [Tentacles]
```
Sprite anchor moved to shrimp → head reached shrimp (unnatural)

### After (Mouth Targeting)
```
  Kraken Sprite
  (x, y) ← anchor (adjusted upward)
    ↓
    ___________
   /           \
  |  (@)  (@)  |
  |            |
   \____/\____/ ← Mouth reaches shrimp!
       |  |
     [Tentacles]
           🦐 ← Shrimp position
```
Sprite anchor adjusted → mouth reaches shrimp (natural!)

## Benefits

✅ **Realistic eating**: Mouth actually reaches the food  
✅ **Visually satisfying**: Looks like the octopus is grabbing shrimp  
✅ **Simple boundaries**: Just clamp coordinates - no complex logic  
✅ **Bug-free edges**: Clamping prevents out-of-bounds issues  
✅ **Consistent**: Same behavior in main app and test script  

## Testing

```bash
# Compile check
python3 -m py_compile desktop_pet.py quick_test.py

# Run test
python3 quick_test.py
# Click to drop shrimp in different locations
# Verify mouth reaches shrimp, not the head
```

## Edge Cases Handled

1. **Shrimp near top edge**: Target clamped to `min_y` - kraken stays in water
2. **Shrimp near bottom**: Target clamped to `max_y` - kraken doesn't hit floor
3. **Shrimp near left/right edges**: Target clamped to safe x bounds
4. **Shrimp outside water**: Already prevented by water boundary checks

All handled by simple coordinate clamping! 🎉
