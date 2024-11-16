import pandas as pd
import numpy as np

# Carregar o dataset tratado
df = pd.read_csv('apartments_for_rent_cleaned.csv', encoding='ISO-8859-1', delimiter=';')

# Função para detectar e remover outliers na variável target usando Z-Score
def remover_outliers_target(df, coluna_target, limite=3):
    # Calcular o Z-Score para a variável target
    media = df[coluna_target].mean()
    desvio_padrao = df[coluna_target].std()
    z_scores = (df[coluna_target] - media) / desvio_padrao

    # Identificar os outliers
    outliers = df[np.abs(z_scores) > limite]
    num_outliers = len(outliers)

    # Remover os outliers
    df_sem_outliers = df[np.abs(z_scores) <= limite]

    # Exibir informações
    print(f"Outliers na coluna '{coluna_target}': {num_outliers} removidos.")
    print(f"O dataset agora contém {len(df_sem_outliers)} registros (linhas).")

    return df_sem_outliers

# Aplicar o tratamento de outliers apenas na variável target ('price')
df_sem_outliers_price = remover_outliers_target(df, 'price')

# Salvar o dataset tratado em um novo arquivo CSV
df_sem_outliers_price.to_csv('apartments_for_rent_cleaned_target_no_outliers.csv', index=False, encoding='ISO-8859-1', sep=';')
print("\nO dataset sem outliers na variável 'price' foi salvo como 'apartments_for_rent_cleaned_target_no_outliers.csv'.")
