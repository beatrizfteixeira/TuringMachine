from Transicao import Transicao
from TuringMachine import TuringMachine

# Esse conjunto de transições define uma MT decididora sobre uma linguagem L que verifica se a entrada é um PALÍNDROMO
transicoes = [
    Transicao('q0', 'a', 'B', 'R', 'q1'),
    Transicao('q0', 'B', 'B', 'R', 'q7'),
    Transicao('q0', 'b', 'B', 'R', 'q4'),  
    Transicao('q1', 'a', 'a', 'R', 'q1'),
    Transicao('q1', 'b', 'b', 'R', 'q1'),
    Transicao('q1', 'B', 'B', 'L', 'q2'), 
    Transicao('q2', 'a', 'B', 'L', 'q3'),
    Transicao('q3', 'a', 'a', 'L', 'q3'),
    Transicao('q3', 'b', 'b', 'L', 'q3'),
    Transicao('q3', 'B', 'B', 'R', 'q0'),  
    Transicao('q4', 'a', 'a', 'R', 'q4'),
    Transicao('q4', 'b', 'b', 'R', 'q4'),
    Transicao('q4', 'B', 'B', 'L', 'q5'),
    Transicao('q5', 'b', 'B', 'L', 'q6'),  
    Transicao('q6', 'a', 'a', 'L', 'q6'),  
    Transicao('q6', 'b', 'b', 'L', 'q6'),   
    Transicao('q6', 'B', 'B', 'R', 'q0')   
]

# Alfabeto da linguagem
alfabeto = {'a', 'b', 'B'}
# A fita sempre terminando em B
fita = list("baabbaabB")
estado_inicial = 'q0'
estados_aceitacao = {'q7'}

tm = TuringMachine(alfabeto, fita, estado_inicial, estados_aceitacao, transicoes)
tm.executar()
