from generadorGrafico import GeneradorGrafico 

# Este código es para probar la clase GeneradorGrafico
tags = ["INGRESOS TRABAJADORES", "GASTOS CLIENTES"]
ingresos = 5000
gastos =  3000

# Crear un objeto de la clase GeneradorGrafico
generador = GeneradorGrafico(ingresos,gastos,tags)
# Llamar al método crearGrafico
generador.crearGrafico()