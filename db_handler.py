from pathlib import Path
import sqlite3
from sqlite3.dbapi2 import Error

def create_db_conection(file_location):
    conn = None
    try:
        print(sqlite3.version)
        conn = sqlite3.connect(file_location)
        
    except sqlite3.Error as e:
        print("db connector: ",e)
    
    return conn


def create_message(conn,content):
    pass

def create_user(conn,username,password):
    #c = conn.execute()
    pass






def create_channel(conn,Channel_name):
    c = conn.execute("""INSERT INTO Channels(Channel_id,Display_name) VALUES(?,?)""")




def sql_run(conn,sql_command):
    c = conn.cursor()
    
    try:
        c.execute(sql_command)
        conn.commit()
    except Error as e:
        print("sql_run_error: ",e)

if __name__ == "__main__":
    conn = create_db_conection(str(Path(__file__).resolve().parent.joinpath("test.db")))


