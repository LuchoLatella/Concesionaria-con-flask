
import json

def cargar_transacciones():
    try:
        with open('transacciones.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_transacciones(transacciones):
    with open('transacciones.json', 'w') as file:
        json.dump(transacciones, file)

def agregar_transaccion(transacciones, id_vehiculo, id_cliente, tipo, fecha, monto, observaciones):
    nueva_transaccion = {
        'id': len(transacciones) + 1,
        'id_vehiculo': id_vehiculo,
        'id_cliente': id_cliente,
        'tipo': tipo,
        'fecha': fecha,
        'monto': monto,
        'observaciones': observaciones
    }
    transacciones.append(nueva_transaccion)
    guardar_transacciones(transacciones)