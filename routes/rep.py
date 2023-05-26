from fastapi import APIRouter
from helpers.helper import createFile as cF
from helpers.process import messagealert as messAl
from concurrent.futures import ThreadPoolExecutor as Thpex

import email.mime.multipart
import email.mime.base
from email.mime.text import MIMEText
from notigram import ping
from helpers.respuestas import messageResp as mR
import smtplib

# addressee = 'Cuando2son1@hotmail.com'
correo = 'jaames11@hotmail.com'
pas ='Wellneverdie.201'
Token = 'daa39d53-6283-47a1-b945-b7ee6528dde0'

rep = APIRouter()

@rep.get('/')
def home():
    return 'This route from analize the docs with IA'

@rep.get('/getReport')
def getReport(nameFile: str, addressee: str):

    cF(nameFile)
    executor = Thpex()
    executor.submit(messAl)
    
    server = smtplib.SMTP('smtp-mail.outlook.com', port = 587)
    server.starttls()
    server.login(correo, pas)
    message = email.mime.multipart.MIMEMultipart()
    message['From'] = correo
    message['To'] = addressee
    message['Subject'] = f"Resultados de plagio encontrados en {nameFile}"
    body = mR()
    message.attach(email.mime.text.MIMEText(body, 'plain'))
    routeFile = f'./documents/{nameFile}.pdf'
    file = open(routeFile, 'rb')
    adjunct = email.mime.base.MIMEBase('application', 'octet-stream')
    adjunct.set_payload(file.read())
    email.encoders.encode_base64(adjunct)
    adjunct.add_header('Content-Disposition', "attachment; filename= %s" % f'{nameFile}.pdf')
    message.attach(adjunct)

    text = message.as_string()
    server.sendmail(correo, addressee, text)
    server.quit()
    ping(Token, f'Llamen a dios por otro cliente iluminado :v')

    return 'Analizando, cuando el documento este listo será notificado directamente a su correo'