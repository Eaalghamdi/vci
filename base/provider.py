import database.models as Models
import database.params as Parms
import preprocessing.sbdextraction as SBDExtraction
import preprocessing.mfextraction as MFExtraction
import functions.colorfulness as Colorfulness
import functions.edgedetection as EdgeDetection
import functions.objectdetection as ObjectDetection
import functions.structuralsimilarity as StructuralSimilarity

# project


def create_project(values):
    return Models.insert_one(Parms.TBNAME_PROJECTS, (Parms.PARAMS_PROJECTS['projecttitle'], Parms.PARAMS_PROJECTS['videotitle'], Parms.PARAMS_PROJECTS['videopath'],
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
    return Models.insert_one(Parms.TBNAME_COLORFULNESS, (Parms.PARAMS_COLORFULNESS['imgcolor'], Parms.PARAMS_COLORFULNESS['meancolor'], Parms.PARAMS_COLORFULNESS['stdcolor'], Parms.PARAMS_COLORFULNESS['meanadj'], Parms.PARAMS_COLORFULNESS['stdadj'], Parms.PARAMS_COLORFULNESS['meanadjabs'], Parms.PARAMS_COLORFULNESS['stdadjabs']
                                                         ), values)


def clear_colorfulness():
    return Models.clear_all(Parms.TBNAME_COLORFULNESS)


def get_colorfulness():
    return Models.get_all(Parms.TBNAME_COLORFULNESS)

# edgedetection


def edgedetection(frameDir, mode, submode, thrHold1, thrHold2):
    return EdgeDetection.edge_detection(frameDir, mode, submode, thrHold1, thrHold2)


def insert_edgedetection(values):
    return Models.insert_one(Parms.TBNAME_EDGEDETECTION, (Parms.PARAMS_EDGEDETECTION['meanval'], Parms.PARAMS_EDGEDETECTION['stdval'], Parms.PARAMS_EDGEDETECTION['meanadjabs'], Parms.PARAMS_EDGEDETECTION['stdadjabs']
                                                          ), values)


def clear_edgedetection():
    return Models.clear_all(Parms.TBNAME_EDGEDETECTION)


def get_edgedetection():
    return Models.get_all(Parms.TBNAME_EDGEDETECTION)

# objectdetection


def objectdetection(frameDir, thrHold):
    return ObjectDetection.object_detection(frameDir, thrHold)


def insert_objectdetection(values):
    return Models.insert_one(Parms.TBNAME_OBJECTDETECTION, (Parms.PARAMS_OBJECTDETECTION['classindex'], Parms.PARAMS_OBJECTDETECTION['confidence'], Parms.PARAMS_OBJECTDETECTION['bbox']
                                                            ), values)


def clear_objectdetection():
    return Models.clear_all(Parms.TBNAME_OBJECTDETECTION)


def get_objectdetection():
    return Models.get_all(Parms.TBNAME_OBJECTDETECTION)

# objectdetection


def structsimilarity(frameDir):
    return StructuralSimilarity.strctural_similarity(frameDir)


def insert_structsimilarity(values):
    return Models.insert_one(Parms.TBNAME_STRUCTSIMILARITY, (Parms.PARAMS_STRUCTSIMILARITY['imganame'], Parms.PARAMS_STRUCTSIMILARITY['imgbname'], Parms.PARAMS_STRUCTSIMILARITY['mse'], Parms.PARAMS_STRUCTSIMILARITY['ssim']
                                                             ), values)


def clear_structsimilarity():
    return Models.clear_all(Parms.TBNAME_STRUCTSIMILARITY)


def get_structsimilarity():
    return Models.get_all(Parms.TBNAME_STRUCTSIMILARITY)
