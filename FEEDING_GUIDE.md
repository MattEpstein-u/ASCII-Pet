# ASCII Underwater Kraken - Quick Start Guide

## 🦐 NEW FEATURE: Interactive Shrimp Feeding!

Your underwater kraken can now hunt and eat shrimp that you drop into the water!

### How to Feed Your Kraken

1. **Click anywhere in the underwater area** (the dark blue portion below the surface)
2. **A shrimp (`,`) will appear** at that location
3. **The kraken will swim to it** and eat it automatically
4. **Drop multiple shrimp** to create a feeding queue - kraken eats them in order!

### Feeding Behavior

- 🦐 **Shrimp Queue**: Kraken eats shrimp in the order they were dropped
- 🏊 **Fast Swimming**: Kraken swims faster when hunting shrimp (8 units vs 2.5 normal)
- 🍽️ **Eating Animation**: Kraken uses attack animation when eating (om nom nom!)
- 🎯 **Priority System**: Kraken ignores cursor and focuses on shrimp when available
- ⏸️ **Return to Normal**: After eating all shrimp, kraken returns to idle/cursor-following behavior

### Visual Changes

- **Doubled Character Density**: ASCII art now uses 12pt font (was 6pt) for more detail
- **Dynamic Sizing**: Window is now roughly 1/8 of your screen size (no longer fixed 800x800)
- **Strict Boundaries**: Kraken cannot cross water surface, ocean floor, or side walls
- **Deep Ocean Colors**: Maintained dark blue background (#0A0F1C), light pink kraken (#FFB6C1)

## Basic Interactions

### Feeding (NEW!)
- **Single Click in Water**: Drop a shrimp
- **Multiple Clicks**: Create a feeding queue
- **Watch**: Kraken hunts and eats automatically

### Movement
- **Click on Kraken**: Drag to move (only in water)
- **Double-Click**: Trigger attack mode
- **Cursor Following**: Kraken follows when no shrimp present

### Behaviors
- **Idle**: Floating peacefully, following cursor if nearby
- **Swimming**: Moving to target (shrimp or cursor)
- **Hunting**: Swimming faster to eat shrimp
- **Attack**: Aggressive animation (eating or double-click)
- **Sleeping**: Resting on ocean floor

## Testing the New Features

Run the interactive test to try the shrimp feeding system:

```bash
python test_interactive.py
```

This will show you:
- Live shrimp queue status
- Kraken state (idle, swimming, hunting, etc.)
- Current position coordinates
- Control buttons to test all behaviors

## Tips & Tricks

1. **Create Feeding Patterns**: Drop shrimp in interesting paths for kraken to follow
2. **Queue Management**: Kraken eats oldest shrimp first (FIFO)
3. **Speed Comparison**: Watch how much faster kraken swims when hunting
4. **Boundary Testing**: Try to make kraken cross boundaries - it won't!
5. **Cursor Behavior**: Move cursor near kraken when no shrimp - it follows!

## Troubleshooting

### Shrimp not appearing
- Make sure you're clicking in the underwater area (dark blue section)
- Clicks on the kraken itself will drag it instead of dropping shrimp
- Clicks above water surface won't create shrimp

### Kraken not eating
- Check that shrimp are in the water (should see `,` character)
- Kraken might be in drag mode - release mouse button
- Wait a moment - kraken will target and swim to shrimp automatically

### Want the old behavior?
All original features still work:
- Cursor following (when no shrimp present)
- Dragging within water
- Double-click attack mode
- Automatic sleep behavior

## What's Next?

Possible future additions:
- Different food types (fish, plankton)
- Hunger system
- Multiple krakens
- Predator/prey interactions
- Day/night cycles

Enjoy feeding your underwater kraken! 🐙🦐
