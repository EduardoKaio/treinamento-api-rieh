import os
import requests
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

base_url = "https://treinamento.administrativo.rieh.nees.ufal.br/"
url_token = base_url + "/api/token/"

def obter_token():
    username = os.getenv("RIEH_CPF")
    password = os.getenv("RIEH_SENHA")

    if not username or not password:
        raise ValueError("Variáveis de ambiente RIEH_CPF e RIEH_SENHA não estão definidas.")

    data = {"username": username, "password": password}
    response = requests.post(url_token, json=data)

    if response.status_code != 200:
        raise Exception(f"Erro ao obter token: {response.text}")

    return response.json().get("access")
