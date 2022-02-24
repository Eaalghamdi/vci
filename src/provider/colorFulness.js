import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode, tmpVideoDirectory } from '../utils/config';


function colorFulness(callback, mode, framePath) {
    pyProcess(epMode.POST,
        (datas) => {
            callback(datas.toString("utf8"));
        },
        [apiArgs.colorFulness, (tmpVideoDirectory() + '/' + framePath).toString("utf8"), mode.toString("utf8")]
    );
};

export default colorFulness;

