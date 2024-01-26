import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px 
from datetime import datetime

NAGEM = st.session_state['NAGEM']

# Unique values for filters
cidades = ['Todos'] + list(NAGEM['CIDADE'].unique())
estados = ['Todos'] + list(NAGEM['UF'].unique())
status_options = ['Todos'] + list(NAGEM['STATUS'].unique())

# Sidebar filters
st.sidebar.title('Filtros')
cidade_selecionada = st.sidebar.selectbox('Selecione a cidade:', cidades)
estado_selecionado = st.sidebar.selectbox('Selecione o estado:', estados)
status_selecionado = st.sidebar.selectbox('Selecione o status:', status_options)

# Filter data based on selected option
df_filtered = NAGEM.copy()

if cidade_selecionada != 'Todos':
    df_filtered = df_filtered[df_filtered['CIDADE'] == cidade_selecionada]

if estado_selecionado != 'Todos':
    df_filtered = df_filtered[df_filtered['ESTADO'] == estado_selecionado]

if status_selecionado != 'Todos':
    df_filtered = df_filtered[df_filtered['STATUS'] == status_selecionado]

# Display filtered data
st.title('Dados Filtrados')
st.write(df_filtered)

# Plot the interactive bar chart for 'STATUS' by city
ocorrencias_por_status_cidade = df_filtered['STATUS'].value_counts().reset_index()
ocorrencias_por_status_cidade.columns = ['Status', 'Quantidade']
fig_status_cidade = px.bar(ocorrencias_por_status_cidade, x='Status', y='Quantidade',
                            title=f'Quantidade de Reclamações por Status em {cidade_selecionada}',
                            labels={'Quantidade': 'Quantidade de Reclamações', 'Status': 'Status'},
                            text='Quantidade')

st.plotly_chart(fig_status_cidade)

# Plot the top 10 cities with the most complaints
ocorrencias_por_cidade = df_filtered['CIDADE'].value_counts().reset_index().head(10)
ocorrencias_por_cidade.columns = ['Cidade', 'Quantidade']
fig_top_cidades = px.bar(ocorrencias_por_cidade, x='Cidade', y='Quantidade',
                         title='Top 10 Cidades com Mais Reclamações',
                         labels={'Quantidade': 'Quantidade de Reclamações', 'Cidade': 'Cidade'},
                         text='Quantidade')

st.plotly_chart(fig_top_cidades)

# Display table for the top 10 cities
st.table(ocorrencias_por_cidade)


# Plot the top 10 states with the most complaints
ocorrencias_por_estado = df_filtered['UF'].value_counts().reset_index().head(10)
ocorrencias_por_estado.columns = ['UF', 'Quantidade']
fig_top_estados = px.bar(ocorrencias_por_estado, x='UF', y='Quantidade',
                          title='Top 10 Estados com Mais Reclamações',
                          labels={'Quantidade': 'Quantidade de Reclamações', 'ESTADO': 'ESTADO'},
                          text='Quantidade')

st.plotly_chart(fig_top_estados)

# Display table for the top 10 states
st.table(ocorrencias_por_estado)

