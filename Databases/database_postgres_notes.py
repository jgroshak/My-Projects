# STEPS:
# 1. Connect to database
# 2. Create cursor object
# 3. Write an SQL query
# 4. Commit changes
# 5. Close database connection

import psycopg2


def create_table():
    conn = psycopg2.connect(" dbname='database1' user='postgres' password='4857570' host='localhost' port='5432' ")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect(" dbname='database1' user='postgres' password='4857570' host='localhost' port='5432' ")
    cur = conn.cursor()

    # this syntax is prone to SQL injections by outside attackers
    #cur.execute("INSERT INTO store VALUES('%s','%s','%s')" % (item,quantity,price))

    cur.execute("INSERT INTO store VALUES(%s, %s, %s)", (item,quantity,price))
    

    conn.commit()
    conn.close()



def view():
    conn = psycopg2.connect(" dbname='database1' user='postgres' password='4857570' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows= cur.fetchall()
    conn.close()
    return rows

 
def delete(item):
    conn = psycopg2.connect(" dbname='database1' user='postgres' password='4857570' host='localhost' port='5432' ")
    cur = conn.cursor()
    ############################################## ADD an extra comma when it's only 1 parameter
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()
 
def update(quantity,price,item):
    conn = psycopg2.connect(" dbname='database1' user='postgres' password='4857570' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()    



create_table()
#update(11,6,"water glass")
#delete("coffee cup")
#print(view())
insert("Orange",10,15)

# NOTICE that if you have multiple, say 'coffee cups', and you delete them. BOTH will be deleted
 
