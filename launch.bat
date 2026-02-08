@echo off
title Alpha Engine — Options Builder
echo Starting Options Builder...
echo.

REM Initialize conda for this shell session
call "%USERPROFILE%\miniconda3\condabin\conda.bat" activate options-tool 2>nul
if errorlevel 1 (
    call "%USERPROFILE%\anaconda3\condabin\conda.bat" activate options-tool 2>nul
)
if errorlevel 1 (
    call "%USERPROFILE%\Miniconda3\condabin\conda.bat" activate options-tool 2>nul
)
if errorlevel 1 (
    call "%USERPROFILE%\Anaconda3\condabin\conda.bat" activate options-tool 2>nul
)
if errorlevel 1 (
    REM Try PATH-based conda as last resort
    call conda activate options-tool 2>nul
)

REM Verify python is available
python --version >nul 2>nul
if errorlevel 1 (
    echo ERROR: Python not found. Is the conda environment set up?
    pause
    exit /b 1
)

echo Opening browser...
start "" http://127.0.0.1:8051/v2
echo Starting server...
python -m frontend_dash.run_vnext
echo.
echo Server stopped. You can close this window.
pause
