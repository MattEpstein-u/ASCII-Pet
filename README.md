# ASCII Underwater Kraken �

A mysterious, deep-sea ASCII art kraken that dwells in an underwater environment on your desktop! This aqu**What you can experience:**
- 🐙 **Kraken Controls** - Swimming, attacking, sleeping, hunting behaviors
- 🦐 **Feed the Kraken** - Click to drop shrimp and watch it hunt them down
- 🌊 **Water Physics** - See how movement is restricted to underwater areas
- 🫧 **Bubble Effects** - Watch bubbles float through the water
- 🌿 **Underwater Environment** - Explore seaweed forests and ocean floor
- ⚡ **Attack Mode** - Trigger aggressive tentacle animations when eating or double-clicking
- 🎯 **Water Boundaries** - Experience realistic aquatic movement constraints with strict boundaries
- 🖱️ **Drag and Drop** - Move the kraken within water areas only
- 📊 **Live Status** - Monitor kraken state, position, and shrimp queue in real-timeanion lives in a beautiful underwater world with swaying seaweed, floating bubbles, and ocean depths.

Unlike simple desktop pets, this kraken features intricate ASCII art tentacles and is restricted to move only in the underwater portions of its environment, creating a realistic aquatic ecosystem on your desktop.

## Features

- **Underwater Environment**: Beautiful ASCII art ocean scene with surface waves, underwater depths, seaweed forests, and floating bubbles
- **Water Physics**: Kraken can only move in underwater areas - realistic environmental constraints
- **Interactive Feeding**: Click anywhere in the water to drop shrimp that the kraken will hunt and eat!
- **Detailed ASCII Art**: Intricate tentacle animations and creature expressions with doubled character density
- **Aquatic Behaviors**: Swimming, resting on ocean floor, tentacle attacks, hunting, and idle floating
- **Environmental Effects**: Animated bubbles, swaying seaweed, ocean waves
- **Desktop Integration**: Lives on your desktop background in a translucent underwater window (1/8 screen size)
- **Cross-Platform**: Works on macOS, Windows, and Linux
- **Interactive**: Click to feed shrimp, drag within water areas, double-click for attack mode
- **Auto-Startup**: Automatically starts when you log in
- **Non-Intrusive**: Subtle underwater scene that complements your wallpaper

## Kraken Behaviors

- **🌊 Swimming**: Gracefully moves through water with flowing tentacle animations
- **🦐 Hunting**: Swims to dropped shrimp and eats them in queue order
- **😴 Resting**: Settles on the ocean floor in a peaceful state
- **⚡ Attack**: Aggressive tentacle thrashing when threatened, excited, or eating
- **🫧 Bubble Effects**: Creates bubbles during movement and breathing
- **🌿 Environment Interaction**: Navigates around seaweed and ocean floor terrain
- **🎯 Water Boundaries**: Cannot move above the water line or through ocean floor - true aquatic behavior
- **👆 Cursor Following**: Only follows cursor when not hunting shrimp

## Installation

### macOS Installation

1. **Download or clone this repository** to your Mac
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

1. **Download or clone this repository** to your Windows PC
2. **Open Command Prompt as Administrator** and navigate to the ASCII-Pet folder:
   ```cmd
   cd C:\path\to\ASCII-Pet
   ```
3. **Run the installation script**:
   ```cmd
   install_windows.bat
   ```

### Linux Installation

1. **Download or clone this repository** to your Linux system
2. **Open Terminal** and navigate to the ASCII-Pet folder:
   ```bash
   cd /path/to/ASCII-Pet
   ```
3. **Run the installation script**:
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

Your underwater kraken will start immediately and appear in its aquatic habitat every time you restart your computer.

## Manual Usage

### macOS/Linux
- **Start the kraken**: `./start_pet.sh`
- **Stop the kraken**: Use Activity Monitor or `killall Python`
- **Uninstall**: `./uninstall.sh`

### Windows
- **Start the kraken**: `start_pet.bat`
- **Stop the kraken**: Use Task Manager to end Python process
- **Uninstall**: `uninstall_windows.bat`

## Interacting with Your Underwater Kraken

