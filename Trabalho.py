import json

def carregar_dados():
    try:
        # Tenta abrir o arquivo JSON para carregar os dados
        with open("Trabalho_Alysson\produtos.json", 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        # Se o arquivo não for encontrado, retorna um dicionário vazio
        return {}

# Carrega os dados do arquivo JSON ou cria um dicionário vazio
banco_dados = carregar_dados()
opcao = 0

while opcao != 8:
    print("="*10)
    print("1 - Inserir um Produto")
    print("2 - Consultar um produto por código")
    print("3 - Consultar todos produtos")
    print("4 - Alterar preço")
    print("5 - Aplicar acréscimo ou desconto / todos")
    print("6 - Salvar")
    print("7 - Excluir um Produto")
    print("8 - Sair")
    
    escolha = input("Escolha a opção: ")
   
    if escolha.strip() and escolha.isdigit():
        opcao = int(escolha)
    else:
        print("Opção inválida.")

    if opcao == 1:
        print('-'*10)
        print("Cadastro")
        codigo = input('Digite o código: ')

        if codigo in banco_dados:
            print("Produto já inserido!")
        else:
            nome = input('Digite o nome do produto: ')
            preco = float(input("Digite o preço do kg: "))
            quantidade = float(input("Digite a quantidade de produtos: "))

            # Adiciona um novo produto ao banco de dados
            banco_dados[codigo] = {"nome": nome, "preco": preco, "quantidade": quantidade}

    elif opcao == 2:
        # Seção de Consulta de Produto por Código
        print('-'*10)
        print("Consultar um produto por código")
        codigo = input('Digite o código do produto: ')

        if codigo in banco_dados:
            produto = banco_dados[codigo]
            print(f"Nome: {produto['nome']}")
            print(f"Preço: {produto['preco']}")
            print(f"Quantidade: {produto['quantidade']}")
        else:
            print("Produto não encontrado.")

    elif opcao == 3:
        # Seção de Consulta de Todos os Produtos
        print('-'*10)
        print("Consultar todos produtos")
        if banco_dados:
            for codigo, produto in banco_dados.items():
                print(f"Código: {codigo}")
                print(f"Nome: {produto['nome']}")
                print(f"Preço: {produto['preco']}")
                print(f"Quantidade: {produto['quantidade']}")
                print("")
        else:
            print("Nenhum produto cadastrado.")

    elif opcao == 4:
        # Seção de Alteração de Preço do Produto
        print('-'*10)
        print("Alterar preço/produto")
        codigo = input('Digite o código do produto: ')

        if codigo in banco_dados:
            novo_preco = float(input('Digite o novo preço: '))
            # Altera o preço do produto no banco de dados
            banco_dados[codigo]['preco'] = novo_preco
        else:
            print("Produto não encontrado.")

    elif opcao == 5:
        # Seção de Aplicação de Acréscimo ou Desconto em Todos os Produtos
        print('-'*10)
        print("Aplicar acréscimo ou desconto / todos")
        percentual = float(input("Digite o percentual de acréscimo (positivo) ou desconto (negativo): "))
        
        for codigo, produto in banco_dados.items():
            produto['preco'] += produto['preco'] * (percentual / 100)
        
        print("Acréscimo ou desconto aplicado em todos os produtos.")

    elif opcao == 6:
        # Seção de Salvamento dos Dados
        print('-'*10)
        print("Salvando....")
        with open("Projeto\estoque.json", 'w') as arquivo:
            # Salva os dados no arquivo JSON com formatação indentada
            json.dump(banco_dados, arquivo, indent=4)

    elif opcao == 7:
        # Seção de Exclusão de Produto
        print('-'*10)
        print("Excluir um Produto")
        codigo = input('Digite o código do produto a ser excluído: ')

        if codigo in banco_dados:
            confirmacao = input(f"Você tem certeza que deseja excluir o produto '{banco_dados[codigo]['nome']}' (S/N)? ").strip().lower()
            if confirmacao == 's':
                # Remove o produto do banco de dados
                del banco_dados[codigo]
                print(f"Produto '{codigo}' excluído com sucesso.")
            else:
                print("Exclusão cancelada.")
        else:
            while True:
                opcao_invalida = input("Produto não encontrado. Digite 'T' para tentar novamente ou 'M' para voltar ao menu central: ").strip().lower()
                if opcao_invalida == 't':
                    codigo = input('Digite o código do produto a ser excluído: ')
                    if codigo in banco_dados:
                        confirmacao = input(f"Você tem certeza que deseja excluir o produto '{banco_dados[codigo]['nome']}' (S/N)? ").strip().lower()
                        if confirmacao == 's':
                            # Remove o produto do banco de dados
                            del banco_dados[codigo]
                            print(f"Produto '{codigo}' excluído com sucesso.")
                        else:
                            print("Exclusão cancelada.")
                        break
                    else:
                        print("Produto não encontrado.")
                elif opcao_invalida == 'm':
                    break
                else:
                    print("Opção inválida. Digite 'T' para tentar novamente ou 'M' para voltar ao menu central.")

    elif opcao == 8:
        # Seção de Encerramento
        print('-'*10)
        print("Saindo")
    else:
        # Seção de Opção Inválida
        print('-'*10)
        print('Opção Inválida')
