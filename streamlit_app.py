import pickle
import numpy as np
import streamlit as st

# Load trained model
breast_disease_model = pickle.load(open("breast_cancer_model.sav", 'rb'))

# Set page config
st.set_page_config(page_title="Breast Disease App", layout="wide")

# Create Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Welcome", "🔬 Diagnosis", "🩺 Recommendations", "❓ FAQ"])

# ========== TAB 1: WELCOME ==========
with tab1:
    st.title("Welcome to the Breast Disease Prediction App")
    st.markdown("""
    ### 👋 Hello!
    This application uses a trained machine learning model to assist in the **early detection of breast cancer** based on tumor characteristics.

    #### 📌 What You Can Do Here:
    - Enter tumor measurements under the **Diagnosis** tab.
    - Get instant prediction results (Malignant or Benign).
    - Read personalized health **Recommendations**.
    - Explore common **FAQs** related to breast health.

    #### 🧠 Disclaimer:
    This app is for educational and informational purposes only and does not replace professional medical advice.
    """)

# ========== TAB 2: DIAGNOSIS ==========
with tab2:
    st.header("Breast Cancer Diagnosis Tool")

    # Input Fields
    col1, col2, col3 = st.columns(3)

    with col1:
        radius_mean = st.number_input('Mean Radius')
    with col2:
        texture_mean = st.number_input('Mean Texture')
    with col3:
        perimeter_mean = st.number_input('Mean Perimeter')
    with col1:
        area_mean = st.number_input('Mean Area')
    with col2:
        smoothness_mean = st.number_input('Mean Smoothness')
    with col3:
        compactness_mean = st.number_input('Mean Compactness')
    with col1:
        concavity_mean = st.number_input('Mean Concavity')
    with col2:
        concave_points_mean = st.number_input('Mean Concave Points')
    with col3:
        symmetry_mean = st.number_input('Mean Symmetry')
    with col1:
        fractal_dimension_mean = st.number_input('Mean Fractal Dimension')

    with col2:
        radius_se = st.number_input('Radius Error')
    with col3:
        texture_se = st.number_input('Texture Error')
    with col1:
        perimeter_se = st.number_input('Perimeter Error')
    with col2:
        area_se = st.number_input('Area Error')
    with col3:
        smoothness_se = st.number_input('Smoothness Error')
    with col1:
        compactness_se = st.number_input('Compactness Error')
    with col2:
        concavity_se = st.number_input('Concavity Error')
    with col3:
        concave_points_se = st.number_input('Concave Points Error')
    with col1:
        symmetry_se = st.number_input('Symmetry Error')
    with col2:
        fractal_dimension_se = st.number_input('Fractal Dimension Error')

    with col3:
        radius_worst = st.number_input('Worst Radius')
    with col1:
        texture_worst = st.number_input('Worst Texture')
    with col2:
        perimeter_worst = st.number_input('Worst Perimeter')
    with col3:
        area_worst = st.number_input('Worst Area')
    with col1:
        smoothness_worst = st.number_input('Worst Smoothness')
    with col2:
        compactness_worst = st.number_input('Worst Compactness')
    with col3:
        concavity_worst = st.number_input('Worst Concavity')
    with col1:
        concave_points_worst = st.number_input('Worst Concave Points')
    with col2:
        symmetry_worst = st.number_input('Worst Symmetry')
    with col3:
        fractal_dimension_worst = st.number_input('Worst Fractal Dimension')

    user_input = [
        radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
        compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,
        radius_se, texture_se, perimeter_se, area_se, smoothness_se,
        compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
        radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst,
        compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst
    ]

    diagnosis_result = ''
    if st.button("Diagnose"):
        user_input = [float(x) for x in user_input]
        prediction = breast_disease_model.predict([user_input])
        diagnosis_result = '🟢 No Breast Cancer Detected' if prediction[0] == 1 else '🔴 Suffering from Breast Cancer'
        st.success(diagnosis_result)

# ========== TAB 3: RECOMMENDATIONS ==========
with tab3:
    st.header("Health & Lifestyle Recommendations")

    st.markdown("""
    ### ✅ For Everyone:
    - Conduct monthly **self-breast exams**.
    - Schedule regular **mammograms** and **clinical check-ups**.
    - **Exercise regularly** (30+ minutes/day).
    - Eat a **balanced diet** (high in fiber, low in processed foods).
    - Avoid **smoking** and **limit alcohol** consumption.

    ### 🧠 If Diagnosed:
    - **Seek professional medical guidance immediately.**
    - Discuss possible treatments: **surgery, chemo, radiation, targeted therapy**.
    - Join a **support group** or get **mental health counseling**.
    - Involve family and friends in your care process.

    ### 🧬 For High-Risk Individuals:
    - Consider **genetic testing**.
    - Maintain a record of your **family medical history**.
    - Consult a doctor for personalized screening schedules.
    """)

# ========== TAB 4: FAQ ==========
with tab4:
    st.header("Frequently Asked Questions (FAQ)")

    with st.expander("❓ What is breast cancer?"):
        st.write("Breast cancer is a disease where cells in the breast grow uncontrollably, forming tumors that may be malignant (cancerous) or benign (non-cancerous).")

    with st.expander("❓ Is this app a replacement for a doctor?"):
        st.write("No. This app is for informational and educational purposes only. Always consult a medical professional for actual diagnosis and treatment.")

    with st.expander("❓ What data does the model use?"):
        st.write("The model uses features like radius, texture, perimeter, area, smoothness, and other tumor characteristics measured through clinical testing.")

    with st.expander("❓ What does a 'malignant' result mean?"):
        st.write("It means the model has found characteristics that are commonly associated with cancerous tumors. You should consult a physician immediately.")

    with st.expander("❓ Can I use this for someone else’s report?"):
        st.write("Yes, but make sure you're entering the correct data. For accurate diagnosis, the data should be from a verified medical test.")
