# -*- coding: utf-8 -*-
"""
FarmTech - Sistema de Gestão Agrícola
Autor: Amanda
Descrição: Sistema em Python para gerenciar culturas e insumos agrícolas.
"""

import csv
import os

# ===========================
# INTERFACE PADRÃO (TERMINAL)
# ===========================

def perguntar(mensagem):
    return input(mensagem)

def mostrar(mensagem):
    print(mensagem)

# ===========================
# VARIÁVEIS GLOBAIS
# ===========================

culturas = []
insumos = []

import csv
import os

# ===========================
# FUNÇÕES PARA PERSISTÊNCIA
# ===========================

def salvar_dados():
    """Salva culturas e insumos em arquivos CSV"""

    # Salvar culturas
    with open("../dados/culturas.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nome", "formato", "area", "ruas"])  # cabeçalho
        for cultura in culturas:
            writer.writerow([cultura["nome"], cultura["formato"], cultura["area"], cultura["ruas"]])

    # Salvar insumos
    with open("../dados/insumos.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nome", "dose_m2"])  # cabeçalho
        for insumo in insumos:
            writer.writerow([insumo["nome"], insumo["dose_m2"]])

def carregar_dados():
    """Carrega culturas e insumos de arquivos CSV, se existirem"""
    if os.path.exists("../dados/culturas.csv"):
        with open("../dados/culturas.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                culturas.append({
                    "nome": row["nome"],
                    "formato": row["formato"],
                    "area": float(row["area"]),
                    "ruas": int(row["ruas"])
                })

    if os.path.exists("../dados/insumos.csv"):
        with open("../dados/insumos.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                insumos.append({
                    "nome": row["nome"],
                    "dose_m2": float(row["dose_m2"])
                })


# ===========================
# FUNÇÕES DE UTILIDADE
# ===========================

def pausar():
    """Pausa a execução até o usuário pressionar ENTER."""
    mostrar()
    perguntar("👉 Pressione ENTER para voltar ao menu")

def instrucao():
    """Instrui o usuário a pressionar # se precisar voltar."""
    mostrar("\n Atenção: Caso precise retornar a qualquer momento, pressione #.")
    mostrar()
    perguntar("👉 Pressione ENTER para continuar")

def voltar(resposta: str):
    """
    Verifica se o usuário digitou '#' para voltar.
    Se sim, mostra a mensagem e retorna True.
    """
    if resposta.strip() == "#":
        mostrar("↩️ Voltando ao menu anterior ...\n")
        return True
    return False


# ===========================
# MENUS (apenas exibição)
# ===========================

def menu_inicial():
    mostrar("\n" + "="*50)
    mostrar("🌱  Bem-vindo ao FarmTech - Gestão Agrícola")
    mostrar("="*50)
    mostrar("\nO que você gostaria de fazer hoje?\n")
    mostrar("[1] 🌾 Gerenciar Culturas")
    mostrar("[2] 🧪 Gerenciar Insumos")
    mostrar("[3] 💧 Aplicar Insumo em Cultura")
    mostrar("[4] 🚪 Sair do Programa")
    mostrar("-"*50)

def menu_culturas():
    mostrar("\n" + "="*50)
    mostrar("🌱  FarmTech - Gestão de Culturas 🌱")
    mostrar("="*50)
    mostrar("\nO que você deseja fazer?\n")
    mostrar("[1] ➕ Cadastrar nova cultura")
    mostrar("[2] 📋 Listar culturas cadastradas")
    mostrar("[3] ✏️  Atualizar dados de uma cultura")
    mostrar("[4] 🗑️  Deletar dados de uma cultura")
    mostrar("[5] 🔙 Voltar ao Menu Principal")
    mostrar("-"*50)

