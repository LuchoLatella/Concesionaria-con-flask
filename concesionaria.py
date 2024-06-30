
from vehiculos import cargar_vehiculos, guardar_vehiculos, agregar_vehiculo, editar_vehiculo, eliminar_vehiculo
from clientes import cargar_clientes, guardar_clientes, agregar_cliente, editar_cliente, eliminar_cliente
from transacciones import cargar_transacciones, guardar_transacciones, agregar_transaccion

def menu():
    print("Bienvenido a la Concesionaria")
    print("1. Gestionar Vehículos")
    print("2. Gestionar Clientes")
    print("3. Registrar Transacciones")
    print("4. Salir")

def submenu_vehiculos():
    print("1. Crear Vehículo")
    print("2. Editar Vehículo")
    print("3. Eliminar Vehículo")
    print("4. Buscar Vehículos")
    print("5. Volver al menú principal")

def submenu_clientes():
    print("1. Crear Cliente")
    print("2. Editar Cliente")
    print("3. Eliminar Cliente")
    print("4. Buscar Clientes")
    print("5. Volver al menú principal")

def submenu_transacciones():
    print("1. Registrar Compra")
    print("2. Registrar Venta")
    print("3. Listar Compras")
    print("4. Listar Ventas")
    print("5. Volver al menú principal")

def gestionar_vehiculos():
    vehiculos = cargar_vehiculos()
    while True:
        submenu_vehiculos()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            patente = input("Patente: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            tipo = input("Tipo: ")
            año = input("Año: ")
            kilometraje = input("Kilometraje: ")
            precio_compra = input("Precio de Compra: ")
            precio_venta = input("Precio de Venta: ")
            estado = input("Estado: ")
            agregar_vehiculo(vehiculos, patente, marca, modelo, tipo, año, kilometraje, precio_compra, precio_venta, estado)
        elif opcion == '2':
            id_vehiculo = int(input("ID del Vehículo: "))
            campos = ["patente", "marca", "modelo", "tipo", "año", "kilometraje", "precio_compra", "precio_venta", "estado"]
            datos = {campo: input(f"{campo.capitalize()}: ") for campo in campos}
            editar_vehiculo(vehiculos, id_vehiculo, **{k: v for k, v in datos.items() if v})
        elif opcion == '3':
            id_vehiculo = int(input("ID del Vehículo: "))
            vehiculos = eliminar_vehiculo(vehiculos, id_vehiculo)
        elif opcion == '4':
            print(vehiculos)
        elif opcion == '5':
            break

def gestionar_clientes():
    clientes = cargar_clientes()
    while True:
        submenu_clientes()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            documento = input("Documento: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            email = input("Correo Electrónico: ")
            agregar_cliente(clientes, nombre, documento, apellido, direccion, telefono, email)
        elif opcion == '2':
            id_cliente = int(input("ID del Cliente: "))
            campos = ["nombre", "documento", "apellido", "direccion", "telefono", "email"]
            datos = {campo: input(f"{campo.capitalize()}: ") for campo in campos}
            editar_cliente(clientes, id_cliente, **{k: v for k, v in datos.items() if v})
        elif opcion == '3':
            id_cliente = int(input("ID del Cliente: "))
            clientes = eliminar_cliente(clientes, id_cliente)
        elif opcion == '4':
            print(clientes)
        elif opcion == '5':
            break

def registrar_transacciones():
    transacciones = cargar_transacciones()
    vehiculos = cargar_vehiculos()
    clientes = cargar_clientes()
    while True:
        submenu_transacciones()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            id_vehiculo = int(input("ID del Vehículo: "))
            id_cliente = int(input("ID del Cliente: "))
            fecha = input("Fecha: ")
            monto = input("Monto: ")
            observaciones = input("Observaciones: ")
            agregar_transaccion(transacciones, id_vehiculo, id_cliente, "Compra", fecha, monto, observaciones)
            editar_vehiculo(vehiculos, id_vehiculo, estado="Comprado")
        elif opcion == '2':
            id_vehiculo = int(input("ID del Vehículo: "))
            id_cliente = int(input("ID del Cliente: "))
            fecha = input("Fecha: ")
            monto = input("Monto: ")
            observaciones = input("Observaciones: ")
            agregar_transaccion(transacciones, id_vehiculo, id_cliente, "Venta", fecha, monto, observaciones)
            editar_vehiculo(vehiculos, id_vehiculo, estado="Vendido")
        elif opcion == '3':
            for t in transacciones:
                if t['tipo'] == 'Compra':
                    print(t)
        elif opcion == '4':
            for t in transacciones:
                if t['tipo'] == 'Venta':
                    print(t)
        elif opcion == '5':
            break

def menu_inicial():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            gestionar_vehiculos()
        elif opcion == '2':
            gestionar_clientes()
        elif opcion == '3':
            registrar_transacciones()
        elif opcion == '4':
            break
menu_inicial()