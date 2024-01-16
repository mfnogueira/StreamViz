# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import seaborn as sns
import pandas_profiling

# Configurando o nome da página do aplicativo web (opcional)
st.set_page_config(page_title='SAMPLE WEB APP', page_icon=None, layout='wide')

# Lendo os dados
data = pd.read_csv('Housing.csv')
data.columns = data.columns.str.upper()  # Convertendo os nomes das colunas para maiúsculas

# Realizando o Pandas Profiling
profile = pandas_profiling.ProfileReport(data)

# Salvando o relatório como um arquivo HTML
profile.to_file("analysis_report_profilereport.html")

# Escrevendo um texto ou comentário (o número de "#" determina o tamanho do texto)
st.write('### 1. Visão geral dos dados')

# Visualizando o dataframe no Streamlit
st.dataframe(data, use_container_width=True)

st.write('### 2. Analisando os dados')

# Criando um botão de seleção
selected = st.radio("**O que você quer saber sobre os dados?**",
                    ["Descrição", "Amostra de Dados", "Cabeçalho/Final", "Formato dos Dados"])

if selected == 'Descrição':
    st.dataframe(data.describe(), use_container_width=True)  # Mostra estatísticas descritivas básicas
elif selected == 'Amostra de Dados':
    st.dataframe(data.sample(10), use_container_width=True)  # Seleciona linhas aleatórias
elif selected == 'Cabeçalho/Final':
    st.dataframe(data.head(), use_container_width=True)  # Mostra o cabeçalho do dataframe
else:
    st.write('###### O formato dos dados é:', data.shape)  # Mostra o formato dos dados 


# cereating sidebar and raido button simultaneously
selected = st.sidebar.radio(
    "**O que você quer saber sobre os dados?**",
    ["Descrição", "Amostra de Dados", "Cabeçalho/Final", "Formato dos Dados"],
    key="identificador_unico"  # Adicione uma chave única aqui
)

# Criando uma lista de opções para os gráficos
graph_options = st.sidebar.multiselect("SELECIONE O TIPO DE GRÁFICO:", options=['HISTOGRAMA', 'COUNT-PLOT', 'BOX-PLOT'],
                                       default=['HISTOGRAMA', 'COUNT-PLOT', 'BOX-PLOT'])

# Criando três colunas para exibir os gráficos em três colunas
col1, col2, col3 = st.columns(3)

# Definindo as colunas para exibir no Streamlit
col1.write('##### Gráfico de Histograma')
col2.write('##### Gráfico de Caixa')
col3.write('##### Gráfico de Contagem')

# Identificando as características numéricas e categóricas
numerical_features = data.select_dtypes(exclude='object').columns
categorical_features = data.select_dtypes('object').columns

# Se a opção de histograma estiver selecionada, mostrar o histograma para cada característica numérica
if 'HISTOGRAMA' in graph_options:
    for feature in numerical_features:
        fig1 = plt.figure()
        # Plotando o gráfico de histograma
        sns.histplot(data=data, x=feature, color="black")
        col1.pyplot(fig1)

# Se a opção de gráfico de caixa estiver selecionada, mostrar o gráfico de caixa para cada característica categórica
if 'BOX-PLOT' in graph_options:
    for feature in categorical_features:
        fig2 = plt.figure()
        sns.boxplot(x=feature, y='PRICE', data=data, palette="Set1")
        col2.pyplot(fig2)

# Se a opção de gráfico de contagem estiver selecionada, criar um gráfico de contagem para cada característica categórica
if 'COUNT-PLOT' in graph_options:
    for feature in categorical_features:
        fig3 = plt.figure()
        sns.countplot(x=feature, data=data, palette="Set3")
        col3.pyplot(fig3)
