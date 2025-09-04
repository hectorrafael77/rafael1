from pymongo import MongoClient
from datetime import datetime

def registrar_log(email, accion, motivo, resultado):
    try:
        client = MongoClient("mongodb+srv://jacoraf77_db_user:19733Teamo217847%3F@cluster0.plre4nh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db = client.tradingApp
        log = {
            "email": email,
            "accion": accion,
            "motivo": motivo,
            "resultado": resultado,
            "fecha": datetime.now()
        }
        db.logs.insert_one(log)
        print("✅ Log registrado en MongoDB")
    except Exception as e:
        print("❌ Error al registrar log:", str(e))
