# RIEH - Scripts de Automação

Este repositório contém scripts em Python para automatizar processos relacionados à plataforma **RIEH**, como autenticação, cadastro de alunos e clonagem de itinerários escolares. Os scripts utilizam a API RIEH em ambiente de treinamento.

## Estrutura dos Arquivos

### `auth.py`
Responsável por autenticar na API e obter um token de acesso.

- Carrega as variáveis de ambiente `RIEH_CPF` e `RIEH_SENHA` do arquivo `.env`.
- Realiza uma requisição à API de login e retorna o token de autenticação necessário para os outros scripts.

### `gerar_alunos.py`
Gera dados fictícios de alunos utilizando a biblioteca Faker.

- Cria um arquivo CSV (`data/insercao_alunos.csv`) com um número configurável de alunos.
- Os dados incluem: nome, CPF, e-mail, cidade, estado, escola e série.
- Pode ser utilizado para testes ou para simulações de cadastros em massa.

### `cadastro_alunos.py`
Lê os dados dos alunos do CSV gerado por `gerar_alunos.py` e realiza o cadastro dos alunos na API RIEH.

- Utiliza o token obtido via `auth.py`.
- Envia os dados de cada aluno com os campos obrigatórios formatados conforme a API.
- Informa no console o sucesso ou falha no cadastro de cada aluno.

### `clonagem_itinerario.py`
Realiza a clonagem de um itinerário escolar existente para uma ou mais escolas.

- Requer o ID do itinerário de origem e uma lista de códigos INEP das escolas de destino.
- Busca os IDs internos das escolas na API com base nos códigos INEP.
- Clona o itinerário usando o endpoint apropriado da API.
- Os resultados são exibidos no terminal.

### `desativa_alunos.py`
Desativa alunos cadastrados na plataforma RIEH.

- Lê uma lista de CPFs do arquivo CSV (`data/desativar_alunos.csv`).
- Para cada CPF, busca o aluno correspondente na API.
- Atualiza o status do aluno para "formado" (`is_formed: True`) via requisição PATCH.
- Informa no console o sucesso ou falha na desativação

---

## Requisitos

- Python 3.8+
- Arquivo `.env` com as seguintes variáveis:

```env
RIEH_CPF=seu_usuario
RIEH_SENHA=sua_senha
```

### Instalação das dependências

```bash
pip install requests python-dotenv pandas faker
```

---

## Observações

- Todos os testes são realizados no ambiente de treinamento da API.
- Certifique-se de ajustar o `id_itinerario_origem` em `clonagem_itinerario.py` conforme necessário.
- O número de alunos gerados pode ser ajustado na variável `NUMERO_ALUNOS` em `gerar_alunos.py`.

---

## Licença

Uso interno para fins de treinamento e testes com a plataforma RIEH.