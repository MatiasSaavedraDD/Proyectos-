# MODELO - Lógica de datos y estructuras de datos
from datetime import datetime

class NodoTarea:
    """
    Representa un nodo individual en la Lista Enlazada.
    Contiene los datos de una tarea y el puntero al siguiente nodo.
    """
    def __init__(self, descripcion, descripcion_detallada="", prioridad="media"):
        self.descripcion = descripcion
        self.descripcion_detallada = descripcion_detallada
        self.estado = "Pendiente"
        self.prioridad = prioridad  # "alta", "media", "baja"
        self.fecha_creacion = datetime.now()
        self.siguiente = None
    
    def obtener_fecha_formateada(self):
        """Retorna la fecha de creación en formato legible."""
        return self.fecha_creacion.strftime("%d/%m/%Y %H:%M:%S")
    
    def obtener_fecha_corta(self):
        """Retorna la fecha de creación en formato corto."""
        return self.fecha_creacion.strftime("%d/%m/%Y")

class ListaEnlazada:
    """
    Modelo de datos que gestiona la colección de tareas usando lista enlazada.
    Contiene solo la lógica de datos, sin interfaz de usuario.
    """
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, descripcion, descripcion_detallada="", prioridad="media"):
        """Añade un nuevo nodo al final de la lista."""
        nuevo_nodo = NodoTarea(descripcion, descripcion_detallada, prioridad)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return True

        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
            
        actual.siguiente = nuevo_nodo
        return True

    def obtener_todas_las_tareas(self):
        """Retorna una lista con todas las tareas para ser procesada por la vista."""
        tareas = []
        actual = self.cabeza
        
        while actual is not None:
            tareas.append({
                'descripcion': actual.descripcion,
                'descripcion_detallada': actual.descripcion_detallada,
                'estado': actual.estado,
                'prioridad': actual.prioridad,
                'fecha_creacion': actual.obtener_fecha_formateada(),
                'fecha_corta': actual.obtener_fecha_corta()
            })
            actual = actual.siguiente
            
        return tareas

    def marcar_completada(self, descripcion_buscada):
        """Busca una tarea por descripción y cambia su estado."""
        actual = self.cabeza
        
        while actual is not None:
            if actual.descripcion.lower() == descripcion_buscada.lower():
                actual.estado = "Completada"
                return True
            actual = actual.siguiente
        
        return False

    def eliminar_tarea(self, descripcion_buscada):
        """Busca una tarea y la elimina re-enlazando los punteros."""
        actual = self.cabeza
        anterior = None 

        if actual is None:
            return False

        # Búsqueda de la tarea
        while actual is not None and actual.descripcion.lower() != descripcion_buscada.lower():
            anterior = actual
            actual = actual.siguiente

        # Tarea no encontrada
        if actual is None:
            return False

        # Caso: Tarea es la cabeza
        if anterior is None:
            self.cabeza = actual.siguiente
        else:
            # Re-enlazar: el anterior apunta al siguiente del actual
            anterior.siguiente = actual.siguiente
            
        return True

    def contar_tareas(self):
        """Retorna el número total de tareas."""
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

    def esta_vacia(self):
        """Verifica si la lista está vacía."""
        return self.cabeza is None
    
    def obtener_color_prioridad(self, prioridad):
        """Retorna el color asociado a cada prioridad."""
        colores = {
            'alta': '#dc3545',    # Rojo
            'media': '#ffc107',   # Amarillo
            'baja': '#28a745'     # Verde
        }
        return colores.get(prioridad, '#6c757d')  # Gris por defecto
    
    def contar_por_prioridad(self):
        """Retorna un diccionario con el conteo de tareas por prioridad."""
        conteo = {'alta': 0, 'media': 0, 'baja': 0}
        actual = self.cabeza
        
        while actual is not None:
            if actual.prioridad in conteo:
                conteo[actual.prioridad] += 1
            actual = actual.siguiente
            
        return conteo