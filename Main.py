import json
import os

ARQUIVO = "equipamentos.json"

# Função para carregar os equipamentos do arquivo
def carregar_equipamentos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Função para salvar os equipamentos no arquivo
def salvar_equipamentos(equipamentos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(equipamentos, f, indent=4, ensure_ascii=False)

# Função para cadastrar equipamento
def cadastrar_equipamento(nome, codigo):
    equipamentos = carregar_equipamentos()

    # Verifica se já existe equipamento com o mesmo código
    for equipamento in equipamentos:
        if equipamento["codigo"] == codigo:
            print("⚠️ Já existe um equipamento com esse código.")
            return

    novo_equipamento = {
        "nome": nome,
        "codigo": codigo
    }

    equipamentos.append(novo_equipamento)
    salvar_equipamentos(equipamentos)
    print("✅ Equipamento cadastrado com sucesso!")

# Função para buscar equipamento pelo código
def buscar_equipamento(codigo):
    equipamentos = carregar_equipamentos()

    for equipamento in equipamentos:
        if equipamento["codigo"] == codigo:
            print("🔎 Equipamento encontrado:")
            print(f"Nome: {equipamento['nome']}")
            print(f"Código: {equipamento['codigo']}")
            return

    print("❌ Equipamento não encontrado.")

# Menu simples
def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Cadastrar equipamento")
        print("2 - Buscar equipamento por código")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do equipamento: ")
            codigo = input("Digite o código do equipamento: ")
            cadastrar_equipamento(nome, codigo)

        elif opcao == "2":
            codigo = input("Digite o código do equipamento: ")
            buscar_equipamento(codigo)

        elif opcao == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

# Executa o programa
menu()

[
    {
        "nome": "Notebook Dell",
        "codigo": "123"
    },
    {
        "nome": "Impressora HP",
        "codigo": "456"
    }
]