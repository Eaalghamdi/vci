import { nativeImage } from "electron"
import { assetsPath } from "../utils/config";
import path from 'path'


const alertYellow = nativeImage.createFromPath(path.join(assetsPath(), 'alert_yellow.png'))

export { alertYellow }