import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode } from '../utils/config';


function getCompression(callback) {
    pyProcess(epMode.POST,
        (datas) => {
            let array = JSON.parse(datas.toString("utf8"))
            let list = array.sort(function (a, b) { return parseInt(a.filename) - parseInt(b.filename) });
            callback(list);
        },
        [apiArgs.getCompression]
    );
};

export default getCompression;

