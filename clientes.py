
import json
import os

def cargar_clientes():
    if os.path.exists('data/clientes.json'):
        with open('data/clientes.json', 'r') as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                return []
    else:
        return []

def guardar_clientes(clientes):
    with open('data/clientes.json', 'w') as archivo:
        json.dump(clientes, archivo, indent=4)

def agregar_cliente(clientes, nombre, apellido, documento, direccion, telefono, email):
    id_cliente = len(clientes) + 1
    cliente = {
        "id": id_cliente,
        "nombre": nombre,
        "apellido": apellido,
        "documento": documento,
        "direccion": direccion,
        "telefono": telefono,
        "email": email
    }
    clientes.append(cliente)
    guardar_clientes(clientes)

def editar_cliente(clientes, id_cliente, **kwargs):
    for cliente in clientes:
        if cliente['id'] == id_cliente:
            cliente.update(kwargs)
            guardar_clientes(clientes)
            return

def eliminar_cliente(clientes, id_cliente):
    clientes = [cliente for cliente in clientes if cliente['id'] != id_cliente]
    guardar_clientes(clientes)
    return clientes