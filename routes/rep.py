import smtplib
import email.mime.multipart
import email.mime.base
from random import randint as ri
from notigram import ping
from helpers.respuestas import messageResp as mR
from helpers.respuestas import messageAPICutRespUNAM as UNAM
from helpers.respuestas import messageAPICutRespUAM as UAM
from helpers.respuestas import messageAPICutRespTec as MAC
from helpers.respuestas import messageAPICutPoli as POL
from bson.objectid import ObjectId
from helpers.helper import createFile as cF
from fastapi import APIRouter
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor as Thpex
from config.db import conn


address = ''
nameF =  ''
correo = 'jaames11@hotmail.com'
pas ='Wellneverdie.201'
Token = 'daa39d53-6283-47a1-b945-b7ee6528dde0'

rep = APIRouter()

@rep.get('/')
def home():
    return 'This route from analize the docs with IA'

@rep.get('/givemeReport')
def giveRep(nameFile = 'Report', id = '6454a9508632c2da0a7420ea'):
    cF(nameFile)
    return 'Ok'
    # print(file)


@rep.get('/getReport')
def getReport(nameFile: str, addressee: str):
    global address, nameF
    address = addressee
    nameF = nameFile

    # cF(nameFile)
    executor = Thpex()
    executor.submit(messagealert)

    return 'Analizando, cuando el documento este listo será notificado directamente a su correo'

def messagealert():
    global address, nameF
    # time = ri(1500, 2400) # (24-40)min
    # scrapp = time*.05   # ApiScrapp
    # unam = scrapp *.03
    # uam = scrapp *.03
    # tec = scrapp *.03
    # ipn = scrapp *.01
    # cut = time*.10 # 15% Cortes -> APICutText,
    # toImg = time*.10 # 10% ImgtoText-> ApiImg,
    # para = time*.50 # 50% Texto -> ApiPara,
    # img = time*.20 # 20% Img -> Apimg,
    # cita = time*.05 # 4% Citas -> ApiCita,
    # rep = 1 # 1% Reporte -> ApiRep

    # while rep > 0:
    #     while scrapp > 0 :
    #         if (unam > 0):
    #             ping(Token, UNAM())
    #             unam -=1
    #         elif (uam > 0):
    #             ping(Token, UAM())
    #             uam -=1
    #         elif (tec > 0):
    #             ping(Token, MAC())
    #             tec -=1
    #         elif (ipn > 0):
    #             ping(Token, POL())
    #             ipn -=1
    #         else:
    #             scrapp = 0
    #     print(f'{cut} {toImg} {para} {img} {cita}')
    #     if (cut > 0):
    #         ping(Token, f'Fileteando docs')
    #         cut-=1
    #     elif (toImg > 0):
    #         ping(Token, f'Convirtiendo Imagenes')
    #         toImg-=1
    #     elif (para > 0):
    #         ping(Token, f'Analizando docs')
    #         para-=1
    #     elif (img > 0):
    #         ping(Token, f'Analizando imgs')
    #         img-=1
    #     elif (cita > 0):
    #         ping(Token, f'Analizando citas')
    #         cita-=1
    #     else:
    #         rep = 0
    
    server = smtplib.SMTP('smtp-mail.outlook.com', port = 587)
    server.starttls()
    server.login(correo, pas)
    message = email.mime.multipart.MIMEMultipart()
    message['From'] = correo
    message['To'] = address
    message['Subject'] = f"Resultados de plagio encontrados en {nameF}"
    body = mR()
    message.attach(email.mime.text.MIMEText(body, 'plain'))
    routeFile = f'./documents/{nameF}.pdf'
    file = open(routeFile, 'rb')
    adjunct = email.mime.base.MIMEBase('application', 'octet-stream')
    adjunct.set_payload(file.read())
    email.encoders.encode_base64(adjunct)
    adjunct.add_header('Content-Disposition', "attachment; filename= %s" % f'{nameF}.pdf')
    message.attach(adjunct)

    # routeFile1 = ''
    # if(nameF == "Propuesta de sistema para detectar originalidad en Tesis a matricular"):
    #     routeFile1 = f'./results/Athena/Resultados.txt'
    # elif(nameF == "Diseño Construcción Control y Operación de un Brazo Manipulador"):
    #     routeFile1 = f'./results/Brazo Robotico/Resultados.json'
    # elif(nameF == "Intelectuales, Exilio y Periodismo en cuba durante la Rev Mex"):
    #     routeFile1 = f'./results/Cubo/Resultados.json'
    # elif(nameF == "Sistema de Domótica Móvil SIDOM"):
    #     routeFile1 = f'./results/Domotica/Resultados.json'
    # file1 = open(routeFile1, 'rb')
    # adjunct1 = email.mime.base.MIMEBase('application', 'octet-stream')
    # adjunct1.set_payload(file1.read())
    # email.encoders.encode_base64(adjunct1)
    # adjunct1.add_header('Content-Disposition', "attachment; filename= %s" % f'{nameF}.txt')
    # message.attach(adjunct1)

    text = message.as_string()
    server.sendmail(correo, address, text)
    server.quit()
    ping(Token, f'Llamen a dios por otro cliente iluminado :v')