@echo off
REM ============================================================================
REM ONE-CLICK LOCAL RUN SCRIPT FOR CHOTU-BACKTESTING
REM ============================================================================
REM Last Updated: 2025-11-15
REM ============================================================================

cls
echo ============================================================================
echo           CHOTU-BACKTESTING - BACKTESTING FRAMEWORK
echo ============================================================================
echo.
echo Starting Chotu-backtesting (Streamlit Backtesting Framework)...
echo.

REM Check if virtual environment exists
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        echo Please ensure Python is installed and in PATH
        pause
        exit /b 1
    )
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

REM Install dependencies
echo.
echo Installing dependencies...
pip install -r requirements.txt
pip install -r requirements_web.txt

REM Start Streamlit app
echo.
echo ============================================================================
echo Starting Streamlit app...
echo ============================================================================
echo.
streamlit run streamlit_app.py

pause
