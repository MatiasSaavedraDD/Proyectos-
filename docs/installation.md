# 🛠️ Guía de Instalación

## Prerrequisitos

- **Python 3.8 o superior**
- **pip** (gestor de paquetes de Python)
- **Git** (opcional, para clonar el repositorio)

### Verificar Python
```bash
python --version
# Debe mostrar Python 3.8 o superior
```

## 📥 Instalación

### Paso 1: Obtener el Proyecto
```bash
# Opción A: Clonar repositorio (si está en Git)
git clone <url-del-repositorio>
cd gestor-tareas

# Opción B: Descargar y extraer ZIP
# Descargar el archivo ZIP y extraer
cd gestor-tareas
```

### Paso 2: Crear Entorno Virtual
```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# En Windows:
.venv\Scripts\activate

# En Linux/Mac:
source .venv/bin/activate
```

### Paso 3: Instalar Dependencias
```bash
# Instalar dependencias del proyecto
pip install -r requirements.txt

# Verificar instalación
pip list
```

## 🔧 Configuración

### Estructura de Archivos
Asegúrate de que la estructura sea:
```
gestor-tareas/
├── src/
│   ├── main.py
│   └── mi_paquete/
│       ├── __init__.py
│       ├── modelo_tareas.py
│       ├── app.py
│       └── templates/
│           └── index.html
├── tests/
├── docs/
├── requirements.txt
└── README.md
```

### Variables de Entorno (Opcional)
Para la aplicación web:
```bash
# Windows
set FLASK_APP=app.py
set FLASK_ENV=development

# Linux/Mac
export FLASK_APP=app.py
export FLASK_ENV=development
```

## ✅ Verificación de Instalación

### Test 1: Interfaz de Consola
```bash
cd src
python main.py
```
Deberías ver el menú del gestor de tareas.

### Test 2: Interfaz Web
```bash
cd src/mi_paquete
python app.py
```
Abre http://127.0.0.1:5000 en tu navegador.

### Test 3: Tests Unitarios
```bash
cd tests
python test_modelo1.py
```
Todos los tests deben pasar (OK).

## 🚨 Solución de Problemas Comunes

### Error: "ModuleNotFoundError"
```bash
# Asegúrate de estar en el directorio correcto
cd src
python main.py

# O agregar al PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
```

### Error: "No module named 'flask'"
```bash
# Activar entorno virtual
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Reinstalar dependencias
pip install -r requirements.txt
```

### Error: "Address already in use" (Puerto ocupado)
```bash
# Cambiar puerto en app.py
app.run(debug=True, port=5001)
```

## 🔄 Reinstalación Limpia

Si hay problemas, reinstalación completa:
```bash
# 1. Eliminar entorno virtual
rm -rf .venv  # Linux/Mac
rmdir /s .venv  # Windows

# 2. Crear nuevo entorno
python -m venv .venv

# 3. Activar
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# 4. Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt
```

## 📋 Dependencias del Proyecto

### Principales
- **Flask 2.3.3** - Framework web
- **Werkzeug 2.3.7** - Utilidades WSGI
- **Jinja2 3.1.2** - Motor de templates

### Desarrollo (Opcionales)
- **pytest** - Framework de testing
- **black** - Formateo de código
- **flake8** - Linting

## 🎯 Próximos Pasos

Una vez instalado correctamente:
1. Lee **[usage.md](usage.md)** para aprender a usar el sistema
2. Consulta **[api_reference.md](api_reference.md)** para la API web
3. Explora el código fuente para entender la implementación