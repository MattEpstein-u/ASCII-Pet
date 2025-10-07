#!/bin/bash
# Desktop Pet Startup Script for macOS and Linux

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Path to the desktop pet Python script
PET_SCRIPT="$SCRIPT_DIR/pet.py"

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "Error: Python not found. Please install Python 3."
    exit 1
fi

# Check if the pet script exists
if [ ! -f "$PET_SCRIPT" ]; then
    echo "Error: pet.py not found in $SCRIPT_DIR"
    exit 1
fi

# Run the ASCII desktop pet
echo "Starting ASCII Desktop Pet..."
cd "$SCRIPT_DIR"
$PYTHON_CMD "$PET_SCRIPT" &

echo "ASCII Desktop Pet started! Check your desktop corner."