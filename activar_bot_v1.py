from utils.estrategia_binance import estrategia_binance
import time

while True:
    estrategia_binance("agresivo")
    time.sleep(60)