def menu_insumos():
    mostrar("\n" + "="*50)
    mostrar("🧪  FarmTech - Gestão de Insumos 🧪")
    mostrar("="*50)
    mostrar("\nO que você deseja fazer?\n")
    mostrar("[1] ➕ Cadastrar novo insumo")
    mostrar("[2] 📋 Listar insumos cadastrados")
    mostrar("[3] ✏️  Atualizar dados de um insumo")
    mostrar("[4] 🗑️  Deletar dados de um insumo")
    mostrar("[5] 🔙 Voltar ao Menu Principal")
    mostrar("-"*50)

# ==============================
# FUNÇÕES DE AÇÃO - CULTURAS
# ==============================

def cadastrar_cultura():

    instrucao()

    mostrar("\n" + "="*50)
    mostrar("🌱 Cadastro de Cultura 🌱")
    mostrar("="*50)

    nome = perguntar("\n👉 Digite o nome da cultura: ")
    if voltar(nome):
        return

    while True:
        mostrar("\nQual o formato da área de plantio?")
        mostrar("[1] Retângulo")
        mostrar("[2] Círculo")
        opcao_formato = perguntar("👉 Digite o número da opção desejada: ")
        if voltar(opcao_formato):
            return

        if opcao_formato == "1":
            largura = perguntar("Digite a largura do terreno (em metros): ")
            if voltar(largura):
                return
            largura = float(largura)
            comprimento = perguntar("Digite o comprimento do terreno (em metros): ")
            if voltar(comprimento):
                return
            comprimento = float(comprimento)
            area = largura * comprimento
            formato = "retangular"
            mostrar(f"De acordo com essas informações, esse terreno {formato} possui uma área de {area:.2f} m²!")
            break

        elif opcao_formato == "2":
            raio = perguntar("Digite o raio do terreno (em metros): ")
            if voltar (raio):
                return
            raio = float(raio)
            area = 3.14159 * (raio ** 2)
            formato = "circular"
            mostrar(f"De acordo com essas informações, esse terreno {formato} possui uma área de {area:.2f} m²!")
            break

        else:
            mostrar("⚠️ Opção inválida! Tente novamente.\n")

    ruas = perguntar("Digite quantas ruas há nessa lavoura: ")
    if voltar(ruas):
        return
    ruas = int(ruas)

    cultura = {
        "nome": nome,
        "formato": formato,
        "area": area,
        "ruas": ruas
    }
    culturas.append(cultura)
    salvar_dados()

    mostrar("\n✅ Cultura cadastrada com sucesso!")
    mostrar(f"\n🌾 Nome: {nome}")
    mostrar(f"📐 Formato: {formato}")
    mostrar(f"📏 Área calculada: {area:.2f} m²")
    mostrar(f"🛤️ Número de ruas: {ruas}\n")
    pausar()

def listar_culturas():
    mostrar("\n" + "="*50)
    mostrar("📋 Lista de Culturas Cadastradas")
    mostrar("="*50)

    if not culturas:
        mostrar("\n⚠️ Nenhuma cultura cadastrada.\n")
        pausar()
        return

    for i, cultura in enumerate(culturas, start=1):
        mostrar(f"\nCultura {i}:")
        mostrar(f"🌾 Nome: {cultura['nome']}")
        mostrar(f"📐 Formato: {cultura['formato']}")
        mostrar(f"📏 Área: {cultura['area']:.2f} m²")
        mostrar(f"🛤️ Quantidade de ruas: {cultura['ruas']}")

    pausar()

