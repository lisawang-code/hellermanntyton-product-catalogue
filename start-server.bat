@echo off
chcp 65001 >nul
echo ==========================================
echo  HellermannTyton Product Catalogue
echo  Local Server Launcher
echo ==========================================
echo.
echo Starting local server on http://localhost:8088
echo.
echo Please keep this window open while using the catalogue.
echo Press Ctrl+C to stop the server.
echo.
start http://localhost:8088
python -m http.server 8088
