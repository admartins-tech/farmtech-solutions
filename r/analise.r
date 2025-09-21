# ================================
# FarmTech Solutions - Análise em R
# ================================

# Instalar pacotes (somente 1x, depois pode comentar)
# install.packages(c("httr", "jsonlite", "dplyr", "ggplot2"))

library(httr)
library(jsonlite)
library(dplyr)
library(ggplot2)

# ================================
# 1. Ler os dados exportados pelo Python
# ================================

tryCatch({
  culturas <- read.csv("../dados/culturas.csv", encoding = "UTF-8")
  insumos  <- read.csv("../dados/insumos.csv", encoding = "UTF-8")
  print("✅ Dados carregados com sucesso!")
}, error = function(e) {
  stop("❌ ERRO: Arquivos CSV não encontrados. Execute primeiro o programa em Python para gerar os dados.")
})

# ================================
# 2. Estatísticas básicas
# ================================

df_summary <- culturas %>%
  summarise(
    Area_media = mean(area),
    Area_total = sum(area),
    Faixas_media = mean(faixas),
    Desvio_area = sd(area)
  )

print("📊 Resumo das Culturas:")
print(df_summary)

resumo_insumos <- insumos %>%
  summarise(
    Dose_media = mean(dose_m2),
    Dose_max   = max(dose_m2),
    Dose_min   = min(dose_m2),
    Desvio_dose = sd(dose_m2)
  )

print("🧪 Resumo dos Insumos:")
print(resumo_insumos)

# ================================
# 3. API de Clima (Belo Horizonte - MG)
# ================================

lat <- -19.9167
lon <- -43.9345
api_key <- "d15e6bd014a6b5a87a2b7b55a9dec8c0"

url <- paste0("https://api.openweathermap.org/data/2.5/weather?",
              "lat=", lat, "&lon=", lon,
              "&units=metric&lang=pt_br&appid=", api_key)

clima_info <- NULL
tryCatch({
  res <- GET(url)
  if (status_code(res) == 200) {
    dados_clima <- fromJSON(content(res, "text"))
    
    clima_info <- data.frame(
      Local = "Belo Horizonte - MG",
      Temperatura = dados_clima$main$temp,
      Umidade = dados_clima$main$humidity,
      Condicao = dados_clima$weather$description[1]
    )
    
    print("🌤️ Dados de clima obtidos com sucesso:")
    print(clima_info)
    
  } else {
    print(paste("⚠️ Aviso: Não foi possível obter os dados de clima. Código:", status_code(res)))
  }
}, error = function(e) {
  print(paste("⚠️ Erro na chamada da API de clima:", e$message))
})

# ================================
# 4. Gráfico
# ================================

if (!is.null(clima_info)) {
  temp_label <- paste0("🌡️ Temp: ", round(clima_info$Temperatura, 1), "°C")
  umid_label <- paste0("💧 Umid: ", clima_info$Umidade, "%")
} else {
  temp_label <- "Sem dados de clima"
  umid_label <- ""
}

ggplot(culturas, aes(x = nome, y = area, fill = nome)) +
  geom_col() +
  geom_text(aes(label = round(area, 1)), vjust = -0.5, color = "black") + # valores de área
  annotate("text", x = 1, y = max(culturas$area) * 1.1, label = temp_label, size = 5, color = "red") +
  annotate("text", x = 1, y = max(culturas$area) * 1.2, label = umid_label, size = 5, color = "blue") +
  labs(
    title = "Área total plantada por cultura",
    subtitle = paste("Dados climáticos de", clima_info$Local),
    x = "Cultura",
    y = "Área (m²)"
  ) +
  theme_minimal()