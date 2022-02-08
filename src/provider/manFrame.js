import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode, tmpVideoDirectory, resDefaultHeight, resDefaultWidth } from '../utils/config';


function manFrame(callback, videoFileName, time) {
    pyProcess(epMode.POST,
        (datas) => {
            callback(JSON.parse(datas.toString("utf8")));
        },
        [apiArgs.manFrame, tmpVideoDirectory().toString("utf8"), videoFileName.toString("utf8"), ('' + time).toString("utf8"), ('' + resDefaultHeight).toString("utf8"), ('' + resDefaultWidth).toString("utf8")]
    );
};

export default manFrame;

