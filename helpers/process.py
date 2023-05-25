from time import sleep as sl
from time import sleep_ms as slm
from notigram import ping
from random import randint as ri
from helpers.respuestas import messageAPICutRespUNAM as UNAM
from helpers.respuestas import messageAPICutRespUAM as UAM
from helpers.respuestas import messageAPICutRespTec as MAC
from helpers.respuestas import messageAPICutPoli as POL

Token = 'daa39d53-6283-47a1-b945-b7ee6528dde0'

def messagealert():
    time = ri(1500, 2400) # (24-40)min
    scrapp = time*.10    # ApiScrapp
    unam = scrapp *.3
    uam = scrapp *.3
    tec = scrapp *.3
    ipn = scrapp *.1
    cut = time*.10 # 15% Cortes -> APICutText,
    toImg = time*.5 # 10% ImgtoText-> ApiImg,
    para = time*.50 # 50% Texto -> ApiPara,
    img = time*.20 # 20% Img -> Apimg,
    cita = time*.04 # 4% Citas -> ApiCita,
    rep = time*0.1 # 1% Reporte -> ApiRep

    while rep > 0:
        wait = ri(0, 100)*0.01

        if (scrapp > 0 ):
            ping(Token, f'Iniciando Busqueda en repositorios')
            if (unam > 0):
                ping(Token, UNAM())
                unam -=1
            elif (uam > 0):
                ping(Token, UAM())
                uam -=1
            elif (tec > 0):
                ping(Token, MAC())
                tec -=1
            elif (ipn > 0):
                ping(Token, POL())
                ipn -=1
            else:
                scrapp = 0
        ping(Token, f'Fileteando documentos')
        if (cut > 0):
            ping(Token, f'Fileteando docs')
            cut-=1
        slm(wait)