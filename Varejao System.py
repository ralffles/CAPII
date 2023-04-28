class Produto:
    def __init__(self, cod, nome, preco, estoque):
        self.cod = cod
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

class CadastroProduto:
    def __init__(self):
        self.produtos = []
    
    def cadastrar_produto(self, cod, nome, preco, estoque):
        produto = Produto(cod, nome, preco, estoque)
        self.produtos.append(produto)
        print("Produto cadastrado.")

    def listar_produtos(self):
        if len(self.produtos) == 0:
            print("Não há produto cadastrado.")
        else:
            for produto in self.produtos:
                print("Codigo: {}".format(produto.cod))
                print("Nome: {}".format(produto.nome))
                print("Preco: {}".format(produto.preco))
                print("estoque: {}".format(produto.estoque))

cadastro = CadastroProduto()

while True:
    print ("Varejao System")
    print("1- Cadastrar Produtos")
    print("2- Listar Produtos")
    print("3- Buscar Produtos")
    print("4- Alterar Produto")
    print("5- Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cod = int(input("Digite o código do produto: "))
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o valor do produto: "))
        estoque = int(input("Digite a quantidade de estoque: "))
        cadastro.cadastrar_produto(cod, nome, preco, estoque)
    
    elif opcao =="2":
        cadastro.listar_produtos()
    
    elif opcao =="5":
        break
    else:
        print("Opção inválida.")