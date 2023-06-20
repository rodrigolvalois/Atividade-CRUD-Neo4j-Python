from py2neo import Graph, Node, Relationship

# Conectar ao banco de dados Neo4j
graph= Graph("bolt://localhost:7687", auth=("neo4j", "12345678"))

# Função para criar um carro
def criar_carro(nome):
    carro = Node("Carro", nome=nome)
    graph.create(carro)
    return carro

# Função para obter todos os carros
def obter_carros():
    query = "MATCH (carro:Carro) RETURN carro"
    result = graph.run(query)
    return [record["carro"] for record in result]

# Função para atualizar o nome de um carro
def atualizar_carro(carro, nome):
    carro["nome"] = nome
    graph.push(carro)

# Função para excluir um carro
def excluir_carro(carro):
    graph.delete(carro)

# Exemplo de uso do CRUD
carro1 = criar_carro("Fusca")
carro2 = criar_carro("Gol")

print("Carros antes da atualização:")
carros = obter_carros()
for carro in carros:
    print(carro["nome"])

atualizar_carro(carro1, "Fusca 1970")

print("Carros após a atualização:")
carros = obter_carros()
for carro in carros:
    print(carro["nome"])

excluir_carro(carro2)

print("Carros após a exclusão:")
carros = obter_carros()
for carro in carros:
    print(carro["nome"])

#Fim do CRUD

#Menu usuário
def menu():
    while True:
        print("\n===== Menu =====")
        print("1. Criar carro")
        print("2. Obter nome dos carros")
        print("3. Atualizar carro")
        print("4. Excluir carro")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do carro: ")
            criar_carro(nome)
            print("Carro criado com sucesso!")
        elif opcao == "2":
            nome = input("Digite o nome do carro: ")
            carro = obter_carros()
            if carro:
                print(f"Carro encontrado: {carro}")
            else:
                print("Carro não encontrado.")
        elif opcao == "3":
            nome = input("Digite o nome do carro: ")
            novo_nome = input("Digite o novo nome do carro: ")
            carro = obter_carros(nome)
            if carro:
                atualizar_carro(carro, novo_nome)
                print("Carro atualizado com sucesso!")
            else:
                print("Carro não encontrado.")
        elif opcao == "4":
            nome = input("Digite o nome do carro: ")
            carro = obter_carros(nome)
            if carro:
                excluir_carro(carro)
                print("Carro excluído com sucesso!")
            else:
                print("Carro não encontrado.")
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

menu()

#Retorna para o menu (em loop)