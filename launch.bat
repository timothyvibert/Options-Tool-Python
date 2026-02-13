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
set WEASYPRINT_DLL_DIRECTORIES=%CONDA_PREFIX%\Library\bin
set FONTCONFIG_FILE=%CONDA_PREFIX%\Library\etc\fonts\fonts.conf
copy /Y "%CONDA_PREFIX%\Library\bin\expat.dll" "%CONDA_PREFIX%\DLLs\expat.dll" >nul 2>nul
REM Fix WeasyPrint DLL naming (conda ships without lib- prefix, WeasyPrint expects lib- prefix)
REM Uses hardlinks (not copies) to avoid double-loading DLLs
set _LIBBIN=%CONDA_PREFIX%\Library\bin
if exist "%_LIBBIN%\fontconfig-1.dll"     if not exist "%_LIBBIN%\libfontconfig-1.dll"     mklink /H "%_LIBBIN%\libfontconfig-1.dll"     "%_LIBBIN%\fontconfig-1.dll"     >nul 2>nul
if exist "%_LIBBIN%\gobject-2.0-0.dll"    if not exist "%_LIBBIN%\libgobject-2.0-0.dll"    mklink /H "%_LIBBIN%\libgobject-2.0-0.dll"    "%_LIBBIN%\gobject-2.0-0.dll"    >nul 2>nul
if exist "%_LIBBIN%\pango-1.0-0.dll"      if not exist "%_LIBBIN%\libpango-1.0-0.dll"      mklink /H "%_LIBBIN%\libpango-1.0-0.dll"      "%_LIBBIN%\pango-1.0-0.dll"      >nul 2>nul
if exist "%_LIBBIN%\pangoft2-1.0-0.dll"   if not exist "%_LIBBIN%\libpangoft2-1.0-0.dll"   mklink /H "%_LIBBIN%\libpangoft2-1.0-0.dll"   "%_LIBBIN%\pangoft2-1.0-0.dll"   >nul 2>nul
if exist "%_LIBBIN%\pangocairo-1.0-0.dll" if not exist "%_LIBBIN%\libpangocairo-1.0-0.dll" mklink /H "%_LIBBIN%\libpangocairo-1.0-0.dll" "%_LIBBIN%\pangocairo-1.0-0.dll" >nul 2>nul
if exist "%_LIBBIN%\harfbuzz.dll"         if not exist "%_LIBBIN%\libharfbuzz-0.dll"        mklink /H "%_LIBBIN%\libharfbuzz-0.dll"        "%_LIBBIN%\harfbuzz.dll"         >nul 2>nul
if exist "%_LIBBIN%\expat.dll"            if not exist "%_LIBBIN%\libexpat.dll"             mklink /H "%_LIBBIN%\libexpat.dll"             "%_LIBBIN%\expat.dll"            >nul 2>nul
if exist "%_LIBBIN%\glib-2.0-0.dll"       if not exist "%_LIBBIN%\libglib-2.0-0.dll"       mklink /H "%_LIBBIN%\libglib-2.0-0.dll"       "%_LIBBIN%\glib-2.0-0.dll"       >nul 2>nul
python -m frontend_dash.run_vnext
echo.
echo Server stopped. You can close this window.
pause
