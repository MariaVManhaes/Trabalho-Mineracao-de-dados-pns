import pandas as pd

print("Lendo base...")

df = pd.read_csv("pns2019certa.csv", sep=";", low_memory=False)

# Converter idade para número
df["C008"] = pd.to_numeric(df["C008"], errors="coerce")

print("Selecionando colunas de doenças (Q)...")

# Selecionar todas as colunas que começam com Q
colunas_doencas = [col for col in df.columns if col.startswith("Q")]

print("Filtrando pessoas >60 sem nenhuma doença...")

# Condição: nenhuma coluna Q pode ser igual a 1
sem_doenca = df[
    (df["C008"] > 60) &
    ~(df[colunas_doencas] == 1).any(axis=1)
]

print("Salvando nova base...")

sem_doenca.to_csv("idosos_sem_doencas.csv", index=False)

print("Pronto!")
print("Total de idosos (>60) sem nenhuma doença:", len(sem_doenca))