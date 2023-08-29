#Explorando IA Generativa em um Pipeline de ETL com Python

import pandas as pd

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'
df = pd.read_csv('SantanderDevWeek.csv')
user_ids = df['UserID'].tolist()
print(user_ids)
