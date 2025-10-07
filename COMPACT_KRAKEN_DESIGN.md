# Compact Kraken Design

## Overview
This is a **simple, clean octopus/kraken design** based on the user-provided ASCII art. It's much more compact than previous versions while maintaining all the core features.

## Specifications

- **Sprite Height**: 11 lines (reduced from 18)
- **Sprite Width**: ~20 characters
- **Total Sprites**: 8 (idle×2, swim×3, eat×3)
- **Animation States**: 3 (idle, swimming, eating)
- **Mouth Offset**: y=6 (updated from y=7)

## Visual Showcase

### Idle State (User's Custom Design)
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

### Swimming State
```
         ______        
        /      \       
       /        \      
       |        |      
    )  @        @   ?  
   (    \  >   /    |  
  _ \___/||||||\___/ _ 
   \____/ |||| \____/ `
   ,-.___/ || \__,-._  
  /    ___/  \__       
     _/         `---   
```

### Eating State (Chewing - No Wrapping)
```
         ______        
        /      \       
       /        \      
       |        |      
    )  X        X   ?  
   (    \ /VV\ /    |  
  _ \___/||||||\___/ _ 
   \____/ |||| \____/ `
   ,-.___/ || \__,-._  
  /    ___/  \__       
     _/         `---   
```## Design Features

### Head Structure
- **Rounded dome top**: `______` creates a smooth mantle
- **Side walls**: Clear octopus head shape
- **Simple geometry**: Easy to read and understand

### Eyes & Expressions
- **o** - Calm/resting (idle)
- **O** - Open/alert (idle2, swimming)
- **@** - Very alert (swimming)
- **X** - Excited (eating)
- ***** - Intense (eating)
- **^** - Happy (eating)

### Mouth Variations
- **\\      /** - Calm/closed (idle)
- **\\  __  /** - Neutral (idle2)
- **\\  >   /** - Forward motion (swimming)
- **\\  ^   /** - Upward motion (swimming)
- **\\ /VV\\ /** - Eating/chomping
- **\\ <WW> /** - Wide open
- **\\ /^^\\ /** - Satisfied

### Tentacles
- **||||||** - Main tentacle cluster (6 visible)
- **||||** - Secondary tentacles
- Tentacles remain **consistent** across all states
- **NO wrapping** during eating - structure stays the same

### Eating Behavior
The eating animation is **simple and clean**:
1. Kraken **swims to shrimp** location
2. Mouth (line 6) **positions directly over** shrimp
3. **Chewing animation** begins with mouth variations
4. Tentacles **do NOT wrap** - they stay as ||||||
5. Only **eyes and mouth change** during eating

## Technical Details

### Mouth Targeting
```python
mouth_offset_x = 0  # Centered horizontally
mouth_offset_y = 6  # Line 6 of 11-line sprite
```

The mouth is located at the **bottom of the head** where the tentacles connect (line 6). When the kraken swims to eat a shrimp, the sprite position is calculated so that **line 6 reaches the shrimp location**.

### Compact Benefits
1. **Smaller file size** - Less ASCII art data
2. **Faster rendering** - Fewer lines to draw
3. **Cleaner appearance** - Easier to read at a glance
4. **More screen space** - Takes up less room in the underwater environment

## Comparison with Previous Design

| Feature | Previous (Detailed) | Current (Compact) |
|---------|-------------------|-------------------|
| Height | 18 lines | 11 lines |
| Width | ~50 characters | ~20 characters |
| Complexity | High detail, realistic | Simple, clean |
| Style | Professional ASCII art | Geometric/minimalist |
| Tentacles | Flowing, organic curves | Straight lines (||) |
| Mouth Offset | y=7 | y=6 |

## Usage

Run the test script to see it in action:
```bash
python3 quick_test.py
```

Or launch the full desktop pet:
```bash
python3 desktop_pet.py
```

## Animation Sequences

### Idle Animation
`idle1` ↔️ `idle2`
- Eyes alternate: o → O (blinking)
- Mouth changes: plain → __ (slight movement)
- Calm, floating state

### Swimming Animation  
`swim1` → `swim2` → `swim3` → (repeat)
- Eyes: @ → O → @ (alert, scanning)
- Mouth shows directional intent: > → ^ → >
- Swimming toward shrimp location

### Eating Animation
`eat1` → `eat2` → `eat3` → (repeat)
- Eyes: X → * → ^ (excited to satisfied)
- Mouth: /VV\\ → <WW> → /^^\\ (chewing motion)
- Tentacles: **||||||** (unchanged, NO wrapping)
- Mouth is positioned directly over shrimp

## Code Compatibility

✅ **Fully compatible** with:
- `desktop_pet.py` - Updated mouth offset to y=6
- `quick_test.py` - Updated mouth offset to y=6
- `ascii_pet_designs.py` - All 8 sprites redesigned

No other code changes needed!
