import streamlit as st
import pandas as pd
import numpy as np


#textos

#st.header("Minha dashboard")
#st.sidebar.text("Escolha o que deseja filtrar")

#st.markdown("~~Riscado~~")
#st.caption("minha legenda")

#pessoas = [{'nome': 'caio', 'idade': 24}, 
#           {'nome': 'jonatas', 'idade': 24}]

#st.write("# pessoas", pessoas)


#exibição de dados

#df = pd.DataFrame(
#    np.random.rand(10, 3),
#    columns=['Preço', 'Taxa de ocupação', 'Taxa de inadimplencia']
#)

#st.bar_chart(df)


#interação

st.sidebar.button("Exibir gráfico")