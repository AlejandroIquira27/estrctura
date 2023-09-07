class Fecha:
    def __init__(self, d, m, a):
        self.dd = d
        self.mm = m
        self.aa = a

    def getdd(self):
        return self.dd

    def getmm(self):
        return self.mm

    def getaa(self):
        return self.aa

    def setdd(self, d):
        self.dd = d

    def setmm(self, m):
        self.mm = m

    def setaa(self, a):
        self.aa = a

    def toString(self):
        return f"{self.dd}/{self.mm}/{self.aa}"


class Direccion:
    def __init__(self, calle, noCalle, nomenclatura, barrio, ciudad):
        self.calle = calle
        self.noCalle = noCalle
        self.nomenclatura = nomenclatura
        self.barrio = barrio
        self.ciudad = ciudad

    def formato_direc(self):
        return f"{self.calle} {self.noCalle} {self.nomenclatura}, {self.barrio}, {self.ciudad}"

    def get_calle(self):
        return self.calle

    def get_noCalle(self):
        return self.noCalle

    def get_nomenclatura(self):
        return self.nomenclatura

    def get_barrio(self):
        return self.barrio

    def get_ciudad(self):
        return self.ciudad


class Usuario:
    def __init__(self, id, nombre, fecha_nacimiento, ciudad_nacimiento, direccion, telefono, correo):
        self.id = id
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    def getid(self):
        return self.id

    def getnombre(self):
        return self.nombre

    def getfechaNac(self):
        return self.fecha_nacimiento

    def getciudadNac(self):
        return self.ciudad_nacimiento

    def getdir(self):
        return self.direccion

    def gettel(self):
        return self.telefono

    def getemail(self):
        return self.correo

    def setid(self, id):
        self.id = id

    def setnombre(self, nombre):
        self.nombre = nombre

    def setfechaNac(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def setciudadNac(self, ciudad_nacimiento):
        self.ciudad_nacimiento = ciudad_nacimiento

    def setdir(self, direccion):
        self.direccion = direccion

    def settel(self, telefono):
        self.telefono = telefono

    def setemail(self, correo):
        self.correo = correo

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Fecha de Nacimiento: {self.fecha_nacimiento.toString()}, " \
               f"Ciudad de Nacimiento: {self.ciudad_nacimiento}, Dirección: {self.direccion.formato_direc()}, " \
               f"Teléfono: {self.telefono}, Email: {self.correo}"


class Registro:
    def __init__(self, capacity):
        self.usuarios = []
        self.noRegistros = 0
        self.capacity = capacity

    def agregar(self, usuario):
        if self.noRegistros >= self.capacity:
            return False  # No hay espacio disponible en el registro
        if self.buscarPosicion(usuario.id) is not None:
            return False  # Ya existe un usuario con ese número de identificación

        pos = 0
        while pos < self.noRegistros and self.usuarios[pos].id < usuario.id:
            pos += 1

        self.usuarios.insert(pos, usuario)
        self.noRegistros += 1
        return True

    def eliminar(self, id):
        pos = self.buscarPosicion(id)
        if pos is not None:
            return self.usuarios.pop(pos)

    def buscarPosicion(self, id):
        for i, usuario in enumerate(self.usuarios):
            if usuario.id == id:
                return i
        return None

    def buscarUsuario(self, id):
        pos = self.buscarPosicion(id)
        if pos is not None:
            return self.usuarios[pos]

    def toFile(self, filename):
        with open(filename, 'w') as file:
            for usuario in self.usuarios:
                file.write(f"{usuario.id},{usuario.nombre},{usuario.fecha_nacimiento.toString()},"
                           f"{usuario.ciudad_nacimiento},{usuario.direccion.get_calle()},"
                           f"{usuario.direccion.get_noCalle()},{usuario.direccion.get_nomenclatura()},"
                           f"{usuario.direccion.get_barrio()},{usuario.direccion.get_ciudad()},"
                           f"{usuario.telefono},{usuario.correo}\n")

    def importFile(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                id, nombre, fecha_nacimiento, ciudad_nacimiento, calle, noCalle, nomenclatura, barrio, ciudad, \
                telefono, correo = line.strip().split(',')
                direccion = Direccion(calle, int(noCalle), nomenclatura, barrio, ciudad)
                fecha = Fecha(*map(int, fecha_nacimiento.split('/')))
                usuario = Usuario(int(id), nombre, fecha, ciudad_nacimiento, direccion, telefono, correo)
                self.agregar(usuario)  # Agregar el usuario al registro


# Programa principal
if __name__ == "__main__":  # Corregir "_main_" por "__main__"
    registro = Registro(100)  # Crear un registro con capacidad para 100 usuarios

    while True:
        print("\nMenú:")
        print("1. Agregar Usuario")
        print("2. Eliminar Usuario")
        print("3. Buscar Usuario")
        print("4. Guardar Registro en Archivo")
        print("5. Cargar Registro desde Archivo")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id = int(input("Ingresa el ID del usuario: "))
            nombre = input("Ingresa el nombre del usuario: ")
            fecha_nac = input("Ingresa la fecha de nacimiento (DD/MM/AAAA): ")
            ciudad_nac = input("Ingresa la ciudad de nacimiento: ")
            calle = input("Ingresa la calle de la dirección: ")
            noCalle = int(input("Ingresa el número de la calle: "))
            nomenclatura = input("Ingresa la nomenclatura de la dirección: ")
            barrio = input("Ingresa el barrio de la dirección: ")
            ciudad = input("Ingresa la ciudad de la dirección: ")
            telefono = input("Ingresa el número de teléfono: ")
            email = input("Ingresa el correo electrónico: ")

            fecha_nacimiento = Fecha(*map(int, fecha_nac.split('/')))
            direccion = Direccion(calle, noCalle, nomenclatura, barrio, ciudad)
            nuevo_usuario = Usuario(id, nombre, fecha_nacimiento, ciudad_nac, direccion, telefono, email)

            if registro.agregar(nuevo_usuario):
                print("Usuario agregado con éxito.")
            else:
                print("No se pudo agregar el usuario. Verifica que haya espacio disponible y que el ID sea único.")

        elif opcion == "2":
            id = int(input("Ingresa el ID del usuario a eliminar: "))
            eliminado = registro.eliminar(id)
            if eliminado:
                print(f"Usuario eliminado:\n{eliminado}")
            else:
                print("No se encontró un usuario con ese ID.")

        elif opcion == "3":
            id = int(input("Ingresa el ID del usuario a buscar: "))
            usuario = registro.buscarUsuario(id)
            if usuario:
                print(f"Usuario encontrado:\n{usuario}")
            else:
                print("No se encontró un usuario con ese ID.")

        elif opcion == "4":
            filename = input("Ingresa el nombre del archivo para guardar el registro: ")
            registro.toFile(filename)
            print(f"Registro guardado en {filename}.")

        elif opcion == "5":
            filename = input("Ingresa el nombre del archivo para cargar el registro: ")
            registro.importFile(filename)
            print(f"Registro cargado desde {filename}.")

        elif opcion == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción válida del menú.")