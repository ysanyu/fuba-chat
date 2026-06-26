# 福利吧聊天室桌面客户端 - 快速启动指南

## ✅ 项目已完成！

我已经为你创建了一个完整的 Electron 桌面应用，让你可以输入 Cookie 后进入福利吧聊天室。

## 📁 项目文件

所有文件已保存在：`/Users/ysanyu/Desktop/fuba-chat/`

```
fuba-chat/
├── package.json       # 项目配置
├── main.js           # Electron 主进程
├── preload.js        # 预加载脚本
├── login.html        # 登录界面
├── login.js          # 登录逻辑
├── webview_app.py   # Python 备用版本
├── README.md         # 项目说明
├── INSTALL.md        # 安装指南
└── USAGE.md         # 使用说明
```

## 🚀 三种使用方式

### 方式一：Electron 版本（推荐）

```bash
# 1. 进入项目目录
cd /Users/ysanyu/Desktop/fuba-chat

# 2. 安装 Electron（如果失败，参考 INSTALL.md）
npm install electron --registry=https://registry.npmmirror.com

# 3. 启动应用
npm start
```

### 方式二：Python WebView 版本（备用）

```bash
# 1. 安装依赖
pip install PyQt6 PyQt6-WebEngine

# 2. 启动应用
python webview_app.py
```

### 方式三：浏览器 PWA（最简单）

1. 浏览器访问 `https://fuliba2023.net` 并登录
2. 点击地址栏的"安装"图标
3. 将网站安装为桌面应用

## 🔐 如何获取 Cookie？

1. 在浏览器中登录福利吧论坛
2. 按 `F12` 打开开发者工具
3. 切换到 `Console`（控制台）标签
4. 输入 `document.cookie` 并回车
5. 复制输出的完整 Cookie 字符串

## ⚠️ 重要提示

- Cookie 包含你的登录信息，**请勿分享给他人**！
- Cookie 有过期时间，过期后需要重新获取
- 如果遇到问题，请查看 `USAGE.md` 中的常见问题解答

## 📖 详细文档

- **README.md** - 项目介绍和功能特性
- **INSTALL.md** - 详细的安装指南（解决安装问题）
- **USAGE.md** - 完整的使用说明和常见问题

---

**开始使用吧！** 🎉

如果遇到任何问题，请查看详细文档或向我提问。
