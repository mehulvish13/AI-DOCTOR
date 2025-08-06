#!/usr/bin/env python3
"""
Test script for the AI Doctor application
"""

from model import predict_disease

def test_predictions():
    """Test the prediction function with various symptoms"""
    
    test_cases = [
        "fever cough fatigue",
        "chest pain shortness of breath",
        "headache nausea sensitivity to light",
        "persistent cough weight loss",
        "joint pain stiffness swelling"
    ]
    
    print("=== AI Doctor Test Results ===\n")
    
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

if __name__ == "__main__":
    test_predictions()
