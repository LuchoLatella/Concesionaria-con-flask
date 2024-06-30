
import json

def cargar_clientes():
    try:
        with open('clientes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_clientes(clientes):
    with open('clientes.json', 'w') as file:
        json.dump(clientes, file)

def agregar_cliente(clientes, nombre, documento, apellido, direccion, telefono, email):
    nuevo_cliente = {
        'id': len(clientes) + 1,
        'nombre': nombre,
        'documento': documento,
        'apellido': apellido,
        'direccion': direccion,
        'telefono': telefono,
        'email': email
    }
    clientes.append(nuevo_cliente)
    guardar_clientes(clientes)

def editar_cliente(clientes, id_cliente, **datos_actualizados):
    for cliente in clientes:
        if cliente['id'] == id_cliente:
            cliente.update(datos_actualizados)
            guardar_clientes(clientes)
            return

def eliminar_cliente(clientes, id_cliente):
    clientes = [cliente for cliente in clientes if cliente['id'] != id_cliente]
    guardar_clientes(clientes)
    return clientes