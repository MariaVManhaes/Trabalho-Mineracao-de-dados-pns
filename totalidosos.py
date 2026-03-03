import pandas as pd

# Coluna de idade
coluna_idade = 'C008'  # ajuste se for outra na sua base

print("Lendo base...")

df = pd.read_csv("pns2019certa.csv", sep=";", usecols=[coluna_idade])

print("Convertendo idade para numérico...")

df[coluna_idade] = pd.to_numeric(df[coluna_idade], errors='coerce')

print("Filtrando idosos (>60 anos)...")

idosos = df[df[coluna_idade] > 60]

total_idosos = len(idosos)

print(f"Total de idosos com mais de 60 anos: {total_idosos}")