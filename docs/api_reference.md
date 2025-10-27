# 🌐 Referencia de API

## Resumen

Este documento describe la API web del Gestor de Tareas, implementada con Flask.

## 🔗 Base URL

```
http://localhost:5000
```

## 📋 Endpoints Disponibles

### GET /
**Descripción**: Página principal que muestra todas las tareas

**Método**: `GET`

**Parámetros**: Ninguno

**Respuesta**: Página HTML con lista de tareas

**Código de respuesta**: 200 OK

**Ejemplo**:
```http
GET http://localhost:5000/
```

### POST /agregar
**Descripción**: Crear una nueva tarea

**Método**: `POST`

**Content-Type**: `application/x-www-form-urlencoded`

**Parámetros del formulario**:
- `descripcion` (requerido): Descripción de la tarea
- `descripcion_detallada` (opcional): Detalles adicionales

**Respuesta**: Redirección 302 a la página principal

**Ejemplo**:
```http
POST http://localhost:5000/agregar
Content-Type: application/x-www-form-urlencoded

descripcion=Compras supermercado&descripcion_detallada=verduras, pan, queso
```

### POST /completar/<descripcion_tarea>
**Descripción**: Marcar una tarea como completada

**Método**: `POST`

**Parámetros URL**:
- `descripcion_tarea`: Descripción exacta de la tarea (URL encoded)

**Respuesta**: Redirección 302 a la página principal

**Ejemplo**:
```http
POST http://localhost:5000/completar/Compras%20supermercado
```

### POST /eliminar/<descripcion_tarea>
**Descripción**: Eliminar una tarea de la lista

**Método**: `POST`

**Parámetros URL**:
- `descripcion_tarea`: Descripción exacta de la tarea (URL encoded)

**Respuesta**: Redirección 302 a la página principal

**Ejemplo**:
```http
POST http://localhost:5000/eliminar/Compras%20supermercado
```

## 📊 Estructura de Datos

### Objeto Tarea (Interno)
```python
{
    "descripcion": "Compras supermercado",
    "descripcion_detallada": "verduras, pan, queso",
    "estado": "Pendiente",  # o "Completada"
    "fecha_creacion": "27/10/2025 16:48:04",
    "fecha_corta": "27/10/2025"
}
```

## 🔧 Configuración del Servidor

### Modo Desarrollo
```python
app.run(debug=True, port=5000)
```

### Variables de Entorno
```bash
FLASK_APP=app.py
FLASK_ENV=development
```

## ⚠️ Consideraciones

### Limitaciones
- No hay autenticación
- Datos en memoria (se pierden al reiniciar)
- Una sola lista global de tareas
- No hay validación de entrada avanzada

### Codificación de URL
- Los espacios deben codificarse como `%20`
- Caracteres especiales deben estar URL encoded

### Manejo de Errores
- Tareas no encontradas: Mensaje de error en consola
- Formularios vacíos: Se ignoran silenciosamente
- Errores de servidor: Página de error de Flask

## 🧪 Testing de la API

### Con curl
```bash
# Agregar tarea
curl -X POST http://localhost:5000/agregar \
  -d "descripcion=Test tarea" \
  -d "descripcion_detallada=Detalles de prueba"

# Completar tarea
curl -X POST http://localhost:5000/completar/Test%20tarea

# Eliminar tarea
curl -X POST http://localhost:5000/eliminar/Test%20tarea
```

### Con navegador
- Usar las herramientas de desarrollador (F12)
- Inspeccionar formularios y requests
- Verificar redirecciones y respuestas

## 🚀 Extensiones Futuras

### API REST JSON
Posibles endpoints adicionales:
```
GET /api/tareas          # Listar tareas en JSON
POST /api/tareas         # Crear tarea (JSON)
PUT /api/tareas/{id}     # Actualizar tarea
DELETE /api/tareas/{id}  # Eliminar tarea
```

### Autenticación
- Sistema de usuarios
- Tokens de acceso
- Listas privadas por usuario