def atualizar_cultura():

    instrucao()

    mostrar("\n" + "="*50)
    mostrar("✏️  Atualizar Cultura")
    mostrar("="*50)

    if not culturas:
        mostrar("⚠️ Nenhuma cultura cadastrada.\n")
        pausar()
        return
    
    for i, cultura in enumerate(culturas, start=1):
        mostrar(f"{i}. {cultura['nome']}")

    escolha = perguntar("\nDigite o número da cultura que deseja atualizar: ")
    if voltar(escolha):
        return
    escolha = int(escolha) - 1

    if 0 <= escolha < len(culturas):
        cultura = culturas[escolha]

        mostrar(f"\nCultura selecionada: {cultura['nome']}")
        mostrar("Quais dados você deseja alterar?")
        mostrar("[1] Nome")
        mostrar("[2] Formato")
        mostrar("[3] Área")
        mostrar("[4] Ruas")

        opcao = perguntar("👉 Digite o número da opção desejada: ")
        if voltar(opcao):
            return

        if opcao == "1":
            cultura["nome"] = perguntar("Novo nome: ")
            if voltar(cultura["nome"]):
                return

        elif opcao == "2":
            while True:
                novo_formato = perguntar("Novo formato: (retangular/circular)").lower()
                if voltar(novo_formato):
                    return
                if novo_formato in ["retangular", "circular"]:
                    cultura["formato"] = novo_formato
                    break
                else:
                    mostrar("⚠️ Opção inválida! Precisa ser 'retangular' ou 'circular'. Tente novamente.\n")

        elif opcao == "3":
            if cultura["formato"] == "retangular":
                largura = perguntar("Nova largura (em metros): ")
                if voltar(largura):
                    return
                largura = float(largura)
                comprimento = perguntar("Novo comprimento (em metros): ")
                if voltar(comprimento):
                    return
                comprimento = float(comprimento)
                cultura["area"] = largura * comprimento
            else:
                raio = perguntar("Novo raio (em metros): ")
                if voltar(raio):
                    return
                raio = float(raio)
                cultura["area"] = 3.14159 * (raio ** 2)

        elif opcao == "4":
            cultura["ruas"] = perguntar("Novo número de ruas: ")
            if voltar(cultura["ruas"]):
                return
            cultura["ruas"] = int(cultura["ruas"])

        else:
            mostrar("⚠️ Opção inválida! Tente novamente.\n")
            pausar()
            return

        salvar_dados()
        mostrar("\n✅ Cultura atualizada com sucesso!\n")
        pausar()

    else:
        mostrar("⚠️ Opção inválida! Tente novamente.\n")
        pausar()

def deletar_cultura():

    instrucao()

    mostrar("\n" + "="*50)
    mostrar("🗑️  Deletar Cultura")
    mostrar("="*50)

    if not culturas:
        mostrar("⚠️ Nenhuma cultura cadastrada.\n")
        pausar()
        return

    for i, cultura in enumerate(culturas, start=1):
        mostrar(f"{i}. {cultura['nome']}")

    escolha = perguntar("\nDigite o número da cultura que deseja deletar: ")
    if voltar(escolha):
        return
    escolha = int(escolha) - 1

    if 0 <= escolha < len(culturas):
        cultura = culturas[escolha]
        confirmacao = perguntar(f"Tem certeza que deseja deletar a cultura '{cultura['nome']}'? (sim/não): ").lower()
        if confirmacao == "sim":
            culturas.pop(escolha)
            salvar_dados()
            mostrar(f"\n✅ Cultura '{cultura['nome']}' deletada com sucesso!\n")
        else:
            mostrar("\n❌ Operação cancelada.\n")
    else:
        mostrar("⚠️ Opção inválida! Tente novamente.\n")

    pausar()

# ==============================
# FUNÇÕES DE AÇÃO - INSUMOS
# ==============================

def cadastrar_insumo():

    instrucao()

    mostrar("\n" + "="*50)
    mostrar("🧪 Cadastro de Insumo 🧪")
    mostrar("="*50)

    nome = perguntar("👉 Digite o nome do insumo: ")
    if voltar(nome):
        return

    while True:
        try:
            dose = perguntar("👉 Digite a dose de aplicação (em litros por m²): ")
            if voltar(dose):
                return
            dose = float(dose)
            break
        except ValueError:
            mostrar("⚠️ Valor inválido! Digite um número, por exemplo: 0.5\n")

    insumo = {"nome": nome, "dose_m2": dose}
    insumos.append(insumo)
    salvar_dados()

    mostrar("\n✅ Insumo cadastrado com sucesso!")
    mostrar(f"🧪 Nome: {nome}")
    mostrar(f"💧 Dose: {dose} L/m²\n")
    pausar()

