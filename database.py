
import sqlite3, hashlib
DB = "hydrosentinel.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        email TEXT PRIMARY KEY, password_hash TEXT, name TEXT, 
        water_credits INTEGER DEFAULT 100,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS sensor_logs (
        id INTEGER PRIMARY KEY, location TEXT, ph REAL, turbidity REAL, flow REAL, temp REAL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()
    conn.close()

def hash_pw(pw): return hashlib.sha256(pw.encode()).hexdigest()

def create_user(email, pw, name=""):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO users (email, password_hash, name) VALUES (?,?,?)", (email, hash_pw(pw), name))
    conn.commit(); conn.close()

def get_user(email):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT email, password_hash, name, water_credits FROM users WHERE email=?", (email,))
    row = c.fetchone(); conn.close()
    if row: return {"email": row[0], "password_hash": row[1], "name": row[2], "credits": row[3]}
    return None

def verify_password(pw, hash_val): return hash_pw(pw) == hash_val
