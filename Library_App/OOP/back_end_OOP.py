import sqlite3

class Database:

    # create connection to database server
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()


    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()
      

    def update(self, id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.conn.commit()
    
    def __del__(self): 
        self.conn.close()

        







# MANIPULATING THE DATA

#insert("The Hitchhiker's Guide to the Galaxy","Douglas Adams",1977,9781529046137)
#delete()
#update(3,"The Hitchhiker's Guide to the Galaxy", 'Douglas Adams', 1979, 9781529046137)
#print(search(author="J.R.R. Tolkien"))

#print(view())
