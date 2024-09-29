import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega o DataFrame
df = pd.read_csv('Ciencia.csv')

# Imprime os nomes das colunas
print("Nomes das colunas no DataFrame:")
print(df.columns)

# Imprime a quantidade de objetos (linhas) e atributos (colunas)
print(f"Quantidade de objetos (linhas): {df.shape[0]}")
print(f"Quantidade de atributos (colunas): {df.shape[1]}")

# Imprime os tipos de dados dos atributos
print("\nTipos de dados dos atributos:")
print(df.dtypes)

# Análise estatística dos atributos numéricos
print("\nAnálise estatística dos atributos numéricos:")
print(df.describe().T)

# Boxplot das variáveis numéricas
numerical_vars = ['Porcen_Fatura', 'Curva', 'Porcen_Fatura_Acumula']
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[numerical_vars])
plt.title('Boxplot de Variáveis Numéricas')
plt.show()

# Gráfico de barras para a variável categórica
categorical_var = 'VariavelCateg'
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x=categorical_var)
plt.title('Gráfico de Barras de Variável Categórica')
plt.show()
