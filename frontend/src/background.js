"use strict";

import { app, protocol, BrowserWindow } from "electron";
import { createProtocol } from "vue-cli-plugin-electron-builder/lib";
import installExtension, { VUEJS3_DEVTOOLS } from "electron-devtools-installer";
const path = require("path");

const isDevelopment = process.env.NODE_ENV !== "production";

// Scheme must be registered before the app is ready
protocol.registerSchemesAsPrivileged([
  { scheme: "app", privileges: { secure: true, standard: true } },
]);



/*************************************************************
 * py process
 *************************************************************/

const PY_MAC_DIST_FOLDER = "../../app.asar.unpacked/daemon";
const PY_WIN_DIST_FOLDER = "../../app.asar.unpacked/daemon";
const PY_DIST_FILE = "daemon";
const PY_FOLDER = "../backend";
const PY_MODULE = "api_server"; // without .py suffix

let pyProc = null;
let ws = null;

const guessPackaged = () => {
  let packed;
  if (process.platform === "win32") {
    const fullPath = path.join(__dirname, PY_WIN_DIST_FOLDER);
    packed = require("fs").existsSync(fullPath);
    console.log(fullPath);
    console.log(packed);
    return packed;
  }
  const fullPath = path.join(__dirname, PY_MAC_DIST_FOLDER);
  packed = require("fs").existsSync(fullPath);
  console.log(fullPath);
  console.log(packed);
  return packed;
};

const getScriptPath = () => {
  if (!guessPackaged()) {
    return path.join(PY_FOLDER, PY_MODULE + ".py");
  }
  if (process.platform === "win32") {
    return path.join(__dirname, PY_WIN_DIST_FOLDER, PY_DIST_FILE + ".exe");
  }
  return path.join(__dirname, PY_MAC_DIST_FOLDER, PY_DIST_FILE);
};

const createPyProc = () => {
  let script = getScriptPath();
  let processOptions = {};
  //processOptions.detached = true;
  //processOptions.stdio = "ignore";
  pyProc = null;
  if (guessPackaged()) {
    try {
      console.log("Running python executable: ");
      const Process = require("child_process").spawn;
      pyProc = new Process(script, [], processOptions);
    } catch {
      console.log("Running python executable: Error: ");
      console.log("Script " + script);
    }
  } else {
    console.log("Running python script");
    console.log("Script " + script);

    const Process = require("child_process").spawn;
    pyProc = new Process("python", [script], processOptions);
  }
  if (pyProc != null) {
    pyProc.stdout.setEncoding("utf8");

    pyProc.stdout.on("data", function(data) {
      process.stdout.write(data.toString());
    });

    pyProc.stderr.setEncoding("utf8");
    pyProc.stderr.on("data", function(data) {
      //Here is where the error output goes
      process.stdout.write("stderr: " + data.toString());
    });

    pyProc.on("close", function(code) {
      //Here you can get the exit code of the script
      console.log("closing code: " + code);
    });

    console.log("child process success");
  }
  //pyProc.unref();
};

const exitPyProc = e => {};

app.on("will-quit", exitPyProc);

/*************************************************************
 * window management
 *************************************************************/

async function createWindow() {
  

  // Create the browser window.
  const win = new BrowserWindow({
    width: 1400,
    height: 900,
    webPreferences: {
      // Use pluginOptions.nodeIntegration, leave this alone
      // See nklayman.github.io/vue-cli-plugin-electron-builder/guide/security.html#node-integration for more info
      webSecurity: false,
      enableRemoteModule: true,
      nodeIntegration: process.env.ELECTRON_NODE_INTEGRATION,
      contextIsolation: !process.env.ELECTRON_NODE_INTEGRATION,
    },
  });

  if (process.env.WEBPACK_DEV_SERVER_URL) {
    // Load the url of the dev server if in development mode
    await win.loadURL(process.env.WEBPACK_DEV_SERVER_URL);
    if (!process.env.IS_TEST) win.webContents.openDevTools();
  } else {
    createProtocol("app");
    // Load the index.html when not in development
    win.loadURL("app://./index.html");
    
    win.webContents.openDevTools()    // delete this once you finished debugging in prodcution
  }
  createPyProc();
}

// Quit when all windows are closed.
app.on("window-all-closed", () => {
  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== "darwin") {
    app.quit();
  }
});

app.on("activate", () => {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) createWindow();
});

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on("ready", async () => {
  if (isDevelopment && !process.env.IS_TEST) {
    // Install Vue Devtools
    try {
      await installExtension(VUEJS3_DEVTOOLS);
    } catch (e) {
      console.error("Vue Devtools failed to install:", e.toString());
    }
  }
  createWindow();
});

// app.on('ready', pythonServer())
// 1. Introduce dialog box and IPC communication module
const ipc = require("electron").ipcMain;
const dialog = require("electron").dialog;


global.outDir = path.join(__dirname, "../assets/temp");
global.appPath = app.getAppPath();
const homeDir = app.getPath('home');
const desktopDir = path.resolve(homeDir, 'Desktop');

ipc.on("open-file-upload-dialog", function (event) {
  // If the platform is 'win32' or 'Linux'
  if (process.platform !== "darwin") {
    // Resolves to a Promise<Object>
    dialog
      .showOpenDialog({
        title: "Select the File to be uploaded",
        defaultPath: desktopDir,

        // Restricting the user to only Text Files.
        filters: [
          {
            name: "Video Files",
            extensions: ["mp4"],
          },
        ],
        // Specifying the File Selector Property
        properties: ["openFile"],
      })
      .then((file) => {
        // Stating whether dialog operation was
        // cancelled or not.
        // console.log(file.canceled);
        if (!file.canceled) {
          // Updating the GLOBAL filepath variable
          // to user-selected file.
          let filepath = file.filePaths[0].toString();
          // console.log(global.filepath);
        }
      })
      .catch((err) => {
        console.log(err);
      });
  } else {
    // If the platform is 'darwin' (macOS)
    dialog
      .showOpenDialog({
        title: "Select the File to be uploaded",
        defaultPath: desktopDir,
        filters: [
          {
            name: "Video Files",
            extensions: ["mp4"],
          },
        ],
        // Specifying the File Selector and Directory
        // Selector Property In macOS
        properties: ["openFile", "openDirectory"],
      })
      .then((file) => {
        // console.log(file.canceled);
        if (!file.canceled) {
          let filepath = file.filePaths[0].toString();
          
          var fs = require("fs");
          const { basename } = require("path");
          let videoName = basename(filepath, '.mp4');
          let videoFolder = path.join(global.outDir,  videoName);
          let videoPath =  path.join(videoFolder, basename(filepath));
         
  

          if (!fs.existsSync(videoFolder)) {
            fs.mkdirSync(videoFolder, {
              recursive: true,
            });
          }
  
        
          fs.copyFile(filepath, videoPath, (err) => {
            if (err) throw err;
              console.log("There is an error copyign your file")
          });
         const newProject = {videoPath: filepath, ProjectTitle: videoName}
         
    
          event.sender.send("save-finished", newProject);
        }
      })
      .catch((err) => {
        console.log(err);
      });
  }
});

// Exit cleanly on request from parent process in development mode.
if (isDevelopment) {
  if (process.platform === "win32") {
    process.on("message", (data) => {
      if (data === "graceful-exit") {
        app.quit();
        exitPyProc();
      }
    });
  } else {
    process.on("SIGTERM", () => {
      app.quit();
      exitPyProc();
    });
  }
}
