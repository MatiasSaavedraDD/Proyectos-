#!/usr/bin/env python3
"""
Tests unitarios para el modelo de tareas (Lista Enlazada).
Prueba las funcionalidades básicas de la estructura de datos.
"""

import sys
import os
import unittest
from datetime import datetime

# Agregar el directorio src al path para importar el módulo
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from mi_paquete.modelo_tareas import ListaEnlazada, NodoTarea


class TestNodoTarea(unittest.TestCase):
    """Tests para la clase NodoTarea."""
    
    def test_crear_nodo(self):
        """Prueba la creación de un nodo de tarea."""
        antes_creacion = datetime.now()
        nodo = NodoTarea("Tarea de prueba")
        despues_creacion = datetime.now()
        
        self.assertEqual(nodo.descripcion, "Tarea de prueba")
        self.assertEqual(nodo.descripcion_detallada, "")
        self.assertEqual(nodo.estado, "Pendiente")
        self.assertIsNone(nodo.siguiente)
        
        # Verificar que la fecha de creación está en el rango esperado
        self.assertGreaterEqual(nodo.fecha_creacion, antes_creacion)
        self.assertLessEqual(nodo.fecha_creacion, despues_creacion)
    
    def test_crear_nodo_con_descripcion_detallada(self):
        """Prueba la creación de un nodo con descripción detallada."""
        nodo = NodoTarea("Compras supermercado", "verduras, pan, queso, leche")
        
        self.assertEqual(nodo.descripcion, "Compras supermercado")
        self.assertEqual(nodo.descripcion_detallada, "verduras, pan, queso, leche")
        self.assertEqual(nodo.estado, "Pendiente")
        self.assertIsInstance(nodo.fecha_creacion, datetime)
    
    def test_nodo_con_descripcion_vacia(self):
        """Prueba crear un nodo con descripción vacía."""
        nodo = NodoTarea("")
        
        self.assertEqual(nodo.descripcion, "")
        self.assertEqual(nodo.estado, "Pendiente")
        self.assertIsInstance(nodo.fecha_creacion, datetime)
    
    def test_formato_fecha(self):
        """Prueba los métodos de formateo de fecha."""
        nodo = NodoTarea("Tarea con fecha")
        
        # Verificar que los métodos de formato retornan strings
        fecha_formateada = nodo.obtener_fecha_formateada()
        fecha_corta = nodo.obtener_fecha_corta()
        
        self.assertIsInstance(fecha_formateada, str)
        self.assertIsInstance(fecha_corta, str)
        
        # Verificar formato básico (debe contener números y separadores)
        self.assertRegex(fecha_formateada, r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}')
        self.assertRegex(fecha_corta, r'\d{2}/\d{2}/\d{4}')


