import pandas as pd

# Carregar o dataset original (de entrada)
df_original = pd.read_csv('apartments_columns_removed.csv', encoding='ISO-8859-1', delimiter=';', on_bad_lines='skip')

# Criar uma cópia do dataset para tratamento
df = df_original.copy()

# Selecionar colunas numéricas
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Preencher valores nulos com a mediana de cada coluna
for column in numeric_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].median())
        print(f"Valores nulos preenchidos na coluna '{column}' com a mediana.")

# Verificação de valores nulos após o tratamento
print("\nVerificação de valores nulos após o tratamento:")
print(df[numeric_columns].isnull().sum())

# Salvar o dataset tratado em um novo arquivo CSV
df.to_csv('apartments_for_rent_cleaned.csv', index=False, encoding='ISO-8859-1', sep=';')

print("\nO dataset tratado foi salvo como 'apartments_for_rent_cleaned-1.csv'.")
