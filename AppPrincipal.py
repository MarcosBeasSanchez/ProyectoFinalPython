import tkinter as tk
from tkinter import messagebox
import mysql.connector
from frames import VentanaPrincipal

def verificar_id():
    id_ingresada = entrada_id.get()
    
    conn = mysql.connector.connect(user="root", password="1234", host="localhost", database='proyectofn')
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM JEFES WHERE ID = %s", (id_ingresada,))
    resultado = cursor.fetchone() #Cojemos la Primera linea para comprobar abajo si hay
    
    conn.close()
    
    if resultado: #Si exsite el jefe accede a la pagina por los frames
        messagebox.showinfo("Acceso Concedido", "Bienvenido, Jefe.")
        root.destroy()
        ventana_principal = VentanaPrincipal(800, 600, 700, 700, "Proyecto Final SGE 2ºDAM")
        ventana_principal.mainloop()
    else:
        messagebox.showerror("Acceso Denegado", "No tienes permisos para acceder.")

root = tk.Tk()
root.title("Inicio de Sesión")
root.geometry("300x150")

tk.Label(root, text="Ingrese su ID de Jefe:").pack(pady=5)
entrada_id = tk.Entry(root)
entrada_id.pack(pady=5)

btn_verificar = tk.Button(root, text="Ingresar", command=verificar_id)
btn_verificar.pack(pady=10)

root.mainloop()