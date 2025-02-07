import tkinter as tk
from tkinter import PhotoImage
from colores import ColoresAplicacion
from text import Texto
class VentanaPrincipal(tk.Tk):
    def __init__(self, weight, height, x, y, title):
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
        self.Cajas()


    def cargarBBDD(self):
        print("hola")
    def cargarGrafica(self):
        print("hola")
    def mandarCorreo(self):
        print("hola")
    def mostrarCreditos(self):
        print("hola")   

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
        self.principal.pack(side=tk.TOP, expand=True, fill="both") 

        Texto(seccion=self.cabecera,texto="Titulo Provisional hasta que se nos ocurra un titulo mejor",fuente="Monserrat",tamanio=18,posicion="top",color="white",bold="bold")
       
        #self.logo = tk.PhotoImage(file='package/images.png')
        #tk.Label(self.izquierda, image=self.logo, bg=self.Color_izquierda).pack(side=tk.TOP, pady=10, padx=10)
  
        self.btnOpcion1 = tk.Button(self.pie)
        self.btnOpcion2 = tk.Button(self.pie)
        self.btnOpcion3 = tk.Button(self.pie)
        self.btnOpcion4 = tk.Button(self.pie)
       

        Buttons_Options = [
            ("BBDD", self.btnOpcion1, self.cargarBBDD,self.color.Color_Boton_Primario), 
            ("Gráfica", self.btnOpcion2, self.cargarGrafica,self.color.Color_Boton_Secundario),
            ("Correo", self.btnOpcion3, self.mandarCorreo,self.color.Color_Boton_Tercero),
            ("Creditos", self.btnOpcion4, self.mostrarCreditos,self.color.Color_Boton_Cuarto)
        ]
        for texto, boton, comando, color in Buttons_Options:
            self.configurar_boton_menu(boton, texto, comando,color)


    def configurar_boton_menu(self, boton, texto, comando,color):
        boton.config(text=f"{texto}",bg=color,font=("Montserrat",15,"bold"),fg="white", width=10, command=comando,activebackground="purple",  borderwidth=0, )
        boton.pack(side=tk.LEFT, padx=10, pady=5, expand=True, fill="both")
        

    def clear_frame(self):
        for widget in self.principal.winfo_children():
            widget.destroy()
