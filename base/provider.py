import models as Models
import params as Parms


def create_project(values):
    return Models.insert_one(Parms.TBNAME_PROJECTS, (Parms.PARAMS_PROJECTS['projecttitle'], Parms.PARAMS_PROJECTS['videotitle'], Parms.PARAMS_PROJECTS['videopath'],
                                                     ), values)


def get_projects():
    return Models.get_all(Parms.TBNAME_PROJECTS)


def delete_project(id):
    return Models.delete_one(Parms.TBNAME_PROJECTS, id)
