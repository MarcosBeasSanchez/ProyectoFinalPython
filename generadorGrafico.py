import matplotlib.pyplot as plt
import tkinter as tk

class GeneradorGrafico:
    def __init__(self, ingresos, gastos, tags):
        self.tags = tags
        self.ingresos = ingresos
        self.gastos = gastos

    def crearGrafico(self):
        # Configuración de barras
        bar_width = 0.8  # Ancho de las barras
        x_positions = range(len(self.tags))  # Posiciones de las barra
        color_rojo = "#ff0505"  # Color rojo
        color_verde = "#2bff05"  # Color verde
    
        # Crear la gráfica 
        if self.ingresos > self.gastos:
            plt.bar(x_positions[1], self.gastos, width=bar_width, label="Gastos", color=color_rojo, alpha=0.8)
            plt.bar(x_positions[0], self.ingresos, width=bar_width, label="Ingresos", color=color_verde, alpha=0.8)
        else:
            plt.bar(x_positions[0], self.ingresos, width=bar_width, label="Ingresos", color=color_rojo, alpha=0.8)
            plt.bar(x_positions[1], self.gastos, width=bar_width, label="Gastos", color=color_verde, alpha=0.8)

        # Personalización del gráfico
        plt.style.use("fast")  # Color de fondo
        plt.title("INGRESOS Y GASTOS", fontsize=16, fontweight="bold", color="black")
        plt.ylabel("EUROS €", fontsize=10,color="black",fontweight="bold")
        plt.xticks(ticks=x_positions, labels=self.tags ,color="black",fontsize=9)
        plt.grid(True, linestyle="-", alpha=0.3)
        plt.legend(fontsize=12)

        # Guardar y mostrar la gráfica
        graph_route = "./grafico.png"
        plt.savefig(graph_route)
        #plt.show()
        plt.clf()
        plt.close()
        return graph_route

    def display_graph_in_frame(self, principal, image_path):
        # Cargar la imagen
        img = tk.PhotoImage(file=image_path)
        label = tk.Label(principal, image=img)
        label.image = img  
        label.pack(expand=True)
