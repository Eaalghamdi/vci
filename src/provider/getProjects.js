import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode } from "../utils/config";


function getProjects(callback) {
    pyProcess(epMode.GET,
        (datas) => {
            callback(JSON.parse(datas.toString("utf8")));
        },
        [apiArgs.getProjects]
    );
};

export default getProjects;

