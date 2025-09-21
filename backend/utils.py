import sqlite3
from backend.models import DB_PATH

# --- Appointment helpers ---
def add_appointment(patient_name, doctor, datetime, email):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO appointments (patient_name, doctor, datetime, email)
        VALUES (?, ?, ?, ?)
    ''', (patient_name, doctor, datetime, email))
    conn.commit()
    conn.close()

def get_appointments():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM appointments')
    results = cursor.fetchall()
    conn.close()
    return results

def update_appointment_status(appointment_id, status):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE appointments
        SET status = ?
        WHERE id = ?
    ''', (status, appointment_id))
    conn.commit()
    conn.close()

# --- FAQ helpers ---
def log_faq(question, answer):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO faq_logs (question, answer)
        VALUES (?, ?)
    ''', (question, answer))
    conn.commit()
    conn.close()
