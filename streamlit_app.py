from urllib import response
import requests
import streamlit as st
import json


BASE_URL = "http://172.214.88.215"

def dados_inadimplencia(body):
    body_json = json.dumps(body)
    url = f'{BASE_URL}/predict?model=default_propensity'
    resposta = requests.post(url, data=body_json)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return "erro"
    
def ui():
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">', unsafe_allow_html=True)

    st.title('FINTECH QUANTUMFINANCE')
    occupancy_type = st.text_input('Insira o occupancy_type:')
    co_applicant_credit_type = st.text_input('Insira o co_applicant_credit_type:')
    credit_Score = st.text_input('Insira o Credit_Score:')
    lvt = st.text_input('Insira o LVT:')
    loan_purpose = st.text_input('Insira o loan_purpose:')
    dtir1 = st.text_input('Insira o dtir1:')
    property_value = st.text_input('Insira o property_value:')
    submission_of_application = st.text_input('Insira o submission_of_application:')
    approv_in_adv = st.text_input('Insira o approv_in_adv:')
    income = st.text_input('Insira o income:')

    body = {
        'occupancy_type': occupancy_type,
        'co_applicant_credit_type': co_applicant_credit_type,
        'Credit_Score': credit_Score,
        'lvt': lvt,
        'loan_purpose': loan_purpose,
        'dtir1': dtir1,
        'property_value': property_value,
        'submission_of_application': submission_of_application,
        'approv_in_adv': approv_in_adv,
        'income': income
    }
    
    if st.button('Executar'):
        retorno = dados_inadimplencia(body)
        if retorno is not None:
            st.write(retorno)

ui()