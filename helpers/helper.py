from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

#Para el tipo de letras
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

#Para la grafica
import matplotlib.pyplot as plt

#Para las img
from reportlab.lib.utils import ImageReader

def createText(c,w:float,h:float,den:int,x:int,y:int,tamLet:int,text:str):
    title=c.beginText((w/den)+x,h+y)
    title.setFont("FUTURAM",tamLet)
    title.textLine(text)
    return c.drawText(title)

def createImg(porPlag:list,section:str):
    docs=['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13','D14','D15','D16',]
    fig,ax=plt.subplots()
    #Etiqueta eje y
    ax.set_title('% Plagio')
    #Creamos la grafica de barras utilizando 'docs' como X y 'porPlag' como y
    plt.bar(docs,porPlag)
    plt.savefig(section)


def createFile(nameFile: str,):
    #Tamaño de la hoja
    w,h=A4
    print('here create file :v/')

    #Nombre del archivo
    c = canvas.Canvas(nameFile,pagesize=A4)

    #Tipo de letra
    pdfmetrics.registerFont(TTFont('FUTURAM','FUTURAM.ttf'))

    #Titulo
    createText(c,w,h,4,-5,-90,24,'Reporte de analisis de Tesis')

    #Dibujar una línea horizontal
    x=50
    y=h-100
    c.line(x,y,w-50,y)

        #Dibujar imagenes
    img_ipn=ImageReader("ipn.png")
    #Ancho y alto de la imagen
    img_wi, img_hi=img_ipn.getSize()
    c.drawImage(img_ipn,10,h-img_hi)
    img_upiita=ImageReader("upiita.png")
    #Ancho y alto de la imagen
    img_wu, img_hu=img_upiita.getSize()
    c.drawImage(img_upiita,10,730)
    img_atenea=ImageReader("atenea.png")
    #Ancho y alto de la imagen
    img_wu,img_ha=img_atenea.getSize()
    c.drawImage(img_atenea,w-img_ha,h-img_ha)

    #Dibujar línea Vertical
    c.line((w/2),400,(w/2),720)

    #Titulo lado Izquierdo
    createText(c,w,h,8,-5,-140,18,'Reporte de Texto')

    #Primer Subtitulo lado Izquierdo
    createText(c,w,h,14,-15,-170,14,'Introducción:')
    porPlag=[25,50,100,60,12,14,28,26,36,80,70,45,38,19,25,50]
    createImg(porPlag,'Introduccion')
    img_Intro=ImageReader("Introduccion.png")
    #Ancho y alto de la imagen
    img_wIn,img_hIn=img_Intro.getSize()
    c.drawImage(img_Intro,14,h-334,164,164)

    #Segundo Subtitulo lado Izquierdo
    createText(c,w,h,14,-15,-340,14,'Marco Teórico:')

    #Titulo lado Derecho
    createText(c,w,h,2,50,-120,18,'Reporte de Bibliografía')

    #Segunda Línea Horizontal
    c.line(x,350,w-50,350)

    #Titulo Inferior
    createText(c,w,h,3,20,-520,18,'Reporte de Imágenes')

    #Tercer Subtitulo lado Izquierdo
    createText(c,w,h,14,-15,-550,14,'Marco Teórico:')

    #Total
    createText(c,w,h,2,140,-820,16,'Total:')

    c.save()
    return 'ok'

createFile('Report.pdf')