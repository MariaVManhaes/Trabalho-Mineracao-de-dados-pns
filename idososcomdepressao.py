import pandas as pd

print("Lendo base...")

df = pd.read_csv("pns2019certa.csv", sep=";", low_memory=False)

print("Convertendo idade...")

df["C008"] = pd.to_numeric(df["C008"], errors="coerce")

print("Filtrando idosos (>60) com diagnóstico de depressão...")

idosos_depressao = df[(df["C008"] > 60) & (df["Q092"] == 1)]

print("Salvando nova base...")

idosos_depressao.to_csv("idosos_depressao.csv", index=False)

print("Pronto!")
print("Total de idosos com depressão:", len(idosos_depressao))

print("Menor idade no filtro:", idosos_depressao["C008"].min())
print("Maior idade no filtro:", idosos_depressao["C008"].max())
print("Valores únicos de Q092 no filtro:", idosos_depressao["Q092"].unique())
print("Total pelo shape:", idosos_depressao.shape[0])