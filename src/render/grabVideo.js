import { prefs } from '../utils/prefs'
import { prefKeys } from '../utils/config'
import { fileDir } from './dialogs'
import { openFileDirc } from './ipcs'


function grabVideo() {
    openFileDirc((event, data) => {
        fileDir((file) => {
            if (!file.canceled) {
                let path_array = file.filePaths[0].split('/')
                let selectedFileName = path_array[path_array.length - 1]
                let selectedFilePath = file.filePaths[0].replace(selectedFileName.toString(), '')

                // save the file name and path
                prefs(prefKeys.selVideoFileName, { val: selectedFileName, event: event, task: true })
                prefs(prefKeys.selVideoPath, { val: selectedFilePath, event: event, task: true })

                console.log('selected video name ***** ' + prefs(prefKeys.selVideoFileName))
                console.log('selected video path ***** ' + prefs(prefKeys.selVideoPath))
            }
        })
    })
}

export default grabVideo