# Ubicación: mi-proyecto/src/mi_paquete/modelo_tareas.py

from datetime import datetime

class NodoTarea:
    """
    Representa un nodo individual en la Lista Enlazada.
    """
    def __init__(self, descripcion, descripcion_detallada=""):
        self.descripcion = descripcion
        self.descripcion_detallada = descripcion_detallada  # Información adicional
        self.estado = "Pendiente"  # Estado inicial
        self.fecha_creacion = datetime.now()  # Fecha y hora de creación
        self.siguiente = None      # Puntero al siguiente nodo
    
    def obtener_fecha_formateada(self):
        """Retorna la fecha de creación en formato legible."""
        return self.fecha_creacion.strftime("%d/%m/%Y %H:%M:%S")
    
    def obtener_fecha_corta(self):
        """Retorna la fecha de creación en formato corto."""
        return self.fecha_creacion.strftime("%d/%m/%Y")

class ListaEnlazada:
    """
    Gestiona la colección de NodoTarea y las operaciones de la lista.
    """
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, descripcion, descripcion_detallada=""):
        """Añade un nuevo nodo al final de la lista."""
        nuevo_nodo = NodoTarea(descripcion, descripcion_detallada)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            print(f"✅ Tarea '{descripcion}' agregada como la primera.")
            if descripcion_detallada:
                print(f"    📝 Detalles: {descripcion_detallada}")
            print(f"    📅 Creada el: {nuevo_nodo.obtener_fecha_formateada()}")
            return

        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
            
        actual.siguiente = nuevo_nodo
        print(f"✅ Tarea '{descripcion}' agregada al final.")
        if descripcion_detallada:
            print(f"    📝 Detalles: {descripcion_detallada}")
        print(f"    📅 Creada el: {nuevo_nodo.obtener_fecha_formateada()}")

    def mostrar_tareas(self):
        """Recorre e imprime todas las tareas y sus estados."""
        if self.cabeza is None:
            print("\n➡️ La lista de tareas está vacía.")
            return

        print("\n--- LISTADO DE TAREAS ---")
        actual = self.cabeza
        contador = 1
        while actual is not None:
            estado_display = f"[{actual.estado}]"
            fecha_display = actual.obtener_fecha_formateada()
            print(f"{contador}. {estado_display:<15} - {actual.descripcion}")
            if actual.descripcion_detallada:
                print(f"    📝 Detalles: {actual.descripcion_detallada}")
            print(f"    📅 Creada: {fecha_display}")
            actual = actual.siguiente
            contador += 1
        print("-------------------------\n")

    def marcar_completada(self, descripcion_buscada):
        """Busca una tarea por descripción y cambia su estado."""
        actual = self.cabeza
        
        while actual is not None:
            if actual.descripcion.lower() == descripcion_buscada.lower():
                actual.estado = "Completada"
                print(f"✅ Tarea '{actual.descripcion}' marcada como COMPLETADA.")
                return 
            
            actual = actual.siguiente
        
        print(f"❌ Error: Tarea con descripción '{descripcion_buscada}' no encontrada.")

    def eliminar_tarea(self, descripcion_buscada):
        """Busca una tarea y la elimina re-enlazando los punteros."""
        actual = self.cabeza
        anterior = None 

        if actual is None:
            print("❌ La lista de tareas está vacía.")
            return

        # 1. Búsqueda de la tarea
        while actual is not None and actual.descripcion.lower() != descripcion_buscada.lower():
            anterior = actual
            actual = actual.siguiente

        # 2. Tarea NO encontrada
        if actual is None:
            print(f"❌ Error: Tarea con descripción '{descripcion_buscada}' no encontrada para eliminar.")
            return

        # 3. Caso: Tarea es la CABEZA
        if anterior is None:
            self.cabeza = actual.siguiente
        # 4. Caso: Tarea en medio o al final
        else:
            # Re-enlazar: el anterior apunta al siguiente del actual
            anterior.siguiente = actual.siguiente
            
        print(f"🗑️ Tarea '{actual.descripcion}' eliminada.")