import fs from "fs";


function getGallary(callback, filePath, fileName) {

    let folderName = fileName.substr(0, fileName.lastIndexOf('.'))

    if (fs.existsSync(filePath + '/' + folderName)) {
        let files = fs.readdirSync(filePath + '/' + folderName)

        const regex = /.jpe?g$/gim;
        for (let file of files) {

            // Ignore non jpg files
            if (!file.match(regex)) {
                continue
            }
            let image = {}
            image.name = file
            image.path = filePath + '/' + folderName + '/'

            image.base64 = new Buffer.from(fs.readFileSync(image.path + '/' + image.name)).toString(
                "base64"
            );

            callback(image)
        }
    }
};

export default getGallary;





