import { nativeImage } from "electron"
import { assetsPath } from "../utils/config";


const alertYellow = nativeImage.createFromPath(assetsPath() + '/' + 'alert_yellow.png')

export { alertYellow }