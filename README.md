# ASCII Underwater Kraken 🐙

A mysterious, colossal ASCII art octopus that dwells in the deep ocean on your desktop! This magnificent creature features **8 thick tentacles radiating in all directions**, complete with visible suction cups, and lives in a beautiful underwater world with realistic bubble physics.

Unlike simple desktop pets, this kraken features intricate ASCII art with tentacles spreading upward, downward, and diagonally in all directions. Watch as it hunts shrimp with precise mouth targeting while continuous streams of bubbles rise naturally to the ocean surface.

---

## ✨ New in Version 2.0

### 🦑 **8-Directional Tentacle Redesign**
- **8 thick tentacles** radiating in ALL directions:
  - 2 tentacles pointing **upward**
  - 2 tentacles pointing **downward**
  - 4 tentacles at **diagonals** (2 left, 2 right at ±45°)
- **Visible suction cups** on all tentacles (`oOo`, `O o`, `o O` patterns)
- **Colossal octopus design** with distinct octopus-shaped head
- **Enhanced animations**: 8 sprites (idle×2, swim×3, eat×3)

### 🫧 **Realistic Bubble Physics**
- **Continuous bubble stream**: Bubbles spawn randomly every frame (5% chance)
- **Rising physics**: Bubbles smoothly rise upward at 2 pixels/frame
- **Natural lifecycle**: Bubbles disappear when reaching ocean surface
- **Atmospheric effect**: Creates authentic underwater feeling

### 🎯 **Precision Mouth Targeting**
- Kraken's **mouth** (not sprite anchor) reaches shrimp location
- Mouth offset calculation for perfect eating alignment
- Natural hunting behavior with smooth movement

---

## Features

### Creature Design
- **8 Directional Tentacles**: Thick tentacles with suction cups spreading in all directions
- **Detailed ASCII Art**: ~19 lines tall, ~25 characters wide with 12pt font
- **Expressive Eyes**: Change based on state - normal `(@)`, alert `(O)`, excited `(X)`, `(*)`, `(^)`
- **Dynamic Mouth**: Opens wide `VVV` when eating shrimp
- **Tentacle Animation**: Different positions for idle, swimming, and eating states

### Underwater Environment
- **Beautiful Ocean Scene**: Surface waves, underwater depths, seaweed forests
- **Realistic Bubble Physics**: Continuous rising bubbles with frame-based spawning
- **Water Boundaries**: Kraken restricted to underwater movement only
- **Natural Colors**: Deep ocean `#0A0F1C`, pink kraken `#FFB6C1`, white bubbles

### Interactive Behaviors
- 🦐 **Shrimp Hunting**: Click underwater to drop shrimp - kraken hunts and eats them in queue order
- 🌊 **Swimming**: Smooth movement with tentacles in propulsion positions
- 😋 **Eating**: Tentacles curl inward with `((` and `))` wrapping animation
- 🫧 **Bubble Effects**: Continuous stream of rising bubbles for atmosphere
- 🎯 **Mouth Precision**: Kraken's mouth precisely reaches shrimp location

### Desktop Integration
- **Non-Intrusive**: Lives in bottom-right corner (1/8 screen size)
- **Cross-Platform**: macOS, Windows, and Linux
- **Auto-Startup**: Automatically starts when you log in
- **Translucent**: Subtle underwater scene that complements your wallpaper

---

## 🎮 Try It First!

**Test the kraken in a regular window before installing:**

```bash
python3 quick_test.py
```

**What you'll see:**
- 🐙 8 thick tentacles with suction cups radiating in all directions
- 🫧 Continuous stream of rising bubbles
- 🦐 Click to drop shrimp and watch the kraken hunt with mouth precision
- 🌊 Beautiful underwater environment with water physics

---

## Installation

### macOS Installation

1. **Download or clone this repository**
2. **Open Terminal** and navigate to the ASCII-Pet folder:
   ```bash
   cd /path/to/ASCII-Pet
   ```
3. **Run the installation script**:
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

### Windows Installation

1. **Download or clone this repository**
2. **Open Command Prompt as Administrator** and navigate to the ASCII-Pet folder:
   ```cmd
   cd C:\path\to\ASCII-Pet
   ```
3. **Run the installation script**:
   ```cmd
   install_windows.bat
   ```

### Linux Installation

1. **Download or clone this repository**
2. **Open Terminal** and navigate to the ASCII-Pet folder:
   ```bash
   cd /path/to/ASCII-Pet
   ```
3. **Run the installation script**:
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

---

## Manual Usage

### macOS/Linux
- **Start**: `python3 desktop_pet.py`
- **Stop**: Close window or `killall Python`
- **Uninstall**: `./uninstall.sh`

### Windows
- **Start**: `python desktop_pet.py`
- **Stop**: Close window or Task Manager
- **Uninstall**: `uninstall_windows.bat`

---

## Interacting with Your Kraken

### Controls
- **Click underwater** → Drop shrimp for kraken to hunt
- **Kraken hunts** → Automatically swims to shrimp and eats them
- **Queue system** → Drop multiple shrimp, kraken eats them in order
- **Watch animations** → Different tentacle positions for idle/swim/eat states
- **Observe bubbles** → Continuous rising stream for underwater atmosphere

