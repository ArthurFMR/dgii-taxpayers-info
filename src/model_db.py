from psycopg2 import Error
from psycopg2.extras import RealDictCursor
import os

DATABASE_URL = os.environ['DATABASE_URL']

def create_connection():
    conn = None

    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    except Error as e:
        print('Error conecting to db' + str(e))
    finally:
        return conn


def select_all_taxpayers(limit=100):
    conn = create_connection()
    
    sql = f"SELECT * FROM taxpayers limit {limit}"

    try:
        cur = conn.cursor(cursor_factory=RealDictCursor)
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
        cur = conn.cursor(cursor_factory=RealDictCursor)
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
        cur = conn.cursor(cursor_factory=RealDictCursor)
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
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(sql)
        data = cur.fetchall()
        return data   
    except Error as e:
        print('Error Selecting by state: ' + str(e))
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    create_connection()
