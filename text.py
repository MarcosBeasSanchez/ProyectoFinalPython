import tkinter as tk
class Texto():
    def __init__(self, seccion, texto, fuente, tamanio, posicion, color,bold):
        self.seccion = seccion
        self.texto = texto
        self.fuente = fuente
        self.tamanio = tamanio
        self.posicion = posicion
        self.color = color
        self.bold=bold
        self.textLoad()

    def textLoad(self):
        self.sec = tk.Label(self.seccion, text=self.texto)
        self.sec.config(fg=self.color, font=(self.fuente, self.tamanio,self.bold), borderwidth=0,bg=self.seccion["bg"],padx=10, pady=10)
        self.sec.pack(side=self.posicion)

