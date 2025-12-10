# Django Server Startup Script
# This script ensures a clean server start every time

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Django Sales Dashboard - Server Start" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Kill all Python processes
Write-Host "[1/4] Stopping any running Python processes..." -ForegroundColor Yellow
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Sleep -Seconds 1

# Delete ALL cache files
Write-Host "[2/4] Clearing Python cache files..." -ForegroundColor Yellow
Get-ChildItem -Path . -Include "*.pyc","__pycache__" -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force

# Wait for cleanup
Write-Host "[3/4] Preparing environment..." -ForegroundColor Yellow
Start-Sleep -Seconds 2

# Set environment variable to prevent bytecode generation
$env:PYTHONDONTWRITEBYTECODE = "1"

# Start server
Write-Host "[4/4] Starting Django server..." -ForegroundColor Green
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  Server running at: http://127.0.0.1:8000/" -ForegroundColor Green
Write-Host "  Press CTRL+C to stop the server" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

# Start server with no bytecode generation
& ".\venv\Scripts\python.exe" manage.py runserver
