import { init, productionPath, tmpVideoDirectory } from '../utils/config'
import { prefsClearAll } from '../utils/prefs'
import { initPyProcess } from '../controller/pyProcess'

function initProcess(basepath, overwrite) {
    console.log('initialization is processing...')

    if (prefsClearAll() == "completed") {
        console.log('clearing previous pref data...')
        var process = init(basepath, overwrite)
        console.log('initialization completed...')
        if (process.length == 2) {
            console.log('production path : ' + productionPath())
            console.log('tmp path : ' + tmpVideoDirectory())
            // make sure database has created
            console.log('initiate py process...')
            initPyProcess()

            console.log('initiate py process done...')
            return 'completed'
        }
    }
}

export default initProcess

