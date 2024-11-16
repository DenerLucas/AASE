import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Carregar o dataset tratado (sem nulos e outliers)
df = pd.read_csv('apartments_for_rent_cleaned_price_no_outliers.csv', encoding='ISO-8859-1', delimiter=';')

# Criar a coluna 'price_per_sqft' se não existir
if 'price_per_sqft' not in df.columns:
    df['price_per_sqft'] = df['price'] / df['square_feet']
    df['price_per_sqft'].fillna(0, inplace=True)

# Selecionar colunas numéricas para transformação
numeric_columns = ['price', 'bathrooms', 'bedrooms', 'square_feet', 'price_per_sqft']

# Escolha entre normalização ou padronização
modo = 'normalizar'  # Altere para 'padronizar' se preferir padronização

if modo == 'normalizar':
    scaler = MinMaxScaler()
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
elif modo == 'padronizar':
    scaler = StandardScaler()
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

# Salvar o dataset com um delimitador alternativo (|) ou aspas
output_file = 'apartments_for_rent_scaled_pipe.csv'
df.to_csv(output_file, index=False, encoding='ISO-8859-1', sep='|')
print(f"\nO dataset transformado foi salvo como '{output_file}' com delimitador '|'.")
