import mysql.connector

class BaseDatos():
    def __init__(self, host="localhost", user="root", password="1234", database="proyectofn"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def conectar(self):
        try:
            return mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except mysql.connector.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None

    def ejecutar_consulta(self, consulta, valores=None):
        conexion = self.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                if valores:
                    cursor.execute(consulta, valores)
                else:
                    cursor.execute(consulta)
                conexion.commit()
                return cursor.fetchall()
            except mysql.connector.Error as e:
                print(f"Error en la consulta: {e}")
            finally:
                conexion.close()
        return None

    def insertar_empleado(self, id_empleado, nombre, apellidos, dni, telefono, fecha_contratacion, sueldo, comision):
        consulta = """
        INSERT INTO EMPLEADOS (ID_Empleado, Nombre, Apellidos, DNI, Teléfono_Móvil, Fecha_Contratación, sueldo, comision)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (id_empleado, nombre, apellidos, dni, telefono, fecha_contratacion, sueldo, comision)
        self.ejecutar_consulta(consulta, valores)

    def obtener_empleados(self):
        consulta = "SELECT * FROM EMPLEADOS"
        return self.ejecutar_consulta(consulta)

    def actualizar_empleado(self, id_empleado, nombre, apellidos, dni, telefono, fecha_contratacion, sueldo, comision):
        consulta = """
        UPDATE EMPLEADOS SET Nombre=%s, Apellidos=%s, DNI=%s, Teléfono_Móvil=%s, Fecha_Contratación=%s, sueldo=%s, comision=%s
        WHERE ID_Empleado=%s
        """
        valores = (nombre, apellidos, dni, telefono, fecha_contratacion, sueldo, comision, id_empleado)
        self.ejecutar_consulta(consulta, valores)

    def eliminar_empleado(self, id_empleado):
        consulta = "DELETE FROM EMPLEADOS WHERE ID_Empleado=%s"
        self.ejecutar_consulta(consulta, (id_empleado,))
