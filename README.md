# 📋 Gestor de Tareas - Patrón MVC con Lista Enlazada

Un proyecto educativo que implementa un gestor de tareas web usando **estructuras de datos** (lista enlazada) y el **patrón MVC (Modelo-Vista-Controlador)** correctamente separado.

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


### 1. Activar entorno virtual
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

