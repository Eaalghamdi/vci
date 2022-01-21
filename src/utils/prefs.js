import Store from 'electron-store'
const store = new Store()
import { prefKeys, ipcKeys, prefKeysForClear } from "./config";

export function prefs(key, args = { "val": undefined, "event": undefined, "task": undefined }) {
    if (args["val"] == undefined) {
        var val = store.get(key)
        return val
    } else {
        store.set(key, args["val"])
        if (args["task"] == true) {
            args["event"].reply(ipcKeys.uplVidStatAck)
        }
        return ''
    }
}

export function prefsClear(key, args = { "event": undefined, "key": undefined, "task": undefined }) {
    store.delete(key)
    if (args["task"] == true) {
        args["event"].reply(args["key"])
    }
}

export function prefsClearAll() {
    for (let i = 0; i < Object.keys(prefKeys).length; i++) {
        store.delete(prefKeysForClear[i])
    }
    return 'completed'
}

