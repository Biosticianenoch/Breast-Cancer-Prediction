import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

breast_disease_model = pickle.load(open("breast_cancer_model.sav", 'rb'))

st.title("BREAST DISEASE PREDICTION")

# Input columns
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

# Create feature array
user_input = [
    radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
    compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,
    radius_se, texture_se, perimeter_se, area_se, smoothness_se,
    compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
    radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst,
    compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst
]

# Predict
breast_cancer_prediction = ''
if st.button('Diagnose'):
    user_input = [float(x) for x in user_input]
    prediction = breast_cancer_model.predict([user_input])
    breast_cancer_prediction = 'No Breast Cancer' if prediction[0] == 1 else 'SUFFERING FROM Breast Cancer'

st.success(breast_cancer_prediction)
