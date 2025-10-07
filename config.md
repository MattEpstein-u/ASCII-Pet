# ⚙️ Configuration Guide

## ASCII Density Configuration

Located at the top of `designs.py`:

```python
ASCII_DENSITY_CONFIG = {
    'font_size': 10,      # MAIN CONTROL - Lower = more density
    'line_spacing': 2,    # Vertical spacing between lines
    'char_spacing': 1.0,  # Reserved for horizontal density (future)
}
```

### Effect of Font Size

| Font Size | Effect | Character Density | Use Case |
|-----------|--------|-------------------|----------|
| **6** | Tiny | Maximum | Small screens, many elements |
| **8** | Small | High | Compact display |
| **10** | Medium | **Balanced (default)** | General use |
| **12** | Large | Low | Easy reading |
| **14** | Very Large | Minimum | Accessibility |

### Line Spacing

| Spacing | Effect | Visual Density |
|---------|--------|----------------|
| **1** | Tight | Very compact |
| **2** | Normal | **Balanced (default)** |
| **3** | Loose | Airy, easy to read |

### Quick Presets

#### 🔬 Maximum Density
```python
'font_size': 6,
'line_spacing': 1,
```
Result: ~3x more characters visible

#### 📊 High Density
```python
'font_size': 8,
'line_spacing': 2,
```
Result: ~2x more characters visible

#### ⚖️ Balanced (Current Default)
```python
'font_size': 10,
'line_spacing': 2,
```
Result: Good balance of size and visibility

#### 👁️ Low Density
```python
'font_size': 14,
'line_spacing': 3,
```
Result: Large, very easy to read

---

## Debug Configuration

Located in `designs.py`:

```python
DEBUG_CONFIG = {
    'show_grid': False,        # Enable/disable debug overlay
    'grid_size': 50,           # Grid cell size in pixels
    'grid_color': '#444444',   # Grid line color
    'show_coordinates': True,  # Show X/Y coordinate labels
    'show_boundaries': True,   # Show boundary lines
}
```

### Debug Options

#### show_grid
- `True` = Show debug overlay
- `False` = Hide debug overlay (production)

#### grid_size
- Smaller = Finer grid (25px)
- Larger = Coarser grid (100px)
- Default: 50px

#### grid_color
- `'#444444'` = Dark gray (subtle)
- `'#666666'` = Medium gray
- `'#888888'` = Light gray
- `'#FF0000'` = Red (high visibility)

#### show_coordinates
- `True` = Show X/Y numbers on grid
- `False` = Hide coordinate labels

#### show_boundaries
- `True` = Show colored boundary lines
- `False` = Hide boundary markers

---

## What Auto-Adjusts

When you change `ASCII_DENSITY_CONFIG`, these automatically update:

### ✅ Kraken Sprite
- Font size
- Line height
- Total sprite height

### ✅ Ocean Surface
- Wave line font (2px smaller than kraken)
- Wave line spacing
- Surface height (2 lines)

### ✅ Boundaries
- Underwater start position
- Kraken movement limits
- Bubble spawn/removal zones

### ✅ Mouth Targeting
- Calculated as: `5 * line_height`
- Updates when density changes

### ✅ Shrimp Size
- Scales with kraken: `font_size * 1.4`

### ✅ Bubble Sizes
- Base sizes scale proportionally

---

## Testing Your Configuration

### 1. Preview in Terminal
```bash
python3 designs.py
```
Shows current config and sprite previews

### 2. Run Desktop Pet
```bash
python3 pet.py
```
See changes in action

### 3. Enable Debug Grid
Set `'show_grid': True` to verify boundaries

---

## Recommended Configurations

### For Small Screens (< 800px wide)
```python
ASCII_DENSITY_CONFIG = {
    'font_size': 8,
    'line_spacing': 2,
}
```

### For Large Screens (> 1200px wide)
```python
ASCII_DENSITY_CONFIG = {
    'font_size': 12,
    'line_spacing': 3,
}
```

### For Debugging
```python
ASCII_DENSITY_CONFIG = {
    'font_size': 10,
    'line_spacing': 2,
}

DEBUG_CONFIG = {
    'show_grid': True,
    'grid_size': 50,
    'grid_color': '#666666',
    'show_coordinates': True,
    'show_boundaries': True,
}
```

### For Production/Release
```python
DEBUG_CONFIG = {
    'show_grid': False,  # ← IMPORTANT!
    ...
}
```

---

## Tips

1. **Start with font_size** - It has the biggest impact
2. **Test after changes** - Run pet.py to see effects
3. **Use debug grid** - When fine-tuning boundaries
4. **Check all states** - Test idle, swimming, and eating animations
5. **Try different shrimp** - Verify eating works at various positions

---

Enjoy customizing your kraken! 🐙⚙️
