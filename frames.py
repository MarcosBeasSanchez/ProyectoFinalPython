import tkinter as tk
from colores import ColoresAplicacion
from text import Texto
from correo import Correo
from tkinter import ttk, messagebox
import mysql.connector
from PdfCreacion import Pdf
#from GeneradorGrafica import GeneradorGrafico 


class VentanaPrincipal(tk.Tk):
    def __init__(self, weight, height, x, y, title, id):
        super().__init__()
        self.weight = weight
        self.height = height
        self.x = x
        self.y = y
        self.miTitulo = title
        self.id = id
        self.color=ColoresAplicacion()
        self.geometry("%dx%d+%d+%d" %(self.weight, self.height, self.x, self.y))
        self.title(self.miTitulo)
        self.resizable(False, False)
        self.Cajas()


    def cargarBBDD(self):
        
        self.clear_frame()  

        tk.Label(self.principal, text="Seleccione tipo de registro:", font=("Arial", 14)).pack(pady=10)

        tipo_seleccionado = tk.StringVar()
        tipo_combo = ttk.Combobox(self.principal, textvariable=tipo_seleccionado, values=["Empleado", "Cliente"])
        tipo_combo.pack(pady=5)
        """"Si luego en un futuro quieres mas lo cambias a switch"""
        def abrir_formulario():
            tipo = tipo_seleccionado.get()
            if tipo == "Empleado":
                self.formulario_empleado()
            elif tipo == "Cliente":
                self.formulario_cliente()
            else:
                messagebox.showwarning("Selección requerida", "Seleccione una opción válida")

        tk.Button(self.principal, text="Continuar", command=abrir_formulario).pack(pady=10)

    def formulario_empleado(self):
        """Carga el formulario de empleados en la sección principal."""
        self.clear_frame() 

        tk.Label(self.principal, text="Agregar Empleado", font=("Arial", 16, "bold")).pack(pady=10)

        labels = ["ID", "Nombre", "Apellidos", "DNI", "Teléfono", "Fecha Contratación", "Sueldo", "Comisión"]
        entries = {}

        #Un for de label, donde coges una lista con la info y la vas escribiendo una por una para guardar el resultado en otra lista
        for label in labels:
            frame = tk.Frame(self.principal)
            frame.pack(pady=5)
            tk.Label(frame, text=label, width=20, anchor="w").pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.RIGHT, padx=10)
            entries[label] = entry

        def guardar_empleado():
            datos = [entries[label].get() for label in labels]
            try:
                conn = mysql.connector.connect(user="root", password="1234", host="localhost", database="proyectofn")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO EMPLEADOS VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", datos)
                conn.commit()
                conn.close()
                messagebox.showinfo("Éxito", "Empleado agregado correctamente")
                self.clear_frame()  
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar: {e}")

        tk.Button(self.principal, text="Guardar", command=guardar_empleado).pack(pady=10)

    def formulario_cliente(self):
        """Carga el formulario de clientes en la sección principal."""
        self.clear_frame()  

        tk.Label(self.principal, text="Agregar Cliente", font=("Arial", 16, "bold")).pack(pady=10)

        labels = ["ID", "NIF", "Nombre", "Apellidos", "Email", "Teléfono", "Cartera"]
        entries = {}

        for label in labels:
            frame = tk.Frame(self.principal)
            frame.pack(pady=5)
            tk.Label(frame, text=label, width=20, anchor="w").pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.RIGHT, padx=10)
            entries[label] = entry

        def guardar_cliente():
            datos = [entries[label].get() for label in labels]
            try:
                
                conn = mysql.connector.connect(user="root", password="1234", host="localhost", database="proyectofn")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO CLIENTES VALUES (%s, %s, %s, %s, %s, %s, %s)", datos)
                conn.commit()
                conn.close()
                messagebox.showinfo("Éxito", "Cliente agregado correctamente")
                self.clear_frame() 
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar: {e}")

        tk.Button(self.principal, text="Guardar", command=guardar_cliente).pack(pady=10)

    def cargarGrafica(self):
        self.clear_frame()

    def mandarCorreo(self):
        self.clear_frame()

        # Configuración de estilos
        self.bg_color = "#F5F7FA"  
        self.fg_color = "#37474F"  
        self.entry_bg = "#FFFFFF"  
        self.button_color = "#007BFF"  
        self.button_PorEncima = "#0056b3"  
        self.font_style = ("Monserrat", 10)  
        self.entry_width = 10  
        self.pad_y = 8  
        self.pad_x = 16

        # Obtener el correo del jefe desde la base de datos
        try:
            conn = mysql.connector.connect(user="root", password="1234", host="localhost", database="proyectofn")
            cursor = conn.cursor()
            cursor.execute("SELECT Correo FROM JEFES WHERE ID = %s", (self.id,))
            resultado = cursor.fetchone()
            correo_jefe = resultado[0] if resultado else ""
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener el correo del jefe: {e}")
            correo_jefe = ""

        # Crear campos con el correo cargado automáticamente
        self.origen = self.crear_label_entry("Origen", default_text=correo_jefe)
        self.contrasenia = self.crear_label_entry("Contraseña", show="*")
        self.destinatario = self.crear_label_entry("Destinatario")
        self.asunto = self.crear_label_entry("Asunto")
        self.contenido = self.crear_label_textarea("Contenido")

        self.boton_enviar = tk.Button(
        self.principal, text="Enviar Correo", font=self.font_style,
        bg=self.button_color, fg="white", activebackground=self.button_PorEncima, activeforeground="white",
        padx=10, pady=5, command=self.enviar_info
        )
        self.boton_enviar.pack(side=tk.TOP, pady=self.pad_y * 2)


    def crear_label_entry(self, texto, show=None, default_text=""):
        frame = tk.Frame(self.principal, bg=self.bg_color)
        frame.pack(side=tk.TOP, pady=self.pad_y, fill=tk.X)

        label = tk.Label(frame, text=texto, font=self.font_style, bg=self.bg_color, fg=self.button_color, anchor="w")
        label.pack(side=tk.TOP, fill=tk.X)

        entry = tk.Entry(frame, font=self.font_style, width=self.entry_width, bg=self.entry_bg, fg=self.fg_color, show=show)
    
        if default_text:  # Si hay un texto por defecto, se inserta en el campo
            entry.insert(0, default_text)

        entry.pack(side=tk.TOP, fill=tk.X, pady=(1, 0))
        return entry

    def crear_label_textarea(self, texto=""):
            frame =tk.Frame(self.principal, bg=self.bg_color)
            frame.pack(side=tk.TOP, pady=self.pad_y, fill=tk.X)
            
            label = tk.Label(frame, text=texto, font=self.font_style, bg=self.bg_color, fg=self.button_color, anchor="w")
            label.pack(side=tk.TOP, fill=tk.X)
            
            textarea = tk.Text(frame, font=self.font_style, width=self.entry_width, height=5, bg=self.entry_bg, fg=self.fg_color)
            textarea.pack(side=tk.TOP, fill=tk.X, pady=(1, 0))
            return textarea
    

    def enviar_info(self):
                Correo.enviar(
                    asunto=self.asunto.get(),
                    contenido=self.contenido.get("1.0","end"),
                    origen=self.origen.get(),
                    password=self.contrasenia.get(),
                    destino=self.destinatario.get(),
                )  

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
                conn = mysql.connector.connect(user="root", password="1234", host="localhost", database="proyectofn")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM CLIENTES")
                datos=cursor.fetchall()
                info = {
                    'registros': datos
                 }
                generador=Pdf(info=info,nombreHtml="indexsecundario",nombreCss="indexsecundario",nombrePdf="clientes")
                generador.crear_pdf()
                conn.commit()
                conn.close()
                cursor.close()
                self.clear_frame()  
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo obtener los registros: {e}")
        self.boton_clientes = tk.Button(
            self.principal, text="Generar Clientes", font=self.font_style,
            bg=self.button_color, fg="white", activebackground=self.button_PorEncima, activeforeground="white",
            padx=10, pady=5, command=enviar_clientes
        )
        self.boton_clientes.pack(side=tk.TOP, pady=self.pad_y * 2)


        def enviar_empleados():
            try:
                conn = mysql.connector.connect(user="root", password="1234", host="localhost", database="proyectofn")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM EMPLEADOS")
                datos=cursor.fetchall()
                info = {
                    'registros': datos
                 }
                generador=Pdf(info=info,nombreHtml="indexprimario",nombreCss="indexprimario",nombrePdf="empleados")
                generador.crear_pdf()
                conn.commit()
                conn.close()
                cursor.close()
                self.clear_frame()  
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo obtener los registros: {e}")



        self.boton_empleados = tk.Button(
            self.principal, text="Generar Empleados", font=self.font_style,
            bg=self.button_color, fg="white", activebackground=self.button_PorEncima, activeforeground="white",
            padx=10, pady=5, command=enviar_empleados
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
       
        #Botones para las funciones
        Buttons_Options = [
            ("BBDD", self.btnOpcion1, self.cargarBBDD,self.color.Color_Boton_Primario), #Para crear empleado o cliente
            ("Gráfica", self.btnOpcion2, self.cargarGrafica,self.color.Color_Boton_Secundario), #Ver la grafica
            ("Correo", self.btnOpcion3, self.mandarCorreo,self.color.Color_Boton_Tercero), # Enviar Correo
            ("Creditos Y PDF", self.btnOpcion4, self.mostrarCreditos,self.color.Color_Boton_Cuarto) #Creacion del Pdf
        ]
        for texto, boton, comando, color in Buttons_Options:
            self.configurar_boton_menu(boton, texto, comando,color)


    def configurar_boton_menu(self, boton, texto, comando,color):
        boton.config(text=f"{texto}",bg=color,font=("Montserrat",15,"bold"),fg="white", width=10, command=comando,activebackground="purple",  borderwidth=0 )
        boton.pack(side=tk.LEFT, padx=10, pady=5, expand=True, fill="both")
        
    #Funcion para limpiar el frame del medio
    def clear_frame(self):
        for widget in self.principal.winfo_children():
            widget.destroy()