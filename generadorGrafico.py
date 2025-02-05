import matplotlib.pyplot as plt
import tkinter as tk

class GeneradorGrafico:
    def __init__(self, ingresos, meses):
     
        self.ingresos = ingresos
        self.meses = meses

    def crearGrafico(self):

        # Configuración de barras
        bar_width = 0.8  # Ancho de las barras
        x_positions = range(len(self.meses))  # Posiciones de las barras

        colores = [] # Lista para almacenar los colores de las barras

        for i in range(1, len(self.ingresos)):
            if self.ingresos[i] > self.ingresos[i - 1]:
                colores.append("#61e800")  # Verde si sube
            else:
                colores.append("#e8003e")  # Rojo si baja

        plt.bar([x - bar_width / 2 for x in x_positions], self.ingresos, width=bar_width, label="Ingresos",color=colores, alpha=0.7)

        # Configuración de líneas
        plt.plot(self.meses, self.ingresos, linewidth=2, color="#8799d6", linestyle="--")

        # Personalización del gráfico
        plt.style.use("fast")  # Color de fondo
        plt.title("INGRESOS ANUALES", fontsize=16)
        plt.xlabel("Mes", fontsize=14)
        plt.ylabel("INGRESOS DEL TRABAJADOR", fontsize=14)
        plt.xticks(ticks=x_positions, labels=self.meses)
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.legend(fontsize=12)

        # Guardar y mostrar la gráfica
        graph_route = "./grafico.png"
        plt.savefig(graph_route)
        plt.show()
        plt.clf()
        

        return graph_route
    

    def display_graph_in_frame(self, principal, image_path):
        
        # Cargar la imagen
        img = tk.PhotoImage(file=image_path)
        label = tk.Label(principal, image=img)
        label.image = img  
        label.pack(expand=True)
