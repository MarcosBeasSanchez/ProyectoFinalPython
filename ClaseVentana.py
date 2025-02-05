import tkinter as tk

class Ventana():
    def __init__(self, geometry, title, resizable):
        self._root = tk.Tk()
        self._root.title(title)
        self._root.geometry(f"{geometry}")
        self._root.resizable(width=resizable, height=resizable)

    def get_root(self):
        return self._root

    def apagar(self):
        self._root.mainloop()

if __name__ == "__main__":
    ventana = Ventana("300x250", "Mi Ventana Prueba", False)
    root = ventana.get_root()
    
    top = tk.Toplevel(root)
    top.title("Toplevel Prueba")
    top.geometry("200x150")
    
    ventana.apagar()
