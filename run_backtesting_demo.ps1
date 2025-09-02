# PowerShell script to run the backtesting demo
# Run this script by right-clicking and selecting "Run with PowerShell"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "🚀 BACKTESTING.PY ONE-CLICK DEMO LAUNCHER" -ForegroundColor Yellow
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "This will run the backtesting demo with Google stock data." -ForegroundColor White
Write-Host "The interactive plot will open in your browser." -ForegroundColor White
Write-Host ""
Write-Host "Press any key to start..." -ForegroundColor Green
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

Write-Host ""
Write-Host "🔄 Starting backtesting demo..." -ForegroundColor Yellow
Write-Host ""

try {
    # Check if Python is available
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Python is not installed or not in PATH" -ForegroundColor Red
        Write-Host "Please install Python 3.9+ and try again." -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
    
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
    
    # Run the demo script
    python demo_backtesting.py
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "✅ Demo completed successfully!" -ForegroundColor Green
    } else {
        Write-Host ""
        Write-Host "❌ Demo failed with exit code: $LASTEXITCODE" -ForegroundColor Red
    }
    
} catch {
    Write-Host ""
    Write-Host "❌ Error running demo: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Demo completed! Press Enter to exit..." -ForegroundColor Yellow
Write-Host "============================================================" -ForegroundColor Cyan
Read-Host
