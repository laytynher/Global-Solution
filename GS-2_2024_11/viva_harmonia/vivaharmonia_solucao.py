from pwn import remote
from Crypto.Util.number import long_to_bytes
from colorama import Fore, Style, init

init(autoreset=True)

modulo = 256

def obter_valores(conexao, posicao_bit):
    conexao.sendline(str(posicao_bit).encode())
    conexao.recvuntil(b"Aqui est\xc3\xa1 o texto cifrado:")

    while True:
        linha_a = conexao.recvline().decode().strip()
        if linha_a.startswith("A ="):
            break

    while True:
        linha_b = conexao.recvline().decode().strip()
        if linha_b.startswith("b ="):
            break

    valor_a = int(linha_a.split('=')[1].strip())
    valor_b = int(linha_b.split('=')[1].strip())
    return valor_a, valor_b

def converter_bits_em_bytes(bits):
    while len(bits) % 8 != 0:
        bits.insert(0, 0)  # Adiciona zeros à esquerda para múltiplos de 8

    resultado_bytes = bytearray(len(bits) // 8)
    for i in range(0, len(bits), 8):
        byte = 0
        for posicao, bit in enumerate(bits[i:i + 8]):
            byte |= (bit << (7 - posicao))
        resultado_bytes[i // 8] = byte
    return bytes(resultado_bytes)

def exibir_bits_formatados(bits):
    visualizacao = ""
    for bit in bits:
        cor = Fore.CYAN if bit == 1 else Fore.MAGENTA
        visualizacao += f"{cor}{bit}{Style.RESET_ALL}"
    print(f"[INFO] Sequência atual de bits: {visualizacao}")

def reconstruir_flag():
    sequencia_bits = []
    comprimento = 287  # Quantidade total de bits a analisar

    for posicao in range(comprimento):
        bit_definido = False

        for tentativa in range(30):  # Mantido o número de tentativas original
            try:
                a, b = obter_valores(conexao, posicao)
                if b < 0 or b >= modulo:
                    sequencia_bits.append(1)
                    bit_definido = True
                    break
            except ValueError:
                continue

        if not bit_definido:
            sequencia_bits.append(0)

        exibir_bits_formatados(sequencia_bits)

    flag_bytes = converter_bits_em_bytes(sequencia_bits)
    print(f"[SUCESSO] Flag gerada em bytes: {flag_bytes}")
    print("Dica: Adicione um 0 no início e converta para ASCII!")
    return flag_bytes

if __name__ == "__main__":
    servidor = '167.71.240.113'
    porta = 1337

    conexao = remote(servidor, porta, level='error')
    print(f"[CONECTADO] Acessando o servidor: {servidor}:{porta}")
    print("Processamento iniciado... isso pode levar alguns minutos.")
    print("Acompanhe o progresso visualizando a sequência de bits.")
    reconstruir_flag()
    print("Finalizado! Certifique-se de ajustar e validar a flag extraída.")