import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode } from '../utils/config';


function getMotion(callback) {
    pyProcess(epMode.POST,
        (datas) => {
            let array = JSON.parse(datas.toString("utf8"))
            let list = array.sort(function (a, b) { return parseInt(a.videoname) - parseInt(b.videoname) });
            callback(list);
        },
        [apiArgs.getMotion]
    );
};

export default getMotion;

