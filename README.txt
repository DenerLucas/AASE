Os scripts estão organizados de forma a executar cada etapa do pipeline de preparação de dados, incluindo limpeza, tratamento de outliers, criação de colunas derivadas e transformação de variáveis categóricas.

Os arquivos CSV gerados não estão incluídos no repositório. Para reproduzir os resultados, você deve executar os scripts na ordem descrita abaixo, utilizando o dataset original.

Ordem de Execução dos Scripts


1. Exclusão de Atributos
	Script: ExcluirAtributos.py
	Descrição: Este script realiza a exclusão de colunas consideradas irrelevantes para a análise ou redundantes no contexto do projeto. As colunas removidas foram selecionadas com base na justificativa de que não contribuem diretamente para o objetivo de prever a variável-alvo (price).

	Colunas removidas:
	id, title, body, source, time: Dados meramente informativos que não são úteis para a análise.
	price_display: Representa a coluna price formatada (redundante).
	currency: Moeda única em todo o dataset (USD), considerada redundante.
	As colunas foram removidas e o dataset resultante foi salvo em um novo arquivo.
	Entrada:
	Arquivo original: apartments_for_rent_classified_10K.csv
	Saída:
	Arquivo gerado: apartments_columns_removed.csv


2. Tratamento de Valores Nulos
	Script: TratarNulosColunasNumericas.py
	Descrição: Preenche valores nulos em colunas numéricas com a mediana (ex.: bathrooms, bedrooms, latitude, longitude).
	Entrada: apartments_columns_removed.csv
	Saída: apartments_for_rent_cleaned.csv


3. Remoção de Outliers
	Script: calcular_Outlyers_ZScore.py
	Descrição: Remove outliers na variável-alvo price com base no método Z-Score, utilizando um limite de ±3 desvios padrão.
	Entrada: apartments_for_rent_cleaned.csv
	Saída: apartments_for_rent_cleaned_target_no_outliers.csv


4. Criação de Colunas Derivadas
	Script: 2Classes.py
	Descrição:
	Cria a coluna price_per_sqft, que representa o preço por unidade de área.
	Cria a coluna price_class, que separa os registros em duas classes: "baratos" e "caros".
	Entrada: apartments_for_rent_cleaned_target_no_outliers.csv
	Saída: apartments_with_price_classes.csv


5. Tratamento de Colunas Categóricas
	Script: TratarColunasCategoricas.py
	Descrição: Aplica One-Hot Encoding às colunas categóricas (ex.: category, state, pets_allowed), transformando-as em representações numéricas binárias.
	Entrada: apartments_with_price_classes.csv
	Saída: apartments_categoricals_encoded.csv


6. Tratamento de Colunas Textuais (Opcional)

	Script: TratarColunasTextuais.py
	Descrição: Aplica TF-IDF às colunas textuais (amenities) para representá-la numericamente.
	Entrada: apartments_categoricals_encoded.csv
	Saída: apartments_textuals_treated.csv

Nota: Este passo é opcional e pode ser ignorado, dependendo da abordagem escolhida para a modelagem.
Observações Importantes
Manutenção do Dataset Original:

Em todas as etapas, o dataset original (apartments_for_rent_classified_10K.csv) é preservado. Cada script gera um novo arquivo CSV com as transformações aplicadas.
Formato dos Arquivos Gerados:

Os arquivos CSV gerados utilizam o delimitador | (pipe) para garantir compatibilidade com ferramentas de análise.
Reprodução dos Resultados:

Para reproduzir os resultados, siga a ordem de execução dos scripts conforme descrito acima.
Dependências Necessárias:

Python 3.10 ou superior.
Bibliotecas:
pandas
numpy
scikit-learn
