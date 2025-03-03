import os
import subprocess
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

# Imprimir as variáveis de ambiente para depuração
print("DB_HOST_PROD:", os.getenv("DB_HOST_PROD"))
print("DB_USER_PROD:", os.getenv("DB_USER_PROD"))
print("DB_PASS_PROD:", os.getenv("DB_PASS_PROD"))

# Rodar o comando DBT
subprocess.run(["dbt", "run"])