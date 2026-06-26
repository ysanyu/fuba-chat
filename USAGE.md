# 福利吧聊天室桌面客户端 - 使用说明

## 项目简介

这是一个基于 Electron 的福利吧聊天室桌面客户端，支持 Cookie 登录，可以快速访问网页版聊天室的所有功能。

## 文件说明

```
fuba-chat/
├── package.json       # 项目配置文件
├── main.js           # Electron 主进程
├── preload.js        # 预加载脚本（安全桥梁）
├── login.html        # 登录界面（Cookie 输入）
├── login.js          # 登录界面的业务逻辑
├── webview_app.py   # Python WebView 版本（备用）
├── README.md         # 项目说明文档
├── INSTALL.md        # 安装说明文档
└── USAGE.md         # 本文件 - 使用说明
```

## 快速开始

### 方法一：使用 Electron 版本（推荐）

#### 1. 安装依赖

```bash
cd /Users/ysanyu/Desktop/fuba-chat
npm install
```

如果遇到安装问题，请参考 `INSTALL.md` 中的详细解决方案。

#### 2. 获取 Cookie

1. 在浏览器中访问 [福利吧论坛](https://fuliba2023.net) 并登录
2. 按 `F12` 打开开发者工具
3. 切换到 `Console`（控制台）标签页
4. 输入以下命令并回车：
   ```javascript
   document.cookie
   ```
5. 复制输出的完整 Cookie 字符串（例如：`bbs_sid=xxx; bbs_auth=xxx; ...`）

⚠️ **注意**：Cookie 包含你的登录信息，请勿分享给他人！

#### 3. 启动应用

```bash
npm start
```

#### 4. 输入 Cookie

将复制的 Cookie 字符串粘贴到应用的文本框中，点击"进入聊天室"按钮。

应用将自动打开聊天室窗口，并加载福利吧论坛页面，自动点击聊天室按钮打开聊天室。

### 方法二：使用 Python WebView 版本（备用）

如果无法安装 Electron，可以使用 Python 版本：

#### 1. 安装依赖

```bash
pip install PyQt6 PyQt6-WebEngine
```

#### 2. 启动应用

```bash
python webview_app.py
```

#### 3. 输入 Cookie

同样需要输入 Cookie 才能登录。

### 方法三：使用浏览器 PWA（最简单）

如果不想安装任何软件，可以直接使用浏览器的 PWA 功能：

1. 在浏览器中访问 [福利吧论坛](https://fuliba2023.net) 并登录
2. 点击浏览器地址栏右侧的"安装"图标（不同浏览器位置可能不同）
3. 将网站安装为 PWA 应用
4. 直接从桌面或开始菜单启动应用

## 功能特性

- ✅ 支持 Cookie 登录
- ✅ 完整聊天室功能（与网页版一致）
- ✅ 自动打开聊天室
- ✅ 原生桌面体验
- ✅ 支持拖拽移动聊天室按钮
- ✅ 支持调整聊天室窗口大小

## 常见问题

### Q1: Cookie 输入后无法登录？

**解决方法**：
1. 检查 Cookie 是否完整复制（不要漏掉任何一个）
2. 确认 Cookie 未过期（重新登录论坛获取新的 Cookie）
3. 检查 Cookie 格式是否正确（应该是 `name=value;` 的格式）

### Q2: 聊天室无法自动打开？

**解决方法**：
1. 检查网络连接是否正常
2. 确认论坛网站可正常访问
3. 手动点击页面右下角的聊天室按钮

### Q3: Electron 安装失败？

**解决方法**：
1. 参考 `INSTALL.md` 中的详细解决方案
2. 使用国内镜像加速下载
3. 尝试使用 Python WebView 版本或浏览器 PWA

### Q4: 应用界面显示异常？

**解决方法**：
1. 检查屏幕尺寸和分辨率
2. 尝试调整应用窗口大小
3. 重启应用

## 开发说明

### 修改登录界面样式

编辑 `login.html` 中的 CSS 代码。

### 修改主窗口行为

编辑 `main.js` 中的 `createChatWindow` 函数。

### 调试模式

在 `main.js` 中取消注释以下代码以打开开发者工具：

```javascript
// mainWindow.webContents.openDevTools();
// chatWindow.webContents.openDevTools();
```

## 技术栈

- **Electron**: 28+
- **Node.js**: 16+
- **Python** (备用版本): 3.6+ (如果使用 WebView 版本)

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

---

**开发者**: ysanyu  
**创建时间**: 2026-06-26  
**版本**: 1.0.0
