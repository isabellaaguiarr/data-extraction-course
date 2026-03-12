# Setup inicial — execute esta célula antes de tudo
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')
import warnings
warnings.filterwarnings('ignore')

print("✅ Bibliotecas carregadas com sucesso!")


# ----------------------------------- # 
# Criando o dataset de cidades com alta cardinalidade
np.random.seed(42)
cidades_comuns = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
cidades_raras  = ['Cabo Frio', 'Itu', 'Bauru', 'Gramado', 'Ouro Preto', 'Ilhéus', 'Picos']

amostra_cidades = np.random.choice(cidades_comuns, 950, p=[0.6, 0.3, 0.1]).tolist()
amostra_cidades.extend(np.random.choice(cidades_raras, 50))

df_exemplo = pd.DataFrame({'ID_Cliente': range(1, 1001), 'Cidade': amostra_cidades})

print(f"Total de linhas: {len(df_exemplo)}")
print(f"Cidades únicas: {df_exemplo['Cidade'].nunique()}")
df_exemplo.head()


# ----------------------------------- #
frequencias = df_exemplo['Cidade'].value_counts(normalize=True)

fig, ax = plt.subplots(figsize=(10, 4))
frequencias.plot(kind='bar', ax=ax, color='steelblue', edgecolor='white')
ax.axhline(0.02, color='red', linestyle='--', linewidth=1.5, label='Limiar 2%')
ax.set_title('Proporção de Clientes por Cidade (antes do tratamento)', fontsize=13)
ax.set_ylabel('Proporção')
ax.set_xlabel('')
ax.legend()
plt.tight_layout()
plt.show()

print("\n--- Proporção Original ---")
print(frequencias.to_string())
# ----------------------------------- #
# Definindo o limiar
limite = 0.02
cidades_para_agrupar = frequencias[frequencias < limite].index

print(f"Cidades que serão agrupadas em 'Outros': {list(cidades_para_agrupar)}")

# Aplicando a transformação com .loc e .isin()
df_exemplo.loc[df_exemplo['Cidade'].isin(cidades_para_agrupar), 'Cidade'] = 'Outros'

# Visualização após tratamento
freq_apos = df_exemplo['Cidade'].value_counts(normalize=True)

fig, ax = plt.subplots(figsize=(7, 4))
freq_apos.plot(kind='bar', ax=ax, color='seagreen', edgecolor='white')
ax.set_title('Proporção de Clientes por Cidade (após tratamento)', fontsize=13)
ax.set_ylabel('Proporção')
ax.set_xlabel('')
plt.tight_layout()
plt.show()

print("\n--- Proporção Após Tratamento ---")
print(freq_apos.to_string())