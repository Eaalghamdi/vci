import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode, tmpVideoDirectory } from '../utils/config';


function faceDetection(callback, framePath, minNeig) {
    pyProcess(epMode.POST,
        (datas) => {
            callback(datas.toString("utf8"));
        },
        [apiArgs.faceDetection, (tmpVideoDirectory() + '/' + framePath).toString("utf8"), ('' + minNeig).toString("utf8")]
    );
};

export default faceDetection;

