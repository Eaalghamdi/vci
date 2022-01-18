<template>
  <div class="content"></div>
  <router-view />
</template>

<style>
html {
  font-size: 14px;
}
:root {
  --surface-a: #1e1e1e;
  --surface-b: #121212;
  --surface-c: rgba(255, 255, 255, 0.03);
  --surface-d: #383838;
  --surface-e: #1e1e1e;
  --surface-f: #1e1e1e;
  --text-color: rgba(255, 255, 255, 0.87);
  --text-color-secondary: rgba(255, 255, 255, 0.6);
  --primary-color: #81c784;
  --primary-color-text: #212529;
  --font-family: -apple-system, Roboto, BlinkMacSystemFont, Segoe UI, Roboto,
    Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji,
    Segoe UI Symbol;
}
body {
  margin: 0;
  overflow-x: hidden;
  overflow-y: auto;
  background-color: black;
  /*  font-family: var(--font-family); */
  font-family: "Roboto", sans-serif;
  font-weight: 400;
  color: var(--text-color);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.content {
  color: var(--text-color);
}

a:link {
  text-decoration: none;
}

:focus {
  outline: none;
}
.p-inputtext:enabled:focus {
  border-color: black;
}
.p-inputtext:enabled:hover {
  border-color: black;
}

*::-webkit-scrollbar {
  width: 12px;
}

*::-webkit-scrollbar-track {
  background: black;
}

*::-webkit-scrollbar-thumb {
  background-color: #81c784;
  border-radius: 20px;
  border: 3px solid #81c784;
}

.p-panel .p-panel-header .p-panel-title {
  font-weight: 800;
  font-size: large;
}
</style>
