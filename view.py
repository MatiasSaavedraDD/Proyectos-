# VISTA - Presentación y generación de HTML
def generar_estilos_css():
    """Genera los estilos CSS para la aplicación basado en el index.html original."""
    return """
    <style>
        body { 
            font-family: 'Inter', sans-serif; 
            background-color: #f4f7f9; 
            padding: 1rem;
        }
        
        .max-w-3xl { 
            max-width: 48rem; 
            margin: 0 auto; 
        }
        
        .card { 
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1); 
            background-color: white;
            padding: 1.5rem;
            border-radius: 0.75rem;
            margin-bottom: 2rem;
        }
        
        .completed { 
            text-decoration: line-through; 
            color: #6b7280; 
        }
        
        /* Título principal */
        .text-4xl { 
            font-size: 2.25rem; 
            font-weight: bold; 
            color: #1d4ed8; 
            text-align: center;
            margin-bottom: 0.5rem;
        }
        
        .text-gray-600 { 
            color: #4b5563; 
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Estadísticas */
        .estadisticas {
            display: flex;
            justify-content: space-around;
            background-color: #f3f4f6;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1.5rem;
        }
        
        .stat-item {
            text-align: center;
        }
        
        .stat-number {
            font-size: 1.5rem;
            font-weight: bold;
            color: #1d4ed8;
        }
        
        .stat-label {
            color: #6b7280;
            font-size: 0.875rem;
        }
        
        .prioridades-stats {
            background-color: #f3f4f6;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1.5rem;
        }
        
        .prioridades-stats h3 {
            margin: 0 0 1rem 0;
            color: #374151;
            text-align: center;
            font-size: 1.125rem;
        }
        
        .prioridades-container {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        
        .prioridad-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .prioridad-color {
            width: 16px;
            height: 16px;
            border-radius: 50%;
        }
        
        .prioridad-texto {
            font-weight: 600;
            color: #374151;
            font-size: 0.875rem;
        }
        
        /* Formulario */
        .text-2xl { 
            font-size: 1.5rem; 
            font-weight: 600; 
            margin-bottom: 1rem; 
            color: #374151;
        }
        
        .flex { 
            display: flex; 
        }
        
        .flex-col { 
            flex-direction: column; 
        }
        
        .space-y-3 > * + * { 
            margin-top: 0.75rem; 
        }
        
        .flex-grow { 
            flex-grow: 1; 
        }
        
        input[type="text"], textarea, select { 
            padding: 0.75rem; 
            border: 1px solid #d1d5db; 
            border-radius: 0.5rem; 
            width: 100%;
            box-sizing: border-box;
            font-size: 1rem;
        }
        
        input[type="text"]:focus, textarea:focus, select:focus { 
            outline: none;
            border-color: #3b82f6; 
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
        }
        
        textarea {
            resize: vertical;
            min-height: 80px;
        }
        
        .prioridad-selector {
            margin: 0.75rem 0;
        }
        
        .prioridad-selector label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: #374151;
        }
        
        .bg-green-600 { 
            background-color: #16a34a; 
            color: white; 
            font-weight: bold; 
            padding: 0.75rem 1.5rem; 
            border-radius: 0.5rem; 
            border: none;
            cursor: pointer;
            transition: background-color 0.15s ease-in-out;
        }
        
        .bg-green-600:hover { 
            background-color: #15803d; 
        }
        
        /* Lista de tareas */
        .tarea-item {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            padding: 0.75rem;
            margin: 0.5rem 0;
            border-bottom: 1px solid #e5e7eb;
            border-radius: 0.375rem;
            transition: background-color 0.15s ease-in-out;
        }
        
        .tarea-item:last-child {
            border-bottom: none;
        }
        
        .tarea-item:hover {
            background-color: #f9fafb;
        }
        
        .tarea-completada-bg {
            background-color: rgba(34, 197, 94, 0.1);
        }
        
        .tarea-content {
            flex: 1;
            margin-right: 1rem;
        }
        
        .tarea-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 0.5rem;
        }
        
        .tarea-titulo {
            font-size: 1.125rem;
            font-weight: 500;
            margin: 0;
            flex: 1;
        }
        
        .prioridad-badge {
            background-color: #374151;
            color: white;
            padding: 0.25rem 0.5rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 600;
            margin-left: 0.5rem;
            flex-shrink: 0;
        }
        
        .tarea-detalles {
            background-color: #f3f4f6;
            padding: 0.5rem;
            border-radius: 0.375rem;
            margin: 0.5rem 0;
            font-style: italic;
            color: #4b5563;
            border-left: 4px solid #3b82f6;
        }
        
        .tarea-fecha {
            color: #6b7280;
            font-size: 0.875rem;
            margin-top: 0.5rem;
        }
        
        .estado-badge {
            font-size: 0.875rem;
            font-weight: 600;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            margin-right: 1rem;
            width: 7rem;
            text-align: center;
        }
        
        .bg-green-200 {
            background-color: #bbf7d0;
            color: #166534;
        }
        
        .bg-yellow-200 {
            background-color: #fef3c7;
            color: #92400e;
        }
        
        /* Botones de acción */
        .botones-accion {
            display: flex;
            gap: 0.5rem;
        }
        
        .btn-accion {
            padding: 0.5rem;
            border: none;
            border-radius: 0.5rem;
            cursor: pointer;
            transition: background-color 0.15s ease-in-out;
        }
        
        .bg-blue-500 {
            background-color: #3b82f6;
            color: white;
        }
        
        .bg-blue-500:hover {
            background-color: #2563eb;
        }
        
        .bg-red-500 {
            background-color: #ef4444;
            color: white;
        }
        
        .bg-red-500:hover {
            background-color: #dc2626;
        }
        
        /* Lista vacía */
        .lista-vacia {
            text-align: center;
            color: #6b7280;
            padding: 2.5rem 1rem;
        }
        
        /* Responsive */
        @media (max-width: 640px) {
            body {
                padding: 0.5rem;
            }
            
            .card {
                padding: 1rem;
            }
            
            .text-4xl {
                font-size: 1.875rem;
            }
            
            .estadisticas {
                flex-direction: column;
                gap: 0.75rem;
            }
            
            .prioridades-container {
                flex-direction: column;
                align-items: center;
            }
            
            .tarea-header {
                flex-direction: column;
                align-items: flex-start;
            }
            
            .prioridad-badge {
                margin-left: 0;
                margin-top: 0.25rem;
            }
            
            .tarea-item {
                flex-direction: column;
                align-items: stretch;
            }
            
            .botones-accion {
                margin-top: 0.75rem;
                justify-content: flex-start;
            }
        }
    </style>
    """

