from time import sleep as sl
from notigram import ping

def messagealert():
    time = 1800
    ping('daa39d53-6283-47a1-b945-b7ee6528dde0', 'Conteo de tiempo para la emulación')
    while time > 0:
        ping('daa39d53-6283-47a1-b945-b7ee6528dde0', f'Restan {time} seg')
        # print("Enviando mensaje")
        time-=1
        sl(1)