- **Underwater World**: Kraken lives in a detailed ASCII underwater environment
- **Water Movement**: Can only swim in underwater areas - true aquatic physics!
- **Feed Your Kraken**: Click anywhere underwater to drop a shrimp (`,` character)
- **Hunting Behavior**: Kraken swims to shrimp in queue order and eats them
- **Swimming**: Click on the kraken to make it swim to a new location
- **Attack Mode**: Double-click to trigger aggressive tentacle thrashing, or watch it attack while eating!
- **Drag & Drop**: Click and drag the kraken within water areas only
- **Ocean Floor**: Kraken rests on the sandy bottom when sleeping
- **Bubble Effects**: Watch bubbles float up during movement and breathing
- **Seaweed Forest**: Navigate through swaying underwater vegetation
- **Environmental Immersion**: Realistic underwater ecosystem on your desktop
- **Smart Behavior**: Kraken prioritizes eating shrimp over following your cursor

## Requirements

- **macOS** (tested on recent versions) OR **Windows 10/11** OR **Linux**
- **Python 3.6+** (usually pre-installed on Mac/Linux, download from python.org for Windows)
- **Tkinter** (included with Python)
- **Optional for Windows**: pywin32 (automatically installed for better desktop integration)

## Troubleshooting

### Pet doesn't start automatically
1. **macOS**: Check if the LaunchAgent is loaded:
   ```bash
   launchctl list | grep asciidesktoppet
   ```
   If not found, try reinstalling:
   ```bash
   ./uninstall.sh
   ./install.sh
   ```

2. **Windows**: Check the Startup folder for the shortcut:
   ```cmd
   %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
   ```

## 🎮 Interactive Testing Mode - **TRY THE KRAKEN FIRST!**

**Test the underwater kraken in a regular window before installing:**

```bash
python3 test_interactive.py    # Interactive kraken test
# OR
python3 demo.py               # Animation preview
```

**What you can experience:**
- 🐙 **Kraken Controls** - Swimming, attacking, sleeping behaviors
- 🌊 **Water Physics** - See how movement is restricted to underwater areas
- 🫧 **Bubble Effects** - Watch bubbles float through the water
- � **Underwater Environment** - Explore seaweed forests and ocean floor
- ⚡ **Attack Mode** - Trigger aggressive tentacle animations
- 🎯 **Water Boundaries** - Experience realistic aquatic movement constraints
- 🖱️ **Drag and Drop** - Move the kraken within water areas only
- � **Live Status** - Monitor kraken state and position in real-time

### Preview and Test the Pet
See what your ASCII pet will look like and test its behavior before installing:
```bash
# macOS/Linux
python3 demo.py              # Animation preview
python3 test_container.py    # Container size preview  
python3 test_interactive.py  # Interactive test mode - play with the pet!

# Windows  
python demo.py               # Animation preview
python test_container.py     # Container size preview
python test_interactive.py   # Interactive test mode - play with the pet!
```

### Testing Compatibility
Run the compatibility test before installation (optional):
```bash
python3 test_compatibility.py    # Check system compatibility
```

**Ready to try it? Just run:**
```bash
python3 quick_test.py    # Comprehensive interactive test - everything in one place!
```

## Troubleshooting

### Kraken appears but doesn't respond
- Make sure you're clicking directly on the ASCII kraken tentacles
- Try double-clicking to trigger attack mode
- Check that the underwater window is active

### No shrimp appearing when clicking
- Make sure you're clicking in the underwater area (dark blue section)
- Clicks on the kraken itself will drag it instead of dropping shrimp
- Clicks above the water surface won't create shrimp

### ASCII art looks distorted
- Make sure you're using a monospace font
- The kraken now uses 12pt font for better visibility
- Try adjusting your display scaling if needed

### Water physics not working
- Ensure you're trying to move the kraken only in blue/underwater areas
- The kraken cannot move above the water line - this is intentional!
- Try clicking deeper in the underwater area

### Permission issues (macOS)
If you get permission errors, you may need to give Terminal or Python accessibility permissions:
1. Go to System Preferences > Security & Privacy > Privacy
2. Click on "Accessibility" 
3. Add Terminal or Python to the list of allowed apps

## Customization

You can customize your underwater kraken by editing the files:

- **Change ASCII art**: Modify `ascii_pet_designs.py` to create new kraken designs or environment elements
- **Adjust water level**: Change the water boundary calculations in the environment rendering
- **Add sea creatures**: Create new ASCII art for fish, coral, or other ocean life (shrimp are already included!)
- **Modify behaviors**: Edit swimming patterns, hunting speed, and animation sequences
- **Environment effects**: Add new bubble patterns or seaweed animations
- **Feeding mechanics**: Adjust shrimp appearance, drop frequency, or eating animations
- **Size and density**: Modify container size calculation or font size for different visual density

