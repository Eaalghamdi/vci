import fs from 'fs'
import path from 'path'
import { pyProcess } from "../controller/pyProcess"
import { apiArgs, epMode } from '../utils/config'


function deleteProject(selectedIds, reload, projects) {
    if (selectedIds.length != 0) {
        for (let i = 0; i < selectedIds.length; i++) {
            pyProcess(epMode.POST,
                (datas) => {
                    if (JSON.parse(datas.toString("utf8"))['data'] == 'completed') {
                        fs.unlink(projects[i].VideoPath + '/' + projects[i].VideoTitle, function (err) {
                            console.log('error while delete video ' + err)
                        });
                        reload(selectedIds[i])
                    }
                },
                [apiArgs.deleteProject, selectedIds[i]]
            );
        }
    }
};

export default deleteProject;

