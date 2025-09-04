from utils.binance_config import client
from utils.perfil_riesgo import obtener_porcentaje_operacion
from utils.auditoria import registrar_log
from utils.entorno_profetico import evaluar_entorno_profetico

def estrategia_binance(perfil):
    print("🚀 Estrategia Binance activada")
    
    entorno = evaluar_entorno_profetico()
    if entorno["estado"] == "alerta":
        print("⚠️ Alerta profética:", entorno["motivo"])
        registrar_log("jacoraf77@gmail.com", "no operó", entorno["motivo"], "suspendido por entorno profético")
        return

    porcentaje = obtener_porcentaje_operacion(perfil)
    balance = float(client.get_asset_balance(asset='USDT')['free'])
    monto_operar = balance * porcentaje

    orden = client.order_market_buy(
        symbol='BTCUSDT',
        quoteOrderQty=round(monto_operar, 2)
    )

    registrar_log("jacoraf77@gmail.com", "compra", f"perfil {perfil}, entorno OK", "ejecutado")
    print("✅ Orden ejecutada:", orden)
