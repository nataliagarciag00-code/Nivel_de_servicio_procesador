import sqlite3
import pandas as pd
from datetime import datetime

from db import init_db, guardar_ejecucion, leer_historico
init_db()


DB_NAME = "historico.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS ejecuciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT,
            fecha TEXT,
            ns_llegada REAL,
            ns_salida REAL,
            total_viajes INTEGER
        )
    """)

    conn.commit()
    conn.close()

def guardar_ejecucion(usuario, ns_llegada, ns_salida, total_viajes):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        INSERT INTO ejecuciones (usuario, fecha, ns_llegada, ns_salida, total_viajes)
        VALUES (?, ?, ?, ?, ?)
    """, (
        usuario,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        ns_llegada,
        ns_salida,
        total_viajes
    ))

    conn.commit()
    conn.close()

def leer_historico():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql("SELECT * FROM ejecuciones ORDER BY fecha DESC", conn)
    conn.close()
    return df
