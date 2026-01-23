--lista dados dos usuários para análise
SELECT
    u.nome        AS "Nome",
    u.email       AS "E-mail",
    u.idade       AS "Idade",
    CASE
        WHEN u.genero = 'F' THEN 'Feminino'
        WHEN u.genero = 'M' THEN 'Masculino'
        ELSE 'Não informado'
    END           AS "Sexo",
    c.logradouro  AS "Logradouro",
    u.cidade      AS "Cidade",
    u.estado      AS "Estado",
    u.cep         AS "CEP",
    c.regiao      AS "Região"
FROM users u
LEFT JOIN cep_info c
    ON c.cep = u.cep;
