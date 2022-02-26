import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode } from '../utils/config';


function getStruSimilarity(callback) {
    pyProcess(epMode.POST,
        (datas) => {
            callback(JSON.parse(datas.toString("utf8")));
        },
        [apiArgs.getStructSimilarity]
    );
};

export default getStruSimilarity;

