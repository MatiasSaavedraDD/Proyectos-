# VISTA - Presentación y generación de HTML
def generar_estilos_css():
    """Genera los estilos CSS para la aplicación."""
    return """
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
            font-style: italic;
        }
        
        .estadisticas {
            display: flex;
            justify-content: space-around;
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        
        .stat-item {
            text-align: center;
        }
        
        .stat-number {
            font-size: 2em;
            font-weight: bold;
            color: #007bff;
        }
        
        .stat-label {
            color: #666;
            font-size: 0.9em;
        }
        
        .form-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 30px;
        }
        
        .form-container h2 {
            margin-top: 0;
            color: white;
        }
        
        input, textarea {
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            border: none;
            border-radius: 6px;
            box-sizing: border-box;
            font-size: 16px;
        }
        
        .btn-primary {
            background-color: #28a745;
            color: white;
            border: none;
            cursor: pointer;
            padding: 12px 25px;
            border-radius: 6px;
            font-size: 16px;
            font-weight: bold;
            transition: background-color 0.3s;
        }
        
        .btn-primary:hover {
            background-color: #218838;
        }
        
        .tarea-card {
            border: 1px solid #e0e0e0;
            margin: 15px 0;
            padding: 20px;
            border-radius: 10px;
            background-color: #fafafa;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        
        .tarea-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        
        .tarea-completada {
            background-color: #d4edda;
            border-color: #c3e6cb;
        }
        
        .tarea-titulo {
            margin: 0 0 10px 0;
            font-size: 1.3em;
            font-weight: bold;
        }
        
        .tarea-pendiente {
            color: #856404;
        }
        
        .tarea-completada-texto {
            color: #155724;
            text-decoration: line-through;
        }
        
        .tarea-detalles {
            background-color: #e9ecef;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
            font-style: italic;
        }
        
        .tarea-fecha {
            color: #6c757d;
            font-size: 0.9em;
            margin: 10px 0;
        }
        
        .botones-accion {
            margin-top: 15px;
        }
        
        .btn-completar {
            background-color: #17a2b8;
            color: white;
            padding: 8px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-right: 10px;
            font-size: 14px;
        }
        
        .btn-completar:hover {
            background-color: #138496;
        }
        
        .btn-eliminar {
            background-color: #dc3545;
            color: white;
            padding: 8px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
        }
        
        .btn-eliminar:hover {
            background-color: #c82333;
        }
        
        .lista-vacia {
            text-align: center;
            color: #6c757d;
            font-style: italic;
            padding: 40px;
            background-color: #f8f9fa;
            border-radius: 10px;
        }
        
        .prioridades-stats {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        
        .prioridades-stats h3 {
            margin: 0 0 15px 0;
            color: #333;
            text-align: center;
        }
        
        .prioridades-container {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            gap: 10px;
        }
        
        .prioridad-item {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .prioridad-color {
            width: 20px;
            height: 20px;
            border-radius: 50%;
        }
        
        .prioridad-texto {
            font-weight: bold;
            color: #333;
        }
        
        .prioridad-selector {
            margin: 15px 0;
        }
        
        .prioridad-selector label {
            color: white;
        }
        
        .tarea-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 10px;
        }
        
        .prioridad-badge {
            flex-shrink: 0;
            margin-left: 10px;
        }
        
        .tarea-info {
            margin-bottom: 10px;
        }
        
        @media (max-width: 600px) {
            .estadisticas {
                flex-direction: column;
                gap: 10px;
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
                margin-top: 5px;
            }
            
            .container {
                padding: 20px;
            }
            
            h1 {
                font-size: 2em;
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
    """Genera el HTML del formulario para agregar tareas."""
    return """
    <div class="form-container">
        <h2>➕ Agregar Nueva Tarea</h2>
        <form method="POST" action="/agregar">
            <input type="text" name="descripcion" placeholder="¿Qué necesitas hacer?" required>
            <textarea name="descripcion_detallada" placeholder="Detalles adicionales (opcional)..." rows="3"></textarea>
            
            <div class="prioridad-selector">
                <label for="prioridad" style="display: block; margin-bottom: 5px; font-weight: bold;">Prioridad:</label>
                <select name="prioridad" id="prioridad" style="width: 100%; padding: 12px; border: none; border-radius: 6px; font-size: 16px;">
                    <option value="baja" style="color: #28a745;">🟢 Baja</option>
                    <option value="media" selected style="color: #ffc107;">🟡 Media</option>
                    <option value="alta" style="color: #dc3545;">🔴 Alta</option>
                </select>
            </div>
            
            <button type="submit" class="btn-primary">Crear Tarea</button>
        </form>
    </div>
    """

def generar_tarea_html(tarea, contador):
    """Genera el HTML para una tarea individual."""
    es_completada = tarea['estado'] == 'Completada'
    clase_card = 'tarea-card tarea-completada' if es_completada else 'tarea-card'
    clase_titulo = 'tarea-completada-texto' if es_completada else 'tarea-pendiente'
    
    # Obtener color y emoji de prioridad
    colores_prioridad = {
        'alta': {'color': '#dc3545', 'emoji': '🔴', 'texto': 'Alta'},
        'media': {'color': '#ffc107', 'emoji': '🟡', 'texto': 'Media'},
        'baja': {'color': '#28a745', 'emoji': '🟢', 'texto': 'Baja'}
    }
    
    prioridad_info = colores_prioridad.get(tarea['prioridad'], colores_prioridad['media'])
    
    html = f"""
    <div class="{clase_card}" style="border-left: 5px solid {prioridad_info['color']};">
        <div class="tarea-header">
            <h3 class="tarea-titulo {clase_titulo}">
                {contador}. {tarea['descripcion']}
            </h3>
            <div class="prioridad-badge" style="background-color: {prioridad_info['color']}; color: white; padding: 4px 8px; border-radius: 12px; font-size: 0.8em; font-weight: bold;">
                {prioridad_info['emoji']} {prioridad_info['texto']}
            </div>
        </div>
        
        <div class="tarea-info">
            <p><strong>Estado:</strong> 
                <span style="color: {'#28a745' if es_completada else '#ffc107'};">
                    {'✅ ' + tarea['estado'] if es_completada else '⏳ ' + tarea['estado']}
                </span>
            </p>
        </div>
    """
    
    if tarea['descripcion_detallada']:
        html += f"""
        <div class="tarea-detalles">
            📝 <strong>Detalles:</strong> {tarea['descripcion_detallada']}
        </div>
        """
    
    html += f"""
        <div class="tarea-fecha">
            📅 <strong>Creada:</strong> {tarea['fecha_creacion']}
        </div>
        
        <div class="botones-accion">
    """
    
    if not es_completada:
        html += f"""
            <form method="POST" action="/completar/{tarea['descripcion']}" style="display: inline;">
                <button type="submit" class="btn-completar">✓ Completar</button>
            </form>
        """
    
    html += f"""
            <form method="POST" action="/eliminar/{tarea['descripcion']}" style="display: inline;">
                <button type="submit" class="btn-eliminar">🗑️ Eliminar</button>
            </form>
        </div>
    </div>
    """
    
    return html

def generar_lista_tareas_html(tareas):
    """Genera el HTML para la lista completa de tareas."""
    if not tareas:
        return """
        <div class="lista-vacia">
            <h3>📝 No hay tareas</h3>
            <p>¡Agrega tu primera tarea usando el formulario de arriba!</p>
        </div>
        """
    
    html_tareas = ""
    for i, tarea in enumerate(tareas, 1):
        html_tareas += generar_tarea_html(tarea, i)
    
    return html_tareas

def generar_pagina_principal(tareas, estadisticas):
    """Genera la página HTML completa."""
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gestor de Tareas - Lista Enlazada MVC</title>
        {generar_estilos_css()}
    </head>
    <body>
        <div class="container">
            <h1>📋 Gestor de Tareas</h1>
            <p class="subtitle">Implementación MVC con Lista Enlazada</p>
            
            {generar_estadisticas_html(estadisticas)}
            
            {generar_formulario_html()}
            
            <h2>📋 Mis Tareas</h2>
            {generar_lista_tareas_html(tareas)}
        </div>
    </body>
    </html>
    """