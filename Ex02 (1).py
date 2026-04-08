class No:
    def __init__(self, dado):
        self.dado = dado
        self.dir = None
        self.esq = None

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserir_final(self, dado):
        novo = No(dado)
        if self.tamanho == 0:
            self.inicio = novo
            self.fim = novo
        else:
            novo.esq = self.fim
            self.fim.dir = novo
            self.fim = novo
        self.tamanho += 1

    def remover_no(self, aux):
        if aux is not None:
            if self.tamanho == 1:
                self.inicio = None
                self.fim = None
            elif aux == self.inicio:
                self.inicio = aux.dir
                self.inicio.esq = None
            elif aux == self.fim:
                self.fim = aux.esq
                self.fim.dir = None
            else:
                aux.esq.dir = aux.dir
                aux.dir.esq = aux.esq
            
            self.tamanho -= 1
            return True
        return False

class Processo:
    def __init__(self, id_proc, nome, tempo_total):
        self.id = id_proc
        self.nome = nome
        self.tempo_total = tempo_total
        self.tempo_restante = tempo_total
        self.tempo_retorno = 0
        self.tempo_espera = 0

def modulo_gerenciamento_aria():
    fila = Lista()
    lista_relatorio = []

    print("===== SISTEMA ARIA =====")
    qtd = int(input("Quantos processos deseja inserir? "))

    # Entrada de dados
    for _ in range(qtd):
        print("-" * 20)
        id_proc = input("ID do processo: ")
        nome = input("Nome do processo: ")
        tempo = int(input("Tempo necessario: "))
        
        p = Processo(id_proc, nome, tempo)
        fila.inserir_final(p)
        lista_relatorio.append(p)

    print("-" * 20)
    fatia_tempo = int(input("Informe a fatia de tempo da CPU: "))

    print("\nSIMULACAO DA EXECUCAO")
    tempo_atual = 0
    no_atual = fila.inicio

    while fila.tamanho > 0:
        p = no_atual.dado
        
        execucao = fatia_tempo if p.tempo_restante > fatia_tempo else p.tempo_restante
        
        tempo_atual += execucao
        p.tempo_restante -= execucao
        
        proximo_no = no_atual.dir if no_atual.dir else fila.inicio

        if p.tempo_restante > 0:
            print(f"t = {tempo_atual - execucao} -> {p.nome} executa {execucao} u | restam: {p.tempo_restante} u")
        else:
            p.tempo_retorno = tempo_atual
            print(f"t = {tempo_atual - execucao} -> {p.nome} executa {execucao} u | ✓ CONCLUIDO (terminou em t = {tempo_atual} )")
            fila.remover_no(no_atual)
        
        no_atual = proximo_no

    print("\nRELATORIO FINAL - ARIA Recovery Module")
    print(f"Fatia de tempo: {fatia_tempo} unidades\n")
    print("Processo - Tempo Total - Tempo Espera - Tempo Retorno")
    
    soma_espera = 0
    soma_retorno = 0
    
    for p in lista_relatorio:
        p.tempo_espera = p.tempo_retorno - p.tempo_total
        soma_espera += p.tempo_espera
        soma_retorno += p.tempo_retorno
        
      
        print(f"{p.nome:<13} -   {p.tempo_total}u   -   {p.tempo_espera}u   -   {p.tempo_retorno}u")
    
    media_espera = soma_espera / len(lista_relatorio)
    media_retorno = soma_retorno / len(lista_relatorio)
    
    print(f"Media - {media_espera:.1f}u - {media_retorno:.1f}u\n")
    
    if media_espera < 16:
        print("ARIA reativada com sucesso.")
        print("Tempo medio de espera abaixo do limite critico.")
        print("Synthetica esta salva.")
    else:
        print("Falha critica confirmada. Iniciando protocolo de desligamento de emergencia.")

if __name__ == "__main__":
    modulo_gerenciamento_aria()