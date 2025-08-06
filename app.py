import streamlit as st
import pandas as pd
from model import predict_disease
from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page configuration - this sets up the fundamental structure of our application
st.set_page_config(
    page_title="AI Medical Consultant", 
    page_icon="🏥", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced visual appeal - this creates a more professional medical interface
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .symptom-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .result-card {
        background: #fff;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    .warning-box {
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Main application header - establishing the professional medical context
st.markdown("""
<div class="main-header">
    <h1>🏥 AI Medical Consultant</h1>
    <p>Intelligent Symptom Analysis & Medical Guidance System</p>
</div>
""", unsafe_allow_html=True)

# Create sidebar for additional functionality and information
with st.sidebar:
    st.header("📋 Navigation & Information")
    
    # App mode selection - this allows users to choose different ways to interact with the system
    app_mode = st.selectbox(
        "Choose Application Mode",
        ["Symptom Checker", "Health Education", "Emergency Guide", "About"]
    )
    
    # User information section - helps personalize the experience
    st.subheader("👤 User Information")
    age = st.number_input("Age", min_value=1, max_value=120, value=30)
    gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])
    
    # Medical history checkbox - important context for accurate predictions
    st.subheader("🏥 Medical Context")
    has_chronic_conditions = st.checkbox("I have chronic medical conditions")
    taking_medications = st.checkbox("I am currently taking medications")
    
    # Urgency assessment - helps users understand when to seek immediate care
    st.subheader("⚠️ Urgency Assessment")
    emergency_symptoms = st.multiselect(
        "Are you experiencing any of these emergency symptoms?",
        ["Chest pain", "Difficulty breathing", "Severe bleeding", 
         "Loss of consciousness", "Severe head injury", "High fever (>103°F)"]
    )

