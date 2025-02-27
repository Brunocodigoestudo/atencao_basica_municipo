import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carregar variáveis de ambiente
load_dotenv()

# Carregar as variáveis de conexão
DB_HOST = os.getenv("DB_HOST_PROD") 
DB_PORT = os.getenv("DB_PORT_PROD") 
DB_NAME = os.getenv("DB_NAME_PROD") 
DB_USER = os.getenv("DB_USER_PROD") 
DB_PASS = os.getenv("DB_PASS_PROD")

# Construir a URL de conexão
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Caminho para o arquivo CSV
data_path = os.getenv("DATA")      

# Ler o arquivo CSV
df = pd.read_csv(data_path)

# Criar a engine do SQLAlchemy com a URL de conexão
engine = create_engine(DATABASE_URL)

# Salvar os dados no PostgreSQL
df.to_sql("tb_atencao_basica_municipio", engine, index=False, if_exists="replace")
