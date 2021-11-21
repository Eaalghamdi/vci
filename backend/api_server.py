from fastapi import FastAPI
import uvicorn
from fastapi import FastAPI
import uvicorn
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
from api import app
# from pytube import YouTube

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

import sys
sys.path.append('/backend/FeatureExtraction')


if __name__ == '__main__':
    uvicorn.run('api:app', host='0.0.0.0', port=8001, reload=True)
