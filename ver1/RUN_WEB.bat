@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo Starting BI304 Thammasat Data Storytelling local preview...
where python >nul 2>&1
if %errorlevel% equ 0 (
    start "BI304 Local Server" /b python -m http.server 8000 --directory "%~dp0"
    timeout /t 2 /nobreak >nul
    start "" "http://localhost:8000/index.html"
    echo.
    echo Local preview: http://localhost:8000/index.html
    echo Keep the server window/process running while testing.
) else (
    where py >nul 2>&1
    if %errorlevel% equ 0 (
        start "BI304 Local Server" /b py -m http.server 8000 --directory "%~dp0"
        timeout /t 2 /nobreak >nul
        start "" "http://localhost:8000/index.html"
        echo.
        echo Local preview: http://localhost:8000/index.html
    ) else (
        echo Python was not found. Opening the file directly; some interactive features may not work.
        start "" "%~dp0index.html"
    )
)
echo.
pause
