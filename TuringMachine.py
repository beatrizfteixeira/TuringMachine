class TuringMachine:

    def __init__(self, alfabeto, fita, estado_inicial, estados_aceitacao, transicoes):
        self.alfabeto = alfabeto
        self.fita = fita
        self.estado_inicial = estado_inicial
        self.estados_aceitacao = estados_aceitacao
        self.estado_atual = estado_inicial
        self.cabeca = 0
        self.transicoes = transicoes
        self.max_passos = 5000
        self.num_passos = 0

    def mover_cabeca(self, direcao):
        if direcao == "esquerda" or direcao == "L":
            self.cabeca -= 1
        elif direcao == "direita" or direcao == "R":
            self.cabeca += 1

    def ler_simbolo(self):
        return self.fita[self.cabeca]

    def escrever_simbolo(self, simbolo):
        self.fita[self.cabeca] = simbolo

    def executar_transicao(self):
        simbolo = self.ler_simbolo()
        transicao_encontrada = False
        for transicao in self.transicoes:
            if transicao.estado_atual == self.estado_atual and transicao.simbolo_lido == simbolo:
                #print(transicao.estado_atual + "lendo" + transicao.simbolo_lido)
                transicao_encontrada = True
                break
        
        if not transicao_encontrada:
            print("Aviso: Transição não encontrada. Continuando a execução.")
            #print("transicao " + self.estado_atual + "lendo " + self.fita[self.cabeca])
            return False
        
        self.escrever_simbolo(transicao.simbolo_escrito)
        self.mover_cabeca(transicao.movimento)
        self.estado_atual = transicao.estado_novo
        
        return True

    def executar(self):
        while self.num_passos < self.max_passos:
            if self.estado_atual in self.estados_aceitacao:
                print(f"A entrada foi aceita. Estado atual: {self.estado_atual}")
                break
            
            if self.cabeca < 0 or self.cabeca >= len(self.fita):
                print("A cabeça de leitura/gravação ultrapassou os limites da fita.")
                break
            
            if not self.executar_transicao():
                print("A execução foi interrompida devido a uma transição não encontrada.")
                break
            
            self.num_passos += 1
        
        if self.estado_atual not in self.estados_aceitacao:
            print(f"A entrada foi rejeitada. Estado atual: {self.estado_atual}")

        print(f"Estados de aceitação: {self.estados_aceitacao}")
        print("Fita no final da execução:")
        print(''.join(self.fita))
