from flask import Flask, render_template, request, redirect, url_for
from modelo_tareas import ListaEnlazada

# Inicializar Flask
app = Flask(__name__)

# Instanciar el Modelo (la Lista Enlazada)
# La lista debe ser global para que se mantenga entre peticiones
lista_tareas = ListaEnlazada()

@app.route('/', methods=['GET'])
def index():
    """Ruta principal que muestra todas las tareas."""
    
    # 1. Obtener los datos del Modelo
    
    # Necesitamos una forma de obtener los datos para mostrarlos en la web.
    # Dado que nuestro método mostrar_tareas solo imprime, crearemos una función
    # temporal para obtener una lista de objetos de tareas.
    
    tareas_para_web = []
    actual = lista_tareas.cabeza
    while actual is not None:
        # Creamos un diccionario para cada tarea
        tareas_para_web.append({
            'descripcion': actual.descripcion,
            'descripcion_detallada': actual.descripcion_detallada,
            'estado': actual.estado,
            'fecha_creacion': actual.obtener_fecha_formateada(),
            'fecha_corta': actual.obtener_fecha_corta()
        })
        actual = actual.siguiente
        
    # 2. Devolver la Vista (View)
    return render_template('index.html', tareas=tareas_para_web)


@app.route('/agregar', methods=['POST'])
def agregar():
    """Ruta que maneja la adición de nuevas tareas."""
    if request.method == 'POST':
        # 1. El Controlador extrae los datos de la petición (Vista)
        descripcion = request.form.get('descripcion')
        descripcion_detallada = request.form.get('descripcion_detallada', '')
        
        if descripcion:
            # 2. El Controlador llama al método del Modelo
            lista_tareas.agregar_tarea(descripcion, descripcion_detallada)
            
    # 3. Redireccionar a la página principal para ver el cambio
    return redirect(url_for('index'))


@app.route('/completar/<descripcion_tarea>', methods=['POST'])
def completar(descripcion_tarea):
    """Ruta que maneja el marcado de tareas como completadas."""
    # El Controlador llama al método del Modelo
    lista_tareas.marcar_completada(descripcion_tarea)
    
    # Redireccionar
    return redirect(url_for('index'))


@app.route('/eliminar/<descripcion_tarea>', methods=['POST'])
def eliminar(descripcion_tarea):
    """Ruta que maneja la eliminación de tareas."""
    # El Controlador llama al método del Modelo
    lista_tareas.eliminar_tarea(descripcion_tarea)
    
    # Redireccionar
    return redirect(url_for('index'))


# Este es el punto de inicio de la aplicación Flask
if __name__ == '__main__':
    # Agregamos algunas tareas de prueba para que la lista no esté vacía al inicio
    lista_tareas.agregar_tarea("Estudiar Listas Enlazadas", "Revisar conceptos de nodos, punteros y operaciones CRUD")
    lista_tareas.agregar_tarea("Preparar el proyecto MVC", "Implementar Modelo, Vista y Controlador con Flask")
    app.run(debug=True)