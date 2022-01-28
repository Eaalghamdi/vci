import sqlite3
from sqlite3 import Error
import os


DATABASE_FILE_NAME = "/AUVANA.db"
DIRECTORY = str(os.path.dirname(os.path.abspath(__file__)))
DATABASE_ROOT = DIRECTORY.replace('api/database', '')
CREATE_TABLE_LIST = [
    """CREATE TABLE IF NOT EXISTS colorfulness (
	"ColorfulnessID" INTEGER NOT NULL, 
	"ColorfulnessModel" VARCHAR, 
	"ColorfulnessResults" VARCHAR, 
	id INTEGER, 
	PRIMARY KEY ("ColorfulnessID"), 
	FOREIGN KEY(id) REFERENCES projects (id)
);""",
    """CREATE TABLE IF NOT EXISTS compression (
	"CompressionID" INTEGER NOT NULL, 
	"CompressionModel" VARCHAR, 
	"CompressionResults" VARCHAR, 
	id INTEGER, 
	PRIMARY KEY ("CompressionID"), 
	FOREIGN KEY(id) REFERENCES projects (id)
);""",
    """CREATE TABLE IF NOT EXISTS "edgeDetection" (
	"EdgeDetectionId" INTEGER NOT NULL, 
	"EdgeDetectionModel" VARCHAR, 
	"EdgeDetectionResults" VARCHAR, 
	id INTEGER, 
	PRIMARY KEY ("EdgeDetectionId"), 
	FOREIGN KEY(id) REFERENCES projects (id)
);""",
    """CREATE TABLE IF NOT EXISTS "faceRecognition" (
	"FaceRecognitionId" INTEGER NOT NULL, 
	"FaceRecognitionModel" VARCHAR, 
	"FaceRecognitionResults" VARCHAR, 
	id INTEGER, 
	PRIMARY KEY ("FaceRecognitionId"), 
	FOREIGN KEY(id) REFERENCES projects (id)
);""",
    """CREATE TABLE IF NOT EXISTS motion (
	"MotionID" INTEGER NOT NULL, 
	"MotionModel" VARCHAR, 
	"MotionResults" VARCHAR, 
	id INTEGER, 
	PRIMARY KEY ("MotionID"), 
	FOREIGN KEY(id) REFERENCES projects (id)
);""",
    """CREATE TABLE IF NOT EXISTS "objectRecognition" (
	"ObjectRecognitionId" INTEGER NOT NULL, 
	"ObjectRecognitionModel" VARCHAR, 
	"ObjectRecognitionResults" VARCHAR, 
	id INTEGER, 
	PRIMARY KEY ("ObjectRecognitionId"), 
	FOREIGN KEY(id) REFERENCES projects (id)
);""",
    """CREATE TABLE IF NOT EXISTS projects (
	id INTEGER NOT NULL, 
	"ProjectTitle" VARCHAR, 
	"VideoTitle" VARCHAR(1000), 
	"VideoPath" VARCHAR(500), 
	PRIMARY KEY (id)
);""",
    """CREATE TABLE IF NOT EXISTS sailency (
	"SailencyId" INTEGER NOT NULL, 
	"SailencyModel" VARCHAR, 
	"SailencyResults" VARCHAR, 
	id INTEGER, 
	PRIMARY KEY ("SailencyId"), 
	FOREIGN KEY(id) REFERENCES projects (id)
);""",
    """CREATE TABLE IF NOT EXISTS "srtructuralSimilarity" (
	"StructuralSimilarityID" INTEGER NOT NULL, 
	"StructuralSimilarityModel" VARCHAR, 
	"StructuralSimilarityResults" VARCHAR, 
	id INTEGER, 
	PRIMARY KEY ("StructuralSimilarityID"), 
	FOREIGN KEY(id) REFERENCES projects (id)
);"""
]

CREATE_INDEX_LIST = [
    """CREATE INDEX IF NOT EXISTS "ix_colorfulness_ColorfulnessID" ON colorfulness ("ColorfulnessID")""",
    """CREATE UNIQUE INDEX IF NOT EXISTS "ix_colorfulness_ColorfulnessModel" ON colorfulness ("ColorfulnessModel")""",
    """CREATE INDEX IF NOT EXISTS "ix_compression_CompressionID" ON compression ("CompressionID")""",
    """CREATE UNIQUE INDEX IF NOT EXISTS "ix_compression_CompressionModel" ON compression ("CompressionModel")""",
    """CREATE INDEX IF NOT EXISTS "ix_edgeDetection_EdgeDetectionId" ON "edgeDetection" ("EdgeDetectionId")""",
    """CREATE UNIQUE INDEX IF NOT EXISTS "ix_edgeDetection_EdgeDetectionModel" ON "edgeDetection" ("EdgeDetectionModel")""",
    """CREATE INDEX IF NOT EXISTS "ix_faceRecognition_FaceRecognitionId" ON "faceRecognition" ("FaceRecognitionId")""",
    """CREATE UNIQUE INDEX IF NOT EXISTS "ix_faceRecognition_FaceRecognitionModel" ON "faceRecognition" ("FaceRecognitionModel")""",
    """CREATE INDEX IF NOT EXISTS "ix_motion_MotionID" ON motion ("MotionID")""",
    """CREATE UNIQUE INDEX IF NOT EXISTS "ix_motion_MotionModel" ON motion ("MotionModel")""",
    """CREATE INDEX IF NOT EXISTS "ix_objectRecognition_ObjectRecognitionId" ON "objectRecognition" ("ObjectRecognitionId")""",
    """CREATE UNIQUE INDEX IF NOT EXISTS "ix_objectRecognition_ObjectRecognitionModel" ON "objectRecognition" ("ObjectRecognitionModel")""",
    """CREATE UNIQUE INDEX IF NOT EXISTS "ix_projects_ProjectTitle" ON projects ("ProjectTitle")""",
    """CREATE INDEX IF NOT EXISTS ix_projects_id ON projects (id)""",
    """CREATE INDEX IF NOT EXISTS "ix_sailency_SailencyId" ON sailency ("SailencyId")""",
    """CREATE UNIQUE INDEX IF NOT EXISTS "ix_sailency_SailencyModel" ON sailency ("SailencyModel")""",
    """CREATE INDEX IF NOT EXISTS "ix_srtructuralSimilarity_StructuralSimilarityID" ON "srtructuralSimilarity" ("StructuralSimilarityID")""",
    """CREATE UNIQUE INDEX IF NOT EXISTS "ix_srtructuralSimilarity_StructuralSimilarityModel" ON "srtructuralSimilarity" ("StructuralSimilarityModel")"""
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
        create_tables(connection, CREATE_INDEX_LIST)
        connection.close()
        return "not existed and created new"
    else:
        connection = create_connection()
        connection.close()
        return "existed and connected"

    
