# -*- coding: utf-8 -*-
"""
FarmTech - Sistema de Gestão Agrícola
Autor: Amanda Damasceno Martins
Descrição: Sistema em Python para gerenciar culturas e insumos agrícolas.
"""

import csv
import os

# ===========================
# VARIÁVEIS GLOBAIS
# ===========================

culturas = []
insumos = []

# ===========================
# FUNÇÕES PARA PERSISTÊNCIA
# ===========================

# Descobre o caminho absoluto da pasta onde está o arquivo gestao_agricola.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Cria (se não existir) a pasta "dados" no nível acima
DADOS_DIR = os.path.join(BASE_DIR, "..", "dados")
os.makedirs(DADOS_DIR, exist_ok=True)

def salvar_dados():
    """Salva culturas e insumos em arquivos CSV"""

    # Salvar culturas
    caminho_culturas = os.path.join(DADOS_DIR, "culturas.csv")
    with open(caminho_culturas, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nome", "formato", "area", "faixas", "area_faixa"])  # cabeçalho
        for cultura in culturas:
            writer.writerow([
                cultura["nome"], 
                cultura["formato"], 
                cultura["area"], 
                cultura["faixas"],
                cultura["area_faixa"]
            ])

    # Salvar insumos
    caminho_insumos = os.path.join(DADOS_DIR, "insumos.csv")
    with open(caminho_insumos, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nome", "dose_m2"])  # cabeçalho
        for insumo in insumos:
            writer.writerow([insumo["nome"], insumo["dose_m2"]])

def carregar_dados():
    """Carrega culturas e insumos de arquivos CSV, se existirem"""
    caminho_culturas = os.path.join(DADOS_DIR, "culturas.csv")
    caminho_insumos = os.path.join(DADOS_DIR, "insumos.csv")

    if os.path.exists(caminho_culturas):
        with open(caminho_culturas, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                culturas.append({
                    "nome": row["nome"],
                    "formato": row["formato"],
                    "area": float(row["area"]),
                    "faixas": int(row["faixas"]),
                    "area_faixa": float(row["area_faixa"])
                })

    if os.path.exists(caminho_insumos):
        with open(caminho_insumos, "r", encoding="utf-8") as f:
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
    print("")
    input("👉 Pressione ENTER para voltar ao menu: ")

def instrucao():
    """Instrui o usuário a pressionar # se precisar voltar."""
    print("")
    print("\n Atenção: Caso precise retornar a qualquer momento, pressione #.")
    print("")
    input("👉 Pressione ENTER para continuar: ")

def voltar(resposta: str):
    """
    Verifica se o usuário digitou '#' para voltar.
    Se sim, mostra a mensagem e retorna True.
    """
    if resposta.strip() == "#":
        print("")
        print("↩️   Voltando ao menu anterior ...\n")
        return True
    return False


# ===========================
# MENUS (apenas exibição)
# ===========================

def menu_inicial():
    print("\n" + "="*50)
    print("🌱  Bem-vindo ao FarmTech - Gestão Agrícola")
    print("="*50)
    print("\nO que você gostaria de fazer hoje?\n")
    print("[1] 🌾 Gerenciar Culturas")
    print("[2] 🧪 Gerenciar Insumos")
    print("[3] 💧 Aplicar Insumo em Cultura")
    print("[4] 🚪 Sair do Programa")
    print("-"*50)

def menu_culturas():
    print("\n" + "="*50)
    print("🌱  FarmTech - Gestão de Culturas 🌱")
    print("="*50)
    print("\nO que você deseja fazer?\n")
    print("[1] ➕ Cadastrar nova cultura")
    print("[2] 📋 Listar culturas cadastradas")
    print("[3] ✏️  Atualizar dados de uma cultura")
    print("[4] 🗑️  Deletar dados de uma cultura")
    print("[5] 🔙 Voltar ao Menu Principal")
    print("-"*50)

def menu_insumos():
    print("\n" + "="*50)
    print("🧪  FarmTech - Gestão de Insumos 🧪")
    print("="*50)
    print("\nO que você deseja fazer?\n")
    print("[1] ➕ Cadastrar novo insumo")
    print("[2] 📋 Listar insumos cadastrados")
    print("[3] ✏️  Atualizar dados de um insumo")
    print("[4] 🗑️  Deletar dados de um insumo")
    print("[5] 🔙 Voltar ao Menu Principal")
    print("-"*50)

# ==============================
# FUNÇÕES DE AÇÃO - CULTURAS
# ==============================

def cadastrar_cultura():
    
    instrucao()

    print("\n" + "="*50)
    print("🌱 Cadastro de Cultura 🌱")
    print("="*50)
    print("")

    nome = input("\n👉 Digite o nome da cultura: ")
    if voltar(nome):
        return

    while True:
        print("")
        print("\nQual o formato da área de plantio?")
        print("")
        print("[1] Retângulo")
        print("[2] Círculo")
        print("")
        opcao_formato = input("👉 Digite o número da opção desejada: ")
        if voltar(opcao_formato):
            return

        if opcao_formato == "1":
            while True:
                try:
                    print("")
                    largura = input("Digite a largura do terreno (em metros): ")
                    if voltar(largura):
                        return
                    largura = float(largura)

                    print("")
                    comprimento = input("Digite o comprimento do terreno (em metros): ")
                    if voltar(comprimento):
                        return
                    comprimento = float(comprimento)

                    area = largura * comprimento
                    formato = "retangular"
                    print("")
                    print(f"✅ Esse terreno {formato} possui uma área total de {area:.2f} m²!")
                    break
                except ValueError:
                    print("")
                    print("⚠️   Valor inválido! Digite apenas números.\n")
            break

        elif opcao_formato == "2":
            while True:
                try:
                    print("")
                    raio = input("Digite o raio do terreno (em metros): ")
                    if voltar(raio):
                        return
                    raio = float(raio)

                    area = 3.14159 * (raio ** 2)
                    formato = "circular"
                    print("")
                    print(f"✅ Esse terreno {formato} possui uma área total de {area:.2f} m²!")
                    break
                except ValueError:
                    print("")
                    print("⚠️   Valor inválido! Digite apenas números.\n")
            break

        else:
            print("")
            print("⚠️   Opção inválida! Tente novamente.\n")

    while True:
        try:
            print("")
            faixas = input("Digite quantas faixas há nessa lavoura: ")
            if voltar(faixas):
                return
            faixas = int(faixas)
            break
        except ValueError:
            print("")
            print("⚠️   Valor inválido! Digite apenas números inteiros.\n")

    # cálculo da área por faixa (média)
    area_faixa = area / faixas
    print("")
    print(f"✅ Esse terreno possui {faixas} faixas, cada uma com área média de {area_faixa:.2f} m²")

    cultura = {
        "nome": nome,
        "formato": formato,
        "area": area,
        "faixas": faixas,
        "area_faixa": area_faixa
    }
    culturas.append(cultura)
    salvar_dados()

    pausar()

    print("")
    print("\n✅ Cultura cadastrada com sucesso!")
    print("")
    print(f"🌾 Nome: {nome}")
    print(f"📐 Formato: {formato}")
    print(f"📏 Área total: {area:.2f} m²")
    print(f"🔢 Quantidade de faixas: {faixas}")
    print(f"📏 Área média por faixa: {area_faixa:.2f} m²\n")
    pausar()

def listar_culturas():
    print("\n" + "="*50)
    print("📋 Lista de Culturas Cadastradas")
    print("="*50)

    if not culturas:
        print("")
        print("\n⚠️   Nenhuma cultura cadastrada.\n")
        pausar()
        return

    for i, cultura in enumerate(culturas, start=1):
        print("")
        print(f"\nCultura {i}:")
        print(f"🌾 Nome: {cultura['nome']}")
        print(f"📐 Formato: {cultura['formato']}")
        print(f"📏 Área total: {cultura['area']:.2f} m²")
        print(f"🔢 Quantidade de faixas: {cultura['faixas']}")
        print(f"📏 Área média de cada faixa: {cultura['area_faixa']:.2f} m²")

    pausar()

def atualizar_cultura():

    instrucao()

    print("\n" + "="*50)
    print("✏️  Atualizar Cultura")
    print("="*50)

    if not culturas:
        print("")
        print("⚠️   Nenhuma cultura cadastrada.\n")
        pausar()
        return
    
    for i, cultura in enumerate(culturas, start=1):
        print("")
        print(f"{i}. {cultura['nome']}")

    print("")
    escolha = input("\nDigite o número da cultura que deseja atualizar: ")
    if voltar(escolha):
        return
    escolha = int(escolha) - 1

    if 0 <= escolha < len(culturas):
        cultura = culturas[escolha]

        print("")
        print(f"\nCultura selecionada: {cultura['nome']}")
        print("")
        print("Quais dados você deseja alterar?")
        print("")
        print("[1] Nome")
        print("[2] Formato")
        print("[3] Área Total")
        print("[4] Quantidade de Faixas")

        print("")
        opcao = input("👉 Digite o número da opção desejada: ")
        if voltar(opcao):
            return

        if opcao == "1":
            print("")
            cultura["nome"] = input("Novo nome: ")
            if voltar(cultura["nome"]):
                return

        elif opcao == "2":
            while True:
                print("")
                novo_formato = input("Novo formato: (retangular/circular)").lower()
                if voltar(novo_formato):
                    return
                if novo_formato in ["retangular", "circular"]:
                    cultura["formato"] = novo_formato
                    if novo_formato == "retangular":
                        while True:
                            try:
                                print("")
                                largura = input("Nova largura (em metros): ")
                                if voltar(largura):
                                    return
                                largura = float(largura)

                                print("")
                                comprimento = input("Novo comprimento (em metros): ")
                                if voltar(comprimento):
                                    return
                                comprimento = float(comprimento)

                                cultura["area"] = largura * comprimento
                                break
                            except ValueError:
                                print("")
                                print("⚠️   Valor inválido! Digite apenas números.\n")
                    else:  # circular
                        while True:
                            try:
                                print("")
                                raio = input("Novo raio (em metros): ")
                                if voltar(raio):
                                    return
                                raio = float(raio)

                                cultura["area"] = 3.14159 * (raio ** 2)
                                break
                            except ValueError:
                                print("")
                                print("⚠️   Valor inválido! Digite apenas números.\n")

                    print("")
                    print(f"✅ Nova área calculada: {cultura['area']:.2f} m².")
                    break
                else:
                    print("")
                    print("⚠️   Opção inválida! Precisa ser 'retangular' ou 'circular'. Tente novamente.\n")

        elif opcao == "3":
            if cultura["formato"] == "retangular":
                while True:
                    try:
                        print("")
                        largura = input("Nova largura (em metros): ")
                        if voltar(largura):
                            return
                        largura = float(largura)

                        print("")
                        comprimento = input("Novo comprimento (em metros): ")
                        if voltar(comprimento):
                            return
                        comprimento = float(comprimento)

                        cultura["area"] = largura * comprimento
                        print("")
                        print(f"✅ A nova área calculada corresponde a {cultura['area']:.2f} m².")
                        break
                    except ValueError:
                        print("")
                        print("⚠️   Valor inválido! Digite apenas números.\n")
            else:
                while True:
                    try:
                        print("")
                        raio = input("Novo raio (em metros): ")
                        if voltar(raio):
                            return
                        raio = float(raio)

                        cultura["area"] = 3.14159 * (raio ** 2)
                        print("")
                        print(f"✅ A nova área calculada corresponde a {cultura['area']:.2f} m².")
                        break
                    except ValueError:
                        print("")
                        print("⚠️   Valor inválido! Digite apenas números.\n")

        elif opcao == "4":
            while True:
                try:
                    print("")
                    cultura["faixas"] = input("Novo número de faixas: ")
                    if voltar(cultura["faixas"]):
                        return
                    cultura["faixas"] = int(cultura["faixas"])
                    break
                except ValueError:
                    print("")
                    print("⚠️   Valor inválido! Digite apenas números inteiros.\n")

        else:
            print("")
            print("⚠️   Opção inválida! Tente novamente.\n")
            pausar()
            return

        # Só recalcula se alterou formato, área ou faixas
        if opcao in ["2", "3", "4"]:
            if cultura["faixas"] > 0:
                cultura["area_faixa"] = cultura["area"] / cultura["faixas"]
                print("")
                print(f"✅ Essa cultura agora possui {cultura['faixas']} faixas, cada uma com área média de {cultura['area_faixa']:.2f} m²")

        salvar_dados()

        print("")
        print("\n✅ Cultura atualizada com sucesso!\n")
        pausar()

    else:
        print("")
        print("⚠️   Opção inválida! Tente novamente.\n")
        pausar()

def deletar_cultura():

    instrucao()

    print("\n" + "="*50)
    print("🗑️  Deletar Cultura")
    print("="*50)

    if not culturas:
        print("")
        print("⚠️   Nenhuma cultura cadastrada.\n")
        pausar()
        return

    for i, cultura in enumerate(culturas, start=1):
        print("")
        print(f"{i}. {cultura['nome']}")

    print("")
    escolha = input("\nDigite o número da cultura que deseja deletar: ")
    if voltar(escolha):
        return

    try:
        escolha = int(escolha) - 1
    except ValueError:
        print("")
        print("⚠️   Valor inválido! Digite apenas números.\n")
        pausar()
        return

    if 0 <= escolha < len(culturas):
        cultura = culturas[escolha]
        print("")
        confirmacao = input(f"Tem certeza que deseja deletar a cultura '{cultura['nome']}'? (sim/não): ").lower()
        if confirmacao == "sim":
            culturas.pop(escolha)
            salvar_dados()
            print("")
            print(f"\n✅   Cultura '{cultura['nome']}' deletada com sucesso!\n")
        else:
            print("")
            print("\n❌   Operação cancelada.\n")
    else:
        print("")
        print("⚠️   Opção inválida! Tente novamente.\n")

    pausar()

# ==============================
# FUNÇÕES DE AÇÃO - INSUMOS
# ==============================

def cadastrar_insumo():

    instrucao()

    print("\n" + "="*50)
    print("🧪 Cadastro de Insumo 🧪")
    print("="*50)

    print("")
    nome = input("👉 Digite o nome do insumo: ")
    if voltar(nome):
        return

    while True:
        try:
            print("")
            dose = input("👉 Digite a dose de aplicação (em litros por m²): ")
            if voltar(dose):
                return
            dose = float(dose)
            break
        except ValueError:
            print("")
            print("⚠️   Valor inválido! Digite um número, por exemplo: 0.5\n")

    insumo = {"nome": nome, "dose_m2": dose}
    insumos.append(insumo)
    salvar_dados()

    print("")
    print("\n✅   Insumo cadastrado com sucesso!")
    print("")
    print(f"🧪 Nome: {nome}")
    print(f"💧 Dose: {dose} L/m²\n")
    pausar()

def listar_insumos():
    print("\n" + "="*50)
    print("📋 Lista de Insumos Cadastrados")
    print("="*50)

    if not insumos:
        print("")
        print("⚠️   Nenhum insumo cadastrado.\n")
        pausar()
        return

    for i, insumo in enumerate(insumos, start=1):
        print("")
        print(f"\nInsumo {i}:")
        print(f"🧪 Nome: {insumo['nome']}")
        print(f"💧 Dose: {insumo['dose_m2']} L/m²")

    pausar()

def atualizar_insumo():

    instrucao()

    print("\n" + "="*50)
    print("✏️  Atualizar Insumo")
    print("="*50)

    if not insumos:
        print("")
        print("⚠️   Nenhum insumo cadastrado.\n")
        pausar()
        return

    for i, insumo in enumerate(insumos, start=1):
        print("")
        print(f"{i}. {insumo['nome']}")

    print("")
    escolha = input("\nDigite o número do insumo que deseja atualizar: ")
    if voltar(escolha):
        return

    try:
        escolha = int(escolha) - 1
    except ValueError:
        print("")
        print("⚠️   Valor inválido! Digite apenas números.\n")
        pausar()
        return

    if 0 <= escolha < len(insumos):
        insumo = insumos[escolha]
        print("")
        print(f"\nInsumo selecionado: {insumo['nome']}")
        print("")
        print("Quais dados você deseja alterar?")
        print("")
        print("[1] Nome")
        print("[2] Dose")

        print("")
        opcao = input("👉 Digite o número da opção desejada: ")
        if voltar(opcao):
            return

        if opcao == "1":
            print("")
            insumo["nome"] = input("Novo nome do insumo: ")
            if voltar(insumo["nome"]):
                return

        elif opcao == "2":
            while True:
                try:
                    print("")
                    insumo["dose_m2"] = input("Nova dose (em L/m²): ")
                    if voltar(insumo["dose_m2"]):
                        return
                    insumo["dose_m2"] = float(insumo["dose_m2"])
                    break
                except ValueError:
                    print("")
                    print("⚠️ Valor inválido! Digite um número, por exemplo: 0.5\n")

        else:
            print("")
            print("⚠️   Opção inválida! Tente novamente.\n")
            pausar()
            return
        
        salvar_dados()
        print("")
        print("\n✅   Insumo atualizado com sucesso!\n")
        pausar()

    else:
        print("")
        print("⚠️   Opção inválida! Tente novamente.\n")
        pausar()

def deletar_insumo():

    instrucao()

    print("\n" + "="*50)
    print("🗑️  Deletar Insumo")
    print("="*50)

    if not insumos:
        print("")
        print("⚠️   Nenhum insumo cadastrado.\n")
        pausar()
        return

    for i, insumo in enumerate(insumos, start=1):
        print("")
        print(f"{i}. {insumo['nome']}")

    print("")
    escolha = input("\nDigite o número do insumo que deseja deletar: ")
    if voltar(escolha):
        return

    try:
        escolha = int(escolha) - 1
    except ValueError:
        print("")
        print("⚠️   Valor inválido! Digite apenas números.\n")
        pausar()
        return

    if 0 <= escolha < len(insumos):
        insumo = insumos[escolha]
        print("")
        confirmacao = input(f"Tem certeza que deseja deletar o insumo '{insumo['nome']}'? (sim/não): ").lower()
        if confirmacao == "sim":
            insumos.pop(escolha)
            salvar_dados()
            print("")
            print(f"\n✅ Insumo '{insumo['nome']}' deletado com sucesso!\n")
        else:
            print("")
            print("\n❌   Operação cancelada.\n")
    else:
        print("")
        print("⚠️   Opção inválida! Tente novamente.\n")

    pausar()

# ==============================
# FUNÇÕES DE AÇÃO - GERAIS
# ==============================

def aplicar_insumo():

    instrucao()

    print("\n" + "="*50)
    print("💧 Aplicar Insumo em Cultura")
    print("="*50)

    if not culturas:
        print("")
        print("⚠️   Nenhuma cultura cadastrada.\n")
        pausar()
        return
    if not insumos:
        print("")
        print("⚠️   Nenhum insumo cadastrado.\n")
        pausar()
        return

    print("")
    print("\nCulturas disponíveis:")
    for i, cultura in enumerate(culturas, start=1):
        print("")
        print(f"{i}. {cultura['nome']} (Área: {cultura['area']:.2f} m², Faixas: {cultura['faixas']})")
    
    print("")
    escolha_cultura = input("\nDigite o número da cultura: ")
    if voltar(escolha_cultura):
        return

    try:
        escolha_cultura = int(escolha_cultura) - 1
    except ValueError:
        print("")
        print("⚠️   Valor inválido! Digite apenas números.\n")
        pausar()
        return

    if not (0 <= escolha_cultura < len(culturas)):
        print("")
        print("⚠️   Número inválido!\n")
        pausar()
        return
    cultura = culturas[escolha_cultura]

    print("")
    print("\nInsumos disponíveis:")
    for i, insumo in enumerate(insumos, start=1):
        print("")
        print(f"{i}. {insumo['nome']} (Dose: {insumo['dose_m2']} L/m²)")
    print("")
    escolha_insumo = input("\nDigite o número do insumo: ")
    if voltar(escolha_insumo):
        return

    try:
        escolha_insumo = int(escolha_insumo) - 1
    except ValueError:
        print("")
        print("⚠️   Valor inválido! Digite apenas números.\n")
        pausar()
        return

    if not (0 <= escolha_insumo < len(insumos)):
        print("")
        print("⚠️   Número inválido!\n")
        pausar()
        return
    insumo = insumos[escolha_insumo]

    # cálculos principais
    total = cultura["area"] * insumo["dose_m2"]
    por_faixa = total / cultura["faixas"] if cultura["faixas"] > 0 else 0
    area_faixa = cultura["area_faixa"]

    print("")
    print("\n✅ Cálculo realizado com sucesso!")
    print("")
    print(f"🌾 Cultura: {cultura['nome']}")
    print(f"🧪 Insumo: {insumo['nome']}")
    print(f"💧 Dose: {insumo['dose_m2']} L/m²")
    print(f"📏 Área total: {cultura['area']:.2f} m²")
    print(f"🔢 Quantidade de Faixas: {cultura['faixas']}")
    print(f"📐 Área média de cada faixa: {area_faixa:.2f} m²")
    print(f"🧴 Quantidade total de insumo necessário: {total:.2f} litros")
    print(f"💦 Quantidade de insumo necessário para cada faixa: {por_faixa:.2f} litros\n")
    pausar()

def sair_programa():
    print("")
    print("\n✅ Programa encerrado. Até logo, agricultor! 🌱\n")
    exit()

# ==============================
# LOOPS
# ==============================

def loop_principal():
    while True:
        menu_inicial()
        print("")
        opcao = input("👉 Digite o número da opção desejada: ")
        if opcao in acoes_principal:
            acoes_principal[opcao]()
        else:
            print("")
            print("\n⚠️   Opção inválida! Tente novamente.\n")
            pausar()

def loop_culturas():
    while True:
        menu_culturas()
        print("")
        opcao = input("👉 Digite o número da opção desejada: ")
        if opcao in acoes_culturas:
            if opcao == "5":
                break
            acoes_culturas[opcao]()
        else:
            print("")
            print("\n⚠️   Opção inválida! Tente novamente.\n")
            pausar()

def loop_insumos():
    while True:
        menu_insumos()
        print("")
        opcao = input("👉 Digite o número da opção desejada: ")
        if opcao in acoes_insumos:
            if opcao == "5":
                break
            acoes_insumos[opcao]()
        else:
            print("")
            print("\n⚠️   Opção inválida! Tente novamente.\n")
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