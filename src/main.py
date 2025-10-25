# Ubicación: mi-proyecto/main.py

# --- CORRECCIÓN CLAVE: Importación Absoluta al paquete ---
from mi_paquete.modelo_tareas import ListaEnlazada

class ControladorApp:
    """
    Clase que implementa el Controlador (Controller) del patrón MVC.
    Maneja la lógica de la aplicación y la interacción del usuario.
    """
    def __init__(self):
        # Instancia el Modelo
        self.lista_tareas = ListaEnlazada()
        print("\n--- Gestor de Tareas (Lista Enlazada) ---")

    def mostrar_menu(self):
        """Muestra las opciones de la Vista (View) al usuario."""
        print("\n--- MENÚ ---")
        print("1. Agregar nueva tarea")
        print("2. Mostrar todas las tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        
    def ejecutar(self):
        """Bucle principal de la aplicación."""
        while True:
            self.mostrar_menu()
            opcion = input("Elige una opción: ")

            if opcion == '1':
                descripcion = input("📝 Ingresa la descripción de la nueva tarea: ")
                # Llama al método del Modelo
                self.lista_tareas.agregar_tarea(descripcion)

            elif opcion == '2':
                # Llama al método del Modelo
                self.lista_tareas.mostrar_tareas()

            elif opcion == '3':
                descripcion = input("✅ Ingresa la descripción de la tarea a COMPLETAR: ")
                # Llama al método del Modelo
                self.lista_tareas.marcar_completada(descripcion)

            elif opcion == '4':
                descripcion = input("🗑️ Ingresa la descripción de la tarea a ELIMINAR: ")
                # Llama al método del Modelo
                self.lista_tareas.eliminar_tarea(descripcion)

            elif opcion == '5':
                print("¡Programa finalizado! 👋")
                break
            
            else:
                print("❌ Opción no válida. Inténtalo de nuevo.")

# Punto de entrada de la aplicación
if __name__ == "__main__":
    app = ControladorApp()
    app.ejecutar()