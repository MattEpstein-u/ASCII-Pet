# Changelog

All notable changes to the ASCII Underwater Kraken project.

## [Unreleased] - Current Development

### Added - Code Consolidation & Cleanup
- **Unified Testing**: Created `quick_test.py` - single comprehensive test script
- **Removed Redundancies**: Eliminated 6 redundant test scripts (test_interactive.py, demo.py, etc.)
- **Cleaned Documentation**: Consolidated multiple summary files into README and CHANGELOG
- **Result**: Cleaner codebase, ~44KB reduction, easier maintenance

### Added - Interactive Shrimp Feeding System
- **Click-to-Feed**: Click anywhere underwater to drop shrimp (`,` ASCII character)
- **Shrimp Queue**: Multiple shrimp are managed in FIFO queue
- **Hunting Behavior**: Kraken automatically targets and swims to oldest shrimp
- **Eating Animation**: Uses attack animation when reaching and eating shrimp
- **Priority System**: Kraken prioritizes shrimp hunting over cursor following
- **Fast Swimming**: Kraken swims 3.2x faster when hunting (8 units vs 2.5 normal)
- **Visual Feedback**: Terminal output shows shrimp drops, targeting, and eating events

### Changed - Visual Enhancements
- **Doubled ASCII Density**: Font size increased from 6pt to 12pt for more detailed artwork
- **Dynamic Sizing**: Restored 1/8 screen calculation (removed fixed 800x800)
- **Strict Boundaries**: Enhanced boundary enforcement prevents crossing water surface, ocean floor, or sides
- **Cursor Following**: Now conditional - only active when shrimp queue is empty
- **Color Scheme**: Maintained deep ocean theme (#0A0F1C bg, #FFB6C1 kraken, #FFFFFF bubbles/surface, #98FB98 kelp)

### Technical Updates
- Added `shrimp_queue` list to track dropped shrimp positions
- Added `current_shrimp_target` to manage active hunting target
- Added `eating_shrimp` boolean flag for state tracking
- New methods: `drop_shrimp()`, `eat_shrimp()`, `get_next_shrimp_target()`
- Enhanced `update_position()` with shrimp targeting logic
- Modified `follow_cursor()` to check shrimp queue before activating
- Enhanced `move_kraken_to()` with strict boundary clamping
- Updated `start_drag()` to handle both dragging and shrimp dropping
- State machine expanded: "idle", "swimming", "sleeping", "attack", "eating"

### Files Modified
- `desktop_pet.py`: All core changes for shrimp feeding and visual updates
- `test_interactive.py`: Updated font size to match production (6pt → 12pt)
- `README.md`: Added feeding documentation and updated feature lists
- `FEEDING_GUIDE.md`: New comprehensive guide for shrimp feeding system
- `validate_changes.py`: New validation script for testing changes

## [0.1.1] - Deep Ocean Color Scheme

### Changed
- Background color: #f5f5f5 → #0A0F1C (deep blue, almost black)
- Kraken color: #FF6B35 → #FFB6C1 (light pink for visibility)
- Surface and bubbles: White (#FFFFFF)
- Kelp: Light green (#98FB98)
- Ocean cross-section layout: Top 1/5 surface, bottom 4/5 underwater

## [0.1.0] - Kraken Transformation

### Added
- Complete underwater environment with ASCII art
- Water physics system with boundary detection
- Multiple kraken states: idle, swimming, sleeping, attack, sleeping_prep
- Underwater elements: kelp forests, coral, ocean floor, surface waves
- Bubble effects with realistic underwater physics
- Single-eye kraken design with bulbous head shape
- Smart sleep behavior (swims to ocean floor before sleeping)
- 4x faster swimming speed (step_size: 2 → 8)
- Bubble frequency increased 6x (every 0.5 seconds)

### Changed
- Transformed from simple ASCII pet to underwater kraken
- Movement restricted to underwater areas only
- Enhanced ASCII art with detailed tentacles
- Added `is_in_water()` function for water boundary checks
- State machine for complex behaviors

## [0.0.1] - Initial ASCII Pet

### Added
- Basic ASCII pet with Mac-pet features
- Desktop integration (macOS, Windows, Linux)
- Simple animations and cursor following
- Click and drag interactions
- Auto-startup capabilities

---

## Version History Summary

- **Current**: Interactive shrimp feeding + enhanced visuals
- **0.1.1**: Deep ocean color scheme
- **0.1.0**: Full kraken transformation
- **0.0.1**: Initial ASCII pet release

## Upgrade Path

From 0.1.1 to Current:
- Existing installations will automatically get shrimp feeding
- No config changes needed - just pull latest code
- All old interactions still work (drag, double-click, cursor follow)
- New: Click in water to drop shrimp!

## Breaking Changes

None! All previous functionality is preserved:
- ✅ Cursor following (now conditional on empty shrimp queue)
- ✅ Dragging within water
- ✅ Double-click attack mode
- ✅ Automatic behaviors (sleep, idle, swimming)
- ✅ Desktop integration
- ✅ Cross-platform compatibility

## Known Issues

None currently. All features validated via `validate_changes.py`.

## Future Roadmap

Potential features being considered:
- Multiple food types (fish, plankton, algae)
- Hunger/satisfaction system
- Multiple krakens with interaction
- Predator/prey dynamics
- Day/night lighting cycles
- Seasonal underwater themes
- Kraken growth over time
- Achievement system
- Save/load kraken state

---

Last Updated: Current Session
