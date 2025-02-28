WITH de_2018_pra_fente AS (
    SELECT *
    FROM {{ ref('stg_atencao_basica_municipio') }}
    WHERE ano >= 2018
)
SELECT * FROM de_2018_pra_fente