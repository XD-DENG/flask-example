import sqlite3
import hashlib

db_file_location = "database_file/users.db"

def list_users():
    _conn = sqlite3.connect(db_file_location)
    _c = _conn.cursor()

    _c.execute("select id from users;")
    result = [x[0] for x in _c.fetchall()]

    _conn.close()
    
    return result

def verify(id, pw):
    _conn = sqlite3.connect(db_file_location)
    _c = _conn.cursor()

    _c.execute("select pw from users where id = '" + id + "';")
    result = _c.fetchone()[0] == hashlib.sha256(pw).hexdigest()
    
    _conn.close()

    return result

def delete_user_from_db(id):
    _conn = sqlite3.connect(db_file_location)
    _c = _conn.cursor()

    _c.execute("delete from users where id = '" + id + "';")

    _conn.commit()
    _conn.close()

def add_user(id, pw):
    _conn = sqlite3.connect(db_file_location)
    _c = _conn.cursor()

    command = "insert into users values('" + id.upper() + "', '" + hashlib.sha256(pw).hexdigest() + "');" 
    _c.execute(command)

    _conn.commit()
    _conn.close()




if __name__ == "__main__":
    print list_users()