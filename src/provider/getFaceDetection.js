import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode } from '../utils/config';


function getFaceDetection(callback) {
    pyProcess(epMode.POST,
        (datas) => {
            callback(JSON.parse(datas.toString("utf8")));
        },
        [apiArgs.getFaceDetection]
    );
};

export default getFaceDetection;

