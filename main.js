const { app, BrowserWindow, ipcMain, session } = require('electron');
const path = require('path');

let mainWindow;
let chatWindow;
let rawCookies = '';

function createLoginWindow() {
  mainWindow = new BrowserWindow({
    width: 500, height: 600,
    title: '福利吧聊天室 - 登录',
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js')
    },
    resizable: false, center: true
  });
  mainWindow.loadFile('login.html');
}

function createChatWindow(cookies) {
  rawCookies = cookies;

  const ses = session.defaultSession;
  ses.webRequest.onBeforeSendHeaders((details, callback) => {
    if (rawCookies && (
      details.url.includes('fuliba2023.net') ||
      details.url.includes('wnflb2023.com') ||
      details.url.includes('uc_server')
    )) {
      details.requestHeaders['Cookie'] = rawCookies;
    }
    callback({ requestHeaders: details.requestHeaders });
  });

  chatWindow = new BrowserWindow({
    width: 900, height: 700, minWidth: 600, minHeight: 500,
    title: '福利吧聊天室',
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js')
    },
    show: false, center: true
  });

  chatWindow.loadFile('chatroom.html');
  chatWindow.once('ready-to-show', () => chatWindow.show());
  chatWindow.on('closed', () => app.quit());
}

ipcMain.on('set-cookies', (event, cookies) => {
  mainWindow.close();
  createChatWindow(cookies);
});

app.whenReady().then(() => {
  createLoginWindow();
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createLoginWindow();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
