from generadorGrafico import GeneradorGrafico 

# Este código es para probar la clase GeneradorGrafico
meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
ingresos = [1000, 2000, 1500, 3000, 2500, 4000, 3500, 5000, 4500, 6000, 5500, 7000]

# Crear un objeto de la clase GeneradorGrafico
generador = GeneradorGrafico(ingresos, meses)
# Llamar al método crearGrafico
generador.crearGrafico()