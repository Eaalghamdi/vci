import { newProjCreated, emptyFieldAlert, delProConfirm, createProLoading } from './render/ipcs'
import { fieldEmpty, confirm } from './render/dialogs'
import { ipcKeys } from './utils/config'
import grabVideo from './render/grabVideo'


function render() {

    newProjCreated()

    emptyFieldAlert(function (event, data) {
        // dialog
        fieldEmpty(event, data)
    })

    delProConfirm(function (event, data) {
        //dialog
        confirm(data, function () {
            event.reply(ipcKeys.delProConfirm)
        })
    })

    createProLoading()

    grabVideo()
}

export default render



