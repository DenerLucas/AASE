import pandas as pd

# Nome do arquivo de entrada e saída
arquivo_entrada = "apartments_with_price_classes.csv"
arquivo_saida = "apartments_categoricals_encoded.csv"

# Carregar o dataset original
df = pd.read_csv(arquivo_entrada, encoding="ISO-8859-1", delimiter=";")

# Colunas categóricas a serem tratadas
colunas_categoricas = ['category', 'currency', 'fee', 'has_photo', 'pets_allowed', 'price_type', 'state']

# Aplicar One-Hot Encoding nas colunas categóricas
df_encoded = pd.get_dummies(df, columns=colunas_categoricas, drop_first=True)

# Salvar o dataset atualizado em um novo arquivo CSV
df_encoded.to_csv(arquivo_saida, index=False, encoding="ISO-8859-1", sep=";")
print(f"Colunas categóricas tratadas com One-Hot Encoding.")
print(f"O novo dataset foi salvo como '{arquivo_saida}'.")