class TestListaEnlazada(unittest.TestCase):
    """Tests para la clase ListaEnlazada."""
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.lista = ListaEnlazada()
    
    def test_lista_vacia_inicial(self):
        """Prueba que la lista esté vacía al inicializar."""
        self.assertIsNone(self.lista.cabeza)
    
    def test_agregar_primera_tarea(self):
        """Prueba agregar la primera tarea a la lista vacía."""
        self.lista.agregar_tarea("Primera tarea")
        
        self.assertIsNotNone(self.lista.cabeza)
        self.assertEqual(self.lista.cabeza.descripcion, "Primera tarea")
        self.assertEqual(self.lista.cabeza.descripcion_detallada, "")
        self.assertEqual(self.lista.cabeza.estado, "Pendiente")
        self.assertIsNone(self.lista.cabeza.siguiente)
    
    def test_agregar_tarea_con_detalles(self):
        """Prueba agregar una tarea con descripción detallada."""
        self.lista.agregar_tarea("Compras supermercado", "verduras, pan, queso")
        
        self.assertIsNotNone(self.lista.cabeza)
        self.assertEqual(self.lista.cabeza.descripcion, "Compras supermercado")
        self.assertEqual(self.lista.cabeza.descripcion_detallada, "verduras, pan, queso")
        self.assertEqual(self.lista.cabeza.estado, "Pendiente")
    
    def test_agregar_multiples_tareas(self):
        """Prueba agregar múltiples tareas a la lista."""
        self.lista.agregar_tarea("Tarea 1")
        self.lista.agregar_tarea("Tarea 2")
        self.lista.agregar_tarea("Tarea 3")
        
        # Verificar que la cabeza es la primera tarea
        self.assertEqual(self.lista.cabeza.descripcion, "Tarea 1")
        
        # Verificar que las tareas están enlazadas correctamente
        segundo_nodo = self.lista.cabeza.siguiente
        self.assertEqual(segundo_nodo.descripcion, "Tarea 2")
        
        tercer_nodo = segundo_nodo.siguiente
        self.assertEqual(tercer_nodo.descripcion, "Tarea 3")
        self.assertIsNone(tercer_nodo.siguiente)
    
    def test_marcar_completada_existente(self):
        """Prueba marcar como completada una tarea existente."""
        self.lista.agregar_tarea("Tarea a completar")
        self.lista.marcar_completada("Tarea a completar")
        
        self.assertEqual(self.lista.cabeza.estado, "Completada")
    
    def test_marcar_completada_no_existente(self):
        """Prueba marcar como completada una tarea que no existe."""
        self.lista.agregar_tarea("Tarea existente")
        
        # Esto no debería cambiar nada
        self.lista.marcar_completada("Tarea inexistente")
        
        # La tarea existente debe seguir pendiente
        self.assertEqual(self.lista.cabeza.estado, "Pendiente")
    
    def test_marcar_completada_case_insensitive(self):
        """Prueba que la búsqueda sea insensible a mayúsculas/minúsculas."""
        self.lista.agregar_tarea("Tarea MAYÚSCULAS")
        self.lista.marcar_completada("tarea mayúsculas")
        
        self.assertEqual(self.lista.cabeza.estado, "Completada")
    
    def test_eliminar_unica_tarea(self):
        """Prueba eliminar la única tarea de la lista."""
        self.lista.agregar_tarea("Única tarea")
        self.lista.eliminar_tarea("Única tarea")
        
        self.assertIsNone(self.lista.cabeza)
    
    def test_eliminar_primera_tarea(self):
        """Prueba eliminar la primera tarea de múltiples."""
        self.lista.agregar_tarea("Primera")
        self.lista.agregar_tarea("Segunda")
        self.lista.agregar_tarea("Tercera")
        
        self.lista.eliminar_tarea("Primera")
        
        # La cabeza ahora debe ser la segunda tarea
        self.assertEqual(self.lista.cabeza.descripcion, "Segunda")
    
    def test_eliminar_tarea_medio(self):
        """Prueba eliminar una tarea del medio de la lista."""
        self.lista.agregar_tarea("Primera")
        self.lista.agregar_tarea("Segunda")
        self.lista.agregar_tarea("Tercera")
        
        self.lista.eliminar_tarea("Segunda")
        
        # Verificar que la primera apunta directamente a la tercera
        self.assertEqual(self.lista.cabeza.descripcion, "Primera")
        self.assertEqual(self.lista.cabeza.siguiente.descripcion, "Tercera")
    
    def test_eliminar_ultima_tarea(self):
        """Prueba eliminar la última tarea de la lista."""
        self.lista.agregar_tarea("Primera")
        self.lista.agregar_tarea("Segunda")
        self.lista.agregar_tarea("Última")
        
        self.lista.eliminar_tarea("Última")
        
        # Verificar que la segunda tarea no tiene siguiente
        segundo_nodo = self.lista.cabeza.siguiente
        self.assertEqual(segundo_nodo.descripcion, "Segunda")
        self.assertIsNone(segundo_nodo.siguiente)
    
    def test_eliminar_tarea_inexistente(self):
        """Prueba eliminar una tarea que no existe."""
        self.lista.agregar_tarea("Tarea existente")
        
        # Esto no debería cambiar la lista
        self.lista.eliminar_tarea("Tarea inexistente")
        
        # La lista debe seguir igual
        self.assertEqual(self.lista.cabeza.descripcion, "Tarea existente")
        self.assertIsNone(self.lista.cabeza.siguiente)
    
    def test_eliminar_de_lista_vacia(self):
        """Prueba eliminar de una lista vacía."""
        # Esto no debería causar errores
        self.lista.eliminar_tarea("Cualquier tarea")
        
        # La lista debe seguir vacía
        self.assertIsNone(self.lista.cabeza)
    
    def test_fechas_diferentes_tareas(self):
        """Prueba que tareas creadas en momentos diferentes tienen fechas diferentes."""
        import time
        
        self.lista.agregar_tarea("Primera tarea")
        primera_fecha = self.lista.cabeza.fecha_creacion
        
        # Esperar un momento para asegurar diferencia en timestamp
        time.sleep(0.01)
        
        self.lista.agregar_tarea("Segunda tarea")
        segunda_fecha = self.lista.cabeza.siguiente.fecha_creacion
        
        # Las fechas deben ser diferentes
        self.assertNotEqual(primera_fecha, segunda_fecha)
        self.assertLess(primera_fecha, segunda_fecha)
    
    def test_fecha_persiste_operaciones(self):
        """Prueba que la fecha de creación persiste después de operaciones."""
        self.lista.agregar_tarea("Tarea persistente")
        fecha_original = self.lista.cabeza.fecha_creacion
        
        # Marcar como completada
        self.lista.marcar_completada("Tarea persistente")
        
        # La fecha debe seguir siendo la misma
        self.assertEqual(self.lista.cabeza.fecha_creacion, fecha_original)
        self.assertEqual(self.lista.cabeza.estado, "Completada")


if __name__ == '__main__':
    unittest.main()