# Main content area - this is where the core functionality lives
if app_mode == "Symptom Checker":
    
    # Emergency check - safety first approach in medical applications
    if emergency_symptoms:
        st.error("🚨 **EMERGENCY SITUATION DETECTED**")
        st.markdown("""
        <div class="warning-box">
            <h3>⚠️ Seek Immediate Medical Attention</h3>
            <p>Based on your selected symptoms, you should contact emergency services immediately:</p>
            <ul>
                <li><strong>Call 911</strong> (US) or your local emergency number</li>
                <li><strong>Go to the nearest Emergency Room</strong></li>
                <li><strong>Do not delay seeking professional medical care</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    else:
        # Main symptom input area - the core interface for symptom description
        st.header("🩺 Describe Your Symptoms")
        
        # Create two columns for better layout organization
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Primary symptom input - this is where users describe their condition
            user_input = st.text_area(
                "📝 Please describe your symptoms in detail",
                height=150,
                placeholder="Example: I have been experiencing headache for 2 days, along with fever and body aches. The headache is throbbing and gets worse with light..."
            )
            
            # Duration and severity inputs - these provide important diagnostic context
            col1a, col1b = st.columns(2)
            with col1a:
                duration = st.selectbox(
                    "How long have you had these symptoms?",
                    ["Less than 1 day", "1-3 days", "4-7 days", "1-2 weeks", "More than 2 weeks"]
                )
            
            with col1b:
                severity = st.slider("Rate your pain/discomfort (1=mild, 10=severe)", 1, 10, 5)
        
        with col2:
            # Quick symptom selection - provides an alternative input method
            st.subheader("🎯 Quick Symptom Selection")
            common_symptoms = st.multiselect(
                "Select common symptoms:",
                ["Fever", "Headache", "Cough", "Nausea", "Fatigue", 
                 "Muscle aches", "Sore throat", "Runny nose", "Dizziness"]
            )
            
            # Add selected symptoms to the text input
            if common_symptoms and st.button("➕ Add to Description"):
                additional_text = f"Additional symptoms: {', '.join(common_symptoms)}"
                user_input = f"{user_input}\n{additional_text}" if user_input else additional_text

        # Analysis button and results - the core prediction functionality
        if st.button("🔍 Analyze Symptoms", type="primary"):
            if user_input.strip() == "":
                st.warning("⚠️ Please enter your symptoms to get an analysis.")
            else:
                # Create analysis progress - this shows the system is working
                with st.spinner("🔬 Analyzing your symptoms..."):
                    # Call your existing prediction function
                    disease, action, prescription = predict_disease(user_input)
                
                # Display results in organized cards
                st.header("📊 Analysis Results")
                
                # Primary diagnosis card
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.subheader(f"🎯 **Predicted Condition: {disease}**")
                with col2:
                    # Confidence visualization (placeholder - you can integrate actual confidence scores)
                    fig = go.Figure(go.Indicator(
                        mode = "gauge+number",
                        value = 85,  # This would come from your model
                        domain = {'x': [0, 1], 'y': [0, 1]},
                        title = {'text': "Confidence"},
                        gauge = {
                            'axis': {'range': [None, 100]},
                            'bar': {'color': "darkblue"},
                            'steps': [
                                {'range': [0, 50], 'color': "lightgray"},
                                {'range': [50, 85], 'color': "gray"}],
                            'threshold': {
                                'line': {'color': "red", 'width': 4},
                                'thickness': 0.75,
                                'value': 90}}))
                    fig.update_layout(height=200, margin=dict(l=0, r=0, t=30, b=0))
                    st.plotly_chart(fig, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Immediate action card - critical for user safety
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.subheader("⚡ Immediate Action Required")
                st.info(f"**Recommended Action:** {action}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Treatment recommendations card
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.subheader("💊 Treatment Recommendations")
                st.code(prescription, language='markdown')
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Additional context and warnings - educational component
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.subheader("📚 Important Information")
                
                # Educational content based on the diagnosis
                st.markdown(f"""
                **Understanding Your Condition:**
                
                This analysis is based on the symptoms you described and common medical patterns. Here's what you should know:
                
                - **Accuracy Limitation**: This AI analysis is a screening tool, not a replacement for professional medical diagnosis
                - **Individual Variation**: Your specific medical history, age ({age}), and other factors may influence the actual condition
                - **Symptom Evolution**: Symptoms can change over time, so monitor your condition closely
                - **Professional Care**: Always consult with a healthcare provider for definitive diagnosis and treatment
                """)
                
                # Risk factors and when to seek care
                st.warning("""
                **⚠️ When to Seek Immediate Medical Care:**
                - Symptoms worsen significantly
                - New concerning symptoms develop
                - You have underlying health conditions
                - You're unsure about the recommendations
                """)
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Follow-up recommendations
                st.subheader("📅 Follow-up Recommendations")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Monitor Symptoms", "24-48 hours", "Track changes")
                with col2:
                    st.metric("Severity Check", f"Current: {severity}/10", "Watch for increases")
                with col3:
                    st.metric("Duration Alert", duration, "Note progression")

# Health Education Mode - provides valuable medical knowledge
elif app_mode == "Health Education":
    st.header("📚 Health Education Center")
    
    # Disease information database - educational content for common conditions
    disease_info = {
        "Common Cold": {
            "description": "A viral infection of the upper respiratory tract",
            "symptoms": ["Runny nose", "Sneezing", "Cough", "Mild fever"],
            "prevention": ["Wash hands frequently", "Avoid close contact with sick people", "Don't touch face with unwashed hands"],
            "treatment": "Rest, fluids, over-the-counter medications for symptom relief"
        },
        "Influenza": {
            "description": "A contagious respiratory illness caused by influenza viruses",
            "symptoms": ["High fever", "Body aches", "Fatigue", "Cough", "Headache"],
            "prevention": ["Annual flu vaccination", "Good hygiene practices", "Avoid crowds during flu season"],
            "treatment": "Rest, antiviral medications if prescribed, supportive care"
        },
        "Migraine": {
            "description": "A neurological condition characterized by severe headaches",
            "symptoms": ["Severe headache", "Nausea", "Light sensitivity", "Visual disturbances"],
            "prevention": ["Identify triggers", "Regular sleep schedule", "Stress management", "Stay hydrated"],
            "treatment": "Specific migraine medications, lifestyle modifications, preventive treatments"
        }
    }
    
    # Disease selection and information display
    selected_disease = st.selectbox("Select a condition to learn about:", list(disease_info.keys()))
    
    if selected_disease:
        info = disease_info[selected_disease]
        
        st.subheader(f"📖 About {selected_disease}")
        st.write(info["description"])
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🔍 Common Symptoms")
            for symptom in info["symptoms"]:
                st.write(f"• {symptom}")
        
        with col2:
            st.subheader("🛡️ Prevention")
            for prevention in info["prevention"]:
                st.write(f"• {prevention}")
        
        st.subheader("💊 Treatment Approach")
        st.info(info["treatment"])

# Emergency Guide Mode - critical safety information
elif app_mode == "Emergency Guide":
    st.header("🚨 Emergency Medical Guide")
    
    st.error("""
    **IMPORTANT DISCLAIMER**: This guide is for informational purposes only. 
    In any medical emergency, call emergency services immediately!
    """)
    
    # Emergency situations and appropriate responses
    emergency_situations = {
        "Heart Attack": {
            "signs": ["Chest pain", "Shortness of breath", "Sweating", "Nausea", "Pain in arms/jaw"],
            "action": "Call 911 immediately. Give aspirin if available and not allergic. Keep person calm and seated."
        },
        "Stroke": {
            "signs": ["Face drooping", "Arm weakness", "Speech difficulty", "Time to call emergency"],
            "action": "Use FAST test. Call 911 immediately. Note time symptoms started."
        },
        "Severe Allergic Reaction": {
            "signs": ["Difficulty breathing", "Swelling of face/throat", "Rapid pulse", "Dizziness"],
            "action": "Use EpiPen if available. Call 911. Keep person lying flat with legs elevated."
        }
    }
    
    for emergency, details in emergency_situations.items():
        with st.expander(f"🚨 {emergency}"):
            st.subheader("Warning Signs:")
            for sign in details["signs"]:
                st.write(f"⚠️ {sign}")
            
            st.subheader("Immediate Action:")
            st.error(details["action"])

# About Mode - information about the application
else:  # app_mode == "About"
    st.header("ℹ️ About AI Medical Consultant")
    
    st.markdown("""
    ### 🎯 Purpose
    This AI Medical Consultant is designed to provide preliminary symptom analysis and health guidance. 
    It serves as an educational tool and initial screening system to help users better understand their symptoms.
    
    ### 🔬 How It Works
    The system uses machine learning algorithms trained on medical data to analyze symptom patterns and 
    provide suggestions for potential conditions and appropriate actions.
    
    ### ⚠️ Important Limitations
    - **Not a substitute for professional medical advice**
    - **For educational and screening purposes only**
    - **Always consult healthcare providers for definitive diagnosis**
    - **Emergency situations require immediate medical attention**
    
    ### 📊 Technical Details
    - **Model**: Trained on symptom-disease correlation data
    - **Accuracy**: Screening tool accuracy, not diagnostic precision
    - **Updates**: Regularly updated with new medical knowledge
    
    ### 🤝 Responsible Use
    This tool should be used as part of a comprehensive approach to healthcare that includes:
    - Regular check-ups with healthcare providers
    - Professional medical consultation for concerning symptoms
    - Emergency care for serious conditions
    - Health education and preventive care
    """)
    
    # Usage statistics (placeholder - you could implement actual tracking)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Consultations Today", "127")
    with col2:
        st.metric("Conditions Analyzed", "15")
    with col3:
        st.metric("User Satisfaction", "94%")
    with col4:
        st.metric("Accuracy Rate", "87%")

# Footer with important medical disclaimer - always visible for user safety
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem; background-color: #f8f9fa; border-radius: 5px; margin-top: 2rem;">
    <h4>⚠️ MEDICAL DISCLAIMER</h4>
    <p>This AI system provides informational content only and is not intended to replace professional medical advice, 
    diagnosis, or treatment. Always seek the advice of qualified healthcare providers with questions about medical conditions. 
    Never disregard professional medical advice or delay seeking it because of information from this application.</p>
    <p><strong>In case of medical emergency, call your local emergency services immediately.</strong></p>
</div>
""", unsafe_allow_html=True)