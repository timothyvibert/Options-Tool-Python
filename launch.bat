@echo off
title Alpha Engine — Options Builder
echo Starting Options Builder...
echo.
call conda activate options-tool
start "" http://127.0.0.1:8051/v2
python -m frontend_dash.run_vnext
pause
