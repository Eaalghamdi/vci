from fastapi import FastAPI
import uvicorn

# from FeatureExtraction.Utils import Processing
# import FeatureExtraction

# from fastapi import FastAPI, Request, Depends, BackgroundTasks, File, UploadFile
# from pydantic import BaseModel
# from schemas import ProjectRequest
# import sqlalchemy
# import models
# from db import SessionLocal, engine
# from sqlalchemy.orm import Session
# from models import Project
# import os
# import sys
# from glob import glob


if __name__ == '__main__':
    uvicorn.run('api:app', host='0.0.0.0', port=8001, reload=True)
