from Transicao import Transicao
from TuringMachine import TuringMachine

# Esse conjunto de transições define uma MT decididora sobre uma linguagem L = {0^n 1^n} 
transicoes = [
    Transicao('q_inicial', 'B', 'B', 'R', 'q0'),
    Transicao('q0', '0', 'X', 'R', 'q1'),
    Transicao('q0', 'Y', 'Y', 'R', 'q3'),
    Transicao('q0', 'B', 'B', 'L', 'q4'),  
    Transicao('q1', 'Y', 'Y', 'R', 'q1'),
    Transicao('q1', '0', '0', 'R', 'q1'),
    Transicao('q1', '1', 'Y', 'L', 'q2'), 
    Transicao('q2', 'Y', 'Y', 'L', 'q2'),
    Transicao('q2', '0', '0', 'L', 'q2'),
    Transicao('q2', 'X', 'X', 'R', 'q0'),
    Transicao('q3', 'Y', 'Y', 'R', 'q3'),
    Transicao('q3', 'B', 'B', 'L', 'q4'),
    
]

# Alfabeto da linguagem
alfabeto = {'0', '1', 'Y', 'X' 'B'}

fita1 = list("000111B") # Deve ser aceita pois |0| = |1|

fita2 = list("00B") # Deve ser rejeitada pois |0| > |1|

fita3 = list("1100B") # Deve ser rejeitada pois a entrada não cumpre a sequência 0 e depois 1

fita4 = list("001111B") # Deve ser rejeitada pois |0| < |1|

fita5 = list("0011B") # Deve ser aceita pois |0| = |1|

estado_inicial = 'q0'

estados_aceitacao = {'q4'}

tm = TuringMachine(alfabeto, fita5, estado_inicial, estados_aceitacao, transicoes)
tm.executar()
