from urllib import response
import requests
import streamlit as st
import json
import Pages.propensao_de_inadimplencia as page_ina
import Pages.clusterizacao_e_classificacao as page_clust

BASE_URL = "http://172.214.88.215"


def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

def ui():
    Page_cliente = st.sidebar.selectbox(
    'Menu', ['Menu Principal','Clusterização', 'Inadimplência'], 0)

    st.set_page_config("Streamlit Components Hub", "🏦", layout="wide")
    icon("🏦")
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">', unsafe_allow_html=True)

    st.title('FINTECH QUANTUMFINANCE')

    if Page_cliente == 'Clusterização':
        page_clust.customer_clustering()

    if Page_cliente == 'Inadimplência':
        page_ina.propensao_de_inadimplencia()

    if Page_cliente == 'Menu Principal':
        page_clust.customer_clustering()
    

ui()
