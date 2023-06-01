from email.mime.text import MIMEText
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import email.mime.base
import email.mime.multipart
import os
import smtplib

#Tamaño de la hoja
W,H=A4

def createFile(nameFile = 'Pruebas' ):
    pdf = canvas.Canvas(f'./documents/{nameFile}.pdf',pagesize=A4)
    pdfmetrics.registerFont(TTFont('FUTURAM','./helpers/FUTURAM.ttf'))
    pdf.setFont("FUTURAM", 12)
    pdf.drawString(100, 200, "Ingrese un texto:")

    # Comienza el formulario
    pdf.acroForm.textfield(name='texto', x=200, y=200, width=200, height=20)
    
    # Agrega un campo de verificación para realizar la modificación
    pdf.acroForm.checkbox(
        name='modificar', x=200, y=160, buttonStyle='check',
        borderColor=None, fillColor=None,
        borderWidth=0, borderStyle=None,
        fieldFlags='radio'
    )

    pdf.save()

createFile()

def email():
    # Crea la conexión SMTP
    server = smtplib.SMTP('smtp-mail.outlook.com', port = 587)

    correo = 'jaames11@hotmail.com'
    pas ='Wellneverdie.201'
    # Inicia sesión en tu cuenta de Gmail
    server.starttls()

    server.login(correo, pas)

    # Definir el remitente y destinatario del correo electrónico
    remitente = 'jaames11@hotmail.com'
    # remitente = 'Cuando2son1@hotmail.com'
    destinatario = 'kenobsta@gmail.com'
    # destinatario = 'itzel.upiita@gmail.com'

    # Crear el mensaje del correo electrónico
    mensaje = email.mime.multipart.MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    # mensaje['Subject'] = "Correo electrónico con archivo adjunto"
    mensaje['Subject'] = "Correo electrónico de prueba"

    # Añadir el cuerpo del mensaje
    cuerpo = "Hola,\n\nEste es un mensaje de prueba enviado desde Python con un archivo adjunto.\n\nSaludos,\n ThunderGer"
    mensaje.attach(email.mime.text.MIMEText(cuerpo, 'plain'))

    # Añadir el archivo Excel como adjunto
    ruta_archivo = 'requirements.txt'
    archivo = open(ruta_archivo, 'rb')
    adjunto = email.mime.base.MIMEBase('application', 'octet-stream')
    adjunto.set_payload((archivo).read())
    email.encoders.encode_base64(adjunto)
    adjunto.add_header('Content-Disposition', "attachment; filename= %s" % ruta_archivo)
    mensaje.attach(adjunto)

    # Convertir el mensaje a texto plano
    texto = mensaje.as_string()

    # Enviar el correo electrónico
    server.sendmail(remitente, destinatario, texto)

    # Cerrar la conexión SMTP
    server.quit()