# 📋 Gestor de Tareas - Patrón MVC con Lista Enlazada

Un proyecto educativo que implementa un gestor de tareas web usando **estructuras de datos** (lista enlazada) y el **patrón MVC (Modelo-Vista-Controlador)** correctamente separado.

## 🎯 Propósito Educativo

Este proyecto demuestra:
- Implementación manual de **lista enlazada** desde cero
- Aplicación correcta del **patrón MVC** con separación clara
- **Modelo**: Lógica de datos pura sin interfaz
- **Vista**: Generación de HTML y presentación
- **Controlador**: Coordinación y lógica de aplicación
- Desarrollo web con **Flask**
- Buenas prácticas de programación en Python

## 🏗️ Arquitectura MVC

### 📊 **MODELO** (`model.py`)
- **Responsabilidad**: Gestión de datos y lógica de negocio
- **Clases**: `NodoTarea`, `ListaEnlazada`
- **Características**:
  - Sin dependencias de interfaz de usuario
  - Operaciones CRUD puras
  - Retorna datos, no los presenta
  - Lista enlazada implementada manualmente

### 🎨 **VISTA** (`view.py`)
- **Responsabilidad**: Presentación y generación de HTML
- **Funciones**: Generación de CSS, HTML, formularios
- **Características**:
  - Solo se encarga de la presentación
  - Recibe datos del controlador
  - Genera HTML dinámico
  - Diseño responsive y moderno

### 🎮 **CONTROLADOR** (`controller.py`)
- **Responsabilidad**: Lógica de aplicación y coordinación
- **Clases**: `ControladorTareas`
- **Características**:
  - Coordina Modelo y Vista
  - Maneja rutas Flask
  - Procesa entrada del usuario
  - Gestiona el flujo de la aplicación

## 🏗️ Estructura del Proyecto

```
mi-proyecto/
├── model.py                    # 📊 MODELO - Lista enlazada y lógica de datos
├── view.py                     # 🎨 VISTA - Generación de HTML y CSS
├── controller.py               # 🎮 CONTROLADOR - Rutas Flask y coordinación
├── requirements.txt            # 📦 Dependencias
├── .gitignore                  # 🚫 Archivos ignorados
└── README.md                   # 📖 Este archivo
```

## 🚀 Instalación y Uso

### 1. Crear entorno virtual
```bash
python -m venv .venv
```

### 2. Activar entorno virtual
**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
python controller.py
```

### 5. Abrir en navegador
```
http://127.0.0.1:5000
```

## 🔧 Funcionalidades

- ✅ **Agregar tareas** con descripción y detalles opcionales
- 🎯 **Sistema de prioridades** con colores visuales:
  - 🔴 **Alta prioridad** (Rojo)
  - 🟡 **Media prioridad** (Amarillo) 
  - 🟢 **Baja prioridad** (Verde)
- 📊 **Estadísticas** en tiempo real (total, pendientes, completadas, por prioridad)
- 📋 **Visualizar tareas** con estado, prioridad y fecha de creación
- ✔️ **Marcar tareas como completadas**
- 🗑️ **Eliminar tareas** de la lista
- 🎨 **Interfaz moderna** con diseño responsive
- 📱 **Compatible con móviles**

## 🧠 Conceptos Implementados

### Estructura de Datos
- **Lista Enlazada Simple**: Implementación manual con nodos
- **Operaciones CRUD**: Create, Read, Update, Delete
- **Complejidad**: O(n) para búsqueda, inserción y eliminación
- **Gestión de memoria**: Dinámica según necesidades

### Patrón MVC
- **Separación clara**: Cada componente tiene responsabilidades específicas
- **Bajo acoplamiento**: Componentes independientes
- **Alta cohesión**: Funcionalidades relacionadas agrupadas
- **Mantenibilidad**: Fácil modificar sin afectar otros componentes

### Desarrollo Web
- **Flask**: Framework web minimalista
- **Rutas HTTP**: GET y POST para diferentes operaciones
- **Templates dinámicos**: Generación de HTML con datos del modelo
- **Responsive design**: Adaptable a diferentes dispositivos

## 🎓 Valor Educativo

### Para Estudiantes de Estructuras de Datos:
- Implementación práctica de lista enlazada
- Operaciones fundamentales en estructuras lineales
- Gestión manual de punteros y memoria

### Para Estudiantes de Ingeniería de Software:
- Aplicación correcta del patrón MVC
- Separación de responsabilidades
- Arquitectura de software escalable

### Para Estudiantes de Desarrollo Web:
- Framework Flask básico
- Manejo de formularios HTML
- Generación dinámica de contenido

## 🔍 Detalles Técnicos

### Modelo (model.py)
- `NodoTarea`: Estructura de datos individual
- `ListaEnlazada`: Colección con operaciones CRUD
- Métodos puros sin efectos secundarios de UI

### Vista (view.py)
- Funciones de generación de HTML
- CSS integrado para estilos
- Componentes reutilizables

### Controlador (controller.py)
- Clase `ControladorTareas` para lógica de aplicación
- Rutas Flask para endpoints web
- Coordinación entre modelo y vista

## 🤝 Contribuciones

Este proyecto educativo puede extenderse con:
- Persistencia en base de datos
- Autenticación de usuarios
- API REST
- Tests unitarios
- Validación avanzada de datos

## 📄 Licencia

Proyecto educativo de código abierto para fines académicos.