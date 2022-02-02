import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode, tmpVideoDirectory } from '../utils/config';


function shotBouDetec(callback, videoFileName, method, treshold) {
    let methodVal

    if (method == 1) {
        methodVal = "ContentDetector"
    } else {
        methodVal = "threshold_detector"
    }

    if (methodVal != undefined) {
        pyProcess(epMode.POST,
            (datas) => {
                callback(JSON.parse(datas.toString("utf8")));
            },
            [apiArgs.shotBounDetec, tmpVideoDirectory().toString("utf8"), videoFileName.toString("utf8"), methodVal.toString("utf8"), ('' + treshold).toString("utf8")]
        );
    }
};

export default shotBouDetec;

