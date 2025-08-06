@echo off
echo ========================================
echo    AI Medical Consultant - Starting
echo ========================================
echo.
echo Checking dependencies...
python -c "import streamlit, plotly, pandas, sklearn; print('✅ All dependencies ready!')"
if %errorlevel% neq 0 (
    echo ❌ Missing dependencies. Installing...
    pip install -r requirements.txt
)

echo.
echo Starting AI Medical Consultant...
echo Open your browser to: http://localhost:8501
echo.
echo ⚠️  MEDICAL DISCLAIMER: This tool is for educational purposes only.
echo    Always consult healthcare professionals for medical advice.
echo.

streamlit run app.py
