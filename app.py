from flask import Flask, render_template, send_file, request
import matplotlib.pyplot as plt
import io
from vehiculos import cargar_vehiculos, guardar_vehiculos, agregar_vehiculo, editar_vehiculo, eliminar_vehiculo
from clientes import cargar_clientes, guardar_clientes, agregar_cliente, editar_cliente, eliminar_cliente
from transacciones import cargar_transacciones, guardar_transacciones, agregar_transaccion

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot.png')
def plot_png():
    fig = create_plot()
    output = io.BytesIO()
    fig.savefig(output, format='png')
    output.seek(0)
    return send_file(output, mimetype='image/png')

def create_plot():
    vehiculos = cargar_vehiculos()
    # Datos de ejemplo para el gráfico
    marcas = [vehiculo['marca'] for vehiculo in vehiculos]
    cantidades = [1 for _ in marcas]  # Ajusta esto según los datos reales
    fig, ax = plt.subplots()
    ax.bar(marcas, cantidades)
    ax.set_xlabel('Marca')
    ax.set_ylabel('Cantidad')
    ax.set_title('Cantidad de Vehículos por Marca')
    return fig

@app.route('/vehiculos', methods=['GET', 'POST'])
def gestionar_vehiculos():
    vehiculos = cargar_vehiculos()
    if request.method == 'POST':
        # Lógica para agregar, editar o eliminar vehículos
        patente = request.form['patente']
        marca = request.form['marca']
        modelo = request.form['modelo']
        tipo = request.form['tipo']
        año = request.form['año']
        kilometraje = request.form['kilometraje']
        precio_compra = request.form['precio_compra']
        precio_venta = request.form['precio_venta']
        estado = request.form['estado']
        agregar_vehiculo(vehiculos, patente, marca, modelo, tipo, año, kilometraje, precio_compra, precio_venta, estado)
        guardar_vehiculos(vehiculos)
    return render_template('vehiculos.html', vehiculos=vehiculos)

@app.route('/clientes', methods=['GET', 'POST'])
def gestionar_clientes():
    clientes = cargar_clientes()
    if request.method == 'POST':
        # Lógica para agregar, editar o eliminar clientes
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        documento = request.form['documento']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        email = request.form['email']
        agregar_cliente(clientes, nombre, documento, apellido, direccion, telefono, email)
        guardar_clientes(clientes)
    return render_template('clientes.html', clientes=clientes)

@app.route('/transacciones', methods=['GET', 'POST'])
def registrar_transacciones():
    transacciones = cargar_transacciones()
    if request.method == 'POST':
        # Lógica para registrar transacciones
        id_vehiculo = request.form['id_vehiculo']
        id_cliente = request.form['id_cliente']
        fecha = request.form['fecha']
        monto = request.form['monto']
        observaciones = request.form['observaciones']
        agregar_transaccion(transacciones, id_vehiculo, id_cliente, "Compra", fecha, monto, observaciones)
        guardar_transacciones(transacciones)
    return render_template('transacciones.html', transacciones=transacciones)

if __name__ == '__main__':
    app.run(debug=True)