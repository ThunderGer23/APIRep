from fastapi import APIRouter
import os
from email.mime.text import MIMEText
from helpers.helper import createFile as cF
from helpers.respuestas import messageResp as mR
from helpers.process import messagealert as messAl
from concurrent.futures import ThreadPoolExecutor as Thpex

rep = APIRouter()

@rep.get('/')
def home():
    return 'This route from analize the docs with IA'

@rep.get('/getReport')
def getReport(nameFile: str, addressee: str):

    cF(nameFile)
    executor = Thpex()
    executor.submit(messAl(nameFile, addressee))
    return 'Analizando, cuando el documento este listo será notificado directamente a su correo'