import { protocol } from 'electron'
import { tmpVideoDirectory } from "../utils/config"

function registerLocalVideoProtocol() {
    protocol.registerFileProtocol('video-server', (request, callback) => {
        const url = request.url.replace(/^video-server:\/\//, '')
        // Decode URL to prevent errors when loading filenames with UTF-8 chars or chars like "#"
        const decodedUrl = decodeURI(url) // Needed in case URL contains spaces
        try {
            // eslint-disable-next-line no-undef
            return callback(tmpVideoDirectory() + '/' + decodedUrl)
        } catch (error) {
            console.error(
                'ERROR: registerLocalVideoProtocol: Could not get file path:',
                error
            )
        }
    })
}

export default registerLocalVideoProtocol