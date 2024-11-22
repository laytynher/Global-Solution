teclas_para_letras = {
    '2': 'A', '22': 'B', '222': 'C',
    '3': 'D', '33': 'E', '333': 'F',
    '4': 'G', '44': 'H', '444': 'I',
    '5': 'J', '55': 'K', '555': 'L',
    '6': 'M', '66': 'N', '666': 'O',
    '7': 'P', '77': 'Q', '777': 'R', '7777': 'S',
    '8': 'T', '88': 'U', '888': 'V',
    '9': 'W', '99': 'X', '999': 'Y', '9999': 'Z'
}

sequencias_teclas = [
    "33", "7", "666", "222", "2", "22", "666", "2", 
    "77", "88", "33", "66", "2", "666", "888", "666", 
    "555", "8", "2", "6", "2", "444", "7777"
]

def traduzir_teclas(sequencias, mapeamento):
    mensagem = ''.join(mapeamento.get(seq, '') for seq in sequencias)
    return mensagem

mensagem_traduzida = traduzir_teclas(sequencias_teclas, teclas_para_letras)

resultado = f"FIAP{{{mensagem_traduzida}}}"
print(resultado)
