import sqlite3


def create_table():
    conn = sqlite3.connect('tutorial.db')

    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS storage(name TEXT, post TEXT)")
    conn.commit()
    c.close()
    conn.close()



def data_entry(name,post):
    conn = sqlite3.connect('tutorial.db')

    c = conn.cursor()

    c.execute("INSERT INTO storage VALUES(?,?);",(name,post))
    conn.commit()
    c.close()
    conn.close()

   
def fech_data():
    conn = sqlite3.connect('tutorial.db')

    c = conn.cursor()

    c.execute('SELECT * FROM storage')
    data = c.fetchall()
    conn.commit()
    c.close()
    conn.close()

    return data



