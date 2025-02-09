@echo off
setlocal enabledelayedexpansion

echo Checking Python installation...
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Checking required packages...
python -m pip show requests pyperclip python-dotenv >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Installing required packages...
    python -m pip install requests pyperclip python-dotenv
)

echo Running QLDT Fast Login Script...
python get_fast_login.py
echo.
pause
