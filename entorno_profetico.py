def evaluar_entorno_profetico():
    eventos_clave = {
        "septiembre_2025": "inicio de nuevo ciclo en Israel",
        "riesgo_profetico": "alto"
    }

    if eventos_clave["riesgo_profetico"] == "alto":
        return {
            "estado": "alerta",
            "motivo": eventos_clave["septiembre_2025"]
        }
    else:
        return {
            "estado": "normal",
            "motivo": "sin señales proféticas relevantes"
        }
