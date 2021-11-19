
const {PythonShell} = require ('python-shell')

function myServer () {
    let options = {
        pythonPath: '/Users/user/anaconda3/envs/auvanaServer/bin/python',
 
      };
    
     PythonShell.run('/Users/user/Desktop/PROJECTS/DesktopApp/AUVANA_electron_vue_2/auvana/backend/api_server.py', options, function (err){
      if (err)
        throw err;
      console.log('server stopped');
      console.log(scriptPath);
    }); 

}

myServer()

