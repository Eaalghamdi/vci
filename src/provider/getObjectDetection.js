import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode } from '../utils/config';


function getObjectDetection(callback) {
    pyProcess(epMode.POST,
        (datas) => {
            let array = JSON.parse(datas.toString("utf8"))
            let list = array.sort(function (a, b) { return parseInt(a.imgname) - parseInt(b.imgname) });
            callback(list);
        },
        [apiArgs.getObjectdetection]
    );
};

export default getObjectDetection;