def generar_estadisticas_html(estadisticas):
    """Genera el HTML para mostrar las estadísticas."""
    return f"""
    <div class="estadisticas">
        <div class="stat-item">
            <div class="stat-number">{estadisticas['total']}</div>
            <div class="stat-label">Total</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">{estadisticas['pendientes']}</div>
            <div class="stat-label">Pendientes</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">{estadisticas['completadas']}</div>
            <div class="stat-label">Completadas</div>
        </div>
    </div>
    
    <div class="prioridades-stats">
        <h3>📊 Por Prioridad</h3>
        <div class="prioridades-container">
            <div class="prioridad-item">
                <div class="prioridad-color" style="background-color: #dc3545;"></div>
                <span class="prioridad-texto">Alta: {estadisticas['prioridades']['alta']}</span>
            </div>
            <div class="prioridad-item">
                <div class="prioridad-color" style="background-color: #ffc107;"></div>
                <span class="prioridad-texto">Media: {estadisticas['prioridades']['media']}</span>
            </div>
            <div class="prioridad-item">
                <div class="prioridad-color" style="background-color: #28a745;"></div>
                <span class="prioridad-texto">Baja: {estadisticas['prioridades']['baja']}</span>
            </div>
        </div>
    </div>
    """

def generar_formulario_html():
    """Genera el HTML del formulario para agregar tareas basado en el estilo original."""
    return """
    <div class="card">
        <h2 class="text-2xl">Agregar Nueva Tarea</h2>
        <form method="POST" action="/agregar" class="space-y-3">
            <div class="flex flex-col space-y-3">
                <input type="text" name="descripcion" placeholder="Escribe la descripción de la tarea..." required>
                <button type="submit" class="bg-green-600">
                    Añadir Tarea
                </button>
            </div>
            <textarea name="descripcion_detallada" placeholder="Detalles adicionales (opcional): ej. verduras, pan, queso..." rows="2"></textarea>
            
            <div class="prioridad-selector">
                <label for="prioridad">Prioridad:</label>
                <select name="prioridad" id="prioridad">
                    <option value="baja">🟢 Baja</option>
                    <option value="media" selected>🟡 Media</option>
                    <option value="alta">🔴 Alta</option>
                </select>
            </div>
        </form>
    </div>
    """