## Files Included

- `desktop_pet.py` - Main underwater kraken application (ASCIIUnderwaterKraken class)
- `ascii_pet_designs.py` - Kraken ASCII art sprites, underwater environment, and water physics
- `demo.py` - Preview script to see kraken animations and underwater world
- `test_interactive.py` - **Interactive test mode - play with the underwater kraken!**
- `test_compatibility.py` - System compatibility checker
- Installation and startup scripts for all platforms

## Cross-Platform Notes

This ASCII desktop pet is designed to work seamlessly on macOS, Windows, and Linux:

### macOS Features:
- Uses macOS LaunchAgents for automatic startup
- Desktop-level window positioning to stay below applications
- Optimized for recent macOS versions

### Windows Features:
- Uses Windows Startup folder for automatic startup
- Optional pywin32 integration for better desktop positioning
- Compatible with Windows 10 and 11

### Linux Features:
- Works with most desktop environments
- Uses standard window manager hints for desktop positioning
- Tested on Ubuntu, but should work on other distributions

### All Platforms:
- Tkinter's transparency features for clean desktop integration
- Smart window management to stay on desktop background only
- Cross-platform cursor following and interaction
- Beautiful ASCII art that works consistently across platforms

## ASCII Art Gallery

The kraken features several detailed underwater states:

**Idle Floating:**
```
    .-""-.
   /      \
  |  o  o  |
  |   <    |
  |  ___   |
   \  ~~~  /
    '-...-'
     |||||
  ===V|||V===
     |||||
```

**Swimming Animation:**
```
    .-""-.     
   /      \    
  |  O  O  |   ~ ~ ~
  |   ^    |  
  |  ___   |  
   \  ~~~  /   
    '-...-'    
   ~~|||||~~   
  ===V|||V===  
   ~~|||||~~   
```

**Attack Mode:**
```
    .-""-.
   /  ^^  \
  | >O  O< |
  |   V    |
  |  \^/   |
   \  ~~~  /
    '-!!-'
    /|||||\\
  ===V|||V===
    \\|||||/
```

**Resting on Ocean Floor:**
```
    .-""-.
   /      \
  |  -  -  |
  |   u    |
  |  ___   |
   \  ~~~  /
    '-...-'
     |||||
════V|||V════
~~~~~~~~~~~~~~~~
```

**Underwater Environment:**
```
~~~~~~~~~~~~~~~~~ (surface waves)
🌊🌊🌊🌊🌊🌊🌊🌊🌊
                     ○ ○ (bubbles)
     |     |    ○
     |     |         (seaweed)
     |     |    
   __|     |__       
════════════════     (ocean floor)
```

## Evolution from ASCII Pet

This underwater kraken evolved from the original ASCII Pet concept with these transformations:

- **Environment**: Added complete underwater ecosystem with water physics
- **Movement Constraints**: Kraken restricted to water areas only - realistic aquatic behavior with strict boundaries
- **Interactive Feeding**: Click-to-drop shrimp system with hunting and eating behaviors
- **Creature Design**: Transformed from land animal to deep-sea kraken with tentacles
- **Environmental Effects**: Added bubbles, seaweed, waves, and ocean floor
- **Aquatic Behaviors**: Swimming replaces walking, ocean floor resting, tentacle attacks, shrimp hunting
- **Visual Density**: Doubled ASCII character density for more detailed artwork
- **Dynamic Sizing**: Smart container sizing (1/8 screen) for optimal desktop integration
- **Visual Immersion**: Dark underwater color scheme with oceanic atmosphere

## Based on Mac-Pet

This underwater kraken is inspired by the [Mac-pet repository](https://github.com/MattEpstein-u/Mac-pet) but completely transformed:

- **Aquatic Environment**: Complete underwater world instead of simple container
- **Water Physics**: Movement restricted to underwater areas
- **Marine Creature**: Deep-sea kraken instead of land animal
- **Environmental Immersion**: Rich underwater ecosystem with multiple elements
- **Same Core Features**: Cursor following, interactions, desktop integration
- **Enhanced ASCII Art**: More detailed creature and environment designs

## Contributing

Contribute new sea creatures, underwater environments, marine behaviors, or aquatic effects!

## License

This project is open source. Feel free to modify and distribute.

---

Dive into the depths with your new underwater ASCII kraken companion! �🌊

*Evolved from the Mac-pet concept into an immersive underwater ecosystem experience.*