import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode } from '../utils/config';


function getFaceDetection(callback) {
    pyProcess(epMode.POST,
        (datas) => {
            let array = JSON.parse(datas.toString("utf8"))
            let list = array.sort(function (a, b) { return parseInt(a.filename) - parseInt(b.filename) });
            callback(list);
        },
        [apiArgs.getFaceDetection]
    );
};

export default getFaceDetection;

