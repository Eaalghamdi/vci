import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode } from '../utils/config';


function getMotion(callback) {
    pyProcess(epMode.POST,
        (datas) => {
            callback(JSON.parse(datas.toString("utf8")));
        },
        [apiArgs.getMotion]
    );
};

export default getMotion;

