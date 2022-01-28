import { app, ipcMain } from 'electron'
import { ipcKeys } from '../utils/config'
var basepath = app.getAppPath()


// in new project for upload video, trigger function
export function openFileDirc(callback) {
    ipcMain.on(ipcKeys.openVidUpDialog, (event, data) => {
        callback(event, data)
        ipcMain.removeListener(
            ipcKeys.openVidUpDialog,
            () => { }
        )
    })
}

// after successfuly created project refresh history
export function newProjCreated(callback) {
    ipcMain.on(ipcKeys.newProCreatedSucc, (event, data) => {
        event.reply(ipcKeys.newProCreatedSucc)
        ipcMain.removeListener(
            ipcKeys.newProCreatedSucc,
            () => { }
        )
    })
}

// delete confirmation
export function delProConfirm(callback) {
    ipcMain.on(ipcKeys.delPro, (event, data) => {
        callback(event, data)
        ipcMain.removeListener(
            ipcKeys.delPro,
            () => { }
        )
    })
}

export function uploadVidStat(callback) {
    ipcMain.on(ipcKeys.uploadVideoStatus, (event, data) => {
        event.reply(ipcKeys.uplVidStatAck, basepath)
        ipcMain.removeListener(
            ipcKeys.uploadVideoStatus,
            () => { }
        )
    })
}

export function emptyFieldAlert(callback) {
    ipcMain.on(ipcKeys.newProFieldsEmpty, function (event, data) {
        callback(event, data)
        ipcMain.removeListener(
            ipcKeys.newProFieldsEmpty,
            () => { }
        )
    })
}

export function createProLoading(callback) {
    ipcMain.on(ipcKeys.createProPageLoading, (event, data) => {
        event.reply(ipcKeys.creProPgeLoadAck, data)
        ipcMain.removeListener(
            ipcKeys.createProPageLoading,
            () => { }
        )
    })
}

export function mainAppLoading(callback) {
    ipcMain.on(ipcKeys.mainAppLoading, (event, data) => {
        event.reply(ipcKeys.mainAppLoadingAck, data)
        ipcMain.removeListener(
            ipcKeys.mainAppLoading,
            () => { }
        )
    })
}

export function mainAppShareData(callback) {
    ipcMain.on(ipcKeys.mainAppSendData, (event, data) => {
        event.reply(ipcKeys.mainAppReciveData, data)
        ipcMain.removeListener(
            ipcKeys.mainAppSendData,
            () => { }
        )
    })
}

export function mainAppFieldEmpty(callback) {
    ipcMain.on(ipcKeys.mainAppFieldEmpty, (event, data) => {
        callback(event, data)
        ipcMain.removeListener(
            ipcKeys.mainAppSendData,
            () => { }
        )
    })
}

export function getGallary(callback) {
    ipcMain.on(ipcKeys.getGallary, (event, data) => {
        event.reply(ipcKeys.getGallaryAck)
        ipcMain.removeListener(
            ipcKeys.getGallary,
            () => { }
        )
    })
}








