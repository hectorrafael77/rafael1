from utils.estrategia_binance import estrategia_binance
import time
import traceback

while True:
    try:
        estrategia_binance("agresivo")
    except Exception as e:
        print("⚠️ Error en la ejecución:", e)
        traceback.print_exc()
    time.sleep(60)
