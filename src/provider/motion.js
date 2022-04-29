import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode, tmpVideoDirectory } from '../utils/config';


function motion(callback, videoPath) {
    pyProcess(epMode.POST,
        (datas) => {
            callback(datas.toString("utf8"));
        },
        [apiArgs.motion, (tmpVideoDirectory() + '/' + videoPath).toString("utf8")]
    );
};

export default motion;

