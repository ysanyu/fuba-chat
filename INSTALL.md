# 福利吧聊天室桌面客户端 - 安装说明

## 方法一：使用 Electron (推荐)

### 1. 安装 Electron

```bash
# 使用国内镜像加速
npm install electron --registry=https://registry.npmmirror.com
```

如果安装失败，可以尝试：

```bash
# 设置 Electron 镜像
export ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron/
export ELECTRON_CUSTOM_DIR=clic
npm install electron
```

### 2. 启动应用

```bash
npm start
```

## 方法二：使用 WebView (无需 Electron)

如果你无法安装 Electron，可以使用简单的 WebView 应用：

### 1. 使用 Python + PyQt (需要 Python 环境)

```bash
pip install PyQt6 PyQt6-WebEngine
python webview_app.py
```

### 2. 使用系统浏览器 + PWA

1. 打开浏览器访问 `https://fuliba2023.net/forum.php`
2. 登录后，点击浏览器地址栏的"安装"图标
3. 将聊天室安装为 PWA 应用

## Cookie 获取教程

1. 在浏览器中登录 [福利吧论坛](https://fuliba2023.net)
2. 按 `F12` 打开开发者工具
3. 切换到 `Console` (控制台) 标签
4. 输入 `document.cookie` 并回车
5. 复制输出的完整 Cookie 字符串

## 常见问题

### Electron 安装失败？

- 尝试使用国内镜像
- 检查网络连接
- 确保 Node.js 版本 >= 16

### Cookie 输入后无法登录？

- 检查 Cookie 是否完整复制
- 确认 Cookie 未过期
- 尝试重新获取 Cookie

---

**项目文件说明**：

- `main.js` - Electron 主进程
- `login.html` - 登录界面
- `login.js` - 登录逻辑
- `preload.js` - 预加载脚本
- `package.json` - 项目配置

**开发者**: ysanyu
