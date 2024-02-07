from urllib import response
import requests
import streamlit as st
import json

BASE_URL = "http://172.214.88.215"

def dados_inadimplencia(body):
    url = f'{BASE_URL}/predict?model=default_propensity'
    headers = {'Content-Type': 'application/json'}  # Adicione os cabeçalhos JSON
    try:
        resposta = requests.post(url, data=json.dumps(body), headers=headers)
        resposta.raise_for_status()  # Lança uma exceção para erros HTTP
        return resposta.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro na requisição: {e}")
        return None

def ui():
    # ... (seu código permanece o mesmo)

    if st.button('Executar'):
        retorno = dados_inadimplencia(body)
        if retorno is not None:
            st.write(retorno)

ui()
