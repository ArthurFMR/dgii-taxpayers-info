import sqlite3
from sqlite3 import Error

def dict_factory(cursor, row):
    dicti = {}
    for index, col in enumerate(cursor.description):
        dicti[col[0]] = row[index]
    return dicti


def create_connection():
    conn = None

    try:
        conn = sqlite3.connect('src/DB.db')
        conn.row_factory = dict_factory
    except Error as e:
        print('Error conecting to db' + str(e))
    finally:
        return conn


def select_all_taxpayers(limit=100):
    conn = create_connection()
    
    sql = f"SELECT * FROM taxpayers limit {limit}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        return data   
    except Error as e:
        print('Error Selecting All taxpayers: ' + str(e))
    finally:
        if conn:
            conn.close()


def select_taxpayer_by_rnc(rnc, limit=100):
    conn = create_connection()
    
    sql = f"SELECT * FROM taxpayers WHERE rnc_cedula LIKE '%{rnc}%' LIMIT {limit}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        return data   
    except Error as e:
        print('Error Selecting by rnc: ' + str(e))
    finally:
        if conn:
            conn.close()


def select_taxpayer_by_name(name, limit=100):
    conn = create_connection()
    
    sql = f"SELECT * FROM taxpayers WHERE business_name LIKE '%{name}%' LIMIT {limit}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        return data   
    except Error as e:
        print('Error Selecting by name: ' + str(e))
    finally:
        if conn:
            conn.close()


def select_taxpayer_by_state(state, limit=100):
    conn = create_connection()
    
    sql = f"SELECT * FROM taxpayers WHERE state = '{state}' LIMIT {limit}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        return data   
    except Error as e:
        print('Error Selecting by state: ' + str(e))
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    select_all_taxpayers()
