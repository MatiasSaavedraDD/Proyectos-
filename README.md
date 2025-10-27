# 📋 Gestor de Tareas - Lista Enlazada

Un proyecto educativo que implementa un gestor de tareas usando **estructuras de datos** (lista enlazada) y el patrón **MVC (Modelo-Vista-Controlador)** con dos interfaces: consola y web.

## 🎯 Propósito Educativo

Este proyecto demuestra:

- Implementación manual de **lista enlazada** desde cero
- Aplicación del patrón **MVC**
- Desarrollo de interfaces múltiples (consola y web)
- Uso de **Flask** para aplicaciones web
- Buenas prácticas de programación en Python

## 🏗️ Estructura del Proyecto

```
mi-proyecto/
├── src/
│   ├── main.py                 # Interfaz de consola (Controlador)
│   └── mi_paquete/
│       ├── __init__.py         # Inicializador del paquete
│       ├── modelo_tareas.py    # Modelo (Lista Enlazada)
│       ├── app.py              # Aplicación Flask (Controlador Web)
│       └── templates/
│           └── index.html      # Vista web
├── tests/                      # Pruebas unitarias
├── .venv/                      # Entorno virtual
├── requirements.txt            # Dependencias
└── README.md                   # Este archivo
```

## 🚀 Instalación y Uso

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd mi-proyecto
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
```

### 3. Activar entorno virtual

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/Mac:**

```bash
source .venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 💻 Ejecución

### Interfaz de Consola

```bash
cd src
python main.py
```

### Interfaz Web

```bash
cd src/mi_paquete
python app.py
```

Luego abrir: http://127.0.0.1:5000

## 🔧 Funcionalidades

- ✅ **Agregar tareas** con descripción y detalles adicionales
- 📝 **Descripción detallada** opcional para información adicional (ej: "verduras, pan, queso")
- 📅 **Fecha y hora de creación** automática para cada tarea
- 📋 **Mostrar todas las tareas** con su estado, detalles y fecha de creación
- ✔️ **Marcar tareas como completadas**
- 🗑️ **Eliminar tareas** de la lista
- 🎨 **Interfaz web moderna** con Tailwind CSS
- 📱 **Diseño responsive** para móviles

## 🧠 Conceptos Implementados

### Estructura de Datos

- **Lista Enlazada Simple**: Implementación manual con nodos
- **Operaciones CRUD**: Create, Read, Update, Delete
- **Traversal**: Recorrido secuencial de nodos

### Patrón MVC

- **Modelo**: `ListaEnlazada` y `NodoTarea` (modelo_tareas.py)
- **Vista**: Consola (main.py) y HTML (index.html)
- **Controlador**: `ControladorApp` y rutas Flask

## 🎓 Uso Educativo

Este proyecto es ideal para:

- Estudiantes de **Estructuras de Datos**
- Aprendizaje de **patrones de diseño**
- Introducción a **desarrollo web con Flask**
- Práctica de **programación orientada a objetos**

## 🤝 Contribuciones

Este es un proyecto educativo. Las mejoras sugeridas incluyen:

- Persistencia en base de datos
- Tests unitarios
- Validación de datos
- Autenticación de usuarios
- API REST

## 📄 Licencia

Proyecto educativo de código abierto.
