# AI Medical Consultant - PowerShell Startup Script

Write-Host "========================================"
Write-Host "   AI Medical Consultant - Starting" -ForegroundColor Cyan
Write-Host "========================================"
Write-Host ""

# Check dependencies
Write-Host "Checking dependencies..." -ForegroundColor Yellow
try {
    python -c "import streamlit, plotly, pandas, sklearn; print('✅ All dependencies ready!')"
    if ($LASTEXITCODE -ne 0) {
        throw "Dependencies check failed"
    }
} catch {
    Write-Host "❌ Missing dependencies. Installing..." -ForegroundColor Red
    pip install -r requirements.txt
}

Write-Host ""
Write-Host "Starting AI Medical Consultant..." -ForegroundColor Green
Write-Host "Open your browser to: http://localhost:8501" -ForegroundColor White
Write-Host ""
Write-Host "⚠️  MEDICAL DISCLAIMER: This tool is for educational purposes only." -ForegroundColor Yellow
Write-Host "   Always consult healthcare professionals for medical advice." -ForegroundColor Yellow
Write-Host ""

# Start the application
streamlit run app.py
