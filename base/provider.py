import database.models as Models
import database.params as Parms
import preprocessing.sbdextraction as SBDExtraction
import preprocessing.mfextraction as MFExtraction
import features.colorfulness as Colorfulness
import features.edgedetection as EdgeDetection
import features.objectdetection as ObjectDetection
import features.structuralsimilarity as StructuralSimilarity
import features.compression as Compression
import features.facedetection as FaceDetection
import features.motion as Motion
import features.saliency as Saliency

# project


def create_project(values):
    return Models.insert_one(Parms.TBNAME_PROJECTS, (
        Parms.PARAMS_PROJECTS['projecttitle'],
        Parms.PARAMS_PROJECTS['videotitle'],
        Parms.PARAMS_PROJECTS['videopath'],
    ), values)


def get_projects():
    return Models.get_all(Parms.TBNAME_PROJECTS)


def get_project(id):
    return Models.get_one(Parms.TBNAME_PROJECTS, id)


def delete_project(id):
    return Models.delete_one(Parms.TBNAME_PROJECTS, id)


# shot boundry detection
def fe_shot_boundry_det(videoPath, videoFileName, method, treshold, defaultH, defaultW):
    return SBDExtraction.shot_bundry_detection(videoPath, videoFileName, method, treshold, defaultH, defaultW)

# manual frame


def fe_manual_frame(videoPath, videoFileName, time, defaultH, defaultW):
    return MFExtraction.manual_frame(videoPath, videoFileName, time, defaultH, defaultW)

# colorfulness


def colorfulness(path, mode):
    return Colorfulness.get_colorfulness(path, mode)


def insert_colorfulness(values):
    return Models.insert_one(Parms.TBNAME_COLORFULNESS, (
        Parms.PARAMS_COLORFULNESS['imgcolor'],
        Parms.PARAMS_COLORFULNESS['meancolor'],
        Parms.PARAMS_COLORFULNESS['stdcolor'],
        Parms.PARAMS_COLORFULNESS['meanadj'],
        Parms.PARAMS_COLORFULNESS['stdadj'],
        Parms.PARAMS_COLORFULNESS['meanadjabs'],
        Parms.PARAMS_COLORFULNESS['stdadjabs']
    ), values)


def clear_colorfulness():
    return Models.clear_all(Parms.TBNAME_COLORFULNESS)


def get_colorfulness():
    return Models.get_all(Parms.TBNAME_COLORFULNESS)

# edgedetection


def edgedetection(frameDir, mode, submode, thrHold1, thrHold2):
    return EdgeDetection.edge_detection(frameDir, mode, submode, thrHold1, thrHold2)


def insert_edgedetection(values):
    return Models.insert_one(Parms.TBNAME_EDGEDETECTION, (
        Parms.PARAMS_EDGEDETECTION['meanval'],
        Parms.PARAMS_EDGEDETECTION['stdval'],
        Parms.PARAMS_EDGEDETECTION['meanadjabs'],
        Parms.PARAMS_EDGEDETECTION['stdadjabs']
    ), values)


def clear_edgedetection():
    return Models.clear_all(Parms.TBNAME_EDGEDETECTION)


def get_edgedetection():
    return Models.get_all(Parms.TBNAME_EDGEDETECTION)

# objectdetection


def objectdetection(frameDir, thrHold):
    return ObjectDetection.object_detection(frameDir, thrHold)


def insert_objectdetection(values):
    return Models.insert_one(Parms.TBNAME_OBJECTDETECTION, (
        Parms.PARAMS_OBJECTDETECTION['classindex'],
        Parms.PARAMS_OBJECTDETECTION['confidence'],
        Parms.PARAMS_OBJECTDETECTION['bbox']
    ), values)


def clear_objectdetection():
    return Models.clear_all(Parms.TBNAME_OBJECTDETECTION)


def get_objectdetection():
    return Models.get_all(Parms.TBNAME_OBJECTDETECTION)

# objectdetection


def structsimilarity(frameDir):
    return StructuralSimilarity.strctural_similarity(frameDir)


def insert_structsimilarity(values):
    return Models.insert_one(Parms.TBNAME_STRUCTSIMILARITY, (
        Parms.PARAMS_STRUCTSIMILARITY['imganame'],
        Parms.PARAMS_STRUCTSIMILARITY['imgbname'],
        Parms.PARAMS_STRUCTSIMILARITY['mse'],
        Parms.PARAMS_STRUCTSIMILARITY['ssim']
    ), values)


def clear_structsimilarity():
    return Models.clear_all(Parms.TBNAME_STRUCTSIMILARITY)


def get_structsimilarity():
    return Models.get_all(Parms.TBNAME_STRUCTSIMILARITY)

# compression


def compression(videoPath, videoDir, widthD, heightD, fps, fileFormat):
    return Compression.compression(videoPath, videoDir, widthD, heightD, fps, fileFormat)


def insert_compression(values):
    return Models.insert_one(Parms.TBNAME_COMPRESSION, (
        Parms.PARAMS_COMPRESSION['filename'],
        Parms.PARAMS_COMPRESSION['cnvformat'],
        Parms.PARAMS_COMPRESSION['sizebytprev'],
        Parms.PARAMS_COMPRESSION['sizebytnew']
    ), values)


def get_compression():
    return Models.get_all(Parms.TBNAME_COMPRESSION)

# facedetection


def facedetection(videoDir, minneigh):
    return FaceDetection.facedetection(videoDir, minneigh)


def insert_facedetection(values):
    return Models.insert_one(Parms.TBNAME_FACEDTECTION, (
        Parms.PARAMS_FACEDTECTION['filename'],
        Parms.PARAMS_FACEDTECTION['numfaces']
    ), values)


def clear_facedetection():
    return Models.clear_all(Parms.TBNAME_FACEDTECTION)


def get_facedetection():
    return Models.get_all(Parms.TBNAME_FACEDTECTION)

# motion


def motion(videoPath):
    return Motion.motion(videoPath)


def insert_motion(values):
    return Models.insert_one(Parms.TBNAME_MOTION, (
        Parms.PARAMS_FACEDTECTION['videoname'],
        Parms.PARAMS_FACEDTECTION['numberofmovingobjects'],
        Parms.PARAMS_FACEDTECTION['movingdurationms'],
        Parms.PARAMS_FACEDTECTION['ratioofmovingobjectsns'],
        Parms.PARAMS_FACEDTECTION['ratioofmovingobjectsnm'],
        Parms.PARAMS_FACEDTECTION['movingdurtiondifferencevaraince'],
        Parms.PARAMS_FACEDTECTION['movingdurtiondifferencemean'],
        Parms.PARAMS_FACEDTECTION['movingdurtiondifferencesd'],
        Parms.PARAMS_FACEDTECTION['ratioofmovingdurtionts'],
        Parms.PARAMS_FACEDTECTION['ratioofmovingdurtiontm'],
        Parms.PARAMS_FACEDTECTION['satrtendtimes']
    ), values)


def get_motion():
    return Models.get_all(Parms.TBNAME_MOTION)

# saliency


def saliency(frameDir):
    return Saliency.saliency(frameDir)


def insert_saliency(values):
    return Models.insert_one(Parms.TBNAME_SALIENCY, (
        Parms.PARAMS_SALIENCY['filename'],
        Parms.PARAMS_SALIENCY['mean'],
        Parms.PARAMS_SALIENCY['std']
    ), values)


def clear_saliency():
    return Models.clear_all(Parms.TBNAME_SALIENCY)


def get_saliency():
    return Models.get_all(Parms.TBNAME_SALIENCY)
