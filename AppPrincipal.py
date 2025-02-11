import tkinter as tk
from tkinter import messagebox
import mysql.connector
from frames import VentanaPrincipal


def crear_base_de_datos():
    """Crea la base de datos, las tablas y un jefe predeterminado si no existen."""
    try:
        conn = mysql.connector.connect(user="root", password="1234", host="localhost")
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS proyectofn")
        conn.close()

        conn = mysql.connector.connect(user="root", password="1234", host="localhost", database="proyectofn")
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS JEFES;")
        cursor.execute("DROP TABLE IF EXISTS EMPLEADOS;")
        cursor.execute("DROP TABLE IF EXISTS CLIENTES;")

        # Crear tabla JEFES
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS JEFES (
                ID INT PRIMARY KEY AUTO_INCREMENT,
                Nombre VARCHAR(50),
                Apellido VARCHAR(50),
                DNI VARCHAR(10) UNIQUE NOT NULL,
                Correo VARCHAR(50)
            )
        """)

        # Crear tabla EMPLEADOS
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS EMPLEADOS (
                ID INT PRIMARY KEY AUTO_INCREMENT,
                Nombre VARCHAR(50),
                Apellidos VARCHAR(50),
                DNI VARCHAR(10) UNIQUE NOT NULL,
                Telefono VARCHAR(15),
                Fecha_Contratacion DATE,
                Sueldo DECIMAL(10,2),
                Comision DECIMAL(10,2)
            )
        """)

        # Crear tabla CLIENTES
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS CLIENTES (
                ID INT PRIMARY KEY AUTO_INCREMENT,
                NIF VARCHAR(15) UNIQUE NOT NULL,
                Nombre VARCHAR(50),
                Apellidos VARCHAR(50),
                Email VARCHAR(100),
                Telefono VARCHAR(15),
                Cartera DECIMAL(10,2)
            )
        """)

        # Insertar jefe predeterminado si no existe
        cursor.execute("SELECT COUNT(*) FROM JEFES WHERE ID = 0")
        existe_jefe = cursor.fetchone()[0]

        if existe_jefe == 0:
            cursor.execute("""
                INSERT INTO JEFES (ID, Nombre, Apellido, DNI, Correo) 
                VALUES (1, 'Administrador', 'Principal', '00000000A', 'inventado@gmail.com')
            """)
            print("Jefe predeterminado creado.")

        conn.commit()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error al crear la base de datos: {err}")

def verificar_id():
    """Verifica si el ID ingresado existe en la base de datos y permite el acceso."""
    id_ingresada = entrada_id.get()
    
    conn = mysql.connector.connect(user="root", password="1234", host="localhost", database='proyectofn')
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*), Nombre FROM JEFES WHERE ID = %s", (id_ingresada,))
    resultado = cursor.fetchone()
    
    conn.close()
    
    if resultado and resultado[0] > 0:  # Si el ID existe en la tabla JEFES
        messagebox.showinfo("Acceso Concedido", f"Bienvenido, {resultado[1]}.")
        root.destroy()
        ventana_principal = VentanaPrincipal(800, 600, 700, 700, "Proyecto Final SGE 2ºDAM",conn=conn)
        ventana_principal.mainloop()
    else:
        messagebox.showerror("Acceso Denegado", "No tienes permisos para acceder.")

# Crear base de datos, tablas y jefe predeterminado antes de iniciar la interfaz
crear_base_de_datos()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Inicio de Sesión")
root.geometry("300x150")

#Lo ponemos asi para que lo sepa el profe, Si quires hacer añadir otro jefe no lo puedes hacer por aqui 
tk.Label(root, text="Ingrese su ID de Jefe(Prete 1=Administrador):").pack(pady=5)
entrada_id = tk.Entry(root)
entrada_id.pack(pady=5)

btn_verificar = tk.Button(root, text="Ingresar", command=verificar_id)
btn_verificar.pack(pady=10)

root.mainloop()