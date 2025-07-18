import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import names

pasta_datasetes = Path(__file__).parent / "datasets"

pasta_datasetes.mkdir(parents=True, exist_ok=True)

LOJAS = [
    {"estado": "SP",
     "cidade": "São Paulo",
     "vendedores": ["Ana Oliveira", "Lucas Pereira"]},
     {"estado": "MG",
     "cidade": "Belo Horizonte",
     "vendedores": ["Carlos Silva", "Fernanda"]},
     {"estado": "RJ",
     "cidade": "Rio de Janeiro",
     "vendedores": ["Juliana Oliveira", "Pedro Pereira"]},
     {"estado": "RS",
     "cidade": "Porto Alegre",
     "vendedores": ["Mário Silva", "Robson Souza"]},
     {"estado": "SC",
     "cidade": "Florianópolis",
     "vendedores": ["Gustavo Lima", "Jorge Ferreira"]}
    ]

PRODUTOS = [
    {"nome": "Smartphone ZetaPhone Universal",
     "id": 0,
     "preço": 2500,},
     {"nome": "Notebook",
     "id": 1,
     "preço": 4500,},
     {"nome": "Tablet ZetaPhone",
     "id": 2,
     "preço": 3000,},
     {"nome": "Smartwatch ZetaWatch",
     "id": 3,
     "preço": 1200,},
     {"nome": "Fone ZetaAudio",
     "id": 4,
     "preço": 600,}
     ]

FORMA_PAGAMENTO = ["cartão de crédito", "boleto", "pix", "espécie", "cartão de débito"]
GENERO_CLIENTES = ["male", "female"]

compras = []

for _ in range(2000):
    loja = random.choice(LOJAS)
    vendedor = random.choice(loja["vendedores"])
    produto = random.choice(PRODUTOS)
    hora_compra = datetime.now() - timedelta(
        days=random.randint(1,365),
        hours=random.randint(-5,5),
        minutes=random.randint(-30,30)
    )

    genero_cliente = random.choice(GENERO_CLIENTES)
    nome_cliente = names.get_full_name(genero_cliente)
    forma_pagamento = random.choice(FORMA_PAGAMENTO)

    compras.append({
        "data": hora_compra,
        "id_compra": 0,
        "loja": loja["cidade"],
        "vendedor":vendedor,
        "produto": produto["nome"],
        "cliente_nome": nome_cliente,
        "cliente_genero": genero_cliente.replace("female", "feminino").replace("male","masculino"),
        "forma_pagamento": forma_pagamento
    })

df_compras = pd.DataFrame(compras).set_index("data").sort_index()
df_compras["id_compra"] = range(len(df_compras))

df_lojas = pd.DataFrame(LOJAS)
df_produtos = pd.DataFrame(PRODUTOS)

# IMPRESSÃO
print(df_lojas)
print(df_produtos)
print(df_compras)

df_compras.to_csv(pasta_datasetes / "compras.csv", decimal=",", sep=";")
df_lojas.to_csv(pasta_datasetes / "lojas.csv", decimal=",", sep=";")
df_produtos.to_csv(pasta_datasetes / "produtos.csv", decimal=",", sep=";")

df_compras.to_excel(pasta_datasetes / "compras.xlsx")
df_lojas.to_excel(pasta_datasetes / "lojas.xlsx")
df_produtos.to_excel(pasta_datasetes / "produtos.xlsx")
