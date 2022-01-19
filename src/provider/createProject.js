import fs from 'fs'
import path from 'path'
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
        fs.access(destDir, (err) => {
            if (err)
                fs.mkdirSync(destDir);
            copyFile(selVideoPath + '/' + selVideoFileName, destDir + '/' + selVideoFileName);
        });

        function copyFile(src, dest) {
            let readStream = fs.createReadStream(src);
            readStream.once('error', (err) => {
                console.log('error while video copying');
                console.log(err);
            });
            readStream.once('end', () => {
                console.log('done video copying');
                pyProcess(epMode.POST,
                    (datas) => {
                        prefsClear(prefKeys.selVideoFileName)
                        prefsClear(prefKeys.selVideoPath)
                        console.log('video info has been cleared')
                        callback(JSON.parse(datas.toString("utf8")));
                    },
                    [apiArgs.createProject, projectName.toString("utf8"), selVideoFileName.toString("utf8"), destDir.toString("utf8")]
                );
            });
            readStream.pipe(fs.createWriteStream(dest));
        }
    } else {
        console.log('create project missing param-----> ' + "1 : " + selVideoFileName + " 2 : " + selVideoPath + " 3 : " + destDir + " 3 : " + projectName)
    }
};

export default createProject;

