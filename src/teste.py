import os
from dotenv import load_dotenv

data_path = r"C:\Users\Bruno\Desktop\projetos_engenharia\projeto_atencao_basica_municipio\data\br_ms_atencao_basica_municipio.csv"

print(f"Arquivo existe? {os.path.exists(data_path)}")
