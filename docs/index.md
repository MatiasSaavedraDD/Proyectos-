# 📚 Documentación del Gestor de Tareas

Bienvenido a la documentación del **Gestor de Tareas con Lista Enlazada**.

## 📋 Descripción del Proyecto

Este proyecto es una implementación educativa de un gestor de tareas que utiliza:
- **Lista enlazada** implementada desde cero
- **Patrón MVC** (Modelo-Vista-Controlador)
- **Doble interfaz**: Consola y Web (Flask)
- **Testing completo** con casos de prueba

## 🎯 Objetivos Educativos

- Aprender estructuras de datos fundamentales
- Entender patrones de diseño
- Practicar desarrollo web básico
- Implementar testing unitario

## 🏗️ Arquitectura

### Modelo
- `NodoTarea`: Representa una tarea individual
- `ListaEnlazada`: Gestiona la colección de tareas

### Vista
- **Consola**: Interfaz de texto interactiva
- **Web**: Templates HTML con Tailwind CSS

### Controlador
- **Consola**: `ControladorApp` en `main.py`
- **Web**: Rutas Flask en `app.py`

## 📁 Estructura del Proyecto

```
gestor-tareas/
├── src/
│   ├── main.py              # Interfaz consola
│   └── mi_paquete/
│       ├── modelo_tareas.py # Lista enlazada
│       ├── app.py           # Aplicación Flask
│       └── templates/
│           └── index.html   # Template web
├── tests/
│   └── test_modelo1.py      # Tests unitarios
├── docs/                    # Documentación
├── requirements.txt         # Dependencias
└── README.md               # Documentación principal
```

## 🚀 Funcionalidades

- ✅ Agregar tareas con descripción y detalles
- 📅 Fecha y hora de creación automática
- 📋 Mostrar todas las tareas
- ✔️ Marcar tareas como completadas
- 🗑️ Eliminar tareas
- 🎨 Interfaz web moderna y responsive

## 📖 Documentación Disponible

- **[installation.md](installation.md)** - Guía de instalación paso a paso
- **[usage.md](usage.md)** - Manual de uso de ambas interfaces
- **[api_reference.md](api_reference.md)** - Referencia de la API web

## 🎓 Valor Educativo

Este proyecto enseña conceptos fundamentales de:
- Estructuras de datos (listas enlazadas)
- Patrones de diseño (MVC)
- Desarrollo web (Flask)
- Testing (unittest)
- Documentación técnica