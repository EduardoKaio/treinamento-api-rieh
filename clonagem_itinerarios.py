import requests
from auth import obter_token

# Lista de códigos INEP das escolas para as quais o itinerário será clonado
codigos_inep = [24000019, 24000027]

# Base da URL da API
base_url = "https://treinamento.administrativo.rieh.nees.ufal.br"

# Lista onde serão armazenados os IDs das escolas encontradas
ids_escolas = []

# ID do itinerário que será clonado (você deve substituir esse valor)
id_itinerario_origem = 81

def buscar_ids_escolas(codigos, token):
    
    # Busca os IDs das escolas a partir de uma lista de códigos INEP.
    
    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json"
    }

    for codigo in codigos:
        url = f"{base_url}/api/schools/?code={codigo}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            if results:
                escola_id = results[0].get("id")
                ids_escolas.append(escola_id)
            else:
                print(f"Nenhum resultado encontrado para o código {codigo}")
        else:
            print(f"Erro ao buscar o código {codigo}: {response.status_code} - {response.text}")

def clonar_itinerario(id_itinerario, escolas_ids, token):
    
    # Clona um itinerário existente para várias escolas.
    
    url = f"{base_url}/api/itineraries/{id_itinerario}/clone/"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "id_schools": escolas_ids
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200 or response.status_code == 201:
        print("Itinerário clonado com sucesso para as escolas:", escolas_ids)
    else:
        print(f"Erro ao clonar itinerário: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Obter token de autenticação
    token = obter_token()

    # Buscar IDs das escolas usando os códigos INEP
    buscar_ids_escolas(codigos_inep, token)
    print("IDs das escolas encontrados:", ids_escolas)

    # Clonar o itinerário para as escolas encontradas
    # Certifique-se de alterar o valor de id_itinerario_origem acima
    clonar_itinerario(id_itinerario_origem, ids_escolas, token)
