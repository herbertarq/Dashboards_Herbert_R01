import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px 
from datetime import datetime

st.write('# Dashboard Reclame aqui ')
st.write('## Dashboard com análise de dados das empresas - Hapvida | Ibyte | Nagem')

st.markdown(
    'Neste trabalho, vamos explorar os dados obtidos do portal "RECLAME AQUI" sobre o desempenho de três empresas no atendimento ao consumidor: **HAPVIDA, IBYTE E NAGEM.** O portal é uma plataforma online que permite aos clientes registrarem suas reclamações sobre produtos ou serviços de diversas empresas. A partir desses registros, podemos analisar como as empresas respondem às demandas dos consumidores e qual é o nível de satisfação dos clientes com as soluções apresentadas. O período de análise abrange os casos de **2016 a 2022.**'
)



st.sidebar.markdown('Trabalho escrito por: Herbert de Sousa Ferreira')

#### CARREGAR OS DADOS ####
Hapvida=pd.read_csv('RECLAMEAQUI_HAPVIDA.csv',sep=',')
Ibyte=pd.read_csv('RECLAMEAQUI_IBYTE.csv',sep=',')
Nagem=pd.read_csv('RECLAMEAQUI_NAGEM.csv',sep=',')

####CRIAR COLUNA EMPRESAS EM TODOS OS DATASETS ###
Hapvida['EMPRESA'] = "HAPVIDA"
Ibyte['EMPRESA'] = "IBYTE"
Nagem['EMPRESA'] = "NAGEM"

####CRIAR COLUNA ESTADO EM TODOS OS DATASETS ###
Hapvida['UF'] = Hapvida['LOCAL'].str[-2:]
Ibyte['UF'] = Ibyte['LOCAL'].str[-2:]
Nagem['UF'] = Nagem['LOCAL'].str[-2:]

####CRIAR COLUNA CIDADES EM TODOS OS DATASETS ###
Hapvida['CIDADE'] = Hapvida['LOCAL'].str.extract(r'([^\-]+)')
Ibyte['CIDADE'] = Ibyte['LOCAL'].str.extract(r'([^\-]+)')
Nagem['CIDADE'] = Nagem['LOCAL'].str.extract(r'([^\-]+)')

####TRATAMENTO DE COLUNAS DATASETS ###
Hapvida.rename(columns={'TEMPO': 'DATA'},inplace = True)
Ibyte.rename(columns={'TEMPO': 'DATA'},inplace = True)
Nagem.rename(columns={'TEMPO': 'DATA'},inplace = True)

#NÚMERO DE RECLAMACOES 
C_HAPVIDA = Hapvida['ID'].nunique()
C_IBYTE = Ibyte['ID'].nunique()
C_NAGEM = Nagem['ID'].nunique()

#STATUS OCORRENCIA 
S_HAPVIDA = Hapvida.STATUS.value_counts()
S_IBYTE = Ibyte.STATUS.value_counts()
S_NAGEM = Nagem.STATUS.value_counts()

####CRIAR DADOS PARA ABAS ###
st.session_state['HAPVIDA'] = Hapvida
st.session_state['IBYTE'] = Ibyte
st.session_state['NAGEM'] = Nagem

##UNIFICANDO DATAFRAMES ## 
GERAL = pd.concat ( [Hapvida, Ibyte, Nagem]).reset_index()
GERAL.drop('index',axis=1,inplace=True)
GERAL.rename(columns={'TEMPO': 'DATA'},inplace = True)

## DATETIME ####

GERAL['DATA']=pd.to_datetime(GERAL['DATA'])

GERAL.drop('DATA',axis=1).sum()

## EXPOSIÇÃO ####

st.markdown('---')

st.write('## TOTAL DE RECLAMAÇÕES POR EMPRESA')

col1, col2, col3= st.columns(3)
col1.metric(label="Reclamações Hapvida", value=C_HAPVIDA)
col2.metric(label="Reclamações Ibyte", value=C_IBYTE)
col3.metric(label="Reclamações Nagem", value=C_NAGEM)

st.markdown('---')