def generar_tarea_html(tarea, contador):
    """Genera el HTML para una tarea individual basado en el estilo original."""
    es_completada = tarea['estado'] == 'Completada'
    clase_item = 'tarea-item tarea-completada-bg' if es_completada else 'tarea-item'
    clase_titulo = 'completed' if es_completada else ''
    
    # Obtener color y emoji de prioridad
    colores_prioridad = {
        'alta': {'color': '#dc3545', 'emoji': '🔴', 'texto': 'Alta'},
        'media': {'color': '#ffc107', 'emoji': '🟡', 'texto': 'Media'},
        'baja': {'color': '#28a745', 'emoji': '🟢', 'texto': 'Baja'}
    }
    
    prioridad_info = colores_prioridad.get(tarea['prioridad'], colores_prioridad['media'])
    
    html = f"""
    <div class="{clase_item}">
        <div class="tarea-content">
            <div class="tarea-header">
                <span class="tarea-titulo {clase_titulo}">
                    {contador}. {tarea['descripcion']}
                </span>
                <div class="prioridad-badge" style="background-color: {prioridad_info['color']};">
                    {prioridad_info['emoji']} {prioridad_info['texto']}
                </div>
            </div>
    """
    
    if tarea['descripcion_detallada']:
        html += f"""
            <div class="tarea-detalles">
                📝 {tarea['descripcion_detallada']}
            </div>
        """
    
    html += f"""
            <div class="tarea-fecha">
                📅 Creada: {tarea['fecha_creacion']}
            </div>
        </div>
        
        <span class="estado-badge {'bg-green-200' if es_completada else 'bg-yellow-200'}">
            {tarea['estado']}
        </span>

        <div class="botones-accion">
    """
    
    if not es_completada:
        html += f"""
            <form method="POST" action="/completar/{tarea['descripcion']}" style="display: inline;">
                <button type="submit" class="btn-accion bg-blue-500" title="Marcar como Completada">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                        <path d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.078 3.097 5.494-5.485z"/>
                    </svg>
                </button>
            </form>
        """
    
    html += f"""
            <form method="POST" action="/eliminar/{tarea['descripcion']}" style="display: inline;">
                <button type="submit" class="btn-accion bg-red-500" title="Eliminar Tarea">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                        <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                        <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                    </svg>
                </button>
            </form>
        </div>
    </div>
    """
    
    return html

def generar_lista_tareas_html(tareas):
    """Genera el HTML para la lista completa de tareas basado en el estilo original."""
    if not tareas:
        return """
        <div class="lista-vacia">
            <p>¡No hay tareas en la lista! Agrega una arriba.</p>
        </div>
        """
    
    html_tareas = ""
    for i, tarea in enumerate(tareas, 1):
        html_tareas += generar_tarea_html(tarea, i)
    
    return html_tareas

def generar_pagina_principal(tareas, estadisticas):
    """Genera la página HTML completa basada en el estilo del index.html original."""
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Proyecto ED - Lista de Tareas Web</title>
        <script src="https://cdn.tailwindcss.com"></script>
        {generar_estilos_css()}
    </head>
    <body class="p-4 md:p-8">
        <div class="max-w-3xl">
            <!-- TÍTULO Y CABECERA -->
            <header class="text-center mb-8">
                <h1 class="text-4xl">📋 Lista de Tareas (Web MVC)</h1>
                <p class="text-gray-600 mt-2">Implementación de Estructura de Datos: Lista Enlazada con Prioridades</p>
            </header>

            <!-- ESTADÍSTICAS -->
            {generar_estadisticas_html(estadisticas)}

            <!-- AÑADIR NUEVA TAREA (FORMULARIO) -->
            {generar_formulario_html()}

            <!-- LISTA DE TAREAS -->
            <div class="card">
                <h2 class="text-2xl">Tareas Pendientes y Completadas</h2>
                
                {generar_lista_tareas_html(tareas)}
            </div>
        </div>
    </body>
    </html>
    """