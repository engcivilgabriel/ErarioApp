# -*- coding: utf-8 -*-
# Copyright 2020-2021 Gabriel Martins

#Importar bibliotecas
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

#Datasets
DATE_TIME = 'data finalizacao'
DATA_URL = 'https://raw.githubusercontent.com/engcivilgabriel/Analysis-of-public-data/master/CSV/EconomiaErario.csv'

#Configuração Mapbox
mapbox_access_token = 'pk.eyJ1IjoiZ2FicmllbGdhbTg5IiwiYSI6ImNrZmlmdXZ3ZTBrOHUzMXA3M2JhMDdsNDgifQ.PS2K3_6hFrBidstQRDJ8Nw'
mapbox_cofig = dict(
    accesstoken=mapbox_access_token,
    style='mapbox://styles/mapbox/light-v9', )

#Carregamento dos dados
@st.cache(persist=True, allow_output_mutation=True)
def load_data(nrows):
    df = pd.read_csv(DATA_URL, sep=';', encoding='latin-1', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    df.rename(lowercase, axis='columns', inplace=True)
    df[DATE_TIME] = pd.to_datetime(df[DATE_TIME])
    df['economia atual'] = df['economia atual'].apply(lambda x: str(x).replace(',', '.'))
    df['economia atual'] = df['economia atual'].astype('float64')
    return df

df = load_data(10000)
df['regiao'] = np.where(df.uf == 'DF', 'CENTRO-OESTE',
                        np.where(df.uf == 'GO', 'CENTRO-OESTE',
                                 np.where(df.uf == 'MS', 'CENTRO-OESTE',
                                          np.where(df.uf == 'MT', 'CENTRO-OESTE',
                                                   np.where(df.uf == 'AL', 'NORDESTE',
                                                            np.where(df.uf == 'BA', 'NORDESTE',
                                                                     np.where(df.uf == 'CE', 'NORDESTE',
                                                                              np.where(df.uf == 'MA', 'NORDESTE',
                                                                                       np.where(df.uf == 'PB',
                                                                                                'NORDESTE',
                                                                                                np.where(df.uf == 'PE',
                                                                                                         'NORDESTE',
                                                                                                         np.where(
                                                                                                             df.uf == 'PI',
                                                                                                             'NORDESTE',
                                                                                                             np.where(
                                                                                                                 df.uf == 'RN',
                                                                                                                 'NORDESTE',
                                                                                                                 np.where(
                                                                                                                     df.uf == 'SE',
                                                                                                                     'NORDESTE',
                                                                                                                     np.where(
                                                                                                                         df.uf == 'AC',
                                                                                                                         'NORTE',
                                                                                                                         np.where(
                                                                                                                             df.uf == 'AM',
                                                                                                                             'NORTE',
                                                                                                                             np.where(
                                                                                                                                 df.uf == 'AP',
                                                                                                                                 'NORTE',
                                                                                                                                 np.where(
                                                                                                                                     df.uf == 'PA',
                                                                                                                                     'NORTE',
                                                                                                                                     np.where(
                                                                                                                                         df.uf == 'RO',
                                                                                                                                         'NORTE',
                                                                                                                                         np.where(
                                                                                                                                             df.uf == 'RR',
                                                                                                                                             'NORTE',
                                                                                                                                             np.where(
                                                                                                                                                 df.uf == 'TO',
                                                                                                                                                 'NORTE',
                                                                                                                                                 np.where(
                                                                                                                                                     df.uf == 'ES',
                                                                                                                                                     'SUDESTE',
                                                                                                                                                     np.where(
                                                                                                                                                         df.uf == 'MG',
                                                                                                                                                         'SUDESTE',
                                                                                                                                                         np.where(
                                                                                                                                                             df.uf == 'RJ',
                                                                                                                                                             'SUDESTE',
                                                                                                                                                             np.where(
                                                                                                                                                                 df.uf == 'SP',
                                                                                                                                                                 'SUDESTE',
                                                                                                                                                                 np.where(
                                                                                                                                                                     df.uf == 'PR',
                                                                                                                                                                     'SUL',
                                                                                                                                                                     np.where(
                                                                                                                                                                         df.uf == 'RS',
                                                                                                                                                                         'SUL',
                                                                                                                                                                         np.where(
                                                                                                                                                                             df.uf == 'SC',
                                                                                                                                                                             'SUL',
                                                                                                                                                                             'NÃO IDENTIFICADO')))))))))))))))))))))))))))

df['lat'] = np.where(df.uf == 'DF', -15.83,
                     np.where(df.uf == 'GO', -15.98,
                              np.where(df.uf == 'MS', -20.51,
                                       np.where(df.uf == 'MT', -12.64,
                                                np.where(df.uf == 'AL', -9.62,
                                                         np.where(df.uf == 'BA', -13.29,
                                                                  np.where(df.uf == 'CE', -5.20,
                                                                           np.where(df.uf == 'MA', -5.42,
                                                                                    np.where(df.uf == 'PB', -7.28,
                                                                                             np.where(df.uf == 'PE',
                                                                                                      -8.38,
                                                                                                      np.where(
                                                                                                          df.uf == 'PI',
                                                                                                          -6.6,
                                                                                                          np.where(
                                                                                                              df.uf == 'RN',
                                                                                                              -5.81,
                                                                                                              np.where(
                                                                                                                  df.uf == 'SE',
                                                                                                                  -10.57,
                                                                                                                  np.where(
                                                                                                                      df.uf == 'AC',
                                                                                                                      -8.77,
                                                                                                                      np.where(
                                                                                                                          df.uf == 'AM',
                                                                                                                          -3.47,
                                                                                                                          np.where(
                                                                                                                              df.uf == 'AP',
                                                                                                                              1.41,
                                                                                                                              np.where(
                                                                                                                                  df.uf == 'PA',
                                                                                                                                  -3.79,
                                                                                                                                  np.where(
                                                                                                                                      df.uf == 'RO',
                                                                                                                                      -10.83,
                                                                                                                                      np.where(
                                                                                                                                          df.uf == 'RR',
                                                                                                                                          1.99,
                                                                                                                                          np.where(
                                                                                                                                              df.uf == 'TO',
                                                                                                                                              -9.46,
                                                                                                                                              np.where(
                                                                                                                                                  df.uf == 'ES',
                                                                                                                                                  -19.19,
                                                                                                                                                  np.where(
                                                                                                                                                      df.uf == 'MG',
                                                                                                                                                      -18.10,
                                                                                                                                                      np.where(
                                                                                                                                                          df.uf == 'RJ',
                                                                                                                                                          -22.25,
                                                                                                                                                          np.where(
                                                                                                                                                              df.uf == 'SP',
                                                                                                                                                              -22.19,
                                                                                                                                                              np.where(
                                                                                                                                                                  df.uf == 'PR',
                                                                                                                                                                  -24.89,
                                                                                                                                                                  np.where(
                                                                                                                                                                      df.uf == 'RS',
                                                                                                                                                                      -30.17,
                                                                                                                                                                      np.where(
                                                                                                                                                                          df.uf == 'SC',
                                                                                                                                                                          -27.45,
                                                                                                                                                                          'NÃO IDENTIFICADO')))))))))))))))))))))))))))

df['lon'] = np.where(df.uf == 'DF', -47.86,
                     np.where(df.uf == 'GO', -49.86,
                              np.where(df.uf == 'MS', -54.54,
                                       np.where(df.uf == 'MT', -55.42,
                                                np.where(df.uf == 'AL', -36.82,
                                                         np.where(df.uf == 'BA', -41.71,
                                                                  np.where(df.uf == 'CE', -39.53,
                                                                           np.where(df.uf == 'MA', -45.44,
                                                                                    np.where(df.uf == 'PB', -36.72,
                                                                                             np.where(df.uf == 'PE',
                                                                                                      -37.86,
                                                                                                      np.where(
                                                                                                          df.uf == 'PI',
                                                                                                          -42.28,
                                                                                                          np.where(
                                                                                                              df.uf == 'RN',
                                                                                                              -36.59,
                                                                                                              np.where(
                                                                                                                  df.uf == 'SE',
                                                                                                                  -37.45,
                                                                                                                  np.where(
                                                                                                                      df.uf == 'AC',
                                                                                                                      -70.55,
                                                                                                                      np.where(
                                                                                                                          df.uf == 'AM',
                                                                                                                          -65.10,
                                                                                                                          np.where(
                                                                                                                              df.uf == 'AP',
                                                                                                                              -51.77,
                                                                                                                              np.where(
                                                                                                                                  df.uf == 'PA',
                                                                                                                                  -52.48,
                                                                                                                                  np.where(
                                                                                                                                      df.uf == 'RO',
                                                                                                                                      -63.34,
                                                                                                                                      np.where(
                                                                                                                                          df.uf == 'RR',
                                                                                                                                          -61.33,
                                                                                                                                          np.where(
                                                                                                                                              df.uf == 'TO',
                                                                                                                                              -48.26,
                                                                                                                                              np.where(
                                                                                                                                                  df.uf == 'ES',
                                                                                                                                                  -40.34,
                                                                                                                                                  np.where(
                                                                                                                                                      df.uf == 'MG',
                                                                                                                                                      -44.38,
                                                                                                                                                      np.where(
                                                                                                                                                          df.uf == 'RJ',
                                                                                                                                                          -42.66,
                                                                                                                                                          np.where(
                                                                                                                                                              df.uf == 'SP',
                                                                                                                                                              -48.79,
                                                                                                                                                              np.where(
                                                                                                                                                                  df.uf == 'PR',
                                                                                                                                                                  -51.55,
                                                                                                                                                                  np.where(
                                                                                                                                                                      df.uf == 'RS',
                                                                                                                                                                      -53.50,
                                                                                                                                                                      np.where(
                                                                                                                                                                          df.uf == 'SC',
                                                                                                                                                                          -50.95,
                                                                                                                                                                          'NÃO IDENTIFICADO')))))))))))))))))))))))))))

# Menu
st.sidebar.image('https://www.gov.br/dnit/pt-br/servicos-/assinaturas-e-marcas/monocromatica-dnit-padrao.png',
                 width=300)
st.sidebar.header('Menu')
paginaSelecionada = st.sidebar.selectbox('Selecione:',
                                         ['Apresentação', 'Base de Dados', 'Análise Exploratória', 'Dashboard'])

if paginaSelecionada == 'Apresentação':
    st.title('APRESENTAÇÃO')
    st.subheader('Departamento Nacional de Infraestrutura de Transportes - DNIT')
    st.markdown('''
    O DNIT é uma autarquia federal vinculada ao Ministério da Infraestrutura, criada pela lei nº 10.233, de 5 de junho 
    de 2001. A legislação reestruturou o sistema de transportes rodoviário, aquaviário e ferroviário do Brasil, extinguindo 
    o antigo Departamento Nacional de Estradas de Rodagem (DNER). A sede do DNIT é em Brasília, no Distrito Federal. 
    
    Atualmente, possui 25 unidades administrativas regionais e 8 administrações hidroviárias. 
    A autarquia tem por objetivo implementar a política de infraestrutura de transportes terrestres e aquaviários, 
    contribuindo para o desenvolvimento sustentável do país. Os recursos para a execução das obras são da União.
    
    Ou seja, o órgão é gestor e executor, sob a jurisdição do Ministério da Infraestrutura, das vias navegáveis, ferrovias e rodovias 
    federais, instalações de vias de transbordo e de interface intermodal e instalações portuárias fluviais e lacustres.
                
    Além disso, o DNIT, é o órgão da União competente para exercer as atribuições elencadas no 
    art. 21 do Código de Trânsito Brasileiro: nas rodovias federais, ele é responsável pela 
    aplicação de multas por excesso de peso e ou de velocidade, por meio dos postos de pesagem e 
    das lombadas eletrônicas.
                
    O DNIT tem como missão implementar a política de infraestrutura de transportes terrestres e 
    aquaviários, contribuindo para o desenvolvimento sustentável do país. O DNIT é administrado 
    pelo diretor-geral e por mais seis diretores setoriais nomeados pelo Presidente da República,
    que integram a Diretoria Colegiada.
                
    As deliberações ocorrem por meio desta Diretoria e do Conselho Administrativo, que é composto
    por seis membros: secretário executivo do Ministério do Transportes, diretor geral do DNIT,
    dois representantes do Ministério da Infraestrutura, um representante do Ministério do
    Planejamento, Orçamento e Gestão e um representante do Ministério da Fazenda.
                
    Nossa visão é ser reconhecido até 2022 pela gestão de uma infraestrutura de transportes com
    padrões de excelência na América Latina.''')
    st.subheader('Diretoria de Planejamento e Pesquisa - DPP')
    st.markdown('''
    A Diretoria de Planejamento e Pesquisa (DPP) é uma das sete diretorias que formam o núcleo de decisão 
    do Departamento Nacional de Infraestrutura de Transportes (DNIT).
    
    À DPP compete:
    
    * planejar, coordenar, supervisionar e executar ações relativas à gestão e à programação de investimentos anual e 
    plurianual para a infra-estrutura do Sistema Federal de Viação.
    
    * Subsidiar o DNIT nos aspectos relacionados à sua participação na formulação dos planos gerais de outorgas dos 
    segmentos da infra-estrutura viária, coordenando o processo de planejamento estratégico do DNIT.
    
    * Orientar as unidades do DNIT no planejamento e gerenciamento das suas atividades, propondo a política de gestão 
    ambiental do DNIT e coordenar as atividades de meio ambiente nos empreendimentos de infra-estrutura e operação dos 
    transportes.
    
    * Acompanhar e avaliar o desempenho das atividades do DNIT, promovendo pesquisas e estudos nas áreas de engenharia 
    da infra-estrutura de transportes, considerando, inclusive, os aspectos relativos ao meio ambiente, definindo 
    padrões e normas técnicas para o desenvolvimento e controle de projetos e obras terrestres e aquaviárias.
    
    * Planejar, promover, implementar e monitorar programas de desenvolvimento tecnológico e de capacitação técnica, 
    subsidiando o Ministério dos Transportes na articulação com entidades públicas e privadas, nacionais e 
    internacionais, para obter financiamento de programas, projetos e obras, bem como realizar programas de estudos e 
    pesquisas.
    
    * Organizar, manter e divulgar as informações estatísticas do setor de infra-estrutura viária, gerenciar as ações 
    para elaboração e análise de projetos de engenharia aquaviária, ferroviária e rodoviária e aprovar projetos de 
    engenharia aquaviária, ferroviária e rodoviária.
    
    A DPP é composta das seguintes Coordenações:
    
    * Coordenação-Geral de Planejamento e Programação de Investimentos - CGPLAN
    * Coordenação-Geral de Desenvolvimento de Projetos - CGDESP
    * Coordenação-Geral de Meio Ambiente - CGMAB
    * Coordenação-Geral de Desapropriação e Reassentamento - CGDR
    * Coordenação-Geral de Custos de Infraestrutura de Transportes - CGCIT
    * Instituto de Pesquisa Rodoviárias - IPR
    * Instituto Nacional de Pesquisas Hidroviárias - INPH''')
    st.subheader('Coordenação-Geral de Custos de Infraestrutura de Transportes - CGCIT')
    st.markdown('''
    A Coordenação-Geral de Custos de Infraestrutura é responsável pela alimentação do Sistema de Custos Referenciais de 
    Obras (SICRO), que permite a manutenção de composições de custos horárias/unitárias, eliminação de custos indiretos 
    das composições de custos, adequação de preços em função do fator de influência de chuvas, entre outros. Bem como, 
    cabe à CGCIT a análise de custos que não são considerados preços-novos, isto é, aqueles preços que não estão 
    presentes no SICRO.
    
    Com isto em mente, existe entre as divisões da CGCIT, a Divisão de Preços Novos (DPN), que é responsável por esta 
    análise. Regularmente, a DPN emite uma análise de economia ao erário, como forma de avaliar seu desempenho e 
    registrar os resultados de seu empenho.
    
    Portanto, considerando que tais dados geram uma grande quantidade de informações, bem como visando a celeridade na 
    análise destas, tomou-se a iniciativa de adptar a metodologia de tratamento e compartilhamento destas informações às 
    atuais ferramentas presentes no campo do conhecimento de ciência de dados.
    
    Para isso, a modelagem da informação se utilizará da linguagem de programação Python, bem como das bibliotecas 
    vinculadas a ela. Intenciona-se também criar um dashboard que permitirá a visualização dos resultados e facilitará 
    seu compartilhamento.''')

elif paginaSelecionada == 'Base de Dados':
    st.title('BASE DE DADOS')
    st.markdown('''
    Os dados que formam o dataframe vêm do registro manual em planilha de Excel dos preços novos aprovados. 
    Por este motivo, esta planilha foi adaptada para os fins desta análise, sem quaisquer alterações em seus valores, 
    para o formato 'csv' visando facilitar o acesso aos dados.''')

    # Dataframe
    st.subheader('Dataframe')
    dfDrop = df.drop(
        columns=['id serviço', 'regiao', 'ano', 'modalidade', 'tipo de indice', 'indice inicial', 'indice final', 'lat',
                 'indice atual', 'peso por uf', 'variacao final x inicial atual', 'variacao ponderada atual',
                 'lon', 'mês', 'dia'])
    st.write(dfDrop)

    # Características
    economia = df['economia atual'].sum()
    st.subheader(
        f""" Características Gerais do Dataframe: 
- Linha Temporal: {sorted(df[DATE_TIME].dt.month)[0]}/{df[DATE_TIME].dt.year.min()} - {df[DATE_TIME].dt.month.iloc[-1]}/{df[DATE_TIME].dt.year.max()}
- Dimensões: {df.shape[0]} linhas e {dfDrop.shape[1]} colunas
- Analistas: {df.groupby('analista').analista.nunique().sum()}
- Modais: {df.groupby('modalidade').modalidade.nunique().sum()}
- Vias: {df.groupby('via').via.nunique().sum()}
- Regiões: {df.groupby('regiao').regiao.nunique().sum()}
- Unidades Federativas: {df.groupby('uf').uf.nunique().sum()}
- Tipos de Processo: {df.groupby('tipo').tipo.nunique().sum()}
- Processos: {df.groupby('processo').processo.nunique().sum()}
- Preços Novos: {df.shape[0]}
""")
    # - Economia Total: {(f'R$ {economia:.2f}'.format(economia).replace('.', ','))}

elif paginaSelecionada == 'Análise Exploratória':
    st.title('ANÁLISE EXPLORATÓRIA')
    st.markdown('Dada à extensão do dataframe e a critério explorativo, se verificará a quantidade de dados nulos '
                'presentes no dataframe para cada coluna.')
    st.write(df.isnull().sum())
    st.markdown('''
    É importante destacar que a existências desses dados não interfirirá na análise neste momento, bem como vale elucidar 
    que muitas análises técnicas produzidas pela Divisão de Preços Novos carecem de informações por parte das empresas 
    orçamentistas, o que promove a remoção de alguns preços mesmo com o tratamento posterior dado pela DPN, por isso é comum 
    serviços com dados faltantes, reforçando a complexidade do serviço desempenhado pela CGCIT.
    
    Posto isto, em prosseguimento a análise exploratória dos dados, pode-se verificar as seguintes distribuições percentuais dos 
    preços de acordo com:
    ''')

    #Distribuição de preços por ano
    st.markdown('- Ano:')
    df['ano finalizacao'] = df['data finalizacao'].dt.year
    import plotly.express as px

    data_ano = sorted(df['ano finalizacao'].unique())
    data_ano_values = df.groupby('ano finalizacao')['id serviço'].sum()

    fig_ano = px.pie(df, values=data_ano_values, names=data_ano,
                 color_discrete_sequence=px.colors.sequential.haline)
    fig_ano.update_traces(textposition='inside')
    fig_ano.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    st.write(fig_ano)

    #Distribuição de preços por mês
    import calendar

    df['mes finalizacao'] = df['mês']
    df['mes finalizacao'] = df['mes finalizacao'].apply(lambda x: calendar.month_name[x])

    st.markdown('- Mês:')

    data_mes = sorted(df['mes finalizacao'].unique())
    data_mes_values = df.groupby('mes finalizacao')['id serviço'].sum()

    fig_mes = px.pie(df, values=data_mes_values, names=data_mes,
                 color_discrete_sequence=px.colors.sequential.haline)
    fig_mes.update_traces(textposition='inside')
    fig_mes.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    st.write(fig_mes)

    #Distribuição de preços por ano e mês
    st.markdown('- Ano/Mês:')
    fig_ano_mes = px.sunburst(df, path=['ano finalizacao', 'mes finalizacao'], values='id serviço',
                      color_discrete_sequence=px.colors.sequential.haline)
    st.write(fig_ano_mes)

    #Distribuição de preços por região
    st.markdown('- Região:')
    data_regiao = sorted(df.regiao.unique())
    data_regiao_values = df.groupby('regiao')['id serviço'].sum()

    fig = px.pie(df, values=data_regiao_values, names=data_regiao,
                 color_discrete_sequence=px.colors.sequential.haline)
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    st.write(fig)

    #Distribuição de preços por unidade federativa
    st.markdown('''- Unidade Federativa:''')
    data_uf = sorted(df.uf.unique())
    data_uf_values = df.groupby('uf')['id serviço'].sum()

    fig = px.pie(df, values=data_uf_values, names=data_uf,
                 color_discrete_sequence=px.colors.sequential.haline)
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    st.write(fig)

    #Distribuição de preços por tipo de processo
    st.markdown('- Tipo de Processo:')

    df.tipo = df.tipo.astype('str')
    data_tipo_proc = sorted(df.tipo.unique())
    data_tipo_proc_values = df.groupby('tipo')['id serviço'].sum()

    fig = px.pie(df, values=data_tipo_proc_values, names=data_tipo_proc,
                 color_discrete_sequence=px.colors.sequential.haline)
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    st.write(fig)

    st.markdown('''Onde:

    - AD - Ação Demolitória
    - AP - Anteprojeto
    - CREMA - Contrato de Restauração e Manutenção
    - DRAG - Dragagem
    - EVTEA - Estudo de Viabilidade Técnica, Econômica e Ambiental
    - IP4 - Instalações Portuárias de Pequeno Porte
    - PATO - Plano Anual e bianual de Trabalho e Orçamento
    - PB - Projeto Básico
    - PE - Projeto Executivo
    - PMH - Plano de Monitoramento Hidroviário
    - PRAD - Projeto de Recuperação de Áreas Degradadas
    - RPFO - Revisão de Projeto em Fase de Obras''')

    #Definir a economia ao erário
    st.markdown(
        f'Como conclusão, é notável a participação do Estado do RJ, da região SUDESTE e dos Processos Executivos (PE) no '
        f'dataframe. Contudo, importa perceber que tais participações se dão no campo quantitativo e que, em termos '
        f'financeiros, as distribuições se dão da seguinte forma:')
    df['id serviço'] = 1
    df = df.rename({'id serviço': 'preço novo'}, axis=1)

    #Tabela Ano
    st.markdown('- Ano:')
    import plotly.figure_factory as ff

    group_ano = df.groupby(['ano finalizacao'])
    groupPreçoNovoAno = group_ano['preço novo'].agg('sum')
    groupEconomiaAno = group_ano['economia atual'].agg('sum')
    groupEconomiaAnual = groupEconomiaAno

    data_matrix_ano = [['Ano', 'Processos', 'Preços Novos', 'Economia Atual'],
                       [df['ano finalizacao'].sort_values().unique()[0],
                        df.groupby('ano finalizacao').processo.nunique().iloc[0],
                        groupPreçoNovoAno.iloc[0],
                        locale.currency(groupEconomiaAnual.iloc[0], grouping=True, symbol='R$')],
                       [df['ano finalizacao'].sort_values().unique()[1],
                        df.groupby('ano finalizacao').processo.nunique().iloc[1],
                        groupPreçoNovoAno.iloc[1],
                        locale.currency(groupEconomiaAnual.iloc[1], grouping=True, symbol='R$')]
                       ]

    figAno = ff.create_table(data_matrix_ano)
    st.write(figAno)

    #Tabela Região
    st.markdown('- Região:')
    import plotly.figure_factory as ff

    grouped = df.groupby(['regiao'])
    dataPreçoNovo1 = grouped['preço novo'].agg('sum')
    dataEconomiaAtual1 = grouped['economia atual'].agg('sum')
    dataEconomiaAtualFormat1 = dataEconomiaAtual1

    #Confecção tabela
    data_matrix1 = [['Região', 'Processos', 'Preços Novos', 'Economia Atual'],
                    [df.regiao.sort_values().unique()[0], df.groupby('regiao').processo.nunique()[0],
                     dataPreçoNovo1[0], locale.currency(dataEconomiaAtualFormat1[0], grouping=True, symbol='R$')],
                    [df.regiao.sort_values().unique()[1], df.groupby('regiao').processo.nunique()[1],
                     dataPreçoNovo1[1], locale.currency(dataEconomiaAtualFormat1[1], grouping=True, symbol='R$')],
                    [df.regiao.sort_values().unique()[2], df.groupby('regiao').processo.nunique()[2],
                     dataPreçoNovo1[2], locale.currency(dataEconomiaAtualFormat1[2], grouping=True, symbol='R$')],
                    [df.regiao.sort_values().unique()[3], df.groupby('regiao').processo.nunique()[3],
                     dataPreçoNovo1[3], locale.currency(dataEconomiaAtualFormat1[3], grouping=True, symbol='R$')],
                    [df.regiao.sort_values().unique()[4], df.groupby('regiao').processo.nunique()[4],
                     dataPreçoNovo1[4], locale.currency(dataEconomiaAtualFormat1[4], grouping=True, symbol='R$')]]

    fig1 = ff.create_table(data_matrix1)
    st.write(fig1)

    #Tabela Economia por Unidade Federativa
    st.markdown('- Unidade Federativa:')
    grouped6 = df.groupby(['uf'])
    dataPreçoNovo6 = grouped6['preço novo'].agg('sum')
    dataEconomiaAtual6 = grouped6['economia atual'].agg('sum')
    dataEconomiaAtualFormat6 = dataEconomiaAtual6

    import plotly.figure_factory as ff

    data_matrix6 = [['UF', 'Processos', 'Preços Novos', 'Economia Atual'],
                    [df.uf.sort_values().unique()[0], df.groupby('uf').processo.nunique()[0],
                     dataPreçoNovo6[0],
                     locale.currency(dataEconomiaAtualFormat6[0], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[1], df.groupby('uf').processo.nunique()[1],
                     dataPreçoNovo6[1],
                     locale.currency(dataEconomiaAtualFormat6[1], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[2], df.groupby('uf').processo.nunique()[2],
                     dataPreçoNovo6[2],
                     locale.currency(dataEconomiaAtualFormat6[2], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[3], df.groupby('uf').processo.nunique()[3],
                     dataPreçoNovo6[3],
                     locale.currency(dataEconomiaAtualFormat6[3], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[4], df.groupby('uf').processo.nunique()[4],
                     dataPreçoNovo6[4],
                     locale.currency(dataEconomiaAtualFormat6[4], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[5], df.groupby('uf').processo.nunique()[5],
                     dataPreçoNovo6[5],
                     locale.currency(dataEconomiaAtualFormat6[5], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[6], df.groupby('uf').processo.nunique()[6],
                     dataPreçoNovo6[6],
                     locale.currency(dataEconomiaAtualFormat6[6], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[7], df.groupby('uf').processo.nunique()[7],
                     dataPreçoNovo6[7],
                     locale.currency(dataEconomiaAtualFormat6[7], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[8], df.groupby('uf').processo.nunique()[8],
                     dataPreçoNovo6[8],
                     locale.currency(dataEconomiaAtualFormat6[8], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[9], df.groupby('uf').processo.nunique()[9],
                     dataPreçoNovo6[9],
                     locale.currency(dataEconomiaAtualFormat6[9], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[10], df.groupby('uf').processo.nunique()[10],
                     dataPreçoNovo6[10],
                     locale.currency(dataEconomiaAtualFormat6[10], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[11], df.groupby('uf').processo.nunique()[11],
                     dataPreçoNovo6[11],
                     locale.currency(dataEconomiaAtualFormat6[11], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[12], df.groupby('uf').processo.nunique()[12],
                     dataPreçoNovo6[12],
                     locale.currency(dataEconomiaAtualFormat6[12], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[13], df.groupby('uf').processo.nunique()[13],
                     dataPreçoNovo6[13],
                     locale.currency(dataEconomiaAtualFormat6[13], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[14], df.groupby('uf').processo.nunique()[14],
                     dataPreçoNovo6[14],
                     locale.currency(dataEconomiaAtualFormat6[14], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[15], df.groupby('uf').processo.nunique()[15],
                     dataPreçoNovo6[15],
                     locale.currency(dataEconomiaAtualFormat6[15], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[16], df.groupby('uf').processo.nunique()[16],
                     dataPreçoNovo6[16],
                     locale.currency(dataEconomiaAtualFormat6[16], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[17], df.groupby('uf').processo.nunique()[17],
                     dataPreçoNovo6[17],
                     locale.currency(dataEconomiaAtualFormat6[17], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[18], df.groupby('uf').processo.nunique()[18],
                     dataPreçoNovo6[18],
                     locale.currency(dataEconomiaAtualFormat6[18], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[19], df.groupby('uf').processo.nunique()[19],
                     dataPreçoNovo6[19],
                     locale.currency(dataEconomiaAtualFormat6[19], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[20], df.groupby('uf').processo.nunique()[20],
                     dataPreçoNovo6[20],
                     locale.currency(dataEconomiaAtualFormat6[20], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[21], df.groupby('uf').processo.nunique()[21],
                     dataPreçoNovo6[21],
                     locale.currency(dataEconomiaAtualFormat6[21], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[22], df.groupby('uf').processo.nunique()[22],
                     dataPreçoNovo6[22],
                     locale.currency(dataEconomiaAtualFormat6[22], grouping=True, symbol='R$')],
                    [df.uf.sort_values().unique()[23], df.groupby('uf').processo.nunique()[23],
                     dataPreçoNovo6[23],
                     locale.currency(dataEconomiaAtualFormat6[23], grouping=True, symbol='R$')]
                    ]

    fig6 = ff.create_table(data_matrix6)
    st.write(fig6)

    st.markdown('''- Tipo de Processo:''')

    #Tabela Economia por Tipo de Processo
    import plotly.figure_factory as ff

    grouped3 = df.groupby(['tipo'])
    dataPreçoNovo3 = grouped3['preço novo'].agg('sum')
    dataEconomiaAtual3 = grouped3['economia atual'].agg('sum')
    dataEconomiaAtualFormat3 = dataEconomiaAtual3

    #Confecção tabela
    data_matrix3 = [['Tipo', 'Processos', 'Preços Novos', 'Economia Atual'],
                    [df.tipo.sort_values().unique()[0], df.groupby('tipo').processo.nunique()[0],
                     dataPreçoNovo3[0], locale.currency(dataEconomiaAtualFormat3[0], grouping=True, symbol='R$')],
                    [df.tipo.sort_values().unique()[1], df.groupby('tipo').processo.nunique()[1],
                     dataPreçoNovo3[1], locale.currency(dataEconomiaAtualFormat3[1], grouping=True, symbol='R$')],
                    [df.tipo.sort_values().unique()[2], df.groupby('tipo').processo.nunique()[2],
                     dataPreçoNovo3[2], locale.currency(dataEconomiaAtualFormat3[2], grouping=True, symbol='R$')],
                    [df.tipo.sort_values().unique()[3], df.groupby('tipo').processo.nunique()[3],
                     dataPreçoNovo3[3], locale.currency(dataEconomiaAtualFormat3[3], grouping=True, symbol='R$')],
                    [df.tipo.sort_values().unique()[4], df.groupby('tipo').processo.nunique()[4],
                     dataPreçoNovo3[4], locale.currency(dataEconomiaAtualFormat3[4], grouping=True, symbol='R$')],
                    [df.tipo.sort_values().unique()[5], df.groupby('tipo').processo.nunique()[5],
                     dataPreçoNovo3[5], locale.currency(dataEconomiaAtualFormat3[5], grouping=True, symbol='R$')],
                    [df.tipo.sort_values().unique()[6], df.groupby('tipo').processo.nunique()[6],
                     dataPreçoNovo3[6], locale.currency(dataEconomiaAtualFormat3[6], grouping=True, symbol='R$')],
                    [df.tipo.sort_values().unique()[7], df.groupby('tipo').processo.nunique()[7],
                     dataPreçoNovo3[7], locale.currency(dataEconomiaAtualFormat3[7], grouping=True, symbol='R$')],
                    [df.tipo.sort_values().unique()[8], df.groupby('tipo').processo.nunique()[8],
                     dataPreçoNovo3[8], locale.currency(dataEconomiaAtualFormat3[8], grouping=True, symbol='R$')],
                    [df.tipo.sort_values().unique()[9], df.groupby('tipo').processo.nunique()[9],
                     dataPreçoNovo3[9], locale.currency(dataEconomiaAtualFormat3[9], grouping=True, symbol='R$')],
                    [df.tipo.sort_values().unique()[10], df.groupby('tipo').processo.nunique()[10],
                     dataPreçoNovo3[10], locale.currency(dataEconomiaAtualFormat3[10], grouping=True, symbol='R$')],
                    [df.tipo.sort_values().unique()[11], df.groupby('tipo').processo.nunique()[11],
                     dataPreçoNovo3[11], locale.currency(dataEconomiaAtualFormat3[11], grouping=True, symbol='R$')]]

    fig3 = ff.create_table(data_matrix3)
    st.write(fig3)

    #Tabela Economia por Analista
    st.markdown('A critério gerencial, também se pode demonstrar a quantidade de preços e processos distribuidos por '
                'analista, bem como sua respectiva economia:')

    import plotly.figure_factory as ff

    grouped2 = df.groupby(['analista'])
    dataPreçoNovo = grouped2['preço novo'].agg('sum')
    dataEconomiaAtual = grouped2['economia atual'].agg('sum')
    dataEconomiaAtualFormat = dataEconomiaAtual

    #Confecção tabela
    data_matrix = [['Analista', 'Processos', 'Preços Novos', 'Economia Atual'],
                   [df.analista.sort_values().unique()[0], df.groupby('analista').processo.nunique()[0],
                    dataPreçoNovo[0], locale.currency(dataEconomiaAtualFormat[0], grouping=True, symbol='R$')],
                   [df.analista.sort_values().unique()[1], df.groupby('analista').processo.nunique()[1],
                    dataPreçoNovo[1], locale.currency(dataEconomiaAtualFormat[1], grouping=True, symbol='R$')],
                   [df.analista.sort_values().unique()[2], df.groupby('analista').processo.nunique()[2],
                    dataPreçoNovo[2], locale.currency(dataEconomiaAtualFormat[2], grouping=True, symbol='R$')],
                   [df.analista.sort_values().unique()[3], df.groupby('analista').processo.nunique()[3],
                    dataPreçoNovo[3], locale.currency(dataEconomiaAtualFormat[3], grouping=True, symbol='R$')],
                   [df.analista.sort_values().unique()[4], df.groupby('analista').processo.nunique()[4],
                    dataPreçoNovo[4], locale.currency(dataEconomiaAtualFormat[4], grouping=True, symbol='R$')],
                   [df.analista.sort_values().unique()[5], df.groupby('analista').processo.nunique()[5],
                    dataPreçoNovo[5], locale.currency(dataEconomiaAtualFormat[5], grouping=True, symbol='R$')],
                   [df.analista.sort_values().unique()[6], df.groupby('analista').processo.nunique()[6],
                    dataPreçoNovo[6], locale.currency(dataEconomiaAtualFormat[6], grouping=True, symbol='R$')],
                   [df.analista.sort_values().unique()[7], df.groupby('analista').processo.nunique()[7],
                    dataPreçoNovo[7], locale.currency(dataEconomiaAtualFormat[7], grouping=True, symbol='R$')],
                   [df.analista.sort_values().unique()[8], df.groupby('analista').processo.nunique()[8],
                    dataPreçoNovo[8], locale.currency(dataEconomiaAtualFormat[8], grouping=True, symbol='R$')],
                   [df.analista.sort_values().unique()[9], df.groupby('analista').processo.nunique()[9],
                    dataPreçoNovo[9], locale.currency(dataEconomiaAtualFormat[9], grouping=True, symbol='R$')],
                   [df.analista.sort_values().unique()[10], df.groupby('analista').processo.nunique()[10],
                    dataPreçoNovo[10], locale.currency(dataEconomiaAtualFormat[10], grouping=True, symbol='R$')]]

    fig = ff.create_table(data_matrix)
    st.write(fig)

    filtro = (df.groupby('ano').analista.nunique()) - 1  # correção
    st.markdown(
        f'''Importa destacar que a dinâmica no serviço público possibilita a locomoção horizontal e vertical de seus
                servidores e colaboradores, por este motivo, muitos dos analistas citados já não se encontram locados
                na DPN. **No ano de {df['ano'].max()}, a divisão contou com uma equipe de {filtro.iloc[1]} analistas.**''')  # filtro.iloc[1] é a soma de analistas para 2020

    #Tabela Economia por Orgão Responsável
    st.markdown(f'''Também a critério gerencial, se entende interessante demonstrar a distribuição de preços novos, 
                processos e economia por orgão responsável, como forma de visualizar com mais clareza como funciona
                a dinâmica interna da DPN e a importânica do Contrato nº 559/2018 – DNIT firmado com a FGV.''')

    grouped4 = df.groupby(['orgao responsavel'])
    dataPreçoNovo4 = grouped4['preço novo'].agg('sum')
    dataEconomiaAtual4 = grouped4['economia atual'].agg('sum')
    dataEconomiaAtualFormat4 = dataEconomiaAtual4

    #Confecção tabela
    data_matrix4 = [['Orgão Responsável', 'Processos', 'Preços Novos', 'Economia Atual'],
                    [df['orgao responsavel'].sort_values().unique()[0],
                     df.groupby('orgao responsavel').processo.nunique()[0], dataPreçoNovo4[0],
                     locale.currency(dataEconomiaAtualFormat4[0], grouping=True, symbol='R$')],
                    [df['orgao responsavel'].sort_values().unique()[1],
                     df.groupby('orgao responsavel').processo.nunique()[1], dataPreçoNovo4[1],
                     locale.currency(dataEconomiaAtualFormat4[1], grouping=True, symbol='R$')]]

    fig4 = ff.create_table(data_matrix4)
    st.write(fig4)

    st.markdown('''Fica evidente assim como a FGV dá suporte ao DNIT na vazão de análises, permitindo que os processos
    mais emblemáticos, desafiantes tecnicamente e que, consequentemente, promovem maior economia ao erário sejam analisados
    pelos servidores públicos atuantes na DPN.''')

    #Tabela Resumo
    st.markdown('''Como resumo, os seguintes dados podem ser extraidos:''')
    data_matrix7 = [['', 'Processos', 'Preços Novos', 'Economia Atual'],
                    ['TOTAL', df.processo.nunique(), df['preço novo'].sum(),
                     locale.currency(df['economia atual'].sum(), grouping=True, symbol='R$')]]

    fig7 = ff.create_table(data_matrix7)
    st.write(fig7)

    #Observações
    processo_max = df.sort_values('economia atual')
    st.subheader('Observações:')
    st.markdown(f'''- Processo com maior economia individual: {processo_max.processo.iloc[0]}''')
    st.markdown(f'''- Unidade Federativa com maior economia individual: {processo_max.uf.iloc[0]}''')
    st.markdown(f'''- Mês-base atual: {df.mês.iloc[-1] - 1}/{df.ano.iloc[-1]}''')

    if st.sidebar.checkbox('WordCloud',value=False,key=None):
        st.markdown('A critério de curiosidade, apresenta-se a seguir as palavras mais recorrentes entre os '
                'preços novos:')

        #Nuvem de palavras
        import matplotlib.pyplot as plt
        from wordcloud import WordCloud, STOPWORDS

        summary = df['descricao servico']
        all_summary = " ".join(s for s in summary)

        # lista de stopword
        stopwords = set(STOPWORDS)
        stopwords.update(['da','e','mm','mm2','km','=','ª','das','de','D=','/','para'])

        # gerar uma wordcloud
        wordcloud = WordCloud(stopwords=stopwords,
                              background_color="white",
                              width=1000, height=800, max_words=1000,
                              max_font_size=100,
                              min_font_size=1).generate(all_summary)

        # mostrar a imagem final
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.set_axis_off()

        plt.imshow(wordcloud)
        wordcloud.to_file("preços_summary_wordcloud.png")
        st.pyplot(fig)

else:
    st.title('DASHBOARD')
    #MAIN
    st.subheader('DASHBOARD GERENCIAL DPN/CGCIT')
    st.markdown(
        f"""Este é um aplicativo que permite a visualização dos dados relacionados à economia ao erário promovidos 
            pela Divisão de Preços Novos (DPN) e sua distribuição temporal e geográfica no Brasil entre os anos 
            {df['ano'].min()} e {df['ano'].max()}. Use os controles laterais para escolher uma data específica e ver 
            como os gráficos mudam.
        """)
    import calendar
    df['ano finalizacao'] = df['data finalizacao'].dt.year
    df['mes finalizacao'] = df['mês']
    df['mes finalizacao'] = df['mes finalizacao'].apply(lambda x: calendar.month_name[x])

    #Sidebar-filtros
    st.sidebar.subheader('Filtros')

    #Mapa
    df['id serviço'] = 1
    df = df.rename({'id serviço': 'preço novo'}, axis=1)
    df.lat = df.lat.apply(lambda x: str(x).replace(',', '.'))
    df.lat = df.lat.astype('float64')
    df.lon = df.lon.apply(lambda x: str(x).replace(',', '.'))
    df.lon = df.lon.astype('float64')

    anoEscolhido = st.sidebar.slider('Ano:', 2019, 2020)
    mesEscolhido = st.sidebar.slider('Mês:',1, 12)
    data = df[(df['ano'] == anoEscolhido) & (df['mês'] == mesEscolhido)]
    midpoint = (np.average(data['lat']), np.average(data['lon']))
    dff = data[['uf','regiao','tipo','preço novo','economia atual','lat','lon','ano finalizacao','mes finalizacao']]

    #Mapa métricas
    dataFinal = pd.to_datetime((df.ano*10000+df.mês*100+df.dia).apply(str),format='%Y%m%d')
    df['data final'] = dataFinal
    data = df[(df['ano'] == anoEscolhido) & (df['mês'] == mesEscolhido)]
    dff = data[
        ['uf','regiao','tipo','preço novo','economia atual','lat','lon','ano finalizacao','mes finalizacao','data final',
         'analista','processo']]

    metrics = ['preço novo','economia atual']
    cols = st.selectbox('Métricas de Economia ao Erário: ', metrics)

    if cols in metrics:
        metric_to_show_in_economic_Layer = cols

    if metric_to_show_in_economic_Layer == 'preço novo':
        dff['metric_to_show_in_economic_Layer'] = dff['preço novo'].apply(lambda preço_count: np.sum(preço_count))
    elif metric_to_show_in_economic_Layer == 'economia atual':
        dff['metric_to_show_in_economic_Layer'] = dff['economia atual'].apply(lambda economia_count: np.sum(economia_count)) * -1 #economia é negativa

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v10',
        initial_view_state={
            'latitude': midpoint[0]-5,
            'longitude': midpoint[1]-7,
            'zoom': 3,
            'pitch': 0
        },
        tooltip={"html": "<b>Preços Novos:</b> {elevationValue}"
                         "<br/> <b>Processo:</b> {processo}"
                         "<br/> <b>Tipo:</b> {tipo}"                         
                         "<br/> <b>Região:</b> {regiao}"
                         "<br/> <b>UF:</b> {uf}"
                         "<br/> <b>Analista:</b> {analista}",
                 "style": {"color": "white"}},
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=dff,
                pickable=True,
                opacity=0.3,
                stroked=True,
                filled=True,
                radius_scale=10,
                radius_min_pixels=10,
                radius_max_pixels=30,
                line_width_min_pixels=1,
                get_position=['lon', 'lat'],
                get_radius="[metric_to_show_in_economic_Layer]",
                get_fill_color=[252, 136, 3],
                get_line_color=[255, 0, 0],
            ),
            pdk.Layer(
                'HexagonLayer',
                data=dff,
                radius=100000,
                get_position=['lon', 'lat'],
                auto_highlight=False,
                elevation_scale=50,
                elevation_range=[0, 4000],
                pickable=True,
                opacity=0.00001,
                extruded=True,
                coverage=1,
            ),
        ],
    ))

    #Tabela auxiliar - Gráfico de Barras (Economia/UF - Contagem/Tipo)
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    ufTable = dff['uf'].unique()
    tipoTable = dff['tipo'].unique()
    economiaTable = dff['economia atual']

    fig = make_subplots(rows=1, cols=2)
    fig.add_trace(go.Bar(
        x=ufTable,
        y=economiaTable,
        name='economia atual',
        marker_color='navy'
    ),row=1, col=1)

    fig.add_trace(go.Bar(
        x=tipoTable,
        y=dff['tipo'].value_counts(),
        name='tipo de processo',
        marker_color='orange'
    ),row=1, col=2)

    fig.update_layout(barmode='group', xaxis_tickangle=0)
    st.plotly_chart(fig)

    #TESTEEEEEEEEEEEEEEEEEE - Gráfico de Pizza
    #import plotly.express as px
    #st.markdown('- Resumo:')
    #fig_ano_mes = px.sunburst(dff, path=['ano finalizacao','mes finalizacao','regiao','uf','tipo'], values='preço novo',
    #                  color_discrete_sequence=px.colors.sequential.Plasma)
    #st.write(fig_ano_mes)

    #TESTEEEEEEE 2 - Player Evolutivo
    #dataFinal = pd.to_datetime((df.ano*10000+df.mês*100+df.dia).apply(str),format='%Y%m%d')
    #df.dataFinal = dataFinal

    #fig = px.bar(df, x="regiao", y="economia atual", color="regiao",
    #             animation_frame="ano", animation_group="uf", range_y=[0, 20000000])
    #st.write(fig)