def listar_insumos():
    mostrar("\n" + "="*50)
    mostrar("📋 Lista de Insumos Cadastrados")
    mostrar("="*50)

    if not insumos:
        mostrar("⚠️ Nenhum insumo cadastrado.\n")
        pausar()
        return

    for i, insumo in enumerate(insumos, start=1):
        mostrar(f"\nInsumo {i}:")
        mostrar(f"🧪 Nome: {insumo['nome']}")
        mostrar(f"💧 Dose: {insumo['dose_m2']} L/m²")

    pausar()

def atualizar_insumo():

    instrucao()

    mostrar("\n" + "="*50)
    mostrar("✏️  Atualizar Insumo")
    mostrar("="*50)

    if not insumos:
        mostrar("⚠️ Nenhum insumo cadastrado.\n")
        pausar()
        return

    for i, insumo in enumerate(insumos, start=1):
        mostrar(f"{i}. {insumo['nome']}")

    escolha = perguntar("\nDigite o número do insumo que deseja atualizar: ")
    if voltar(escolha):
        return
    escolha = int(escolha) - 1

    if 0 <= escolha < len(insumos):
        insumo = insumos[escolha]
        mostrar(f"\nInsumo selecionado: {insumo['nome']}")
        mostrar("Quais dados você deseja alterar?")
        mostrar("[1] Nome")
        mostrar("[2] Dose")

        opcao = perguntar("👉 Digite o número da opção desejada: ")
        if voltar(opcao):
            return

        if opcao == "1":
            insumo["nome"] = perguntar("Novo nome do insumo: ")
            if voltar(insumo["nome"]):
                return

        elif opcao == "2":
            while True:
                try:
                    insumo["dose_m2"] = perguntar("Nova dose (em L/m²): ")
                    if voltar(insumo["dose_m2"]):
                        return
                    insumo["dose_m2"] = float(insumo["dose_m2"])
                    break
                except ValueError:
                    mostrar("⚠️ Valor inválido! Digite um número, por exemplo: 0.5\n")

        else:
            mostrar("⚠️ Opção inválida! Tente novamente.\n")
            pausar()
            return
        
        salvar_dados()
        mostrar("\n✅ Insumo atualizado com sucesso!\n")
        pausar()

    else:
        mostrar("⚠️ Opção inválida! Tente novamente.\n")
        pausar()

def deletar_insumo():

    instrucao()

    mostrar("\n" + "="*50)
    mostrar("🗑️  Deletar Insumo")
    mostrar("="*50)

    if not insumos:
        mostrar("⚠️ Nenhum insumo cadastrado.\n")
        pausar()
        return

    for i, insumo in enumerate(insumos, start=1):
        mostrar(f"{i}. {insumo['nome']}")

    escolha = perguntar("\nDigite o número do insumo que deseja deletar: ")
    if voltar(escolha):
        return
    escolha = int(escolha) - 1

    if 0 <= escolha < len(insumos):
        insumo = insumos[escolha]
        confirmacao = perguntar(f"Tem certeza que deseja deletar o insumo '{insumo['nome']}'? (s/n): ").lower()
        if confirmacao == "sim":
            insumos.pop(escolha)
            salvar_dados()
            mostrar(f"\n✅ Insumo '{insumo['nome']}' deletado com sucesso!\n")
        else:
            mostrar("\n❌ Operação cancelada.\n")
    else:
        mostrar("⚠️ Opção inválida! Tente novamente.\n")

    pausar()

# ==============================
# FUNÇÕES DE AÇÃO - GERAIS
# ==============================

