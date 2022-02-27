import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode, tmpVideoDirectory } from '../utils/config';


function saliency(callback, frameDir) {
    pyProcess(epMode.POST,
        (datas) => {
            callback(datas.toString("utf8"));
        },
        [apiArgs.saliency, (tmpVideoDirectory() + '/' + frameDir).toString("utf8")]
    );
};

export default saliency;

