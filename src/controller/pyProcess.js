import { execFile, spawn } from "child_process";
import {
  developmentPath,
  productionPath,
  guessPackaged,
  apiArgs,
  epMode,
  pyVenvPath,
} from "../utils/config";

// to verify is under prodution or development
export function getMode() {
  if (guessPackaged() == true) {
    console.log(".....production mode.....");
    return "production";
  } else {
    console.log(".....development mode.....");
    return "development";
  }
}

// prepare the database
export function initPyProcess() {
  pyProcess(
    epMode.GET,
    function (data) {
      console.log("database connected : " + data.toString("utf8"));
    },
    [apiArgs.init]
  );
}

// return the data from python based on development mode or production mode
export function pyProcess(mode, widget, args) {
  if (getMode() == "development") {
    var argsMain = [developmentPath()];
    argsMain.push.apply(argsMain, args);
    console.log(argsMain);
    try {
      if (mode == epMode.GET) {
        let datasss = "";
        spawn(pyVenvPath(), argsMain)
          .stdout.on("data", (data) => {
            datasss = datasss + data;
          })
          .on("end", () => {
            widget(datasss);
          });
        argsMain = [];
      } else if (mode == epMode.POST) {
        let datasss = "";
        spawn(pyVenvPath(), argsMain)
          .stdout.on("data", (data) => {
            datasss = datasss + data;
          })
          .on("end", () => {
            widget(datasss);
          });
        argsMain = [];
      }
    } catch (e) {
      console.log(e);
      console.log("file not found " + fileName);
    }
  } else if (getMode() == "production") {
    var argsMain = [];
    argsMain.push.apply(argsMain, args);
    console.log([productionPath(), argsMain]);
    try {
      if (mode == epMode.GET) {
        execFile(productionPath(), argsMain, {}, (error, stdout, stderror) => {
          console.log(error);
          console.log(stderror);
          widget(stdout);
        });
        argsMain = [];
      } else if (mode == epMode.POST) {
        execFile(productionPath(), argsMain, {}, (error, stdout, stderror) => {
          console.log(error);
          console.log(stderror);
          widget(stdout);
        });
        argsMain = [];
      }
    } catch (e) {
      console.log(e);
    }
  }
}

// close py shell
export function closePyProcess() {
  if (getMode() == "development") {
    try {
      spawn(pyVenvPath(), [developmentPath()]).disconnect;
      spawn(pyVenvPath(), [developmentPath()]).killed;
    } catch (e) {
      console.log(e);
      console.log("file not found " + fileName);
    }
  } else if (getMode() == "production") {
    try {
      execFile(productionPath()).disconnect;
      spawn(productionPath()).killed;
    } catch (e) {
      console.log(e);
      console.log("file not found " + fileName);
    }
  }
}
