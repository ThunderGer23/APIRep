from reportlab.pdfgen import canvas

def createFile(nameFile: str):
    print('here create file :v/')

    c = canvas.Canvas(nameFile)
    c.drawString(50, 50, "¡Hola, mundo!")

    
    c.save()
    return 'ok'