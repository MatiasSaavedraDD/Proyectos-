# 📖 Manual de Uso

## 🎯 Introducción

El Gestor de Tareas ofrece dos interfaces para interactuar con tus tareas:
- **Interfaz de Consola**: Para uso en terminal
- **Interfaz Web**: Para uso en navegador

## 💻 Interfaz de Consola

### Iniciar la Aplicación
```bash
cd src
python main.py
```

### Menú Principal
```
--- MENÚ ---
1. Agregar nueva tarea
2. Mostrar todas las tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir
```

### 1. Agregar Nueva Tarea
```
Elige una opción: 1
📝 Ingresa la descripción de la nueva tarea: Compras supermercado
📋 Ingresa detalles adicionales (opcional, presiona Enter para omitir): verduras, pan, queso, leche

✅ Tarea 'Compras supermercado' agregada al final.
    📝 Detalles: verduras, pan, queso, leche
    📅 Creada el: 27/10/2025 16:48:04
```

### 2. Mostrar Todas las Tareas
```
Elige una opción: 2

--- LISTADO DE TAREAS ---
1. [Pendiente]     - Compras supermercado
    📝 Detalles: verduras, pan, queso, leche
    📅 Creada: 27/10/2025 16:48:04
2. [Completada]    - Estudiar para examen
    📝 Detalles: capítulos 3-5, ejercicios
    📅 Creada: 27/10/2025 15:30:15
-------------------------
```

### 3. Marcar Tarea como Completada
```
Elige una opción: 3
✅ Ingresa la descripción de la tarea a COMPLETAR: Compras supermercado

✅ Tarea 'Compras supermercado' marcada como COMPLETADA.
```

### 4. Eliminar Tarea
```
Elige una opción: 4
🗑️ Ingresa la descripción de la tarea a ELIMINAR: Compras supermercado

🗑️ Tarea 'Compras supermercado' eliminada.
```

## 🌐 Interfaz Web

### Iniciar la Aplicación Web
```bash
cd src/mi_paquete
python app.py
```

Abre tu navegador en: **http://127.0.0.1:5000**

### Agregar Nueva Tarea
1. En el formulario superior, escribe la descripción de la tarea
2. (Opcional) Agrega detalles en el área de texto
3. Haz clic en **"Añadir Tarea"**

### Ver Tareas
- Las tareas se muestran automáticamente en la página principal
- **Verde**: Tareas completadas
- **Amarillo**: Tareas pendientes
- Se muestra: descripción, detalles, fecha de creación y estado

### Marcar como Completada
- Haz clic en el botón **✓** (check) junto a la tarea
- Solo aparece en tareas pendientes

### Eliminar Tarea
- Haz clic en el botón **🗑️** (papelera) junto a la tarea
- Disponible para todas las tareas

## 📝 Ejemplos de Uso

### Ejemplo 1: Lista de Compras
```
Descripción: Compras supermercado
Detalles: verduras, pan, queso, leche, huevos, yogur
```

### Ejemplo 2: Tarea de Estudio
```
Descripción: Estudiar para examen de matemáticas
Detalles: capítulos 3-5, hacer ejercicios, repasar fórmulas
```

### Ejemplo 3: Tarea de Trabajo
```
Descripción: Reunión proyecto
Detalles: revisar presupuesto, discutir cronograma, asignar responsabilidades
```

### Ejemplo 4: Tarea Simple
```
Descripción: Llamar al médico
Detalles: (vacío - no es necesario)
```

## 🔍 Características Especiales

### Búsqueda Case-Insensitive
- Puedes escribir "compras supermercado" o "COMPRAS SUPERMERCADO"
- El sistema encontrará la tarea sin importar mayúsculas/minúsculas

### Fechas Automáticas
- Cada tarea registra automáticamente cuándo fue creada
- Formato: DD/MM/YYYY HH:MM:SS

### Descripción Detallada Opcional
- Puedes agregar información adicional a cualquier tarea
- Útil para listas de compras, pasos de procesos, etc.
- Completamente opcional

### Estados de Tareas
- **Pendiente**: Tarea recién creada
- **Completada**: Tarea marcada como terminada

## ⚠️ Limitaciones Actuales

### Persistencia
- Las tareas se almacenan en memoria
- Se pierden al cerrar la aplicación
- Cada interfaz (consola/web) mantiene su propia lista

### Búsqueda
- Solo por descripción exacta
- No hay filtros por fecha o estado

### Edición
- No se pueden editar tareas existentes
- Solo agregar, completar o eliminar

## 💡 Consejos de Uso

### Para Estudiantes
- Usa detalles para especificar capítulos, ejercicios, etc.
- Marca tareas completadas para seguir progreso

### Para Trabajo
- Incluye detalles de reuniones, deadlines, responsables
- Usa descripciones claras y específicas

### Para Uso Personal
- Listas de compras con productos específicos
- Tareas domésticas con pasos detallados
- Recordatorios con información adicional

## 🚀 Flujo de Trabajo Recomendado

1. **Planificar**: Crear tareas con descripciones claras
2. **Detallar**: Agregar información específica cuando sea útil
3. **Ejecutar**: Usar la interfaz que prefieras (consola/web)
4. **Completar**: Marcar tareas terminadas
5. **Limpiar**: Eliminar tareas obsoletas

## 🔄 Cambio entre Interfaces

Puedes usar ambas interfaces según tu preferencia:
- **Consola**: Rápida para usuarios de terminal
- **Web**: Visual y fácil de usar con mouse

**Nota**: Cada interfaz mantiene su propia lista de tareas independiente.