### States
- **Idle**: Calm floating, gentle tentacle movement, relaxed eyes
- **Swimming**: Fast movement, tentacles propelling, alert eyes
- **Eating**: Tentacles curling inward, mouth open, excited eyes

---

## Requirements

- **Python 3.6+** (usually pre-installed on Mac/Linux)
- **Tkinter** (included with Python)
- **macOS, Windows 10/11, or Linux**

---

## 📁 Project Structure

```
ASCII-Pet/
├── ascii_pet_designs.py           # Sprites & bubble physics (NEW)
├── desktop_pet.py                 # Main application
├── quick_test.py                  # Interactive test script
├── verify_bubble_physics.py       # Automated physics tests (NEW)
├── KRAKEN_UPDATE_SUMMARY.md       # Update overview (NEW)
├── VISUAL_COMPARISON.md           # Sprite gallery (NEW)
├── TECHNICAL_IMPLEMENTATION.md    # Technical details (NEW)
├── QUICK_REFERENCE.md             # Quick reference card (NEW)
└── README.md                      # This file
```

---

## 🎨 ASCII Art Preview

### Idle State
```
      \  o O o  /        ← 2 tentacles UP
       \ | | | /
        \| | |/
     ____\   /____
   /      \ /      \
  |    (@)   (@)    |    ← Eyes watching
 |                   |
  \      \___/      /    ← Mouth
   \_______________/
  /  |           |  \
 / oOo|         |oOo \   ← Left & right tentacles
| o O |         | O o |     with suction cups
 \ oOo         oOo /
  \  |           |  /
   \ |           | /
    \|           |/
     |oOo     oOo|       ← 2 tentacles DOWN
     | O |   | O |
     |oOo     oOo|
```

### Eating State
```
       \ o O o /
        \| | |/
         \   /
      ____\ /____
    /      V      \
   |   (X)   (X)   |     ← Excited eyes
  |                 |
   \     /VVV\     /     ← Mouth OPEN!
    \___/‾‾‾‾\___/
   ((  |       |  ))     ← Tentacles wrapping
  ((oOo|       |oOo))       with (( )) symbols
 ((O o |       | o O))
  ((oOo       oOo))
   (( |       | ))
    ((|       |))
     (|       |)
      |oOo oOo|
      | O | O |
      |oOo oOo|
```

---

## 📊 Performance

- **CPU**: Minimal (~1%)
- **Memory**: ~10 MB
- **Update Rate**: 10 FPS (smooth for ASCII)
- **Active Bubbles**: ~25-30 at steady state

---

## 🔧 Customization

Edit `ascii_pet_designs.py` to customize:
- **Bubble density**: Change `spawn_chance` (default: 0.05)
- **Bubble speed**: Modify rise speed (default: 2 px/frame)
- **Kraken appearance**: Edit sprite ASCII art
- **Colors**: Adjust color scheme
- **Animations**: Modify sprite sequences

See `TECHNICAL_IMPLEMENTATION.md` for detailed configuration options.

---

## 📚 Documentation

- **KRAKEN_UPDATE_SUMMARY.md** - Overview of Version 2.0 changes
- **VISUAL_COMPARISON.md** - All 8 sprite states with visual examples
- **TECHNICAL_IMPLEMENTATION.md** - Bubble physics system details
- **QUICK_REFERENCE.md** - Quick reference card for features

---

## Troubleshooting

### Kraken doesn't appear
- Make sure Python 3.6+ is installed
- Check that Tkinter is available: `python3 -c "import tkinter"`

### Bubbles not moving
- The bubble system is frame-based - make sure the application is running
- Check that `update_bubbles()` is being called in `update_behavior()`

### ASCII art looks wrong
- Use a monospace font
- Check display scaling settings
- Font size is 12pt for optimal visibility

### Water boundaries not working
- Ensure `is_in_water()` function is working correctly
- Check that `water_level` is calculated properly

---

## Evolution from ASCII Pet

This underwater kraken evolved with these transformations:

**Version 1.0:**
- Basic kraken with underwater environment
- Simple behaviors (idle, swimming, eating)
- Periodic bubble spawning
- Shrimp hunting system

**Version 2.0 (Current):**
- ✨ **8 directional tentacles** with suction cups
- ✨ **Realistic bubble physics** with continuous rising
- ✨ **Mouth targeting** for precise eating
- ✨ **Enhanced animations** (8 sprites)
- ✨ **Colossal octopus design**

---

## Based on Mac-Pet

Inspired by [Mac-pet repository](https://github.com/MattEpstein-u/Mac-pet) and transformed into an underwater experience with:
- Aquatic environment and water physics
- Marine creature (octopus) instead of land animal
- Realistic bubble physics system
- 8-directional tentacle design
- Shrimp hunting mechanics

---

## Contributing

Contributions welcome! Ideas:
- New sea creatures
- Additional animations
- Environmental effects (currents, schools of fish)
- Enhanced bubble physics (wobble, size changes)
- Different ocean biomes

---

## License

Open source. Feel free to modify and distribute.

---

**Dive into the depths with your ASCII kraken! 🐙🌊**

*Version 2.0 - Now with 8 directional tentacles and realistic bubble physics!*
