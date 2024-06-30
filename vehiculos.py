
import json
import os

def cargar_vehiculos():
    if os.path.exists('data/vehiculos.json'):
        with open('data/vehiculos.json', 'r') as archivo:
            return json.load(archivo)
    else:
        return []

def guardar_vehiculos(vehiculos):
    with open('data/vehiculos.json', 'w') as archivo:
        json.dump(vehiculos, archivo, indent=4)

def agregar_vehiculo(vehiculos, patente, marca, modelo, tipo, año, kilometraje, precio_compra, precio_venta, estado):
    id_vehiculo = len(vehiculos) + 1
    vehiculo = {
        "id": id_vehiculo,
        "patente": patente,
        "marca": marca,
        "modelo": modelo,
        "tipo": tipo,
        "año": año,
        "kilometraje": kilometraje,
        "precio_compra": precio_compra,
        "precio_venta": precio_venta,
        "estado": estado
    }
    vehiculos.append(vehiculo)
    guardar_vehiculos(vehiculos)

def editar_vehiculo(vehiculos, id_vehiculo, **kwargs):
    for vehiculo in vehiculos:
        if vehiculo['id'] == id_vehiculo:
            vehiculo.update(kwargs)
            guardar_vehiculos(vehiculos)
            return

def eliminar_vehiculo(vehiculos, id_vehiculo):
    vehiculos = [vehiculo for vehiculo in vehiculos if vehiculo['id'] != id_vehiculo]
    guardar_vehiculos(vehiculos)
    return vehiculos