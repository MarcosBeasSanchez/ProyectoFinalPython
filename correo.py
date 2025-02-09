import smtplib
from email.message import EmailMessage

class Correo():
    @staticmethod
    def enviar(origen, password, destino, asunto, contenido, archivos=[]):
        try:
            mensaje = EmailMessage()
            mensaje['Subject'] = asunto
            mensaje['From'] = origen
            mensaje['To'] = destino
            mensaje.set_content(contenido)

            for archivo in archivos:
                with open(archivo, 'rb') as adjunto:
                    mensaje.add_attachment(adjunto.read(), maintype='application', filename=archivo)

            with smtplib.SMTP('smtp01.educa.madrid.org', 587) as server:
                server.starttls()
                server.login(origen, password)
                server.send_message(mensaje)

            print("Correo enviado correctamente.")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
