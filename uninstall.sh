#!/bin/bash
# Uninstallation script for ASCII Desktop Pet on macOS

echo "=== ASCII Desktop Pet Uninstallation ==="
echo

# Stop any running pet processes
echo "Stopping any running ASCII desktop pet processes..."
pkill -f "desktop_pet.py" 2>/dev/null || true

# Remove LaunchAgent
LAUNCH_AGENTS_DIR="$HOME/Library/LaunchAgents"
PLIST_FILE="$LAUNCH_AGENTS_DIR/com.user.asciidesktoppet.plist"

if [ -f "$PLIST_FILE" ]; then
    echo "Unloading LaunchAgent..."
    launchctl unload "$PLIST_FILE" 2>/dev/null || true
    rm "$PLIST_FILE"
    echo "✓ Removed LaunchAgent"
else
    echo "! LaunchAgent not found"
fi

echo
echo "=== Uninstallation Complete! ==="
echo "The ASCII desktop pet has been removed from auto-startup."
echo "You can still run it manually with ./start_pet.sh if you want."
echo