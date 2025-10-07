# ASCII Desktop Pet 🐱

A cute, simple ASCII art desktop pet for macOS, Windows, and Linux that lives in a small container on your desktop background and provides companionship while you work!

Unlike other desktop pets that use simple emojis, this pet features beautiful ASCII art animations that bring your desktop companion to life with detailed expressions and movements.

## Features

- **Beautiful ASCII Art**: Detailed ASCII art animations instead of simple emojis
- **Small Container**: Lives in a compact area (1/8 screen size) in desktop corner
- **Desktop Background**: Only visible when all apps are minimized to desktop
- **Cross-Platform**: Works on macOS, Windows, and Linux
- **Interactive**: Click and drag to move within container, double-click to play
- **Smart Behavior**: Follows your cursor and wanders randomly in container
- **Multiple States**: Idle, walking, sleeping, and playing animations
- **Auto-Startup**: Automatically starts when you log in
- **Non-Intrusive**: Subtle design that blends with your wallpaper

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

That's it! Your ASCII desktop pet will start immediately and will automatically appear every time you restart your computer.

## Manual Usage

### macOS/Linux
- **Start the pet**: `./start_pet.sh`
- **Stop the pet**: Use Activity Monitor or `killall Python`
- **Uninstall**: `./uninstall.sh`

### Windows
- **Start the pet**: `start_pet.bat`
- **Stop the pet**: Use Task Manager to end Python process
- **Uninstall**: `uninstall_windows.bat`

## Interacting with Your ASCII Pet

- **Container**: Pet lives in a small, subtle container in the corner of your desktop
- **Visibility**: Only appears when all applications are minimized to show the desktop
- **Move**: Click and drag the pet to move it within its container space
- **Play**: Double-click on the pet to make it happy and playful
- **Follow**: Move your cursor near the container and the pet will follow
- **Wandering**: Pet randomly explores different spots within its container
- **Automatic behaviors**: Pet will randomly sleep, play, and idle
- **ASCII Art**: Enjoy detailed ASCII art animations that change based on mood
- **Subtle design**: Container blends nicely with most desktop wallpapers

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

### 🎮 Interactive Testing Mode - **TRY IT FIRST!**
**Test all pet behaviors in a regular window before installing:**

**Quick Start:**
```bash
python3 test_interactive.py    # Direct interactive test
# OR
python3 play_test.py          # Guided launcher with instructions
```

**What you can test:**
- 🎮 **Control buttons** - Trigger play, sleep, walk, and random movement
- 🖱️ **Mouse following** - Move mouse near pet to make it follow
- 🎯 **Click and drag** - Move the pet around the container
- 🏠 **Container preview** - See exactly how it will look on desktop  
- 📊 **Live status** - See current pet state in real-time
- ✨ **All behaviors** - Test wandering, animations, and interactions
- 🎨 **ASCII Art** - Experience beautiful ASCII art animations
- 🔄 **No restart needed** - Test everything without installation!

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
Run the compatibility test before installation:
```bash
# macOS/Linux
python3 test_compatibility.py

# Windows
python test_compatibility.py
```

### Pet appears but doesn't respond
- Make sure you're clicking directly on the ASCII art
- Try double-clicking to wake it up
- Check that the container window is active

### Permission issues (macOS)
If you get permission errors, you may need to give Terminal or Python accessibility permissions:
1. Go to System Preferences > Security & Privacy > Privacy
2. Click on "Accessibility" 
3. Add Terminal or Python to the list of allowed apps

### ASCII art looks wrong
- Make sure you're using a monospace font in your terminal
- Try adjusting terminal font size if the pet appears distorted
- The ASCII art is optimized for Courier and similar monospace fonts

## Customization

You can customize your ASCII pet by editing the files:

- **Change ASCII art**: Modify `ascii_pet_designs.py` to create new pet designs
- **Adjust behavior timing**: Change values in the `update_behavior()` function in `desktop_pet.py`
- **Modify animations**: Edit the animation sequences in `ascii_pet_designs.py`
- **Container size**: Adjust the calculation in `calculate_container_size()` method

## Files Included

- `desktop_pet.py` - Main ASCII pet application (cross-platform)
- `ascii_pet_designs.py` - ASCII art sprites and animation definitions
- `demo.py` - Preview script to see ASCII pet animations
- `test_container.py` - Container size and position preview
- `test_interactive.py` - **Interactive test mode - play with the ASCII pet!**
- `test_compatibility.py` - System compatibility checker
- `play_test.py` - Quick launcher for interactive testing
- `start_pet.sh` - macOS/Linux startup script
- `start_pet.bat` - Windows startup script
- `install.sh` - macOS/Linux installation script
- `install_windows.bat` - Windows installation script
- `uninstall.sh` - macOS/Linux removal script
- `uninstall_windows.bat` - Windows removal script
- `com.user.asciidesktoppet.plist` - macOS LaunchAgent configuration

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

The pet features several different ASCII art states:

**Idle States:**
```
   /\_/\  
  ( o.o ) 
   > ^ <  
```

**Walking Animation:**
```
   /\_/\  
  ( o.o ) 
   > ^ <  
    / \   
```

**Sleeping:**
```
  /\_/\   
 ( -.- )  
  \___/   
```

**Playing:**
```
   /\_/\  
  ( ^o^ ) 
   >***<  
    !!!   
```

## Differences from Mac-Pet

This ASCII-Pet is based on the [Mac-pet repository](https://github.com/MattEpstein-u/Mac-pet) but with these key improvements:

- **ASCII Art**: Replaced simple emoji sprites with detailed ASCII art
- **Enhanced Animations**: More expressive character states and movements
- **Better Visual Appeal**: More detailed and engaging pet appearance
- **Same Functionality**: All the beloved features of the original (cursor following, interactions, behaviors)
- **Cross-Platform**: Works on Linux in addition to macOS and Windows

## Contributing

Feel free to contribute new ASCII art designs, behaviors, or platform improvements!

## License

This project is open source. Feel free to modify and distribute.

---

Enjoy your new ASCII desktop companion! 🐱

*Based on the original Mac-pet concept but enhanced with beautiful ASCII art for a more engaging desktop experience.*