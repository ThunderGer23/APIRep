import smtplib
import email.mime.multipart
import email.mime.base
import os
from email.mime.text import MIMEText
from reportlab.pdfgen import canvas

def createFile():
    c = canvas.Canvas("hola-mundo.pdf")
    c.drawString(50, 50, "¡Hola, mundo!")
    

    c.save()

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