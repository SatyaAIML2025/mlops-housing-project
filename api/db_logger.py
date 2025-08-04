import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("predictions.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            medinc REAL,
            houseage REAL,
            averooms REAL,
            avebedrms REAL,
            population REAL,
            aveoccup REAL,
            latitude REAL,
            longitude REAL,
            predicted_price REAL
        )
    """)
    conn.commit()
    conn.close()

def log_to_db(data: dict, prediction: float):
    conn = sqlite3.connect("predictions.db")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO logs (timestamp, medinc, houseage, averooms, avebedrms, population,
                          aveoccup, latitude, longitude, predicted_price)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().isoformat(),
        data['MedInc'],
        data['HouseAge'],
        data['AveRooms'],
        data['AveBedrms'],
        data['Population'],
        data['AveOccup'],
        data['Latitude'],
        data['Longitude'],
        prediction
    ))
    conn.commit()
    conn.close()
