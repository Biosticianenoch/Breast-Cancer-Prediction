import pickle
import numpy as np
import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
from streamlit_extras.mention import mention
from streamlit_extras.badges import badge
from streamlit_extras.add_vertical_space import add_vertical_space

# Load model
breast_disease_model = pickle.load(open("breast_cancer_model1.sav", 'rb'))

# Page settings
st.set_page_config(page_title="Breast Cancer Disease Prediction", layout="wide")
st.markdown("""
    <style>
        .main {
            background-color: #F5F7FA;
        }
        .stTabs [data-baseweb="tab"] {
            font-size: 18px;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# Tabs
welcome_tab, diagnosis_tab, recommendations_tab, faq_tab = st.tabs(["🏠 Welcome", "🧪 Diagnosis", "💡 Recommendations", "📘 FAQ"])

# =================== WELCOME TAB ===================
with welcome_tab:
    colored_header("Welcome to Breast Disease Prediction App", description="Your Health Companion", color_name="blue-70")
    st.image("https://cdn.pixabay.com/photo/2017/02/09/23/27/doctor-2055220_1280.jpg", use_column_width=True)
    st.markdown("""
        #### 👩‍⚕️ About the App
        This AI-powered web application predicts the likelihood of breast cancer using clinical tumor characteristics.
        
        **Features:**
        - Accurate breast cancer prediction based on medical data
        - Personalized health and lifestyle recommendations
        - Easy-to-understand interface for non-medical users

        ⚠️ **Disclaimer:** This app is not a substitute for professional medical advice.
    """)
    badge(type="github", name="OpenAI")
    rain(emoji="🎗️", font_size=30, falling_speed=3, animation_length="infinite")

# =================== DIAGNOSIS TAB ===================
with diagnosis_tab:
    colored_header("Breast Cancer Diagnosis Tool", description="Input your tumor features", color_name="violet-60")

    with st.form("diagnosis_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            radius_mean = st.number_input('Mean Radius')
            area_mean = st.number_input('Mean Area')
            concavity_mean = st.number_input('Mean Concavity')
            radius_se = st.number_input('Radius Error')
            perimeter_se = st.number_input('Perimeter Error')
            compactness_se = st.number_input('Compactness Error')
            radius_worst = st.number_input('Worst Radius')
            area_worst = st.number_input('Worst Area')
            concavity_worst = st.number_input('Worst Concavity')
        with col2:
            texture_mean = st.number_input('Mean Texture')
            smoothness_mean = st.number_input('Mean Smoothness')
            concave_points_mean = st.number_input('Mean Concave Points')
            texture_se = st.number_input('Texture Error')
            area_se = st.number_input('Area Error')
            concavity_se = st.number_input('Concavity Error')
            texture_worst = st.number_input('Worst Texture')
            smoothness_worst = st.number_input('Worst Smoothness')
            concave_points_worst = st.number_input('Worst Concave Points')
        with col3:
            perimeter_mean = st.number_input('Mean Perimeter')
            compactness_mean = st.number_input('Mean Compactness')
            symmetry_mean = st.number_input('Mean Symmetry')
            smoothness_se = st.number_input('Smoothness Error')
            fractal_dimension_se = st.number_input('Fractal Dimension Error')
            symmetry_se = st.number_input('Symmetry Error')
            perimeter_worst = st.number_input('Worst Perimeter')
            symmetry_worst = st.number_input('Worst Symmetry')
            fractal_dimension_worst = st.number_input('Worst Fractal Dimension')

        submitted = st.form_submit_button("Diagnose")

        if submitted:
            user_input = [
                radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
                compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, 0.0,
                radius_se, texture_se, perimeter_se, area_se, smoothness_se,
                compactness_se, concavity_se, concave_points_mean, symmetry_se, fractal_dimension_se,
                radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst,
                compactness_mean, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst
            ]
            prediction = breast_disease_model.predict([user_input])
            result = '🟢 No Breast Cancer Detected' if prediction[0] == 1 else '🔴 Suffering from Breast Cancer'
            st.success(result)

# =================== RECOMMENDATIONS TAB ===================
with recommendations_tab:
    colored_header("Personalized Recommendations", description="Health Tips", color_name="green-70")
    st.markdown("""
    ### ✅ General Health Tips:
    - Perform **monthly breast self-exams**.
    - Eat a **balanced diet** with fruits, veggies, and fiber.
    - Engage in **30+ minutes of daily exercise**.
    - Avoid smoking and **limit alcohol consumption**.
    - Get **regular screenings** and follow-up exams.

    ### 🩺 For High-Risk Individuals:
    - Discuss **genetic testing** with your doctor.
    - Monitor family history of breast cancer.
    - Consider **more frequent screenings**.

    ### 🧠 Mental & Emotional Support:
    - Seek **therapy or counseling** if overwhelmed.
    - Join support groups for shared experiences.
    - Talk openly with trusted friends and family.
    """)

# =================== FAQ TAB ===================
with faq_tab:
    colored_header("FAQs", description="Your Questions Answered", color_name="gray-70")
    add_vertical_space(1)
    with st.expander("❓ What is breast cancer?"):
        st.write("Breast cancer is a condition in which cells in the breast grow out of control, forming malignant tumors.")
    with st.expander("❓ Can I rely solely on this app?"):
        st.write("No. This app is a supplemental tool and does not replace professional medical advice or diagnosis.")
    with st.expander("❓ How accurate is the model?"):
        st.write("The model has been trained on real-world data and shows strong predictive power but is not 100% accurate.")
    with st.expander("❓ What should I do after a positive result?"):
        st.write("Consult a licensed medical professional for proper diagnosis and treatment planning.")
    with st.expander("❓ Is my data safe?"):
        st.write("Yes. This app runs locally in your browser and does not transmit your data anywhere.")
