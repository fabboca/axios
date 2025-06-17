# teste

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Ficha de Alunos", page_icon="🧘‍♀️")

st.title('Ficha de Alunos - Pilates')

# 🔸 Arquivo onde os dados serão salvos
DATA_FILE = 'alunos.csv'

# 🔹 Função para carregar dados
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=['Nome', 'Telefone', 'Email', 'Data Nascimento', 'Objetivo', 'Observações'])

# 🔹 Função para salvar dados
def save_data(df):
    df.to_csv(DATA_FILE, index=False)

# 🔹 Carregar dados existentes
data = load_data()

# 🔸 Menu lateral
st.sidebar.title('Menu')
menu = st.sidebar.selectbox('Selecione a opção', ['Cadastrar Aluno', 'Visualizar Alunos'])

# 🔸 Cadastro
if menu == 'Cadastrar Aluno':
    st.subheader('Cadastrar novo aluno')

    nome = st.text_input('Nome completo')
    telefone = st.text_input('Telefone')
    email = st.text_input('Email')
    nascimento = st.date_input('Data de nascimento')
    objetivo = st.text_input('Objetivo')
    obs = st.text_area('Observações')

    if st.button('Salvar'):
        if nome != '':
            novo_dado = {
                'Nome': nome,
                'Telefone': telefone,
                'Email': email,
                'Data Nascimento': nascimento,
                'Objetivo': objetivo,
                'Observações': obs
            }
            data = pd.concat([data, pd.DataFrame([novo_dado])], ignore_index=True)
            save_data(data)
            st.success('Aluno cadastrado com sucesso!')
        else:
            st.error('Por favor, preencha o nome do aluno.')

# 🔸 Visualização
elif menu == 'Visualizar Alunos':
    st.subheader('Lista de alunos cadastrados')

    if data.empty:
        st.info('Nenhum aluno cadastrado ainda.')
    else:
        st.dataframe(data)

        # 🔹 Opção de excluir aluno
        st.subheader('Excluir Aluno')
        aluno_para_excluir = st.selectbox('Selecione o aluno para excluir', data['Nome'])

        if st.button('Excluir'):
            data = data[data['Nome'] != aluno_para_excluir]
            save_data(data)
            st.success(f'Aluno {aluno_para_excluir} excluído com sucesso.')