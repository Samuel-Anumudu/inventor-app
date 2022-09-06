import sqlite3


def connect_database():
    # connect to database
    connection = sqlite3.connect("inventor.db")
    # create cursor object
    cursor_object = connection.cursor()
    # execute an SQL statement
    cursor_object.execute("CREATE TABLE IF NOT EXISTS song (id INTEGER PRIMARY KEY, title text, artiste text, "
                          "genre text, year integer, copyright integer)")
    connection.commit()
    connection.close()


def insert(title, artiste, genre, year, copyright):
    connection = sqlite3.connect("inventor.db")
    cursor_object = connection.cursor()
    cursor_object.execute("INSERT INTO song VALUES (NULL, ?, ?, ?, ?, ?)", (title, artiste, genre, year, copyright))
    connection.commit()
    connection.close()


def view():
    connection = sqlite3.connect("inventor.db")
    cursor_object = connection.cursor()
    cursor_object.execute("SELECT * FROM song")
    rows = cursor_object.fetchall()
    connection.close()
    return rows


def search(title="", artiste="", genre="", year="", copyright=""):
    connection = sqlite3.connect("inventor.db")
    cursor_object = connection.cursor()
    cursor_object.execute("SELECT * FROM song WHERE title=? OR artiste=? OR genre=? OR year=? OR copyright=?",
                          (title, artiste, genre, year, copyright))
    rows = cursor_object.fetchall()
    connection.close()
    return rows


def delete(id):
    connection = sqlite3.connect("inventor.db")
    cursor_object = connection.cursor()
    cursor_object.execute("DELETE FROM song WHERE id=?", (id,))
    connection.commit()
    connection.close()


def update(id, title, artiste, genre, year, copyright):
    connection = sqlite3.connect("inventor.db")
    cursor_object = connection.cursor()
    cursor_object.execute("UPDATE song SET title =?, artiste=?, genre=?, year=?, copyright=? WHERE id=?",
                          (title, artiste, genre, year, copyright, id))
    connection.commit()
    connection.close()


connect_database()

# Songs precluded in the database for testing purposes
"""
insert("Perfect", "Ed Sheeran", "RnB", 2020, 123)
insert("Bebop Blues", "Barry Harris", "Jazz", 1998, 445)
insert("Last Last", "Burna Boy", "Afro", 2022, 509)

"""
