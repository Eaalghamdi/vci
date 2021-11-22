"use strict";
import { dialog } from "electron";
const path = require("path");
const fs = require("fs");

export function uploadVideoFile() {
  // opens a window to choose file
  dialog.showOpenDialog({ properties: ["openFile"] }).then((result) => {
    // checks if window was closed
    if (result.canceled) {
      console.log("No file selected!");
    } else {
      // get first element in array which is path to file selected
      const filePath = result.filePaths[0];

      // get file name
      const fileName = path.basename(filePath);

      // path to app data + fileName = "C:\Users\John\AppData\Roaming\app_name\picture.png"
      const imgFolderPath = path.join("desktop/", fileName);

      // copy file from original location to app data folder
      fs.copyFile(filePath, imgFolderPath, (err) => {
        if (err) throw err;
        console.log(fileName + " uploaded.");
      });
    }
  });
}
