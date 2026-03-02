# Importando 
import pandas as pd

# Carregando dataset
arquivo = ('data_aula_05/salario_ti_nacional_2023.xlsx')  
df_salario = pd.read_excel(arquivo)

# Pegando as informacoes gerais 
# 1. Info 
df_salario.info()

# 2. Head
df_salario.head(20)

# 3.Total de nulos 
df_salario.isnull().sum()

# 3.1 Calculando percentual de nulos
percentual_nulos = (df_salario.isnull().sum() / len(df_salario)) * 100
print(percentual_nulos)

# 3.1 Investigandos os nulos de especialidade
df_salario['especialidade'].value_counts(dropna=False)

# 4. Total de duplicatas
df_salario.duplicated().sum()

# Limpando o dataset 
# 1. Removendo uma coluna especifica 
df_salario_limpo = df_salario.drop(["especialidade","estado"], axis=1)
df_salario_limpo.head(5)

# 2. Removendo NaN
df_salario_limpo.dropna()

# 3. Removendo duplicadas
df_salario_limpo.drop_duplicates() 

# 4. Convertendo as letras para minusculas 
df_salario_limpo['cargo'] = df_salario_limpo['cargo'].str.lower()
