{% docs overview %}

# Documentação do Data Warehouse - Atenção Básica Município

## 📌 Visão Geral
Este projeto de Data Warehouse tem como objetivo organizar e estruturar os dados de atenção básica à saúde dos municípios, garantindo a integridade, qualidade e acessibilidade das informações para análise e tomada de decisão.

## 📂 Camadas do Data Warehouse
O projeto segue uma estrutura de camadas para organização dos dados:

### 🏞️ **Camada STG (Staging)**
- Representa uma cópia dos dados brutos armazenados no **Lake**.
- Não contém transformações ou regras de negócio.
- Mantém a estrutura original para garantir rastreabilidade e auditoria.

📌 **Tabela:** `stg_atencao_basica_municipio`
```sql
WITH source AS (
    SELECT * 
    FROM {{ source('projeto_saude', 'tb_atencao_basica_municipio') }}
) 
SELECT * FROM source
```

### 📊 **Camada DM (Data Mart)**
- Aplica regras de negócio para análise.
- Filtra os dados para incluir apenas registros **a partir de 2018**.
- Melhora a performance para consultas analíticas.

📌 **Tabela:** `dm_atencao_basica_municipio`
```sql
WITH dados_filtrados AS (
    SELECT * 
    FROM {{ ref('stg_atencao_basica_municipio') }}
    WHERE ano >= 2018
)
SELECT * FROM dados_filtrados
```

## 🛠️ Execução do dbt

### 🔍 **Depuração do dbt**
Para garantir que o ambiente está configurado corretamente, execute:
```sh
dbt debug
```

### 🚀 **Execução do modelo**
Para rodar os modelos e gerar as tabelas no banco de dados:
```sh
dbt run
```

## 🔗 Versionamento com Git
Se houver um erro ao realizar `git push`, use:
```sh
git push --set-upstream origin nome-da-branch
```

Se houver arquivos muito grandes, considere usar **Git LFS**:
```sh
git lfs install
git lfs track "NOME_DO_ARQUIVO"
git add .gitattributes NOME_DO_ARQUIVO
git commit -m "Adicionando arquivo grande com LFS"
git push origin nome-da-branch
```

## 📌 Conclusão
Este projeto visa estruturar os dados de atenção básica dos municípios, separando dados brutos (STG) de dados transformados para análise (DM). Caso tenha dúvidas ou precise realizar ajustes, consulte esta documentação.

{% enddocs %}
