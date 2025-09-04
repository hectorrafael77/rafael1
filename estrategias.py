from utils.auditoria import registrar_log

def estrategia_1():
    print("🤖 Bot de trading activado")
    email = "jacoraf77@gmail.com"
    accion = "compra"
    motivo = "señal de indicador"
    resultado = "ejecutado"

    registrar_log(email, accion, motivo, resultado)
