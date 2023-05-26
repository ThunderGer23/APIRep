
from random import randint as ri
from time import sleep as sl

from notigram import ping

from helpers.respuestas import messageAPICutPoli as POL
from helpers.respuestas import messageAPICutRespTec as MAC
from helpers.respuestas import messageAPICutRespUAM as UAM
from helpers.respuestas import messageAPICutRespUNAM as UNAM


# addressee = 'Cuando2son1@hotmail.com'
correo = 'jaames11@hotmail.com'
pas ='Wellneverdie.201'
Token = 'daa39d53-6283-47a1-b945-b7ee6528dde0'

def messagealert():
    time = ri(1500, 2400) # (24-40)min
    scrapp = time*.05   # ApiScrapp
    unam = scrapp *.03
    uam = scrapp *.03
    tec = scrapp *.03
    ipn = scrapp *.01
    cut = time*.10 # 15% Cortes -> APICutText,
    toImg = time*.10 # 10% ImgtoText-> ApiImg,
    para = time*.50 # 50% Texto -> ApiPara,
    img = time*.20 # 20% Img -> Apimg,
    cita = time*.05 # 4% Citas -> ApiCita,
    rep = 1 # 1% Reporte -> ApiRep

    while rep > 0:
        while scrapp > 0 :
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
        print(f'{cut} {toImg} {para} {img} {cita}')
        if (cut > 0):
            ping(Token, f'Fileteando docs')
            cut-=1
        elif (toImg > 0):
            ping(Token, f'Convirtiendo Imagenes')
            toImg-=1
        elif (para > 0):
            ping(Token, f'Analizando docs')
            para-=1
        elif (img > 0):
            ping(Token, f'Analizando imgs')
            img-=1
        elif (cita > 0):
            ping(Token, f'Analizando citas')
            cita-=1
        else:
            rep = 0
    ping(Token, f'Llamen a dios por otro cliente iluminado :v')