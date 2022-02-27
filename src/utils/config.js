import { prefs } from "./prefs";
import fs from 'fs'


export function init(basepaths, overwrite) {
    if (overwrite == true) {
        prefs(prefKeys.mainPath, { val: __dirname.replace('dist_electron', 'base') })
        console.log('main path --- ' + prefs(prefKeys.mainPath))

        prefs(prefKeys.tmpPath, { val: __dirname.replace('dist_electron', '') })
        console.log('tmp path --- ' + prefs(prefKeys.tmpPath))

        prefs(prefKeys.basePath, { val: basepaths })
        console.log('base path --- ' + prefs(prefKeys.basePath))
    }

    return [prefs(prefKeys.mainPath), prefs(prefKeys.tmpPath)]
}

export function developmentPath() {
    var file_name = 'api.py'
    return prefs(prefKeys.mainPath) + '/' + file_name
}

export function pyVenvPath() {
    return prefs(prefKeys.mainPath) + '/env/bin/python3'
}

export function productionPath() {
    let vals = prefs(prefKeys.basePath)
    if (vals != undefined) {
        return vals.toString().replace('app.asar', 'base/dist/api/api')
    }
}

export function guessPackaged() {
    if (prefs(prefKeys.basePath).toString().includes('app.asar') == true) {
        return true
    } else {
        return false
    }
}

export function assetsPath() {
    let vals = prefs(prefKeys.mainPath)
    if (vals != undefined) {
        return vals.toString().replace('base/', 'assets/')
    }
}

export function tmpVideoDirectory() {
    let tmp_dirc_name = 'tmp'
    let tmp_path = prefs(prefKeys.tmpPath)
    let pro_tmp_path = prefs(prefKeys.basePath)

    if (pro_tmp_path.toString().includes('app.asar') == true) {
        var proTmpPath = pro_tmp_path.toString().replace('app.asar', tmp_dirc_name)
        if (fs.existsSync(proTmpPath)) {
            return proTmpPath
        } else {
            fs.promises.mkdir(proTmpPath, { recursive: true })
            return proTmpPath
        }
    } else {
        if (fs.existsSync(tmp_path + '/' + tmp_dirc_name)) {
            return tmp_path + '/' + tmp_dirc_name
        } else {
            fs.promises.mkdir(tmp_path + '/' + tmp_dirc_name, { recursive: true })
            return tmp_path + '/' + tmp_dirc_name
        }
    }
}

export const resDefaultHeight = 768
export const resDefaultWidth = 1024

// add same key in keysForClear while adding new key in keys
export const prefKeys = {
    selVideoFileName: "selVideoFileName",
    selVideoPath: "selVideoPath",
    mainPath: "mainPath",
    tmpPath: "tmpPath",
    basePath: "basePath"
}

export const prefKeysForClear = [
    "selVideoFileName",
    "selVideoPath",
    "mainPath",
    "tmpPath",
    "basePath"
]

export const apiArgs = {
    init: "init",
    getProjects: "get_projects",
    getProject: "get_project",
    createProject: "create_project",
    shotBounDetec: "shot_bundry_detection",
    deleteProject: "delete_project",
    manFrame: "manual_frame",
    colorFulness: "colorfulness",
    getColorfulness: "get_colorfulness",
    edgeDetection: "edgedetection",
    getEdgeDetection: "get_edgedetection",
    objectdetection: "objectdetection",
    getObjectdetection: "get_objectdetection",
    structSimilarity: "strusimilarity",
    getStructSimilarity: "get_strusimilarity",
    compression: "compression",
    getCompression: "get_compression",
    faceDetection: "facedetection",
    getFaceDetection: "get_facedetection",
    motion: "motion",
    getMotion: "get_motion"
}

export const epMode = {
    GET: "get",
    POST: "post",
}

export const ipcKeys = {
    uploadVideoStatus: "upload-video-status",
    uplVidStatAck: "upload-video-status-ack",
    openVidUpDialog: "open-file-upload-dialog",
    newProFieldsEmpty: "new-project-fields-empty",
    newProCreatedSucc: "new-project-created-successfuly",
    videoInfoCleard: "new-project-video-info-cleared",
    delPro: "delete-project",
    delProConfirm: "delete-project-confirm",
    createProPageLoading: "create-page-isloading",
    creProPgeLoadAck: "create-page-isloading-ack",
    mainAppLoading: "main-app-isloading",
    mainAppLoadingAck: "main-app-isloading-ack",
    mainAppSendData: "main-app-send-data",
    mainAppReciveData: "main-app-recive-data",
    mainAppFieldEmpty: "main-app-fields-empty",
    getGallary: "get-gallary-fetch-images",
    getGallaryAck: "get-gallary-fetch-images-ack",
    getResultTable: "get-result-table",
    getResultTableAck: "get-result-table-ack",
    panelVisibility: "get-panel-visibility",
    panelVisibilityAck: "get-panel-visibility-ack",
}



