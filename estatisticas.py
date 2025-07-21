import pandas as pd

df = pd.read_csv("usuarios.csv")

print("Média das idades:", df["idades"].mean())
print("Usuário mais velho:", df.loc[df["idades"].idxmax()]["nomes"])
print("Usuário mais novo:", df.loc[df["idades"].idxmin()]["nomes"])