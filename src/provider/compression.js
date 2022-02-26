import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode, tmpVideoDirectory } from '../utils/config';


function compression(callback, videoPath, width, height, fps, format) {
    pyProcess(epMode.POST,
        (datas) => {
            callback(datas.toString("utf8"));
        },
        [apiArgs.compression, (tmpVideoDirectory() + '/' + videoPath).toString("utf8"), tmpVideoDirectory().toString("utf8"), ('' + width).toString("utf8"), ('' + height).toString("utf8"), ('' + fps).toString("utf8"), format.toString("utf8")]
    );
};

export default compression;

