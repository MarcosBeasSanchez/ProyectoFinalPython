import os
import jinja2
import pdfkit

class Pdf():
    def __init__(self,nombreHtml,nombreCss,nombrePdf,info):
        self.nombreHtml=nombreHtml
        self.nombreCss=nombreCss
        self.nombrePdf=nombrePdf

        self.info=info

        self.rutaHtml=""
        self.rutaHtml=self.darLaRutaMenosLaUltima(self.rutaHtml)
        self.rutaHtml+=nombreHtml+".html"

        self.rutaCss=""
        self.rutaCss=self.darLaRutaMenosLaUltima(self.rutaCss)
        self.rutaCss+=nombreCss+".css"

        self.rutaPdf=""
        self.rutaPdf=self.darLaRutaMenosLaUltima(self.rutaPdf)
        self.rutaPdf+=nombrePdf+".pdf"
        self.rutaWkhtml="/usr/bin/wkhtmltopdf"
        self.options = {
            'page-size': 'letter',
            'margin-top': '0.05in',
            'margin-bottom': '0.05in',
            'margin-left': '0.05in',
            'margin-right': '0.05in',
            'encoding': 'UTF-8'
        }


    def darLaRutaMenosLaUltima(self,ruta):
        separador=[]
        separador=os.getcwd().split("/")
        for indice,r in enumerate(separador):
            if indice < separador.__len__():
                ruta+= separador[indice]+"/"
        return ruta


    def getRutaHtml(self):
       return self.rutaHtml
    def getRutaCss(self):
       return self.rutaCss
    def getRutaPdf(self):
       return self.rutaPdf
    def getRutaWkhtml(self):
        return self.rutaWkhtml
    def getInfo(self):
        return self.info

    def crear_pdf(self):
        nombre_index=self.rutaHtml.split("/")[-1]
        self.rutaHtml=self.rutaHtml.replace(nombre_index,"")

        env=jinja2.Environment(loader=jinja2.FileSystemLoader(self.rutaHtml))
        index=env.get_template(nombre_index)
        html=index.render(self.info)

        config=pdfkit.configuration(wkhtmltopdf=self.rutaWkhtml)

        pdfkit.from_string(html,self.rutaPdf,css=self.rutaCss,options=self.options,configuration=config)







