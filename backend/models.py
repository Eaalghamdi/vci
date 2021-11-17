from sqlalchemy import String, Integer, ForeignKey, Boolean, Numeric, Column
from sqlalchemy.orm import relationship
from db import Base


class Project(Base):
    __tablename__ = "projects"

    ProjectId = Column(Integer, primary_key=True, index=True)
    ProjectTitle = Column(String, unique=True, index=True)
    VideoTitle = Column(String(1000))
    VideoPath = Column(String(500))

    ObjectRecognition = relationship("ObjectRecognition")
    Colorfulness = relationship("Colorfulness")


class ObjectRecognition(Base):
    __tablename__ = "objectRecognition"

    ObjectRecognitionId = Column(Integer, primary_key=True, index=True)
    ObjectRecognitionModel = Column(String, unique=True, index=True)
    ObjectRecognitionResults = Column(String())
    ProjectId = Column(Integer, ForeignKey("projects.ProjectId"))


class Colorfulness(Base):
    __tablename__ = "colorfulness"

    ColorfulnessID = Column(Integer, primary_key=True, index=True)
    ColorfulnessModel = Column(String, unique=True, index=True)
    ColorfulnessResults = Column(String())
    ProjectId = Column(Integer, ForeignKey("projects.ProjectId"))


class StructuralSimilarity(Base):
    __tablename__= "srtructuralSimilarity" 

    StructuralSimilarityID = Column(Integer, primary_key=True, index=True)
    StructuralSimilarityModel = Column(String, unique=True, index=True)
    StructuralSimilarityResults = Column(String())
    ProjectId = Column(Integer, ForeignKey("projects.ProjectId"))

class Compression(Base):
    __tablename__= "compression"

    CompressionID = Column(Integer, primary_key=True, index=True)
    CompressionModel = Column(String, unique=True, index=True)
    CompressionResults = Column(String())
    ProjectId = Column(Integer, ForeignKey("projects.ProjectId"))


class FaceRecognition(Base):
    __tablename__="faceRecognition"
    
    FaceRecognitionId = Column(Integer, primary_key=True, index=True)
    FaceRecognitionModel = Column(String, unique=True, index=True)
    FaceRecognitionResults = Column(String()) 
    ProjectId = Column(Integer, ForeignKey("projects.ProjectId"))

class Motion(Base):
    __tablename__="motion"

    MotionID = Column(Integer, primary_key=True, index=True)
    MotionModel = Column(String, unique=True, index=True)
    MotionResults = Column(String())
    ProjectId = Column(Integer, ForeignKey("projects.ProjectId"))

class Sailency(Base):
    __tablename__="sailency"

    SailencyId =  Column(Integer, primary_key=True, index=True)
    SailencyModel = Column(String, unique=True, index=True)
    SailencyResults = Column(String())
    ProjectId = Column(Integer, ForeignKey("projects.ProjectId"))

class EdgeDetection(Base):
    __tablename__= "edgeDetection"

    EdgeDetectionId = Column(Integer, primary_key=True, index=True)
    EdgeDetectionModel = Column(String, unique=True, index=True)
    EdgeDetectionResults = Column(String())
    ProjectId = Column(Integer, ForeignKey("projects.ProjectId"))
    