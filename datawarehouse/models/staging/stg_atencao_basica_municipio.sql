WITH source AS (
    SELECT * 
    FROM {{ source('projeto_saude', 'tb_atencao_basica_municipio') }}
) 

SELECT * FROM source
