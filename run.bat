@echo off
REM Scars Watch Campaign - Combined Launcher (Windows)
REM This script starts both Flask and Streamlit in separate processes

setlocal enabledelayedexpansion

echo.
echo Scars Watch Campaign - Launcher
echo ================================
echo.

REM Configuration
set FLASK_PORT=5000
set STREAMLIT_PORT=8501
set FLASK_HOST=0.0.0.0

if defined FLASK_PORT_OVERRIDE (
    set FLASK_PORT=!FLASK_PORT_OVERRIDE!
)
if defined STREAMLIT_PORT_OVERRIDE (
    set STREAMLIT_PORT=!STREAMLIT_PORT_OVERRIDE!
)

echo Configuration:
echo   Flask:     http://localhost:%FLASK_PORT%
echo   Streamlit: http://localhost:%STREAMLIT_PORT%
echo.

REM Check if dependencies are installed
python -m pip show flask >nul 2>&1
if errorlevel 1 (
    echo [*] Installing dependencies...
    pip install -e . >nul
    pip install -r requirements.txt >nul
)

REM Create a batch script to start both services
set TEMP_SCRIPT=%TEMP%\start_services.bat

(
    echo @echo off
    echo color 02
    echo title Scars Watch Campaign - Services
    echo.
    echo echo.
    echo echo =========================================
    echo echo Scars Watch Campaign Services
    echo echo =========================================
    echo echo.
    echo echo Starting services...
    echo echo.
    echo.
    echo REM Start Flask
    echo echo [Flask] Starting Flask app on port %FLASK_PORT%...
    echo start "Flask" cmd /k "set FLASK_HOST=%FLASK_HOST% && set FLASK_PORT=%FLASK_PORT% && python app.py"
    echo timeout /t 3 /nobreak
    echo.
    echo REM Start Streamlit
    echo echo [Streamlit] Starting Streamlit app on port %STREAMLIT_PORT%...
    echo start "Streamlit" cmd /k "streamlit run fluff_generator.py --server.port %STREAMLIT_PORT% --server.headless false"
    echo.
    echo echo.
    echo echo =========================================
    echo echo Services Running!
    echo echo =========================================
    echo echo.
    echo echo Map Interface:    http://localhost:%FLASK_PORT%
    echo echo Fluff Generator:  http://localhost:%STREAMLIT_PORT%
    echo echo.
    echo echo Open these URLs in your web browser.
    echo echo.
    echo pause
) > "%TEMP_SCRIPT%"

REM Execute the script
"%TEMP_SCRIPT%"

REM Cleanup
del "%TEMP_SCRIPT%"

endlocal
