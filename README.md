# 🌱 FarmTech Solutions - Sistema de Gestão Agrícola

## 📌 Sobre o Projeto

O **FarmTech Solutions** é um sistema completo para **gestão agrícola**, desenvolvido em **Python** e **R**, com foco em auxiliar agricultores no controle de culturas, insumos e aplicações em campo.

A solução combina:

* **Python** → Gerenciamento de culturas e insumos, com interface em terminal interativa, validações de segurança e persistência em arquivos CSV.
* **R** → Análise estatística, integração com API de clima e visualização de dados em gráficos.

Este projeto simula uma aplicação real para o setor do **agronegócio**, unindo programação, análise de dados, UX (experiência do usuário) e automação.

---

## 📂 Estrutura do Projeto

```
FARMTECH-SOLUTIONS/
│
├── dados/               # Base de dados persistente em CSV
│   ├── culturas.csv
│   └── insumos.csv
│
├── python/
│   └── gestao_agricola.py   # Sistema principal em Python
│
├── r/
│   └── analise.r            # Script de análise em R
│
└── README.md
```

---

## 🚀 Funcionalidades

### 🔹 Python (`gestao_agricola.py`)

* **Gestão de Culturas** → cadastro, listagem, atualização e exclusão.
* **Gestão de Insumos** → cadastro, listagem, atualização e exclusão.
* **Cálculo Automático de Áreas** → suporte a terrenos retangulares e circulares.
* **Divisão em Faixas** → cálculo da área média por faixa.
* **Aplicação de Insumos** → cálculo da quantidade total necessária e por faixa.
* **Persistência Automática** → dados armazenados em CSV.

#### 🔹 Diferenciais Técnicos de Python

* **Validação de Entrada** → bloqueio contra valores inválidos (texto em campos numéricos, valores negativos, etc.).
* **Travas de Segurança** → confirmações antes de exclusões.
* **Mensagens de Erro Claras** → feedback com ⚠️ e instruções para corrigir.
* **Uso de Emojis** → menus mais intuitivos e agradáveis para o agricultor.
* **Navegação Intuitiva** → opção de voltar (`#`) a qualquer momento.
* **Pausas Interativas** → `Pressione ENTER para continuar` ajuda na leitura e evita sobrecarga de informações.
* **Estrutura Modular** → funções bem separadas para facilitar manutenção e evolução.

### 🔹 R (`analise.r`)

* Leitura dos dados exportados em CSV.
* Estatísticas descritivas:

  * Área média e total de culturas.
  * Número médio de faixas.
  * Dose média, mínima, máxima e desvio padrão dos insumos.
* Integração com a **API OpenWeather** para obter dados climáticos.
* Visualização de dados em **gráfico de barras interativo**, incluindo anotações de temperatura e umidade.

---

## ⚙️ Pré-requisitos

### 🔹 Python

* Python 3.8+
* Nenhuma dependência externa além da biblioteca padrão.

### 🔹 R

Pacotes necessários:

```R
install.packages(c("httr", "jsonlite", "dplyr", "ggplot2"))
```

---

## ▶️ Como Executar

### 1. Executar o sistema em Python

```bash
cd python
python gestao_agricola.py
```

👉 O programa cria automaticamente os arquivos `culturas.csv` e `insumos.csv` na pasta **dados/**.

### 2. Executar a análise em R

```R
setwd("r")
source("analise.r")
```

👉 O script irá:

* Carregar os dados.
* Exibir estatísticas.
* Consultar a API de clima.
* Gerar um gráfico com as áreas plantadas e informações climáticas.

---

## 📊 Exemplo de Saída

### Python

```
🌱  Bem-vindo ao FarmTech - Gestão Agrícola

[1] 🌾 Gerenciar Culturas
[2] 🧪 Gerenciar Insumos
[3] 💧 Aplicar Insumo em Cultura
[4] 🚪 Sair do Programa
```

👉 Caso o usuário insira algo inválido:

```
⚠️ Valor inválido! Digite apenas números.
```

👉 Para evitar perda de dados:

```
❌ Operação cancelada.
```

👉 Para navegação simplificada:

```
Digite # para voltar ao menu anterior.
```

### R

```
📊 Resumo das Culturas:
  Area_media Area_total Faixas_media Desvio_area
1      250.5       1002           4         120

🧪 Resumo dos Insumos:
  Dose_media Dose_max Dose_min Desvio_dose
1       0.75     1.2      0.5        0.3
```

---

## 🌐 API de Clima

* Serviço utilizado: [OpenWeatherMap](https://openweathermap.org/api)
* Local de exemplo: **Belo Horizonte - MG**
* Dados integrados ao gráfico: Temperatura e Umidade.

---

## 📌 Objetivo Educacional

Este projeto foi desenvolvido para fins de **aprendizado** e **demonstração prática** de:

* Programação em Python (persistência, UX em terminal, cálculos e validações).
* Análise de dados em R (estatísticas, API, visualização).
* Integração entre linguagens e ferramentas para o **agronegócio**.
* Boas práticas de **usabilidade** para usuários não técnicos (agricultores).

---

## ✨ Autor

👩‍💻 **Amanda Damasceno Martins**

