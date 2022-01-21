import { closePyProcess } from '../controller/pyProcess'

function exitProcess() {
    console.log('preparing for exit...')
    closePyProcess()
}

export default exitProcess