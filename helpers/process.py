from time import sleep as sl
from time import sleep_ms as slm
from notigram import ping

def messagealert():
    time = 1800
    # (24-40)
    # ApiScrapp
    # 15% Cortes -> APICutText,
    # 10% ImgtoText-> ApiImg,
    # 50% Texto -> ApiPara,
    # 20% Img -> Apimg,
    # 4% Citas -> ApiCita,
    # 1% Reporte -> ApiRep
    # ping('daa39d53-6283-47a1-b945-b7ee6528dde0', 'Conteo de tiempo para la emulación')
    while time > 0:
        ping('daa39d53-6283-47a1-b945-b7ee6528dde0', f'Restan {time} seg')
        # print("Enviando mensaje")
        time-=1
        slm(1)