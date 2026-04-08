class No:
    def __init__(self, nome, prioritario):
        self.nome = nome
        self.prioritario = prioritario
        self.esq = None
        self.dir = None


class ListaHospital:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserir(self, nome, prioritario):
        novo = No(nome, prioritario)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
            self.tamanho += 1
            return

        if prioritario == False:
            novo.esq = self.fim
            self.fim.dir = novo
            self.fim = novo
            self.tamanho += 1
            return

        atual = self.inicio

        while atual is not None and atual.prioritario == True:
            atual = atual.dir

        if atual is None:
            novo.esq = self.fim
            self.fim.dir = novo
            self.fim = novo

        elif atual == self.inicio:
            novo.dir = self.inicio
            self.inicio.esq = novo
            self.inicio = novo

        else:
            anterior = atual.esq
            anterior.dir = novo
            novo.esq = anterior
            novo.dir = atual
            atual.esq = novo

        self.tamanho += 1

    def atender(self):
        if self.inicio is None:
            print("Fila vazia")
            return

        paciente = self.inicio
        self.inicio = self.inicio.dir

        if self.inicio is not None:
            self.inicio.esq = None
        else:
            self.fim = None

        self.tamanho -= 1
        tipo = "PRIORITARIO" if paciente.prioritario else "COMUM"
        print("Atendido:", paciente.nome, "-", tipo)

    def exibir(self):
        if self.inicio is None:
            print("Fila vazia")
            return

        atual = self.inicio
        posicao = 0

        while atual:
            tipo = "PRIORITARIO" if atual.prioritario else "COMUM"
            print(posicao, "-", atual.nome, "-", tipo)
            atual = atual.dir
            posicao += 1

    def buscar(self, nome):
        atual = self.inicio
        posicao = 0

        while atual:
            if atual.nome.lower() == nome.lower():
                tipo = "PRIORITARIO" if atual.prioritario else "COMUM"
                print("Encontrado na posicao", posicao, "-", tipo)
                return

            atual = atual.dir
            posicao += 1

        print("Paciente nao encontrado")


fila = ListaHospital()

while True:
    print("\n1 - Inserir paciente")
    print("2 - Atender paciente")
    print("3 - Exibir fila")
    print("4 - Buscar paciente")
    print("5 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        resposta = input("Eh prioritario? (s/n): ")
        prioritario = resposta.lower() == "s"
        fila.inserir(nome, prioritario)

    elif opcao == "2":
        fila.atender()

    elif opcao == "3":
        fila.exibir()

    elif opcao == "4":
        nome = input("Digite o nome: ")
        fila.buscar(nome)

    elif opcao == "5":
        print("Programa encerrado")
        break

    else:
        print("Opcao invalida")
        
        