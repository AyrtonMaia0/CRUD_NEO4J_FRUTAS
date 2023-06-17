from neo4j import GraphDatabase
from senha import password
from uri import uri


# START FUNCOES CRUD
# Função para Criar um Registro de Fruta no banco
def create(tx, nome):
    tx.run("CREATE (:Fruta {nome: $nome})", nome=nome.upper())  # Converte para maiúsculas


# Função Ler todo os Registros Armazenados
def read(tx):
    result = tx.run("MATCH (p:Fruta) RETURN p.nome AS nome")
    for record in result:
        print(record["nome"])


# Função para Atualizar Registro de Fruta que esta armazenada no banco
def update(tx, antigoNome, novoNome):
    tx.run("MATCH (p:Fruta {nome: $antigoNome}) SET p.nome = $novoNome",
           antigoNome=antigoNome.upper(), novoNome=novoNome.upper())  # Converte para maiúsculas


# Função para Excluir um Registro do Banco
def delete(tx, nome):
    tx.run("MATCH (p:Fruta {nome: $nome}) DELETE p", nome=nome.upper())  # Converte para maiúsculas

# END FUNCOES CRUD




# Função Menu
def Menu():
    print("\n\n=== Menu ===")
    print("1. Criar uma Fruta")
    print("2. Visualizar todas as Frutas ")
    print("3. Atualizar uma Fruta")
    print("4. Excluir uma Fruta")
    print("0. Sair")


# Função para ler a opção do usuário
def Escolha():
    opcao = input("Digite a opção desejada: ")
    return opcao


# START FUNÇÃO MAIN
def main():

    # Aqui é a parte que Conecta ao banco Neo4j
    driver = GraphDatabase.driver(uri, auth=("neo4j", password))

    while True:
        Menu()
        opcao = Escolha()

        with driver.session() as session:
            if opcao == "1":
                print("\n\n----CREATE----")
                nome = input("Digite o nome da fruta: ")
                session.write_transaction(create, nome)
                print("Fruta criada com sucesso!\n")

            elif opcao == "2":
                print("\n\n----READ----")
                session.read_transaction(read)
                print("\n")

            elif opcao == "3":
                print("\n\n----UPDATE----")
                antigoNome = input("Digite o nome atual da fruta: ")
                novoNome = input("Digite o novo nome da fruta: ")
                session.write_transaction(update, antigoNome, novoNome)
                print("Fruta alterada com sucesso!\n")

            elif opcao == "4":
                print("\n\n----DELETE----")
                nome = input("Digite o nome da fruta a ser excluída: ")
                session.write_transaction(delete, nome)
                print("Fruta excluída com sucesso!\n")

            elif opcao == "0":
                print("Obrigado e Volte Sempre!\n\n")
                break

            else:
                print("Opção inválida. Por favor, tente novamente.\n")

    # Aqui é o fechamento do driver que conecta ao banco
    driver.close()
# END FUNÇÃO MAIN


# Aqui é uma Verificação de Módulo, para ser chamado
if __name__ == "__main__":
    # Chamada da função Main
    main()
