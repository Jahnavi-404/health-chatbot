import streamlit as st
from api_utils.openfda_api import get_drug_label_data, get_drug_event_data

# Streamlit Web App UI
st.title("Health Chatbot - Drug Information")
st.markdown("⚠️ **Enter correct spelling of the drug for accurate results.**")

# Use a unique key
drug_name = st.text_input("Enter drug name:", key="drug_input")



if drug_name:
    # Fetch Drug Label Data
    label_data = get_drug_label_data(drug_name)
    st.write(f"**Drug Label Information for {drug_name}:**")
    st.write(label_data)
    
    # Fetch Adverse Event Data (Side Effects)
    event_data = get_drug_event_data(drug_name)
    st.write(f"**Reported Side Effects for {drug_name}:**")
    st.write(event_data)
