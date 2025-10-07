#!/bin/bash
# Installation script for ASCII Desktop Pet on macOS

echo "=== ASCII Desktop Pet Installation for macOS ==="
echo

# Get current directory
CURRENT_DIR="$(pwd)"
LAUNCH_AGENTS_DIR="$HOME/Library/LaunchAgents"

# Check if we're in the right directory
if [ ! -f "pet.py" ]; then
    echo "Error: Please run this script from the directory containing pet.py"
    exit 1
fi

echo "Installing ASCII Desktop Pet..."

# Make the startup script executable
chmod +x start_pet.sh
echo "✓ Made start_pet.sh executable"

# Create LaunchAgents directory if it doesn't exist
mkdir -p "$LAUNCH_AGENTS_DIR"
echo "✓ Created LaunchAgents directory"

# Create the plist file for LaunchAgent
PLIST_FILE="$LAUNCH_AGENTS_DIR/com.user.asciidesktoppet.plist"
cat > "$PLIST_FILE" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.asciidesktoppet</string>
    <key>ProgramArguments</key>
    <array>
        <string>$CURRENT_DIR/start_pet.sh</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <false/>
    <key>LaunchOnlyOnce</key>
    <true/>
    <key>WorkingDirectory</key>
    <string>$CURRENT_DIR</string>
</dict>
</plist>
EOF

echo "✓ Created LaunchAgent plist file"

# Load the LaunchAgent
launchctl load "$PLIST_FILE" 2>/dev/null || true
echo "✓ Loaded LaunchAgent"

echo
echo "=== Installation Complete! ==="
echo
echo "Your ASCII desktop pet is now installed and will start automatically when you log in."
echo
echo "Manual Controls:"
echo "• To start the pet manually: ./start_pet.sh"
echo "• To stop the pet: killall Python (or use Activity Monitor)"
echo "• To uninstall: ./uninstall.sh"
echo
echo "Pet Features:"
echo "• Lives in a small container in the corner of your desktop"
echo "• Beautiful ASCII art animations instead of simple emojis"
echo "• Click and drag to move the pet within its container"
echo "• Double-click to make it play"
echo "• The pet will follow your cursor and wander randomly"
echo "• It will sleep, play, and be idle randomly"
echo "• Only visible when all apps are minimized to desktop"
echo
echo "Starting the pet now..."
./start_pet.sh

echo
echo "Enjoy your new ASCII desktop companion! 🐱"