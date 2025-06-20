import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("mental_health_model.pkl")

st.set_page_config(page_title="Mental Health Risk Predictor")
st.title("🧠 Mental Health Risk Predictor")
st.markdown("This app predicts if a person is likely to seek mental health treatment based on their workplace conditions.")

# --- User Inputs ---
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
country = st.selectbox("Country", ["United States", "United Kingdom", "Canada", "Germany", "Other"])
state = st.text_input("State (2-letter code or 'Unknown')", "CA")
self_employed = st.selectbox("Are you self-employed?", ["Yes", "No"])
family_history = st.selectbox("Family history of mental illness?", ["Yes", "No"])
work_interfere = st.selectbox("Work interference due to mental health?", ["Never", "Rarely", "Sometimes", "Often"])
no_employees = st.selectbox("Company size", ["1-5", "6-25", "26-100", "100-500", "500-1000", "More than 1000"])
remote_work = st.selectbox("Do you work remotely?", ["Yes", "No"])
tech_company = st.selectbox("Is it a tech company?", ["Yes", "No"])
benefits = st.selectbox("Mental health benefits?", ["Yes", "No", "Don't know"])
care_options = st.selectbox("Care options provided?", ["Yes", "No", "Not sure"])
wellness_program = st.selectbox("Wellness program?", ["Yes", "No", "Don't know"])
seek_help = st.selectbox("Encouraged to seek help?", ["Yes", "No", "Don't know"])
anonymity = st.selectbox("Anonymous mental health support?", ["Yes", "No", "Don't know"])
leave = st.selectbox("Ease of taking leave?", ["Very easy", "Somewhat easy", "Somewhat difficult", "Very difficult", "Don't know"])
mental_health_consequence = st.selectbox("Consequence of mental health disclosure?", ["Yes", "No", "Maybe"])
phys_health_consequence = st.selectbox("Consequence of physical health disclosure?", ["Yes", "No", "Maybe"])
coworkers = st.selectbox("Can you talk to coworkers?", ["Yes", "No", "Some of them"])
supervisor = st.selectbox("Can you talk to supervisor?", ["Yes", "No", "Some of them"])
mental_health_interview = st.selectbox("Would you discuss in interview?", ["Yes", "No", "Maybe"])
phys_health_interview = st.selectbox("Discuss physical health in interview?", ["Yes", "No", "Maybe"])
mental_vs_physical = st.selectbox("Is mental health as important as physical?", ["Yes", "No", "Maybe"])
obs_consequence = st.selectbox("Observed negative consequence?", ["Yes", "No"])
age_group = st.selectbox("Age Group", ["Youth", "Adult", "Senior"])
support_score = st.slider("Support Score (0 = low support, 3 = high)", 0, 3, 1)

# --- Format input for model ---
input_dict = {
    "Gender": [gender],
    "Country": [country],
    "state": [state],
    "self_employed": [self_employed],
    "family_history": [family_history],
    "work_interfere": [work_interfere],
    "no_employees": [no_employees],
    "remote_work": [remote_work],
    "tech_company": [tech_company],
    "benefits": [benefits],
    "care_options": [care_options],
    "wellness_program": [wellness_program],
    "seek_help": [seek_help],
    "anonymity": [anonymity],
    "leave": [leave],
    "mental_health_consequence": [mental_health_consequence],
    "phys_health_consequence": [phys_health_consequence],
    "coworkers": [coworkers],
    "supervisor": [supervisor],
    "mental_health_interview": [mental_health_interview],
    "phys_health_interview": [phys_health_interview],
    "mental_vs_physical": [mental_vs_physical],
    "obs_consequence": [obs_consequence],
    "age_group": [age_group],
    "support_score": [support_score],  # numeric feature
}

input_df = pd.DataFrame(input_dict)

# --- Prediction ---
if st.button("Predict"):
    result = model.predict(input_df)[0]
    if result == 0:
       st.error("⚠️ The model predicts: Unlikely to seek treatment.")
       st.info("⚠️ While this model is trained on real-world survey data, the dataset is relatively small and imbalanced. As a result, predictions may sometimes favor the majority class (e.g., predicting 'Unlikely to seek treatment' more often). 🔁 Note: The model's accuracy and fairness can significantly improve if it's retrained on larger and more diverse datasets in the future.")

    else:
       st.success("✅ The model predicts: Likely to seek treatment.")
       st.info("⚠️ While this model is trained on real-world survey data, the dataset is relatively small and imbalanced. As a result, predictions may sometimes favor the majority class (e.g., predicting 'likely to seek treatment' more often). 🔁 Note: The model's accuracy and fairness can significantly improve if it's retrained on larger and more diverse datasets in the future.")
