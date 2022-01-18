import { app, ipcMain } from 'electron'
import { ipcKeys } from '../utils/config'
var basepath = app.getAppPath()


// in new project for upload video, trigger function
export function openFileDirc(callback) {
    ipcMain.on(ipcKeys.openVidUpDialog, (event, data) => {
        callback(event, data)
    })
}

// after successfuly created project refresh history
export function newProjCreated(callback) {
    ipcMain.on(ipcKeys.newProCreatedSucc, (event, data) => {
        event.reply(ipcKeys.newProCreatedSucc)
    })
}

// delete confirmation
export function delProConfirm(callback) {
    ipcMain.on(ipcKeys.delPro, (event, data) => {
        callback(event, data)
    })
}

export function uploadVidStat(callback) {
    ipcMain.on(ipcKeys.uploadVideoStatus, (event, data) => {
        event.reply(ipcKeys.uplVidStatAck, basepath)
    })
}

export function emptyFieldAlert(callback) {
    ipcMain.on(ipcKeys.newProFieldsEmpty, function (event, data) {
        callback(event, data)
    })
}

export function createProLoading(callback) {
    ipcMain.on(ipcKeys.createProPageLoading, (event, data) => {
        event.reply(ipcKeys.creProPgeLoadAck, data)
    })
}







