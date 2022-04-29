import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode, tmpVideoDirectory } from '../utils/config';


function edgeDetection(callback, framePath, mode, submode, thrHold1, thrHold2) {
    pyProcess(epMode.POST,
        (datas) => {
            callback(datas.toString("utf8"));
        },
        [apiArgs.edgeDetection, (tmpVideoDirectory() + '/' + framePath).toString("utf8"), mode.toString("utf8"), submode.toString("utf8"), ('' + thrHold1).toString("utf8"), ('' + thrHold2).toString("utf8")]
    );
};

export default edgeDetection;

