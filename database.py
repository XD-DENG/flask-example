import sqlite3
import hashlib
import datetime

user_db_file_location = "database_file/users.db"
note_db_file_location = "database_file/notes.db"
image_db_file_location = "database_file/images.db"

def list_users():
    _conn = sqlite3.connect(user_db_file_location)
    _c = _conn.cursor()

    _c.execute("select id from users;")
    result = [x[0] for x in _c.fetchall()]

    _conn.close()
    
    return result

def verify(id, pw):
    _conn = sqlite3.connect(user_db_file_location)
    _c = _conn.cursor()

    _c.execute("select pw from users where id = '" + id + "';")
    result = _c.fetchone()[0] == hashlib.sha256(pw.encode()).hexdigest()
    
    _conn.close()

    return result

def delete_user_from_db(id):
    _conn = sqlite3.connect(user_db_file_location)
    _c = _conn.cursor()
    _c.execute("delete from users where id = '" + id + "';")
    _conn.commit()
    _conn.close()

    # when we delete a user from database USERS, we also need to delete all his or her notes data from database NOTES
    _conn = sqlite3.connect(note_db_file_location)
    _c = _conn.cursor()
    _c.execute("delete from notes where user = '" + id + "';")
    _conn.commit()
    _conn.close()

    # when we delete a user from database USERS, we also need to 
    # [1] delete all his or her images from image pool (done in app.py)
    # [2] delete all his or her images records from database IMAGES
    _conn = sqlite3.connect(image_db_file_location)
    _c = _conn.cursor()
    _c.execute("delete from images where owner = '" + id + "';")
    _conn.commit()
    _conn.close()

def add_user(id, pw):
    _conn = sqlite3.connect(user_db_file_location)
    _c = _conn.cursor()

    _c.execute("insert into users values(?, ?)", (id.upper(), hashlib.sha256(pw.encode()).hexdigest()))
    
    _conn.commit()
    _conn.close()

def read_note_from_db(id):
    _conn = sqlite3.connect(note_db_file_location)
    _c = _conn.cursor()

    command = "select note_id, timestamp, note from notes where user = '" + id.upper() + "';" 
    _c.execute(command)
    result = _c.fetchall()

    _conn.commit()
    _conn.close()

    return result

def match_user_id_with_note_id(note_id):
    # Given the note id, confirm if the current user is the owner of the note which is being operated.
    _conn = sqlite3.connect(note_db_file_location)
    _c = _conn.cursor()

    command = "select user from notes where note_id = '" + note_id + "';" 
    _c.execute(command)
    result = _c.fetchone()[0]

    _conn.commit()
    _conn.close()

    return result

def write_note_into_db(id, note_to_write):
    _conn = sqlite3.connect(note_db_file_location)
    _c = _conn.cursor()

    current_timestamp = str(datetime.datetime.now())
    _c.execute("insert into notes values(?, ?, ?, ?)", (id.upper(), current_timestamp, note_to_write, hashlib.sha1((id.upper() + current_timestamp).encode()).hexdigest()))

    _conn.commit()
    _conn.close()

def delete_note_from_db(note_id):
    _conn = sqlite3.connect(note_db_file_location)
    _c = _conn.cursor()

    command = "delete from notes where note_id = '" + note_id + "';" 
    _c.execute(command)

    _conn.commit()
    _conn.close()

def image_upload_record(uid, owner, image_name, timestamp):
    _conn = sqlite3.connect(image_db_file_location)
    _c = _conn.cursor()

    _c.execute("insert into images values (?, ?, ?, ?)", (uid, owner, image_name, timestamp))

    _conn.commit()
    _conn.close()

def list_images_for_user(owner):
    _conn = sqlite3.connect(image_db_file_location)
    _c = _conn.cursor()

    command = "select uid, timestamp, name from images where owner = '{0}'".format(owner)
    _c.execute(command)
    result = _c.fetchall()

    _conn.commit()
    _conn.close()

    return result

def match_user_id_with_image_uid(image_uid):
    # Given the note id, confirm if the current user is the owner of the note which is being operated.
    _conn = sqlite3.connect(image_db_file_location)
    _c = _conn.cursor()

    command = "select owner from images where uid = '" + image_uid + "';" 
    _c.execute(command)
    result = _c.fetchone()[0]

    _conn.commit()
    _conn.close()

    return result

def delete_image_from_db(image_uid):
    _conn = sqlite3.connect(image_db_file_location)
    _c = _conn.cursor()

    command = "delete from images where uid = '" + image_uid + "';" 
    _c.execute(command)

    _conn.commit()
    _conn.close()







if __name__ == "__main__":
    print(list_users())