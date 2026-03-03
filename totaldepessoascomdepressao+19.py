import pandas as pd

print("Lendo base...")

df = pd.read_csv("pns2019certa.csv", sep=";", low_memory=False)

# Converter idade para número
df["C008"] = pd.to_numeric(df["C008"], errors="coerce")

print("Filtrando pessoas com 19 anos ou mais com depressão...")

# Filtro: idade >= 19 e Q092 = 1
adultos_depressao = df[(df["C008"] >= 19) & (df["Q092"] == 1)]

print("Salvando nova base...")

adultos_depressao.to_csv("adultos_19mais_depressao.csv", index=False)

print("Pronto!")
print("Total de pessoas (19+ anos) com depressão:", len(adultos_depressao))