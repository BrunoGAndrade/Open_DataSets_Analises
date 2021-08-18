
# coding: utf-8

# # Manipulando dados com Pandas

# In[2]:


# Importando as bibliotecas
import numpy as np
import pandas as pd


# In[7]:


# Lendo o arquivo da SuperStore e adicionando em uma variavel
# pd.set_option é usado para mostrar todas as colunas do dataset

vendas = pd.read_excel("Sample-Superstore.xls")
pd.set_option('display.max_columns', None)


# In[64]:


# Imprimindo as 5 primeiras linhas para analisar o dataset

vendas.head(5)


# In[13]:


# Analisando os tipos dos dados de cada coluna

vendas.dtypes


# In[14]:


# Verificando como o arquivo esta distribuio em colunas e linhas

vendas.shape


# In[15]:


#Iremos usar o Describe para analisar o número de informações das colunas, quantos valores unicos existem, o maximo e frequencia
vendas.describe(include=['object'])


# In[16]:


# Nota-se que há apenas dados do EUA, pois no coluna Country apareceu apenas 1 em valores unicos.
# Há dados de vendas para 49 estados e para as 4 regiões dos EUA


# In[19]:


#Vamos verificar quais sãos os Segmentos, Categorias e Sub-Categorias dos nossos dados

vendas['Segment'].value_counts()


# In[20]:


vendas['Category'].value_counts()


# In[21]:


vendas['Sub-Category'].value_counts()


# In[24]:


#Utilizando a função unique() para verificar a ocorrência dos estados
vendas.State.unique()


# In[65]:


#Verificando quais são os números de vendas por estado

estado_vendas = vendas.groupby('State').Sales.sum()
estado_vendas.sort_values(ascending=False) [:10]


# In[30]:


#Verificando a quantidade média de itens vendidos por categoria

vendas.groupby('Category').Quantity.mean().sort_values()


# In[31]:


#Verificando agora por sub-categoria

vendas.groupby('Sub-Category').Quantity.mean().sort_values()


# In[46]:


#A sub-categoria com a média de quantidade mais vendida é a 'Fasteners', vamos verificar quais produtos a compõem

Fasteners = vendas[(vendas['Sub-Category'] == 'Fasteners')]


# In[66]:


Fasteners['Product Name'].value_counts()[:10]


# In[50]:


#Utilizand o GrupBy para verificar mais informações sobre o número de vendas, por sub-categoria

vendas.groupby('Sub-Category').Sales.agg(['count', 'mean', 'min', 'max','sum'])


# In[52]:


# Como pode-se notar, a Sub-Categoria com a média de quantidade mais vendida 'Fasteners' não é a que possui as maiores vendas
# O grup by de forma a apresentar várias informações, ajuda a conhecer os dados presentes


# In[55]:


# Identificando os 5 produtos mais vendidos
vendas.groupby('Product Name').Sales.max().sort_values(ascending = False)[:5]


# In[56]:


# Identificando os clientes que mais compram

vendas.groupby('Customer Name').Sales.max().sort_values(ascending = False)[:5]

