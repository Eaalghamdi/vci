module.exports = {
    pluginOptions: {
        electronBuilder: {
            nodeIntegration: true,
            builderOptions: {
            extraResources: [
                "./backend/dist/**"
              ],
            }
        }
    }
}
