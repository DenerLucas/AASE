import pandas as pd

# Nome do arquivo de entrada
arquivo_base = "apartments_for_rent_cleaned_target_no_outliers.csv"

# Carregar o dataset tratado sem outliers
df = pd.read_csv(arquivo_base, encoding='ISO-8859-1', delimiter=';')

# 1. Criar a coluna price_per_sqft
if 'price_per_sqft' not in df.columns:
    print("Criando a coluna 'price_per_sqft'...")
    # Evitar divisão por zero
    df['price_per_sqft'] = df['price'] / df['square_feet']
    df['price_per_sqft'].fillna(0, inplace=True)
    print("Coluna 'price_per_sqft' criada com sucesso!")

# 2. Separar os dados em duas classes (baratos e caros) com base no percentil 50%
print("Criando a coluna para separar em duas classes ('baratos' e 'caros')...")
percentil_50 = df['price'].quantile(0.5)
df['price_class'] = df['price'].apply(lambda x: 'baratos' if x <= percentil_50 else 'caros')

print(f"Percentil 50% (mediana) do preço: {percentil_50}")
print("Coluna 'price_class' criada com sucesso!")

# Salvar o novo dataset em um arquivo CSV
arquivo_saida = "apartments_with_price_classes.csv"
df.to_csv(arquivo_saida, index=False, encoding='ISO-8859-1', sep=';')
print(f"\nO novo dataset foi salvo como '{arquivo_saida}'.")
