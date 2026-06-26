const { contextBridge, ipcRenderer } = require('electron');
contextBridge.exposeInMainWorld('electronAPI', {
  sendCookies: (cookies) => ipcRenderer.send('set-cookies', cookies)
});
