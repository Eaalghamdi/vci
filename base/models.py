import db
from sqlite3 import Error
import json
import params

ERROR_CODES = {
    'default': 'undefined error',
    'UNIQUE constraint failed: projects.ProjectTitle': 'project title already exists'
}


def insert_one(tbname, tbkey, tbvalue):
    keys = str(tbkey).replace("'", '')
    keysLen = len(tbkey)
    value = str(params.value_gen(keysLen)).replace("'", '')

    sql = (f"INSERT INTO {tbname}{keys} VALUES{value}")

    try:
        connection = db.create_connection()
        cur = connection.cursor()
        cur.execute(sql, tbvalue)
        connection.commit()
        cur.close()
        connection.close()
        json_output = json.dumps(
            {'error': 'false', 'data':  str(cur.lastrowid)})
        return json_output
    except Error as e:
        if ERROR_CODES.get(e.args[0]):
            json_output = json.dumps(
                {'error': 'true', 'data':  ERROR_CODES.get(e.args[0])})
            return json_output
        else:
            json_output = json.dumps(
                {'error': 'true', 'data':  ERROR_CODES[0]})
            return json_output


def get_all(tbname):
    sql = (f"SELECT * FROM {tbname}")

    def query_db(cur, one=False):
        ab = [dict((cur.description[i][0], value)
                   for i, value in enumerate(row)) for row in cur.fetchall()]
        return (ab[0] if ab else None) if one else ab
    try:
        connection = db.create_connection()
        cur = connection.cursor()
        cur.execute(sql)
        my_query = query_db(cur)
        cur.close()
        connection.close()
        json_output = json.dumps(my_query)
        return json_output
    except Error as e:
        return e


def get_one(tbname, id):
    sql = (f"SELECT * FROM {tbname} WHERE id=?")

    def query_db(cur, one=True):
        ab = [dict((cur.description[i][0], value)
                   for i, value in enumerate(row)) for row in cur.fetchall()]
        return (ab[0] if ab else None) if one else ab
    try:
        connection = db.create_connection()
        cur = connection.cursor()
        cur.execute(sql, id)
        my_query = query_db(cur)
        cur.close()
        connection.close()
        json_output = json.dumps(my_query)
        return json_output
    except Error as e:
        return e


def delete_one(tbname, id):
    sql = (f"DELETE FROM {tbname} WHERE id=?")
    try:
        connection = db.create_connection()
        cur = connection.cursor()
        cur.execute(sql, id)
        connection.commit()
        cur.close()
        connection.close()
        json_output = json.dumps(
            {'error': 'false', 'data': 'completed'})
        return json_output
    except Error as e:
        return e
