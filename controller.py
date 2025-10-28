# CONTROLADOR - Lógica de aplicación y coordinación entre Modelo y Vista
from flask import Flask, request, redirect, url_for
from model import ListaEnlazada
from view import generar_pagina_principal

# Inicializar Flask
app = Flask(__name__)

# Instanciar el Modelo
lista_tareas = ListaEnlazada()

class ControladorTareas:
    """
    Controlador que maneja la lógica de aplicación y coordina
    entre el Modelo (ListaEnlazada) y la Vista (HTML).
    """
    
    def __init__(self, modelo):
        self.modelo = modelo
    
    def obtener_todas_las_tareas(self):
        """Obtiene todas las tareas del modelo para la vista."""
        return self.modelo.obtener_todas_las_tareas()
    
    def agregar_nueva_tarea(self, descripcion, descripcion_detallada="", prioridad="media"):
        """Procesa la adición de una nueva tarea."""
        if descripcion and descripcion.strip():
            # Validar prioridad
            prioridades_validas = ['alta', 'media', 'baja']
            if prioridad not in prioridades_validas:
                prioridad = 'media'  # Valor por defecto
            
            return self.modelo.agregar_tarea(
                descripcion.strip(), 
                descripcion_detallada.strip(), 
                prioridad
            )
        return False
    
    def completar_tarea(self, descripcion):
        """Procesa el marcado de una tarea como completada."""
        return self.modelo.marcar_completada(descripcion)
    
    def eliminar_tarea(self, descripcion):
        """Procesa la eliminación de una tarea."""
        return self.modelo.eliminar_tarea(descripcion)
    
    def obtener_estadisticas(self):
        """Obtiene estadísticas para mostrar en la vista."""
        tareas = self.obtener_todas_las_tareas()
        total = len(tareas)
        completadas = len([t for t in tareas if t['estado'] == 'Completada'])
        pendientes = total - completadas
        
        # Estadísticas por prioridad
        prioridades = self.modelo.contar_por_prioridad()
        
        return {
            'total': total,
            'completadas': completadas,
            'pendientes': pendientes,
            'prioridades': prioridades
        }

# Instanciar el controlador
controlador = ControladorTareas(lista_tareas)

# RUTAS DE LA APLICACIÓN WEB

@app.route('/', methods=['GET'])
def index():
    """Ruta principal que muestra todas las tareas."""
    tareas = controlador.obtener_todas_las_tareas()
    estadisticas = controlador.obtener_estadisticas()
    return generar_pagina_principal(tareas, estadisticas)

@app.route('/agregar', methods=['POST'])
def agregar():
    """Ruta que maneja la adición de nuevas tareas."""
    descripcion = request.form.get('descripcion', '')
    descripcion_detallada = request.form.get('descripcion_detallada', '')
    prioridad = request.form.get('prioridad', 'media')
    
    # El controlador procesa la solicitud
    controlador.agregar_nueva_tarea(descripcion, descripcion_detallada, prioridad)
    
    return redirect(url_for('index'))

@app.route('/completar/<descripcion_tarea>', methods=['POST'])
def completar(descripcion_tarea):
    """Ruta que maneja el marcado de tareas como completadas."""
    controlador.completar_tarea(descripcion_tarea)
    return redirect(url_for('index'))

@app.route('/eliminar/<descripcion_tarea>', methods=['POST'])
def eliminar(descripcion_tarea):
    """Ruta que maneja la eliminación de tareas."""
    controlador.eliminar_tarea(descripcion_tarea)
    return redirect(url_for('index'))

# Función para inicializar datos de prueba
def inicializar_datos_prueba():
    """Agrega algunas tareas de ejemplo para demostración."""
    controlador.agregar_nueva_tarea(
        "Estudiar Listas Enlazadas", 
        "Revisar conceptos de nodos, punteros y operaciones CRUD",
        "alta"
    )
    controlador.agregar_nueva_tarea(
        "Implementar patrón MVC", 
        "Separar Modelo, Vista y Controlador correctamente",
        "media"
    )
    controlador.agregar_nueva_tarea(
        "Crear interfaz web", 
        "Diseñar formularios y mostrar datos dinámicamente",
        "baja"
    )

# Punto de entrada de la aplicación
if __name__ == '__main__':
    # Inicializar con datos de prueba
    inicializar_datos_prueba()
    
    # Ejecutar la aplicación Flask
    app.run(debug=True, host='127.0.0.1', port=5000)