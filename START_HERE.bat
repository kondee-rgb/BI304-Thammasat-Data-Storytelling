@echo off
chcp 65001 > nul
cls
echo ======================================================================
echo   BI304: 90 Years of Thammasat Data Scrollytelling ^& Storyboard
echo   Thammasat Business School (TBS) - Presentation Date: Oct 30
echo ======================================================================
echo.
echo [1/2] Checking environment...
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Python is installed.
    echo [2/2] Starting local HTTP server on port 8000 and opening browser...
    start "" /b python -m http.server 8000 --directory "%~dp0" >nul 2>&1
    timeout /t 2 /nobreak >nul
    start http://localhost:8000/index.html
) else (
    echo [2/2] Opening index.html directly in your default browser...
    start "" "%~dp0index.html"
)

echo.
echo ======================================================================
echo   Website opened successfully! You may minimize or close this window.
echo   - Web Scrollytelling: http://localhost:8000/index.html
echo   - Storyboard PDF: "%~dp0Storyboard_Thammasat_BI304.pdf"
echo   - Google Colab: "%~dp0BI304_Thammasat_Data_Storytelling.ipynb"
echo ======================================================================
pause
