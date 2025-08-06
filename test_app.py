#!/usr/bin/env python3
"""
Test script for the AI Doctor application - Enhanced UI Version
"""

from model import predict_disease
import plotly.graph_objects as go

def test_predictions():
    """Test the prediction function with various symptoms"""
    
    test_cases = [
        "fever cough fatigue",
        "chest pain shortness of breath",
        "headache nausea sensitivity to light",
        "persistent cough weight loss",
        "joint pain stiffness swelling"
    ]
    
    print("=== AI Doctor Enhanced UI Test Results ===\n")
    
    for i, symptoms in enumerate(test_cases, 1):
        try:
            disease, action, prescription = predict_disease(symptoms)
            print(f"Test {i}: {symptoms}")
            print(f"  Disease: {disease}")
            print(f"  Action: {action}")
            print(f"  Prescription: {prescription}")
            print("-" * 50)
        except Exception as e:
            print(f"Test {i} failed: {e}")
            print("-" * 50)

def test_ui_components():
    """Test UI components and dependencies"""
    
    print("\n=== UI Components Test ===")
    
    try:
        import streamlit
        print(f"✅ Streamlit: {streamlit.__version__}")
    except ImportError as e:
        print(f"❌ Streamlit import failed: {e}")
    
    try:
        import plotly
        print(f"✅ Plotly: {plotly.__version__}")
        
        # Test plotly gauge component
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 85,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Test Confidence"},
        ))
        print("✅ Plotly gauge component works")
        
    except ImportError as e:
        print(f"❌ Plotly import failed: {e}")
    
    try:
        import pandas
        print(f"✅ Pandas: {pandas.__version__}")
    except ImportError as e:
        print(f"❌ Pandas import failed: {e}")
    
    try:
        import sklearn
        print(f"✅ Scikit-learn: {sklearn.__version__}")
    except ImportError as e:
        print(f"❌ Scikit-learn import failed: {e}")

if __name__ == "__main__":
    test_ui_components()
    print("\n" + "="*60)
    test_predictions()
