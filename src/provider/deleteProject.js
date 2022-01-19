import fs from 'fs'
import { pyProcess } from "../controller/pyProcess"
import { apiArgs, epMode } from '../utils/config'


function deleteProject(selectedIds, reload, projects, isCompleted) {

    if (selectedIds.length != 0) {
        for (let i = 0; i < selectedIds.length; i++) {
            pyProcess(epMode.POST,
                (datas) => {
                    if (JSON.parse(datas.toString("utf8"))['data'] == 'completed') {
                        fs.unlink(projects[i].VideoPath + '/' + projects[i].VideoTitle, function (err) {
                            console.log('error while delete video ' + err)
                        });
                        let selList = selectedIds
                        let index = selList
                            .map((x) => {
                                return x;
                            })
                            .indexOf(selectedIds[i]);
                        selList.splice(index, 1);

                        reload(selList)
                    }
                },
                [apiArgs.deleteProject, selectedIds[i]]
            );
            if (selectedIds.length == (i + 1)) {
                isCompleted()
            }
        }
    }
};

export default deleteProject;

