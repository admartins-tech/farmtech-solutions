import streamlit as st
import python.gestao_agricola as ga

# Sobrescreve as funções de interface
def perguntar(mensagem, key=None):
    return st.text_input(mensagem, key=key)

def mostrar(mensagem):
    st.write(mensagem)

# Injeta as novas funções no módulo
ga.perguntar = perguntar
ga.mostrar = mostrar

# Configura a página
st.set_page_config(page_title="FarmTech 🌱", layout="centered")

st.title("🌱 FarmTech - Gestão Agrícola")

# Menu lateral
menu = st.sidebar.radio("📌 Navegação", ["Início", "Culturas", "Insumos", "Aplicar Insumo"])

# Botões e chamadas
if menu == "Culturas":
    st.subheader("🌾 Gestão de Culturas")
    if st.button("➕ Cadastrar nova cultura"):
        ga.cadastrar_cultura()
    if st.button("📋 Listar culturas"):
        ga.listar_culturas()
    if st.button("✏️ Atualizar cultura"):
        ga.atualizar_cultura()
    if st.button("🗑️ Deletar cultura"):
        ga.deletar_cultura()

elif menu == "Insumos":
    st.subheader("🧪 Gestão de Insumos")
    if st.button("➕ Cadastrar novo insumo"):
        ga.cadastrar_insumo()
    if st.button("📋 Listar insumos"):
        ga.listar_insumos()
    if st.button("✏️ Atualizar insumo"):
        ga.atualizar_insumo()
    if st.button("🗑️ Deletar insumo"):
        ga.deletar_insumo()

elif menu == "Aplicar Insumo":
    st.subheader("💧 Aplicar Insumo em Cultura")
    ga.aplicar_insumo()

elif menu == "Sair":
    st.success("✅ Programa encerrado. Até logo, agricultor! 🌱")