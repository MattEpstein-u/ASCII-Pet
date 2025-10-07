@echo off
REM Uninstallation script for ASCII Desktop Pet on Windows

echo === ASCII Desktop Pet Uninstallation ===
echo.

REM Stop any running pet processes
echo Stopping any running ASCII desktop pet processes...
taskkill /f /im python.exe /fi "WINDOWTITLE eq ASCII Desktop Pet*" >nul 2>&1
taskkill /f /im pythonw.exe /fi "WINDOWTITLE eq ASCII Desktop Pet*" >nul 2>&1

REM Remove startup shortcut
set STARTUP_DIR=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
set SHORTCUT_PATH=%STARTUP_DIR%\ASCII Desktop Pet.lnk

if exist "%SHORTCUT_PATH%" (
    del "%SHORTCUT_PATH%"
    echo ✓ Removed startup shortcut
) else (
    echo ! Startup shortcut not found
)

echo.
echo === Uninstallation Complete! ===
echo The ASCII desktop pet has been removed from auto-startup.
echo You can still run it manually with start_pet.bat if you want.
echo.
pause