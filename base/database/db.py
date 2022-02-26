import sqlite3
from sqlite3 import Error
import os


DATABASE_FILE_NAME = "/AUVANA.db"
DIRECTORY = str(os.path.dirname(os.path.abspath(__file__)))
DATABASE_ROOT = DIRECTORY.replace('api/database', '')


CREATE_TABLE_LIST = [
    """CREATE TABLE IF NOT EXISTS projects (
	id INTEGER NOT NULL, 
	"ProjectTitle" VARCHAR, 
	"VideoTitle" VARCHAR(1000), 
	"VideoPath" VARCHAR(500), 
	PRIMARY KEY (id)
);""",
    """CREATE TABLE IF NOT EXISTS colorfulness (
	id INTEGER NOT NULL, 
	"imgcolor" VARCHAR, 
	"meancolor" VARCHAR, 
	"stdcolor" VARCHAR, 
    "meanadj" VARCHAR, 
    "stdadj" VARCHAR, 
    "meanadjabs" VARCHAR, 
    "stdadjabs" VARCHAR, 
	PRIMARY KEY (id)
);""",
    """CREATE TABLE IF NOT EXISTS edgedetection (
	id INTEGER NOT NULL, 
	"meanval" VARCHAR, 
	"stdval" VARCHAR, 
	"meanadjabs" VARCHAR, 
    "stdadjabs" VARCHAR, 
	PRIMARY KEY (id)
);""",
    """CREATE TABLE IF NOT EXISTS objectdetection (
	id INTEGER NOT NULL, 
	"classindex" VARCHAR, 
	"confidence" VARCHAR, 
	"bbox" VARCHAR,
	PRIMARY KEY (id)
);""",
    """CREATE TABLE IF NOT EXISTS structuralsimilarity (
	id INTEGER NOT NULL, 
	"imganame" VARCHAR, 
	"imgbname" VARCHAR, 
	"mse" VARCHAR,
    "ssim" VARCHAR,
	PRIMARY KEY (id)
);""",
    """CREATE TABLE IF NOT EXISTS compression (
	id INTEGER NOT NULL, 
	"filename" VARCHAR, 
	"cnvformat" VARCHAR, 
	"sizebytprev" VARCHAR,
    "sizebytnew" VARCHAR,
	PRIMARY KEY (id)
);""",
    """CREATE TABLE IF NOT EXISTS facedetection (
	id INTEGER NOT NULL, 
	"filename" VARCHAR, 
	"numfaces" VARCHAR,
	PRIMARY KEY (id)
);""",
    """CREATE TABLE IF NOT EXISTS motion (
	id INTEGER NOT NULL, 
	"videoname" VARCHAR, 
	"numberofmovingobjects" VARCHAR,
    "movingdurationms" VARCHAR,
    "ratioofmovingobjectsns" VARCHAR,
    "ratioofmovingobjectsnm" VARCHAR,
    "movingdurtiondifferencemean" VARCHAR,
    "movingdurtiondifferencevaraince" VARCHAR,
    "movingdurtiondifferencesd" VARCHAR,
    "ratioofmovingdurtionts" VARCHAR,
    "ratioofmovingdurtiontm" VARCHAR,
    "satrtendtimes" VARCHAR,
	PRIMARY KEY (id)
);""",
    """CREATE TABLE IF NOT EXISTS saliency (
	id INTEGER NOT NULL, 
    "filename" VARCHAR, 
	"mean" VARCHAR, 
	"std" VARCHAR,
	PRIMARY KEY (id)
);""",
]


def db_exists():
    if os.path.isfile(DATABASE_ROOT + DATABASE_FILE_NAME):
        return True
    else:
        return False


def create_connection():
    dbFilePath = DATABASE_ROOT + DATABASE_FILE_NAME
    dbconn = None

    try:
        dbconn = sqlite3.connect(dbFilePath)
    except Error as e:
        return None
    return dbconn


def create_tables(connection, tables):
    try:
        conn = connection.cursor()
        for table in tables:
            conn.execute(table)
    except Error as e:
        return None


def init():
    if db_exists() == False:
        connection = create_connection()
        create_tables(connection, CREATE_TABLE_LIST)
        # create_tables(connection, CREATE_INDEX_LIST)
        connection.close()
        return "not existed and created new"
    else:
        connection = create_connection()
        connection.close()
        return "existed and connected"
