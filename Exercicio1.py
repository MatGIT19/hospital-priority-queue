class No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None


class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserir(self, dado):
        novo = No(dado)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
            novo.dir = novo
            novo.esq = novo
        else:
            novo.esq = self.fim
            novo.dir = self.inicio
            self.fim.dir = novo
            self.inicio.esq = novo
            self.fim = novo

        self.tamanho += 1

    def inserir_posicao(self, posicao, dado):
        novo = No(dado)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
            novo.dir = novo
            novo.esq = novo
            self.tamanho += 1
            return

        if posicao <= 1:
            novo.dir = self.inicio
            novo.esq = self.fim
            self.inicio.esq = novo
            self.fim.dir = novo
            self.inicio = novo
            self.tamanho += 1
            return

        if posicao > self.tamanho:
            self.inserir(dado)
            return

        aux = self.inicio
        for i in range(1, posicao - 1):
            aux = aux.dir

        novo.dir = aux.dir
        novo.esq = aux
        aux.dir.esq = novo
        aux.dir = novo

        self.tamanho += 1

    def imprimir(self):
        if self.inicio is None:
            print("Lista vazia")
            return

        aux = self.inicio
        while True:
            print(aux.dado, end=' ')
            aux = aux.dir
            if aux == self.inicio:
                break
        print()

    def remover(self, dado):
        if self.inicio is None:
            return False

        aux = self.inicio

        while True:
            if aux.dado == dado:
                if self.tamanho == 1:
                    self.inicio = None
                    self.fim = None

                elif aux == self.inicio:
                    self.inicio = aux.dir
                    self.inicio.esq = self.fim
                    self.fim.dir = self.inicio

                elif aux == self.fim:
                    self.fim = aux.esq
                    self.fim.dir = self.inicio
                    self.inicio.esq = self.fim

                else:
                    aux.esq.dir = aux.dir
                    aux.dir.esq = aux.esq

                aux.esq = None
                aux.dir = None
                self.tamanho -= 1
                return True

            aux = aux.dir
            if aux == self.inicio:
                break

        return False
    
lista = Lista()

lista.inserir(10)
lista.inserir(20)
lista.inserir(30)
lista.inserir(40)
lista.imprimir()

lista.inserir_posicao(1, 5)
lista.imprimir()

lista.inserir_posicao(3, 15)
lista.imprimir()

lista.inserir_posicao(20, 50)
lista.imprimir()

lista.remover(5)
lista.imprimir()

lista.remover(30)
lista.imprimir()

lista.remover(50)
lista.imprimir()