import os
from bardapi import Bard
import requests
import json
from bardapi.constants import SESSION_HEADERS
#from bardapi import BardCookies


# Definindo o valor do token

token = "aQgVs0Xv7gO_xUjYbTLbZEabDTAv0N7dqHZKxrotsBzBXjb7HZW1zPci4jO7bKPg_vHrhA."


# instância da classe Bard com a sessão contendo os cookies
bard = Bard(token=token, session=session)

# Função para gerar notícias usando o BARD API
def generate_bard_news(user):
    response = bard.get_answer(f"Não crie nada além do que uma curta mensagem (sem explicações adicionais comuns do ('Bard'), como se fosse o banco Santander, para cada {user['name']} acerca da importância dos investimentos (máximo de 100 caracteres)")
    return response['content'].strip()

# Função para obter dados do usuário
def get_user(id):
    response = requests.get(f'{sdw2023_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

# Obtendo informações dos usuários
users = [user for id in user_ids if (user := get_user(id)) is not None]

# Gerando notícias usando o BARD API e adicionando as informações do usuário
for user in users:
    news = generate_bard_news(user)
    print(news)
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })

# Imprima os usuários atualizados
print(json.dumps(users, indent=2))

