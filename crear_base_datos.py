"""Crear una base SQLite con dos tablas relacionadas a partir de ai4i2020.csv.

Uso:
    python crear_base_datos.py

Archivos generados:
    mantenimiento_industrial.db
    mantenimiento_industrial.sql
"""
from pathlib import Path
import sqlite3
import pandas as pd

BASE = Path(__file__).resolve().parent
CSV = BASE / "ai4i2020.csv"
DB = BASE / "mantenimiento_industrial.db"
SQL = BASE / "mantenimiento_industrial.sql"

if not CSV.exists():
    raise FileNotFoundError(f"No se encontró el CSV original: {CSV}")

df = pd.read_csv(CSV)
maquinas = df[["UDI", "Product ID", "Type"]].copy()
maquinas.columns = ["UDI", "product_id", "tipo"]

operaciones = df[[
    "UDI", "Air temperature [K]", "Process temperature [K]",
    "Rotational speed [rpm]", "Torque [Nm]", "Tool wear [min]",
    "Machine failure", "TWF", "HDF", "PWF", "OSF", "RNF"
]].copy()
operaciones.columns = [
    "UDI", "temperatura_aire", "temperatura_proceso",
    "velocidad_rotacion", "torque", "desgaste_herramienta",
    "falla_maquina", "twf", "hdf", "pwf", "osf", "rnf"
]

with sqlite3.connect(DB) as con:
    con.execute("PRAGMA foreign_keys = ON")
    con.executescript("""
        DROP TABLE IF EXISTS operaciones;
        DROP TABLE IF EXISTS maquinas;
        CREATE TABLE maquinas (
            UDI INTEGER PRIMARY KEY,
            product_id TEXT NOT NULL,
            tipo TEXT NOT NULL
        );
        CREATE TABLE operaciones (
            UDI INTEGER PRIMARY KEY,
            temperatura_aire REAL,
            temperatura_proceso REAL,
            velocidad_rotacion INTEGER,
            torque REAL,
            desgaste_herramienta INTEGER,
            falla_maquina INTEGER,
            twf INTEGER,
            hdf INTEGER,
            pwf INTEGER,
            osf INTEGER,
            rnf INTEGER,
            FOREIGN KEY (UDI) REFERENCES maquinas(UDI)
        );
    """)
    maquinas.to_sql("maquinas", con, if_exists="append", index=False)
    operaciones.to_sql("operaciones", con, if_exists="append", index=False)
    con.commit()
    with SQL.open("w", encoding="utf-8") as f:
        for line in con.iterdump():
            f.write(line + "\n")
    print("Tablas creadas correctamente.")
    print("Maquinas:", con.execute("SELECT COUNT(*) FROM maquinas").fetchone()[0])
    print("Operaciones:", con.execute("SELECT COUNT(*) FROM operaciones").fetchone()[0])
    print("SQL:", SQL)
    print("SQLite:", DB)
