import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Nome do arquivo de entrada e saída
arquivo_entrada = "apartments_categoricals_encoded.csv"
arquivo_saida = "apartments_textuals_treated.csv"

# Carregar o dataset
df = pd.read_csv(arquivo_entrada, encoding="ISO-8859-1", delimiter=";")

# Colunas textuais a serem tratadas
colunas_textuais = ['amenities']

# Criar um vetorizador TF-IDF
vectorizer = TfidfVectorizer(max_features=100)  # Limitar a 100 features para cada coluna

# Processar cada coluna textual
for coluna in colunas_textuais:
    if coluna in df.columns:
        print(f"Transformando a coluna '{coluna}' com TF-IDF...")
        tfidf_matrix = vectorizer.fit_transform(df[coluna].astype(str))
        
        # Criar um DataFrame com os resultados do TF-IDF
        tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=[f"{coluna}_tfidf_{i}" for i in range(tfidf_matrix.shape[1])])
        
        # Concatenar os resultados ao dataset original
        df = pd.concat([df, tfidf_df], axis=1)
        
        # Remover a coluna original
        df.drop(columns=[coluna], inplace=True)

# Salvar o dataset atualizado em um novo arquivo CSV
df.to_csv(arquivo_saida, index=False, encoding="ISO-8859-1", sep=";")
print(f"Colunas textuais tratadas e salvas como '{arquivo_saida}'.")
