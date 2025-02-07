import tkinter as tk
from tkinter import ttk, messagebox
#import mysql.connector
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
        self.color = ColoresAplicacion()
        self.geometry(f"{self.weight}x{self.height}+{self.x}+{self.y}")
        self.title(self.miTitulo)
        self.resizable(False, False)
        self.Cajas()

    def clear_frame(self):
        """Limpia el contenido de la sección principal."""
        for widget in self.principal.winfo_children():
            widget.destroy()

    def cargarBBDD(self):
        """Abre el formulario en el área principal en lugar de una ventana emergente."""
        self.clear_frame()  # Limpiar el área central antes de agregar un nuevo formulario

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
               
                #conn = mysql.connector.connect(user="root", password="1234", host="localhost", database="proyectofn")
                #cursor = conn.cursor()
                #cursor.execute("INSERT INTO EMPLEADOS VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", datos)
                #conn.commit()
                #conn.close()
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
                
                #conn = mysql.connector.connect(user="root", password="1234", host="localhost", database="proyectofn")
                #cursor = conn.cursor()
                #cursor.execute("INSERT INTO CLIENTES VALUES (%s, %s, %s, %s, %s, %s, %s)", datos)
                #conn.commit()
                #conn.close()
                messagebox.showinfo("Éxito", "Cliente agregado correctamente")
                self.clear_frame() 
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar: {e}")

        tk.Button(self.principal, text="Guardar", command=guardar_cliente).pack(pady=10)

    def Cajas(self):
        borde_color = self.color.Color_Cabecera_Principal
        borde_grosor = 1

        self.cabecera = tk.Frame(self, bg=self.color.get_Color_Cabecera_Principal(), height=70,
                                 highlightbackground=borde_color, highlightcolor=borde_color,
                                 highlightthickness=borde_grosor, bd=3, relief="ridge")
        self.cabecera.pack(side=tk.TOP, fill="both")

        self.pie = tk.Frame(self, bg=self.color.get_Color_Pie_Pagina(), height=60,
                            highlightbackground=borde_color, highlightcolor=borde_color,
                            highlightthickness=borde_grosor, bd=3, relief="ridge")
        self.pie.pack(side=tk.BOTTOM, fill="x")

        self.izquierda = tk.Frame(self, bg=self.color.get_Color_Laterales(), width=120,
                                  highlightbackground=borde_color, highlightcolor=borde_color,
                                  highlightthickness=borde_grosor, bd=3, relief="ridge")
        self.izquierda.pack(side=tk.LEFT, fill="y")

        self.derecha = tk.Frame(self, bg=self.color.get_Color_Laterales(), width=120,
                                highlightbackground=borde_color, highlightcolor=borde_color,
                                highlightthickness=borde_grosor, bd=3, relief="ridge")
        self.derecha.pack(side=tk.RIGHT, fill="y")

        self.principal = tk.Frame(self, bg=self.color.get_Color_Principal(), width=300, height=200,
                                  highlightbackground=borde_color, highlightcolor=borde_color,
                                  highlightthickness=borde_grosor, bd=3, relief="ridge")
        self.principal.pack(side=tk.TOP, expand=True, fill="both")

        Texto(seccion=self.cabecera, texto="Aplicacion principla Jefe ||| DAM",
              fuente="Monserrat", tamanio=18, posicion="top", color="white", bold="bold")


        # Botones del menú inferior
        botones = [
            ("BBDD", self.cargarBBDD, self.color.Color_Boton_Primario),
            ("Gráfica", self.cargarGrafica, self.color.Color_Boton_Secundario),
            ("Correo", self.mandarCorreo, self.color.Color_Boton_Tercero),
            ("Créditos", self.mostrarCreditos, self.color.Color_Boton_Cuarto)
        ]

        for texto, comando, color in botones:
            btn = tk.Button(self.pie, text=texto, bg=color, font=("Montserrat", 15, "bold"), fg="white", width=10, command=comando)
            btn.pack(side=tk.LEFT, padx=10, pady=5, expand=True, fill="both")

    def cargarGrafica(self):
        self.clear_frame()
        tk.Label(self.principal, text="Aquí irá la gráfica", font=("Arial", 16)).pack(pady=20)

    def mandarCorreo(self):
        self.clear_frame()
        tk.Label(self.principal, text="Formulario de Correo en construcción", font=("Arial", 16)).pack(pady=20)

    def mostrarCreditos(self):
        self.clear_frame()
        tk.Label(self.principal, text="Créditos del Proyecto", font=("Arial", 16)).pack(pady=20)

if __name__ == "__main__":
    root = VentanaPrincipal(1000, 800, 700, 700, "Proyecto Final SGE 2ºDAM")
    root.mainloop()
