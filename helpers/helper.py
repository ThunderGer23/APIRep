from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import matplotlib.pyplot as plt
from reportlab.lib.utils import ImageReader
from results.Athenea.Resultados import ResAt
from results.BrazoRobotico.Resultados import ResBr
from results.Cubo.Resultados import ResCu
from results.Domotica.Resultados import ResDom

#Tamaño de la hoja
W,H=A4

def dibImagen(name:str, c, x:int, y:int, px:int, py:int):
    img=ImageReader(name)
    img_w,img_h=img.getSize()
    if y!=0 and px==0 and py==0:
        return c.drawImage(img,x,y)
    elif x==0 and y==0 and px==0 and py==0:
        return c.drawImage(img,W-img_h,H-img_h)
    elif px == 0 and py==0:
        return c.drawImage(img,x,H-img_h)
    else:
        return c.drawImage(img,x,H+y,px,py)


def createText(c,den:int,x:int,y:int,tamLet:int,text:str):
    title=c.beginText((W/den)+x,H+y)
    title.setFont("FUTURAM",tamLet)
    title.textLine(text)
    return c.drawText(title)

def createFile(nameFile: str):
    c = canvas.Canvas(f'./documents/{nameFile}.pdf',pagesize=A4)
    pdfmetrics.registerFont(TTFont('FUTURAM','./helpers/FUTURAM.ttf'))
    createText(c,4,-5,-90,24,'Reporte de analisis de Tesis')

    x=50
    y=H-100
    c.line(x,y,W-50,y)

    dibImagen('./helpers/ipn.png',c,10,0,0,0)
    dibImagen('./helpers/upiita.png',c,10,730,0,0)
    dibImagen('./helpers/atenea.png',c,0,0,0,0)

    c.line((W/2),400,(W/2),720)

    #Titulo lado Izquierdo
    createText(c,8,-5,-140,18,'Reporte de Texto')
    Res = {}
    if(nameFile == "Athenea"):
        Res = ResAt
    elif(nameFile == "Diseño Construcción Control y Operación de un Brazo Manipulador"):
        Res = ResBr
    elif(nameFile == "Cubo"):
        Res = ResCu
    elif(nameFile == "Sistema de Domótica Móvil SIDOM"):
        Res = ResDom

    Sec= list(Res['resultados'].keys())
    yFile = -170
    for i in Sec:
        if(type(Res['resultados'][i]) == dict):
            if(Res['resultados'][i]['Nivel'] != "Sin equivalencia"):
                createText(c,14,-15,yFile,14,i)
                createText(c,14,-15,yFile-30,14,Res['resultados'][i]['Similitud'][:30])
                createText(c,14,-15,yFile-45,14,Res['resultados'][i]['Similitud'][30:60])
                createText(c,14,-15,yFile-60,14,Res['resultados'][i]['Similitud'][60:90])
                createText(c,14,-15,yFile-75,14,Res['resultados'][i]['Nivel'][2:4]+"%")
                yFile-=100
    yFile = -170
    for i in Sec:
        if(type(Res['resultados'][i]) != dict):
            createText(c,2,50,-140,18,'Reporte de Bibliografía')
            for j in Res['resultados'][i]:
                createText(c,2,50,yFile,18,j)
                yFile-=15
                if(yFile <= -470):
                    createText(c,2,50,yFile,18,"Para mayor información")
                    createText(c,2,50,yFile-15,18,"revisa el archivo JSON")
                    createText(c,2,50,yFile-30,18,"que hemos anexado")
                    break

    #Segunda Línea Horizontal
    c.line(x,yFile*-1-150,W-50,yFile*-1-150)

    #Total
    createText(c,2,140,yFile-200,16,'Total:')

    c.save()
    return 'ok'

# createFile('Domotica')