import sqlite3
from src.config import DATABASE_CONFIG

def save_analysis_to_db(symbol, analysis):
    """
    Sauvegarde l'analyse dans la base de données.
    """
    conn = sqlite3.connect(DATABASE_CONFIG["dbname"])
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT,
            analysis TEXT
        )
    """)
    cursor.execute("INSERT INTO analysis (symbol, analysis) VALUES (?, ?)", (symbol, str(analysis)))
    conn.commit()
    conn.close()