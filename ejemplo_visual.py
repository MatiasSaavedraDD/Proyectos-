#!/usr/bin/env python3
"""
Ejemplo visual de las nuevas funcionalidades de descripción detallada.
Muestra diferentes casos de uso reales.
"""

import sys
import os

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from mi_paquete.modelo_tareas import ListaEnlazada

def ejemplo_visual():
    """Muestra ejemplos visuales de las funcionalidades."""
    print("📋 EJEMPLO VISUAL: Gestor de Tareas con Descripción Detallada")
    print("=" * 65)
    
    lista = ListaEnlazada()
    
    # Ejemplos de diferentes tipos de tareas
    ejemplos = [
        ("Compras supermercado", "verduras, pan, queso, leche, huevos, yogur"),
        ("Estudiar para examen", "capítulos 3-5, hacer ejercicios, repasar fórmulas"),
        ("Reunión trabajo", "revisar presupuesto, discutir cronograma, asignar responsabilidades"),
        ("Ejercicio", "30 min cardio, 20 min pesas, estiramientos"),
        ("Llamar médico", ""),  # Sin detalles
        ("Preparar cena", "pasta, salsa boloñesa, ensalada, pan de ajo"),
        ("Limpiar casa", "aspirar, trapear, limpiar baños, organizar escritorio")
    ]
    
    print("\n🔄 Agregando tareas de ejemplo...")
    for descripcion, detalles in ejemplos:
        lista.agregar_tarea(descripcion, detalles)
        print()  # Línea en blanco para separar
    
    print("\n📋 VISTA COMPLETA DEL GESTOR DE TAREAS:")
    lista.mostrar_tareas()
    
    print("✅ Completando algunas tareas...")
    lista.marcar_completada("Compras supermercado")
    lista.marcar_completada("Llamar médico")
    
    print("\n📋 ESTADO ACTUALIZADO:")
    lista.mostrar_tareas()
    
    print("🎯 CASOS DE USO DEMOSTRADOS:")
    print("• Tareas con detalles específicos (compras, estudio)")
    print("• Tareas sin detalles adicionales (llamadas simples)")
    print("• Tareas de trabajo con información detallada")
    print("• Tareas personales con especificaciones")
    print("• Visualización clara de fechas y estados")

if __name__ == "__main__":
    ejemplo_visual()