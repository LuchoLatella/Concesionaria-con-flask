
import json
import os

def cargar_transacciones():
    if os.path.exists('data/transacciones.json'):
        with open('data/transacciones.json', 'r') as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                return []
    else:
        return []

def guardar_transacciones(transacciones):
    with open('data/transacciones.json', 'w') as archivo:
        json.dump(transacciones, archivo, indent=4)

def agregar_transaccion(transacciones, id_vehiculo, id_cliente, tipo, fecha, monto, observaciones):
    id_transaccion = len(transacciones) + 1
    transaccion = {
        "id": id_transaccion,
        "id_vehiculo": id_vehiculo,
        "id_cliente": id_cliente,
        "tipo": tipo,
        "fecha": fecha,
        "monto": monto,
        "observaciones": observaciones
    }
    transacciones.append(transaccion)
    guardar_transacciones(transacciones)

def editar_transaccion(transacciones, id_transaccion, **kwargs):
    for transaccion in transacciones:
        if transaccion['id'] == id_transaccion:
            transaccion.update(kwargs)
            guardar_transacciones(transacciones)
            return

def eliminar_transaccion(transacciones, id_transaccion):
   transacciones[:] = [transaccion for transaccion in transacciones if transaccion['id'] != id_transaccion]
   guardar_transacciones(transacciones)
   return transacciones