import streamlit as st
import pandas as pd
import requests
import os

# Configuração da página
st.set_page_config(page_title="Premier League Dashboard", layout="wide")

st.title("⚽ Premier League Dashboard")
st.markdown("---")

def fetch_data():
    """Busca dados diretamente da API caso o arquivo local não esteja disponível."""
    # Lê a chave do segredo configurado no Streamlit Cloud
    api_key = st.secrets.get("API_KEY")
    if not api_key:
        return None
        
    url = "https://api.football-data.org/v4/competitions/PL/standings"
    headers = {"X-Auth-Token": api_key}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        standings = data['standings'][0]['table']
        df = pd.DataFrame(standings)
        # Normalização idêntica à do pipeline
        df_team = pd.json_normalize(df['team']).add_prefix('team_')
        return pd.concat([df.drop(columns=['team']), df_team], axis=1)
    return None

def load_data():
    # Caminho absoluto para evitar erros de diretório na nuvem
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "data", "gold", "kpis.parquet")
    
    if os.path.exists(file_path):
        return pd.read_parquet(file_path)
    else:
        # Se não encontrar localmente, tenta buscar via API
        return fetch_data()

df = load_data()

if df is not None:
    # Barra lateral
    st.sidebar.header("Filtros")
    team_list = sorted(df['team_name'].unique())
    selected_team = st.sidebar.selectbox("Selecione um time:", team_list)

    # Filtragem
    filtered_df = df[df['team_name'] == selected_team]

    # Layout de exibição
    col_img, col_info = st.columns([1, 4])
    
    with col_img:
        st.image(filtered_df['team_crest'].values[0], width=150)
        
    with col_info:
        st.subheader(f"Perfil: {selected_team}")
        c1, c2, c3 = st.columns(3)
        c1.metric("Pontos", int(filtered_df['points'].values[0]))
        c2.metric("Jogos", int(filtered_df['playedGames'].values[0]))
        c3.metric("Saldo de Gols", int(filtered_df['goalDifference'].values[0]))

    st.markdown("---")
    st.subheader("Dados Detalhados")
    st.dataframe(filtered_df, use_container_width=True)
else:
    st.error("Não foi possível carregar os dados. Verifique a configuração da API_KEY no Streamlit Cloud.")