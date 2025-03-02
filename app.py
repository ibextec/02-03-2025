import streamlit as st
from PIL import Image

# Função para gerar a imagem com Stable Diffusion (substitua pela sua lógica)
def gerar_imagem(descricao):
    # Lógica para gerar a imagem com Stable Diffusion
    # ...
    # Retorna a imagem gerada
    imagem = Image.open("imagem_gerada.png")  # Substitua pelo caminho da imagem gerada
    return imagem

# Interface Streamlit
st.title("ZemAI - Gerador de Imagens de Móveis Planejados")

descricao = st.text_area("Descreva o móvel planejado que você deseja:", "")
if st.button("Gerar Imagem"):
    if descricao:
        imagem_gerada = gerar_imagem(descricao)
        st.image(imagem_gerada, caption="Imagem gerada pelo ZemAI")
    else:
        st.warning("Por favor, insira uma descrição do móvel.")
