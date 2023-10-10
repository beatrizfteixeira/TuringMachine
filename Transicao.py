class Transicao:
    def __init__(self, estado_atual, simbolo_lido, simbolo_escrito, movimento, estado_novo):
        self.estado_atual = estado_atual
        self.simbolo_lido = simbolo_lido
        self.simbolo_escrito = simbolo_escrito
        self.movimento = movimento
        self.estado_novo = estado_novo