banner = r'''
###########################
####!!! Feche tudo !!!!!!!#
###########################
'''


def open_chest():
    with open('flag.txt', 'r') as f:
        print(f.read())


blacklist = [
    'import', 'os', 'sys', 'breakpoint',
    'flag', 'txt', 'read', 'eval', 'exec',
    'dir', 'print', 'subprocess', '[', ']',
    'echo', 'cat', '>', '<', '"', '\'', 'open' 
]

print(banner)

while True:
    command = input('O baú está esperando...... ')

    if any(b in command for b in blacklist):
        print('Comando invalido!')
        continue

    try:
        exec(command)
    except Exception:
        print('Voce foi fechado...')
        exit(1337)
