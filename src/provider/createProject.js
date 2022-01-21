import fs from "fs";
import { pyProcess } from "../controller/pyProcess";
import { apiArgs, epMode, prefKeys, tmpVideoDirectory } from '../utils/config';
import { prefs, prefsClear } from '../utils/prefs';


function createProject(callback, projectName) {

    // get vieo info from selected video
    let selVideoFileName = prefs(prefKeys.selVideoFileName)
    let selVideoPath = prefs(prefKeys.selVideoPath)

    // store video path of tmp in pref
    let destDir = tmpVideoDirectory()

    // double verify vieo info in case user cleared or not
    if (projectName != undefined && selVideoFileName != undefined && selVideoPath != undefined && destDir != undefined) {

        // if file already exists it will overwrite the process will flash the screen
        // to avoid that check the file is exists or not the proceed for copy
        fs.access(destDir + '/' + selVideoFileName, async (err) => {
            console.log('check file exists ' + err)
            if (err == null) {
                console.log("copy to tmp video exists skip copy")
                pyCreate()
            } else {
                fs.copyFile(selVideoPath + '/' + selVideoFileName, destDir + '/' + selVideoFileName, async (err) => {
                    if (err == null) {
                        console.log("copy to tmp successfull")
                        pyCreate()
                    } else {
                        console.log("copy to tmp failed " + err)
                    }
                })
            }
        })

        let pyCreate = () => {
            pyProcess(epMode.POST,
                (datas) => {
                    prefsClear(prefKeys.selVideoFileName)
                    prefsClear(prefKeys.selVideoPath)
                    console.log("Copy video to tmp process successfully finished")
                    callback(JSON.parse(datas.toString("utf8")));
                },
                [apiArgs.createProject, projectName.toString("utf8"), selVideoFileName.toString("utf8"), destDir.toString("utf8")]
            );
        }
    } else {
        console.log('create project missing param-----> ' + "1 : " + selVideoFileName + " 2 : " + selVideoPath + " 3 : " + destDir + " 3 : " + projectName)
    }
};

export default createProject;

