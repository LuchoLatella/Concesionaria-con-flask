
import json

def cargar_vehiculos():
    try:
        with open('vehiculos.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_vehiculos(vehiculos):
    with open('vehiculos.json', 'w') as file:
        json.dump(vehiculos, file)

def agregar_vehiculo(vehiculos, patente, marca, modelo, tipo, año, kilometraje, precio_compra, precio_venta, estado):
    nuevo_vehiculo = {
        'id': len(vehiculos) + 1,
        'patente': patente,
        'marca': marca,
        'modelo': modelo,
        'tipo': tipo,
        'año': año,
        'kilometraje': kilometraje,
        'precio_compra': precio_compra,
        'precio_venta': precio_venta,
        'estado': estado
    }
    vehiculos.append(nuevo_vehiculo)
    guardar_vehiculos(vehiculos)

def editar_vehiculo(vehiculos, id_vehiculo, **datos_actualizados):
    for vehiculo in vehiculos:
        if vehiculo['id'] == id_vehiculo:
            vehiculo.update(datos_actualizados)
            guardar_vehiculos(vehiculos)
            return

def eliminar_vehiculo(vehiculos, id_vehiculo):
    vehiculos = [vehiculo for vehiculo in vehiculos if vehiculo['id'] != id_vehiculo]
    guardar_vehiculos(vehiculos)
    return vehiculos