def aplicar_insumo():

    instrucao()

    mostrar("\n" + "="*50)
    mostrar("💧 Aplicar Insumo em Cultura")
    mostrar("="*50)

    if not culturas:
        mostrar("⚠️ Nenhuma cultura cadastrada.\n")
        pausar()
        return
    if not insumos:
        mostrar("⚠️ Nenhum insumo cadastrado.\n")
        pausar()
        return

    mostrar("\nCulturas disponíveis:")
    for i, cultura in enumerate(culturas, start=1):
        mostrar(f"{i}. {cultura['nome']} (Área: {cultura['area']:.2f} m², Ruas: {cultura['ruas']})")
    escolha_cultura = perguntar("\nDigite o número da cultura: ")
    if voltar(escolha_cultura):
        return
    escolha_cultura = int(escolha_cultura) - 1

    if not (0 <= escolha_cultura < len(culturas)):
        mostrar("⚠️ Número inválido!\n")
        pausar()
        return
    cultura = culturas[escolha_cultura]

    mostrar("\nInsumos disponíveis:")
    for i, insumo in enumerate(insumos, start=1):
        mostrar(f"{i}. {insumo['nome']} (Dose: {insumo['dose_m2']} L/m²)")
    escolha_insumo = perguntar("\nDigite o número do insumo: ")
    if voltar(escolha_insumo):
        return
    escolha_insumo = int(escolha_insumo) - 1

    if not (0 <= escolha_insumo < len(insumos)):
        mostrar("⚠️ Número inválido!\n")
        pausar()
        return
    insumo = insumos[escolha_insumo]

    total = cultura["area"] * insumo["dose_m2"]
    por_rua = total / cultura["ruas"] if cultura["ruas"] > 0 else 0

    mostrar("\n✅ Cálculo realizado com sucesso!")
    mostrar(f"🌾 Cultura: {cultura['nome']}")
    mostrar(f"🧪 Insumo: {insumo['nome']}")
    mostrar(f"📏 Área total: {cultura['area']:.2f} m²")
    mostrar(f"💧 Dose: {insumo['dose_m2']} L/m²")
    mostrar(f"🔢 Ruas: {cultura['ruas']}")
    mostrar(f"📊 Total necessário: {total:.2f} litros")
    mostrar(f"🛤️ Insumo por rua: {por_rua:.2f} litros\n")
    pausar()

def sair_programa():
    mostrar("\n✅ Programa encerrado. Até logo, agricultor! 🌱\n")
    exit()

# ==============================
# LOOPS
# ==============================

def loop_principal():
    while True:
        menu_inicial()
        opcao = perguntar("👉 Digite o número da opção desejada: ")
        if opcao in acoes_principal:
            acoes_principal[opcao]()
        else:
            mostrar("\n⚠️ Opção inválida! Tente novamente.\n")
            pausar()

def loop_culturas():
    while True:
        menu_culturas()
        opcao = perguntar("👉 Digite o número da opção desejada: ")
        if opcao in acoes_culturas:
            if opcao == "5":
                break
            acoes_culturas[opcao]()
        else:
            mostrar("\n⚠️ Opção inválida! Tente novamente.\n")
            pausar()

def loop_insumos():
    while True:
        menu_insumos()
        opcao = perguntar("👉 Digite o número da opção desejada: ")
        if opcao in acoes_insumos:
            if opcao == "5":
                break
            acoes_insumos[opcao]()
        else:
            mostrar("\n⚠️ Opção inválida! Tente novamente.\n")
            pausar()

# ==============================
# MAPAS DE AÇÕES (dicionários)
# ==============================

acoes_principal = {
    "1": lambda: loop_culturas(),
    "2": lambda: loop_insumos(),
    "3": aplicar_insumo,
    "4": sair_programa
}

acoes_culturas = {
    "1": cadastrar_cultura,
    "2": listar_culturas,
    "3": atualizar_cultura,
    "4": deletar_cultura,
    "5": lambda: None
}

acoes_insumos = {
    "1": cadastrar_insumo,
    "2": listar_insumos,
    "3": atualizar_insumo,
    "4": deletar_insumo,
    "5": lambda: None
}

# ==============================
# INÍCIO DO PROGRAMA
# ==============================

if __name__ == "__main__":
    carregar_dados()
    loop_principal()
