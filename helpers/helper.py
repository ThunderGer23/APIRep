from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

#Para el tipo de letras
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

#Para las img
from reportlab.lib.utils import ImageReader

def createText(c,w:float,h:float,den:int,x:int,y:int,tamLet:int,text:str):
    title=c.beginText((w/den)+x,h+y)
    title.setFont("FUTURAM",tamLet)
    title.textLine(text)
    return c.drawText(title)


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
    #title=c.beginText((w/4)-5,h-90)
    #title.setFont("FUTURAM",24)
    #title.textLine("Reporte de analisis de Tesis")
    #c.drawText(title)

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
    #title_left=c.beginText((w/8)-5,h-140)
    #title_left.setFont("FUTURAM",18)
    #title_left.textLine("Reporte de Texto")
    #c.drawText(title_left)

    #Primer Subtitulo lado Izquierdo
    createText(c,w,h,14,-15,-170,14,'Introducción:')
    #title_left1=c.beginText((w/14)-15,h-170)
    #title_left1.setFont("FUTURAM",14)
    #title_left1.textLine("Introducción:")
    #c.drawText(title_left1)

    #Segundo Subtitulo lado Izquierdo
    createText(c,w,h,14,-15,-300,14,'Marco Teórico:')
    #title_left2=c.beginText((w/14)-15,h-300)
    #title_left2.setFont("FUTURAM",14)
    #title_left2.textLine("Marco Teórico:")
    #c.drawText(title_left2)

    #Titulo lado Derecho
    createText(c,w,h,2,50,-140,18,'Reporte de Bibliografía')
    #title_right=c.beginText((w/2)+50,h-140)
    #title_right.setFont("FUTURAM",18)
    #title_right.textLine("Reporte de Bibliografía")
    #c.drawText(title_right)

    #Segunda Línea Horizontal
    c.line(x,350,w-50,350)

    #Titulo Inferior
    createText(c,w,h,3,20,-520,18,'Reporte de Imágenes')
    #title_right=c.beginText((w/3)+20,h-520)
    #title_right.setFont("FUTURAM",18)
    #title_right.textLine("Reporte de Imágenes")
    #c.drawText(title_right)

    #Tercer Subtitulo lado Izquierdo
    createText(c,w,h,14,-15,-550,14,'Marco Teórico:')
    #title_left2=c.beginText((w/14)-15,h-550)
    #title_left2.setFont("FUTURAM",14)
    #title_left2.textLine("Marco Teórico:")
    #c.drawText(title_left2)

    #Total
    createText(c,w,h,2,140,-820,16,'Total:')
    #title_right=c.beginText((w/2)+140,h-820)
    #title_right.setFont("FUTURAM",16)
    #title_right.textLine("Total:")
    #c.drawText(title_right)

    c.save()
    return 'ok'

createFile('Report.pdf')