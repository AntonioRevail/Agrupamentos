C-means Fuzzy

1 - As 10 sequências foram alinhadas usando MAUVE. Os cromossomos 10, 28 e 31 foram alinhados separadamente.
Site: https://darlinglab.org/mauve/mauve.html

2 - Una os cromossomos 10, 28 e 31 de cada espécie em arquivos .fasta separados.

3 - Gere 5 sequências adicionais a partir de uma, usando o código abaixo.
Código: Modelojukescantor.py

4 - Combine todas as sequências de todas as espécies em um único arquivo .fasta.
Código: lojacromosmosmos.py

5 - Vetorize as sequências (converta as bases em números). Salve o resultado em um arquivo .csv.
Código: vectorizacao.py

6 - Use o arquivo de saída da etapa 5 (.csv) como entrada para o C-means Fuzzy.
Código: fcm.py

Observação: A saída deste código contém, separadamente, os graus de pertinência e os coeficientes de partição fuzzy. Uma visualização melhor seria colocar esses dados em uma planilha para melhor observar os clusters.
Arquivo: Todos os Clusters Fuzzy cMeans.xlsx

Mapa Fuzzy

1 - Este código cria um gráfico colorido mostrando a distribuição das espécies entre os clusters.
Código: mapfuzzy.py
