from fastapi import APIRouter
import smtplib
import email.mime.multipart
import email.mime.base
import os
from email.mime.text import MIMEText
from helpers.helper import createFile as cF
from helpers.respuestas import messageResp as mR

rep = APIRouter()

pas ='Wellneverdie.201'
email = 'jaames11@hotmail.com'
addressee = 'kenobsta@gmail.com'
server = smtplib.SMTP('smtp-mail.outlook.com', port = 587)
server.starttls()
server.login(email, pas)

@rep.get('/')
def home():
    return 'This route from analize the docs with IA'

@rep.get('/getReport')
def getReport(nameFile: str):
    message = email.mime.multipart.MIMEMultipart()
    message['From'] = email
    message['To'] = addressee
    message['Subject'] = f"Resultados de plagio encontrados en {nameFile}"
    body = mR()
    message.attach(email.mime.text.MIMEText(body, 'plain'))

    routeFile = f'/documents/{nameFile}'
    cF(nameFile)
    
    file = open(routeFile, 'rb')
    adjunct = email.mime.base.MIMEBase('application', 'octet-stream')
    adjunct.set_payload(file.read())
    email.encoders.encode_base64(adjunct)
    adjunct.add_header('Content-Disposition', "attachment; filename= %s" % routeFile)
    message.attach(adjunct)
    text = message.as_string()
    server.sendmail(email, addressee, text)
    server.quit()