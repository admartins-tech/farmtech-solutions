@echo off
echo =========================================
echo 🌱 Iniciando FarmTech - Gestao Agricola
echo =========================================

:: Ativa o ambiente virtual
call venv\Scripts\activate

:: Roda o app no Streamlit
streamlit run app.py

pause