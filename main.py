import pandas as pd
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()


# Your Account SID from twilio.com/console
account_sid = os.environ.get("ACCOUNT_SID")
# Your Auth Token from twilio.com/console
auth_token  = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to=os.environ.get("PHONE_TO"),
            from_=os.environ.get("PHONE_FROM"),
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)
