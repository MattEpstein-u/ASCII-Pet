# Unified Sprite Design - Based on idle1

## Overview

All 8 sprites now share the **exact same base structure** as the user's custom `idle1` design. The only differences between sprites are the **eyes (line 4)** and **mouth (line 5)**. Everything else remains identical.

## Base Structure (Lines 0-3, 6-10)

These lines are **identical across all 8 sprites**:

```
         ______                 # Line 0: Head top
        /      \                # Line 1: Head curve
       /        \               # Line 2: Head sides
       |        |               # Line 3: Head bottom
    )  ?        ?   ?           # Line 4: EYES (varies)
   (    \  ???  /    |          # Line 5: MOUTH (varies)
  _ \___/||||||\___/ _          # Line 6: Body/tentacle junction
   \____/ |||| \____/ `         # Line 7: Tentacle base
   ,-.___/ || \__,-._           # Line 8: Middle tentacles
  /    ___/  \__                # Line 9: Lower tentacles
     _/         `---            # Line 10: Bottom tentacles
```

## Variable Lines (4-5 Only)

### Line 4: Eyes

| Sprite | Eyes | Meaning |
|--------|------|---------|
| idle1  | `o        o` | Calm, resting |
| idle2  | `O        O` | Open, blinking |
| swim1  | `@        @` | Alert, focused |
| swim2  | `O        O` | Open while moving |
| swim3  | `@        @` | Alert, focused |
| eat1   | `X        X` | Excited, eating |
| eat2   | `*        *` | Intense, chewing |
| eat3   | `^        ^` | Happy, satisfied |

### Line 5: Mouth

| Sprite | Mouth | Meaning |
|--------|-------|---------|
| idle1  | `\      /` | Neutral, closed |
| idle2  | `\  __  /` | Slight movement |
| swim1  | `\  >   /` | Forward motion |
| swim2  | `\  ^   /` | Upward motion |
| swim3  | `\  >   /` | Forward motion |
| eat1   | `\ /VV\ /` | Chewing (chomping) |
| eat2   | `\ <WW> /` | Wide open (chewing) |
| eat3   | `\ /^^\ /` | Content (swallowing) |

## Complete Sprite Reference

### idle1
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

### idle2
```
         ______        
        /      \       
       /        \      
       |        |      
    )  O        O   ?  
   (    \  __  /    |  
  _ \___/||||||\___/ _ 
   \____/ |||| \____/ `
   ,-.___/ || \__,-._  
  /    ___/  \__       
     _/         `---   
```

### swim1, swim2, swim3
Eyes and mouth change (@ / O, > / ^), structure identical.

### eat1, eat2, eat3
Eyes and mouth change (X / * / ^, VV / WW / ^^), structure identical.

## Key Design Principles

1. **Consistency**: Base structure never changes
2. **Simplicity**: Only 2 lines vary (eyes + mouth)
3. **No Wrapping**: Tentacles always stay as `||||||`
4. **Clean Animation**: Changes are subtle and expressive
5. **Rectangular**: All sprites 11 lines × 23 characters

## Eating Behavior

**Important**: The eating animation does NOT involve tentacle wrapping.

**Process:**
1. Kraken swims to shrimp location
2. Mouth (line 6: `_ \___/||||||\___/ _`) positions over shrimp
3. Animation cycles through eat1 → eat2 → eat3
4. Only eyes and mouth change during eating
5. Tentacles remain `||||||` throughout

This creates a **simple chewing animation** rather than a grabbing/wrapping motion.

## Implementation Benefits

- **Easy to maintain**: Change 2 lines to create new expressions
- **Consistent rendering**: Same dimensions across all sprites
- **Predictable behavior**: Only facial expressions change
- **Clean code**: No complex tentacle animations
- **User's design**: All based on the custom idle1 art

## Testing

```bash
python3 quick_test.py
```

Watch for:
- Idle blinking (o ↔ O eyes)
- Swimming with alert eyes (@) and directional mouth (>, ^)
- Eating with changing eyes (X → * → ^) and mouth (VV → WW → ^^)
- Tentacles staying constant as ||||||
