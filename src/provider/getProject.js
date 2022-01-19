import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode } from "../utils/config";


function getProject(callback, id) {
    pyProcess(epMode.GET,
        (datas) => {
            callback(JSON.parse(datas.toString("utf8")));
        },
        [apiArgs.getProject, id]
    );
};

export default getProject;

