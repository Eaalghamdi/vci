module.exports = {
  chainWebpack: config => {
    config.module.rules.delete('eslint');
  },
  pluginOptions: {
    electronBuilder: {
      nodeModulesPath: ['./node_modules'],
      nodeIntegration: true,
      builderOptions: {
        asar: true,
        extraResources: ["./dist/**", "./base/dist/**"],
        appId: "com.auvana.ai",
        productName: 'AUVANA',
        // afterSign: "./src/build/notarize.js",
        dmg: {
          sign: false,
          background: null,
          backgroundColor: "#ffffff",
          window: {
            width: 400,
            height: 300
          },
          contents: [
            {
              x: 100,
              y: 100
            },
            {
              x: 300,
              y: 100,
              type: "link",
              path: "/Applications"
            }
          ]
        },
        mac: {
          category: "productivity",
          target: "dmg",
          entitlements: "./src/build/entitlements.mac.plist",
          entitlementsInherit: "./src/build/entitlements.mac.plist",
          hardenedRuntime: true,
          gatekeeperAssess: false,
        },
        win: {
          target: ["nsis"]
        },
        linux: {
          target: "AppImage",
          category: "Utility"
        }
      },
    },
  },
};
