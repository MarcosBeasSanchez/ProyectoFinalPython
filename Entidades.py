class Empleado():
    def __init__(self, id_empleado, nombre, apellidos, dni, telefono, fecha_contratacion, sueldo, comision):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.telefono = telefono
        self.fecha_contratacion = fecha_contratacion
        self.sueldo = sueldo
        self.comision = comision
    
    def get_id_empleado(self):
        return self.id_empleado
    
    def set_id_empleado(self, id_empleado):
        self.id_empleado = id_empleado
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

class Jefe:
    def __init__(self, id_jefe, nombre, apellidos, sueldo):
        self.id_jefe = id_jefe
        self.nombre = nombre
        self.apellidos = apellidos
        self.sueldo = sueldo
    
    def get_id_jefe(self):
        return self.id_jefe
    
    def set_id_jefe(self, id_jefe):
        self.id_jefe = id_jefe
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

class Cliente:
    def __init__(self, id_cliente, nif, nombre, apellidos, email, telefono, cartera):
        self.id_cliente = id_cliente
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.telefono = telefono
        self.cartera = cartera
    
    def get_id_cliente(self):
        return self.id_cliente
    
    def set_id_cliente(self, id_cliente):
        self.id_cliente = id_cliente
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

