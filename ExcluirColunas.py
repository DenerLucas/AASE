import pandas as pd

# Nome do arquivo de entrada e saída
arquivo_entrada = 'apartments_for_rent_classified_10K.csv'  # Dataset original
arquivo_saida = 'apartments_columns_removed.csv'  # Primeiro dataset gerado no pipeline

# Carregar o CSV original
df = pd.read_csv(arquivo_entrada, encoding='ISO-8859-1', delimiter=';', on_bad_lines='skip')

# Colunas a serem excluídas
colunas_para_excluir = [
    'id',          # Coluna informativa
    'title',       # Coluna informativa
    'body',        # Coluna informativa
    'source',      # Coluna informativa
    'time',        # Coluna informativa
    'price_display',  # Representa o preço formatado
    'currency'     # Sempre a mesma moeda (redundante)
]

# Verificar se as colunas existem no dataset antes de excluí-las
colunas_existentes = [col for col in colunas_para_excluir if col in df.columns]
if colunas_existentes:
    # Excluir as colunas
    df.drop(columns=colunas_existentes, inplace=True)
    print(f"As colunas {colunas_existentes} foram removidas com sucesso.")
else:
    print("Nenhuma das colunas para exclusão foi encontrada no dataset.")

# Salvar o dataset transformado em um novo arquivo
df.to_csv(arquivo_saida, index=False, encoding='ISO-8859-1', sep='|')
print(f"O dataset transformado foi salvo como '{arquivo_saida}'.")
