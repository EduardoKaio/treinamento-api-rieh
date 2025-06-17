import pandas as pd
import requests
import json
import re

from auth import obter_token

base_url = "https://treinamento.administrativo.rieh.nees.ufal.br"

def buscar_aluno_por_cpf(cpf, token):
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{base_url}/api/students/?person_cpf={cpf}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data["count"] > 0:
            return data["results"][0]
    return None

def desativar_aluno(aluno_data, token):
    aluno_id = aluno_data["id"]
    pessoa = aluno_data["person"]
    endereco = pessoa.get("address", {})

    payload = {
        "registration": aluno_data.get("registration", ""),
        "person": {
            "name": pessoa["name"],
            "email": pessoa["email"],
            "gender": pessoa.get("gender", ""),
            "address": {
                "country_state": endereco.get("country_state", 0),
                "city": endereco.get("city", ""),
            }
        },
        "school": aluno_data["school"],
        "serie": aluno_data["serie"],
        "is_formed": True,
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    url = f"{base_url}/api/students/{aluno_id}/"
    response = requests.patch(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"Aluno {pessoa['name']} desativado com sucesso.")
    else:
        print(f"Erro ao desativar {pessoa['name']}: {response.status_code} - {response.text}")

def desativar_alunos():
    df = pd.read_csv("data/desativar_alunos.csv")
    token = obter_token()

    for _, row in df.iterrows():
        cpf = row["CPF"].strip()
        aluno_data = buscar_aluno_por_cpf(cpf, token)
        if aluno_data:
            desativar_aluno(aluno_data, token)
        else:
            print(f"Aluno com CPF {cpf} não encontrado.")

desativar_alunos()
