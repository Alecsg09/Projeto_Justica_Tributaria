import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar a planilha Excel
df = pd.read_excel("dados_justica_tributaria.xlsx")

# Visualizar as primeiras linhas do DataFrame
print("Primeiras linhas do DataFrame:")
print(df.head())

# Informações gerais sobre os dados
print("\nInformações sobre o DataFrame:")
print(df.info())

# Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(df.describe())

# Verificar valores nulos
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# Análise de distribuição de status
print("\nDistribuição de Status:")
print(df["Status"].value_counts())

# Análise de distribuição de decisões
print("\nDistribuição de Decisões:")
print(df["Sentença/Decisão/Acórdão"].value_counts())

# Análise de valores envolvidos
plt.figure(figsize=(10, 6))
sns.histplot(df["Valor Envolvido"], bins=30, kde=True)
plt.title("Distribuição dos Valores Envolvidos")
plt.xlabel("Valor Envolvido")
plt.ylabel("Frequência")
plt.show()

# Análise de prazos de audiência
plt.figure(figsize=(10, 6))
sns.histplot(df["Prazo de Audiência"], bins=30, kde=True)
plt.title("Distribuição dos Prazos de Audiência")
plt.xlabel("Prazo de Audiência (dias)")
plt.ylabel("Frequência")
plt.show()

# Análise de status por tipo de tributo
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="Tipo de Tributo", hue="Status")
plt.title("Status dos Processos por Tipo de Tributo")
plt.xlabel("Tipo de Tributo")
plt.ylabel("Contagem")
plt.legend(title="Status")
plt.show()

# Análise de decisões por vara
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="Vara", hue="Sentença/Decisão/Acórdão")
plt.title("Decisões por Vara")
plt.xlabel("Vara")
plt.ylabel("Contagem")
plt.legend(title="Decisão")
plt.show()