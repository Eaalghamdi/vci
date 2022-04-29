import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode } from '../utils/config';


function getStruSimilarity(callback) {
    pyProcess(epMode.POST,
        (datas) => {
            let array = JSON.parse(datas.toString("utf8"))
            let list = array.sort(function (a, b) { return parseInt(a.imganame) - parseInt(b.imganame) });
            callback(list);
        },
        [apiArgs.getStructSimilarity]
    );
};

export default getStruSimilarity;

