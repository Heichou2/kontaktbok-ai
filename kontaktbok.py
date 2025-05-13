# Prompt 1 - Skapa databasmodell för kontakt med flera mail och telefonnummer
import sqlite3

def skapa_tabeller():
    conn = sqlite3.connect("kontakter.db")
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS kontakt (
            id INTEGER PRIMARY KEY,
            namn TEXT NOT NULL
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS telefonnummer (
            id INTEGER PRIMARY KEY,
            kontakt_id INTEGER,
            nummer TEXT,
            FOREIGN KEY (kontakt_id) REFERENCES kontakt(id)
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS epost (
            id INTEGER PRIMARY KEY,
            kontakt_id INTEGER,
            adress TEXT,
            FOREIGN KEY (kontakt_id) REFERENCES kontakt(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    skapa_tabeller()
    print("Databas skapad.")
