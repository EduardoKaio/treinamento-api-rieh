import pandas as pd
import requests

from auth import obter_token

base_url = "https://treinamento.administrativo.rieh.nees.ufal.br/"

def cadastrar_aluno(aluno, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    payload = {
        "person": {
            "name": aluno["Nome"],
            "cpf": aluno["CPF"],
            "email": aluno["E-mail"],
            "address": {
                "country_state": aluno["ID Estado"],
                "city": aluno["Cidade"]
            }
        },
        "school": aluno["ID Escola"],
        "serie": aluno["Série"]
    }

    response = requests.post(base_url + "/api/students/", json=payload, headers=headers)

    if response.status_code == 201:
        print(f"Aluno {aluno['Nome']} cadastrado com sucesso.")
    else:
        print(f"Erro ao cadastrar {aluno['Nome']}: {response.text}")

def realizar_cadastros():
    df_alunos = pd.read_csv("data/insercao_alunos.csv")
    token = obter_token()

    for _, aluno in df_alunos.iterrows():
        cadastrar_aluno(aluno, token)

realizar_cadastros()