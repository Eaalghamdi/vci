module.exports = {
  chainWebpack: config => {
    config.module.rules.delete('eslint');
},
  pluginOptions: {
    electronBuilder: {
      nodeIntegration: true,
      builderOptions: {
        extraResources: ["./dist/**"],
      },
    },
  },
};

