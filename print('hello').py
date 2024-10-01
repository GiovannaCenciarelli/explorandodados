import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho do arquivo CSV
arquivo_csv = r'C:\Users\camil\OneDrive\Documentos\relatoriosficticios\VendasTesouroDireto.csv'

# Ler o arquivo CSV com delimitador de ponto e vírgula
df = pd.read_csv(arquivo_csv, delimiter=';')

# Remover espaços nos nomes das colunas
df.columns = df.columns.str.strip()

# Exibir os nomes das colunas
print("Nomes das colunas após a remoção de espaços:")
print(df.columns)

# Exibir as primeiras 20 linhas do DataFrame
relatorio = df.head(20)

# Exibir o relatório no console
print("\nRelatório - Primeiras 20 Linhas:")
print(relatorio)

# Verificar se a coluna "Tipo de Título" está presente no relatorio
print("\nVerificando a presença da coluna 'Tipo de Título':")
print(relatorio.columns)

# Tratar a coluna 'Valor' para converter os valores para numéricos
# 1. Substituir vírgulas por pontos usando .loc
relatorio.loc[:, 'Valor'] = relatorio['Valor'].astype(str).str.replace(',', '.', regex=False)
# 2. Converter para numérico, forçando erros a se tornarem NaN
relatorio.loc[:, 'Valor'] = pd.to_numeric(relatorio['Valor'], errors='coerce')

# Calcular a média dos valores da coluna 'Valor'
media_valores = relatorio['Valor'].mean()

# Exibir a média
print("\nMédia dos Valores das Primeiras 20 Linhas:")
print(media_valores)

# Opcional: Salvar o relatório em um arquivo CSV
relatorio.to_csv(r'C:\Users\camil\OneDrive\Documentos\relatoriosficticios\Relatorio_Primeiras_20_Linhas.csv', index=False, sep=';')

# Gráfico de barras para os valores
plt.figure(figsize=(10, 6))
sns.barplot(x= 'Tipo Titulo', y= 'Valor', data=relatorio, palette='viridis')
plt.title('Valores por Tipo de Título')
plt.xlabel('Tipo de Título')
plt.ylabel('Valor')
plt.xticks(rotation=45)
plt.tight_layout()  # Ajustar layout
plt.show()


# Gráfico de dispersão entre 'Valor' e 'Quantidade'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Quantidade', y='Valor', data=relatorio, hue='Tipo Título', palette='viridis', s=100)
plt.title('Dispersão entre Quantidade e Valor')
plt.xlabel('Quantidade')
plt.ylabel('Valor')
plt.tight_layout()  # Ajustar layout
plt.show()