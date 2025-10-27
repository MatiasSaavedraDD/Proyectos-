# 📋 Gestor de Tareas - Lista Enlazada


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

