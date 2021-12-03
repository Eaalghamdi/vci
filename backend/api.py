# from FeatureExtraction.Utils import Processing
# import FeatureExtraction

from fastapi import FastAPI, Request, Depends, BackgroundTasks, File, UploadFile
from pydantic import BaseModel
from schemas import ProjectRequest
import sqlalchemy
import models
from db import SessionLocal, engine
from sqlalchemy.orm import Session
from models import Project
import os
import sys
from glob import glob
from fastapi.responses import JSONResponse
# from pytube import YouTube

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

import sys
sys.path.append('/backend/FeatureExtraction')

origins = [
    "http://localhost:8080",
    "http://localhost",
    "https://localhost:8080",
]

# middleware = [
#     Middleware(CORSMiddleware,
#     allow_origins=origins)
# ]

# app = FastAPI(middleware=middleware)
# CORSMiddleware,
# allow_origins=["*"],

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"]
)

# create database
models.Base.metadata.create_all(bind=engine)


# check if the db is connected
def get_db():
    try:
        db = SessionLocal()
        yield db

    finally:
        db.close()


@ app.post('/api/add_projects')
async def post_project(project_request: ProjectRequest, db: Session = Depends(get_db)):

    project = Project()
    project.ProjectTitle = project_request.ProjectTitle
    project.VideoTitle = project_request.VideoTitle
    project.VideoPath = project_request.VideoPath
  

    db.add(project)
    db.commit()
    return project.id


@ app.get('/api/all_projects')
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()


@app.get('/api/projects/{project_id}')
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    return(project)

@app.delete('/api/projects/{project_id}')
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="project not found")
    db.delete(project)
    db.commit()
    return {"ok": True}


@ app.post('/api/processing/sbd')
async def shotBoundryDetection():
    pass


# @app.get('/video_processing')
# def video_processing(video):
#     vid = Processing(video)
#     fbs = vid.get_fb()
#     return fbs

    #   function() {
    #     this.projects.projectName = "";
    #     this.projects.videoURL = "";
    #   }.bind(this)



## PROJECTS ###
# def downloadYT(videoURL, outPath):
#     try:
#         # videoURL = "https://www.youtube.com//watch?v=" + videoURL
#         os.mkdir(outPath)
#         os.chdir(outPath)
#         YouTube(videoURL).streams.first().download()
#         os.chdir("./")

#     except:
#         print("There is somethign wrong with PyTube")






@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )