import tkinter as tk
from colores import ColoresAplicacion
from text import Texto
from correo import Correo
from tkinter import messagebox
import mysql.connector
import threading
from PdfCreacion import Pdf
class VentanaPrincipal(tk.Tk):
    def __init__(self, weight, height, x, y, title,conn):
        super().__init__()
        self.weight = weight
        self.height = height
        self.x = x
        self.y = y
        self.miTitulo = title
        self.color=ColoresAplicacion()
        self.geometry("%dx%d+%d+%d" %(self.weight, self.height, self.x, self.y))
        self.title(self.miTitulo)
        self.resizable(False, False)
        self.conn=conn
        self.Cajas()


    def cargarBBDD(self):
        print("Cuando hagamos el merge lo junto")
    def cargarGrafica(self):
        print("Cuando hagamos el merge lo junto")
  
    def mandarCorreo(self):
        self.clear_frame()
        # Configuración de estilo
        # Estilos
        self.bg_color = "#F5F7FA"  # Fondo principal
        self.fg_color = "#37474F"  # Texto gris oscuro azulado
        self.entry_bg = "#FFFFFF"  # Entradas de texto blancas
        self.button_color = "#007BFF"  # Azul moderno
        self.button_PorEncima = "#0056b3"  # Azul oscuro
        self.font_style = ("Monserrat", 10)
        self.entry_width = 10
        self.pad_y = 10
        self.pad_x = 20
        
        
        # Crear campos
        self.origen = self.crear_label_entry("Origen")
        self.contrasenia = self.crear_label_entry("Contraseña", show="*")
        self.destinatario = self.crear_label_entry("Destinatario")
        self.asunto = self.crear_label_entry("Asunto","")
        self.contenido =self.crear_label_textarea("Contenido")
      
        self.boton_enviar = tk.Button(
            self.principal, text="Enviar Correo", font=self.font_style,
            bg=self.button_color, fg="white", activebackground=self.button_PorEncima, activeforeground="white",
            padx=10, pady=5, command=lambda:threading.Thread(target=self.enviar_info).start()        
            )
        self.boton_enviar.pack(side=tk.TOP, pady=self.pad_y * 2)   


    def crear_label_entry(self, texto, show=None):
            frame = tk.Frame(self.principal, bg=self.bg_color)
            frame.pack(side=tk.TOP, pady=self.pad_y, fill=tk.X)
            
            label = tk.Label(frame, text=texto, font=self.font_style, bg=self.bg_color, fg=self.button_color, anchor="w")
            label.pack(side=tk.TOP, fill=tk.X)
            
            entry = tk.Entry(frame, font=self.font_style, width=self.entry_width, bg= self.entry_bg, fg=self.fg_color, show=show)
            entry.pack(side=tk.TOP, fill=tk.X, pady=(2, 0))
            return entry
    
    def crear_label_textarea(self, texto=""):
            frame =tk.Frame(self.principal, bg=self.bg_color)
            frame.pack(side=tk.TOP, pady=self.pad_y, fill=tk.X)
            
            label = tk.Label(frame, text=texto, font=self.font_style, bg=self.bg_color, fg=self.button_color, anchor="w")
            label.pack(side=tk.TOP, fill=tk.X)
            
            textarea = tk.Text(frame, font=self.font_style, width=self.entry_width, height=5, bg=self.entry_bg, fg=self.fg_color)
            textarea.pack(side=tk.TOP, fill=tk.X, pady=(2, 0))
            return textarea
    

    def enviar_info(self):
                Correo.enviar(
                    asunto=self.asunto.get(),
                    contenido=self.contenido.get("1.0","end"),
                    origen=self.origen.get(),
                    password=self.contrasenia.get(),
                    destino=self.destinatario.get(),
                )  
                print("Correo enviado....")

    def mostrarCreditos(self):
        self.clear_frame()
        
        self.bg_color = "#F5F7FA"  
        self.fg_color = "#37474F" 
        self.button_color = "#007BFF" 
        self.button_PorEncima = "#0056b3"  
        self.font_style = ("Monserrat", 15)
        self.entry_width = 15
        self.pad_y = 10
        self.pad_x = 20
        Texto(self.principal,"Hecho por: Álvaro,Marcos Beas,Diego","Monserrat",20,"top","#007BFF","bold") 
        def enviar_clientes():
            try:
                self.conn = mysql.connector.connect(user="root", password="1234", host="localhost", database="proyectofn")
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM CLIENTES")
                datos=cursor.fetchall()
                info = {
                    'registros': datos
                 }
                generador=Pdf(info=info,nombreHtml="indexsecundario",nombreCss="indexsecundario",nombrePdf="clientes")
                generador.crear_pdf()
                self.conn.commit()
                self.conn.close()
                cursor.close()
                print("Creado el PDF....")  
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo obtener los registros: {e}")
        self.boton_clientes = tk.Button(
            self.principal, text="Generar Clientes", font=self.font_style,
            bg=self.button_color, fg="white", activebackground=self.button_PorEncima, activeforeground="white",
            padx=10, pady=5, command=lambda:threading.Thread(target=enviar_clientes).start()
        )
        self.boton_clientes.pack(side=tk.TOP, pady=self.pad_y * 2)


        def enviar_empleados():
            try:
                self.conn = mysql.connector.connect(user="root", password="1234", host="localhost", database="proyectofn")
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM EMPLEADOS")
                datos=cursor.fetchall()
                info = {
                    'registros': datos
                 }
                generador=Pdf(info=info,nombreHtml="indexprimario",nombreCss="indexprimario",nombrePdf="empleados")
                generador.crear_pdf()
                self.conn.commit()
                self.conn.close()
                cursor.close()
                print("Creado el PDF....")    
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo obtener los registros: {e}")



        self.boton_empleados = tk.Button(
            self.principal, text="Generar Empleados", font=self.font_style,
            bg=self.button_color, fg="white", activebackground=self.button_PorEncima, activeforeground="white",
            padx=10, pady=5, command=lambda:threading.Thread(target=enviar_empleados).start()   
        )
        self.boton_empleados.pack(side=tk.TOP, pady=self.pad_y * 2)
    
       

    def Cajas(self):
        borde_color = self.color.Color_Cabecera_Principal 
        borde_grosor = 1
        #Cabecera
        self.cabecera = tk.Frame(
            self,
            bg=self.color.get_Color_Cabecera_Principal(),
            height=70,
            highlightbackground=borde_color,
            highlightcolor=borde_color,
            highlightthickness=borde_grosor,
            bd=3,
            relief="ridge"
        )
        self.cabecera.pack(side=tk.TOP, fill="both") 

        # Pie de página
        self.pie = tk.Frame(
            self,
            bg=self.color.get_Color_Pie_Pagina(),
            height=60,
            highlightbackground=borde_color,
            highlightcolor=borde_color,
            highlightthickness=borde_grosor,
            bd=3,
            relief="ridge"
        )
        self.pie.pack(side=tk.BOTTOM,fill="x") 

        # Panel izquierdo
        self.izquierda = tk.Frame(
            self,
            bg=self.color.get_Color_Laterales(),
            width=120,
            highlightbackground=borde_color,
            highlightcolor=borde_color,
            highlightthickness=borde_grosor,
            bd=3,
            relief="ridge"
        )
        self.izquierda.pack(side=tk.LEFT, fill="y")  # Se expande solo verticalmente

        # Panel derecho
        self.derecha = tk.Frame(
            self,
            bg=self.color.get_Color_Laterales(),
            width=120,
            highlightbackground=borde_color,
            highlightcolor=borde_color,
            highlightthickness=borde_grosor,
            bd=3,
            relief="ridge"
        )
        self.derecha.pack(side=tk.RIGHT, fill="y")  # Se expande solo verticalmente

        # Área principal
        self.principal = tk.Frame(
            self,
            bg=self.color.get_Color_Principal(),
            width=300,
            height=200,
            highlightbackground=borde_color,
            highlightcolor=borde_color,
            highlightthickness=borde_grosor,
            bd=3,
            relief="ridge"
        )
        self.principal.pack( expand=True, fill="both") 

        Texto(seccion=self.cabecera,texto="Titulo Provisional hasta que se nos ocurra un titulo mejor",fuente="Monserrat",tamanio=18,posicion="top",color="white",bold="bold")
  
        self.btnOpcion1 = tk.Button(self.pie)
        self.btnOpcion2 = tk.Button(self.pie)
        self.btnOpcion3 = tk.Button(self.pie)
        self.btnOpcion4 = tk.Button(self.pie)
       

        Buttons_Options = [
            ("BBDD", self.btnOpcion1, self.cargarBBDD,self.color.Color_Boton_Primario), 
            ("Gráfica", self.btnOpcion2, self.cargarGrafica,self.color.Color_Boton_Secundario),
            ("Correo", self.btnOpcion3, self.mandarCorreo,self.color.Color_Boton_Tercero),
            ("Creditos Y PDF", self.btnOpcion4, self.mostrarCreditos,self.color.Color_Boton_Cuarto)
        ]
        for texto, boton, comando, color in Buttons_Options:
            self.configurar_boton_menu(boton, texto, comando,color)


    def configurar_boton_menu(self, boton, texto, comando,color):
        boton.config(text=f"{texto}",bg=color,font=("Montserrat",15,"bold"),fg="white", width=10, command=comando,activebackground="purple",  borderwidth=0 )
        boton.pack(side=tk.LEFT, padx=10, pady=5, expand=True, fill="both")
        
    
    def clear_frame(self):
        for widget in self.principal.winfo_children():
            widget.destroy()
