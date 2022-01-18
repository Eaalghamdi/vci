import { app, dialog } from 'electron'
import path from 'path'
import { alertYellow } from '../utils/icons_path';
const homeDir = app.getPath('home')
const desktopDir = path.resolve(homeDir, 'Desktop')


export function fileDir(callback) {
    dialog
        .showOpenDialog({
            title: "Select the File to be uploaded",
            defaultPath: desktopDir,
            filters: [
                {
                    name: "Video Files",
                    extensions: ["mp4"],
                },
            ],
            properties: ["openFile"],
        })
        .then((file) => {
            callback(file)
        })
}

export function fieldEmpty(event, data) {
    const options = {
        icon: alertYellow,
        type: 'question',
        buttons: ['Ok'],
        defaultId: 2,
        title: 'Alert',
        message: data,
    };
    dialog.showMessageBox(null, options, () => { });
}

export function confirm(data, callback) {
    const options = {
        icon: alertYellow,
        type: 'question',
        defaultId: 2,
        buttons: ['Yes', 'No'],
        title: 'Confirm',
        message: data,
    };
    dialog.showMessageBox(null, options).then((box) => {
        if (box.response == 0) {
            callback()
        }
    })
}



