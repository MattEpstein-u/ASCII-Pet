# Rectangular Sprite Design

## Summary

All ASCII kraken sprites have been updated to have **perfectly rectangular dimensions**:
- **Width**: 23 characters (every line)
- **Height**: 11 lines (all sprites)

This ensures consistent rendering and eliminates any edge-case bugs related to variable-width text.

## Implementation

Each sprite line is **padded with trailing spaces** to reach exactly 23 characters:

```python
'idle1': [
    "         ______        ",  # 23 chars
    "        /      \\       ",  # 23 chars
    "       /        \\      ",  # 23 chars
    # ... etc
]
```

## Verification

Run this to verify all sprites are rectangular:

```bash
python3 -c "
import ascii_pet_designs
for name, lines in ascii_pet_designs.ASCII_PET_SPRITES.items():
    widths = [len(line) for line in lines]
    print(f'{name}: {len(lines)} lines, width {widths[0]}')
    assert len(set(widths)) == 1, f'{name} has variable width!'
    assert widths[0] == 23, f'{name} width is {widths[0]}, not 23!'
print('✅ All sprites are perfectly rectangular!')
"
```

## Benefits

1. **Consistent rendering** - No alignment issues
2. **Predictable bounds** - Easy collision detection
3. **Clean code** - No special cases for variable widths
4. **Professional appearance** - Uniform sprite shapes

## Custom idle1 Design

The `idle1` sprite uses the user's literal ASCII art:

```
         ______        
        /      \       
       /        \      
       |        |      
    )  o        o   ?  
   (    \      /    |  
  _ \___/||||||\___/ _ 
   \____/ |||| \____/ `
   ,-.___/ || \__,-._  
  /    ___/  \__       
     _/         `---   
```

**Unique characteristics:**
- Asymmetric eye design: `o` and `?`
- Artistic decorations: backticks, hyphens
- Variable indentation for depth
- Custom tentacle patterns

All other sprites (idle2, swim1-3, eat1-3) are padded to match this 23-character width.
