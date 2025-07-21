#1. importando bibliotecas.
import pandas as pd

#2. Criando dicionario com os dados.
usuarios = {
    "nomes":["Marcos","Ana" , "Lucas"], 
    "idades":[25,31,34],
    "cidade":["Guararema", "Jacareí", "Itajuba"]
}

#3. Transformando usuarios em DataFrame.
dados = pd.DataFrame(usuarios)

#4. Adicionando novo usuario.
def adicionar_usuario(dados_df, nome, idade, cidade):
    novo = pd.DataFrame({
        "nomes": [nome], 
        "idades": [idade], 
        "cidade": [cidade]
        })
    return pd.concat([dados_df, novo], ignore_index=True)
dados = adicionar_usuario(dados, "Bruno", 28, "São Paulo")

#5. Salvando como csv.
dados.to_csv("usuarios.csv", index = False)

#6. Ler e exibir os dados em csv.
dados_lidos = pd.read_csv("usuarios.csv")
print(dados_lidos)