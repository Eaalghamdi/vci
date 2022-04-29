import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode, tmpVideoDirectory } from '../utils/config';


function struSimilarity(callback, frameDir) {
    pyProcess(epMode.POST,
        (datas) => {
            callback(datas.toString("utf8"));
        },
        [apiArgs.structSimilarity, (tmpVideoDirectory() + '/' + frameDir).toString("utf8")]
    );
};

export default struSimilarity;

