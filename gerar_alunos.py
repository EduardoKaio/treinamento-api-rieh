from faker import Faker
import csv
import random

fake = Faker('pt_BR')

NUMERO_ALUNOS = 2

CIDADES = ['Natal']
ESCOLAS = [8413, 8417]
SERIES = [2]

with open('data/insercao_alunos.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Nome', 'CPF', 'E-mail', 'ID Estado', 'Cidade', 'ID Escola', 'Série']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for _ in range(NUMERO_ALUNOS):
        nome = fake.name()
        cpf = fake.cpf()
        email = fake.email()
        cidade = random.choice(CIDADES)
        escola = random.choice(ESCOLAS)
        serie = random.choice(SERIES)

        writer.writerow({
            'Nome': nome,
            'CPF': cpf,
            'E-mail': email,
            'ID Estado': 20,
            'Cidade': cidade,
            'ID Escola': escola,
            'Série': serie
        })
