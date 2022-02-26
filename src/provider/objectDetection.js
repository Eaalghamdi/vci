import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode, tmpVideoDirectory } from '../utils/config';


function objectDetection(callback, framePath, thrHold) {
    pyProcess(epMode.POST,
        (datas) => {
            callback(datas.toString("utf8"));
        },
        [apiArgs.objectdetection, (tmpVideoDirectory() + '/' + framePath).toString("utf8"), ('' + thrHold).toString("utf8")]
    );
};

export default objectDetection;

