def obtener_porcentaje_operacion(perfil):
    """
    Devuelve el porcentaje de capital a operar según el perfil de riesgo.
    """
    perfiles = {
        "conservador": 0.5,
        "moderado": 0.75,
        "agresivo": 1.0
    }

    return perfiles.get(perfil.lower(), 0.5)  # Por defecto: conservador
