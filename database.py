import psycopg2
import hashlib
import datetime

conn_params = {
    "host": "localhost",
    "port": "5432",
    "database": "postgres",
    "user": "postgres",
    "password": "postgres",
}

def list_users():
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()

    cur.execute("SELECT id FROM users;")
    result = [x[0] for x in cur.fetchall()]

    conn.close()

    return result

def verify(id, pw):
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()

    cur.execute("SELECT pw FROM users WHERE id = %s;", (id,))
    result = cur.fetchone()[0] == hashlib.sha256(pw.encode()).hexdigest()

    conn.close()

    return result

def delete_user_from_db(id):
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()

    cur.execute("DELETE FROM users WHERE id = %s;", (id,))
    conn.commit()

    cur.execute("DELETE FROM notes WHERE user = %s;", (id,))
    conn.commit()

    cur.execute("DELETE FROM images WHERE owner = %s;", (id,))
    conn.commit()

    conn.close()

def add_user(id, pw):
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()

    cur.execute("INSERT INTO users (id, pw) VALUES (%s, %s);", (id.upper(), hashlib.sha256(pw.encode()).hexdigest()))
    conn.commit()

    conn.close()

def read_note_from_db(id):
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()

    command = "SELECT note_id, timestamp, note FROM notes WHERE user = %s;"
    cur.execute(command, (id.upper(),))
    result = cur.fetchall()

    conn.close()

    return result

def match_user_id_with_note_id(note_id):
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()

    command = "SELECT user FROM notes WHERE note_id = %s;"
    cur.execute(command, (note_id,))
    result = cur.fetchone()[0]

    conn.close()

    return result

def write_note_into_db(id, note_to_write):
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()

    current_timestamp = str(datetime.datetime.now())
    cur.execute(
        "INSERT INTO notes (user, timestamp, note, note_id) VALUES (%s, %s, %s, %s);",
        (id.upper(), current_timestamp, note_to_write, hashlib.sha1((id.upper() + current_timestamp).encode()).hexdigest()),
    )
    conn.commit()

    conn.close()

def delete_note_from_db(note_id):
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()

    command = "DELETE FROM notes WHERE note_id = %s;"
    cur.execute(command, (note_id,))
    conn.commit()

    conn.close()

def image_upload_record(uid, owner, image_name, timestamp):
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()

    cur.execute("INSERT INTO images (uid, owner, name, timestamp) VALUES (%s, %s, %s, %s);", (uid, owner, image_name, timestamp))
    conn.commit()

    conn.close()

def list_images_for_user(owner):
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()

    command = "SELECT uid, timestamp, name
