from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import matplotlib.pyplot as plt
from reportlab.lib.utils import ImageReader

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

def createImg(porPlag:list,section:str):
    docs=['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13','D14','D15','D16',]
    fig,ax=plt.subplots()
    ax.set_title('% Plagio')
    plt.bar(docs,porPlag)
    plt.savefig(section)


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

    #Primer Subtitulo lado Izquierdo
    createText(c,14,-15,-170,14,'Introducción:')
    porPlag=[25,50,100,60,12,14,28,26,36,80,70,45,38,19,25,50]
    createImg(porPlag,'Introduccion')
    dibImagen('Introduccion.png',c,14,-334,164,164)

    #Segundo Subtitulo lado Izquierdo
    createText(c,14,-15,-340,14,'Marco Teórico:')

    #Titulo lado Derecho
    createText(c,2,50,-140,18,'Reporte de Bibliografía')

    #Segunda Línea Horizontal
    c.line(x,350,W-50,350)

    #Titulo Inferior
    createText(c,3,20,-520,18,'Reporte de Imágenes')

    #Tercer Subtitulo lado Izquierdo
    createText(c,14,-15,-550,14,'Marco Teórico:')

    #Total
    createText(c,2,140,-820,16,'Total:')

    c.save()
    return 'ok'

# createFile('Report.pdf')