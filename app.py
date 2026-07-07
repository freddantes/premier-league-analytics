import streamlit as st
import pandas as pd
import os

# Configuração da página para um visual profissional
st.set_page_config(page_title="Premier League Dashboard", layout="wide")

st.title("⚽ Premier League Dashboard")
st.markdown("---")

def load_data():
    # Obtém o caminho absoluto baseado na localização do app.py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "data", "gold", "kpis.parquet")
    
    if os.path.exists(file_path):
        return pd.read_parquet(file_path)
    else:
        # Exibe o caminho tentado para facilitar o debug caso ocorra erro
        st.error(f"Arquivo não encontrado em: {file_path}")
        return None

df = load_data()

if df is not None:
    # Barra lateral para o filtro de times
    st.sidebar.header("Filtros")
    team_list = sorted(df['team_name'].unique())
    selected_team = st.sidebar.selectbox("Selecione um time:", team_list)

    # Filtragem dos dados para o time selecionado
    filtered_df = df[df['team_name'] == selected_team]

    # Layout de exibição com imagem e métricas
    col_img, col_info = st.columns([1, 4])
    
    with col_img:
        # Exibe o escudo do time
        st.image(filtered_df['team_crest'].values[0], width=150)
        
    with col_info:
        st.subheader(f"Perfil: {selected_team}")
        
        # Linha de métricas rápidas
        c1, c2, c3 = st.columns(3)
        c1.metric("Pontos", int(filtered_df['points'].values[0]))
        c2.metric("Jogos", int(filtered_df['playedGames'].values[0]))
        c3.metric("Saldo de Gols", int(filtered_df['goalDifference'].values[0]))

    st.markdown("---")
    st.subheader("Dados Detalhados")
    st.dataframe(filtered_df, use_container_width=True)

else:
    st.info("O pipeline está em execução ou os dados ainda não foram processados. Por favor, aguarde o carregamento.")