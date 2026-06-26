<div align="center">

# 💬 福利吧聊天室

### 一个简洁的福利吧论坛聊天室桌面客户端

[![Version](https://img.shields.io/badge/version-1.0.1-667eea.svg)](https://github.com/ysanyu/fuba-chat/releases)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-blue.svg)](https://github.com/ysanyu/fuba-chat/releases)
[![Electron](https://img.shields.io/badge/built%20with-Electron-47848F.svg)](https://www.electronjs.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**[Releases 下载](https://github.com/ysanyu/fuba-chat/releases)** · **[使用说明](#-使用说明)** · **[开发指南](#-开发指南)**

</div>

---

## 📖 简介

基于 [Electron](https://www.electronjs.org/) 构建的福利吧论坛聊天室桌面客户端。输入 Cookie 即可进入聊天室，无需打开浏览器，提供原生桌面聊天体验。

### ✨ 特性

- **🔐 Cookie 登录** — 输入 Cookie 即可进入，安全便捷
- **💬 气泡式消息** — 自己消息靠右紫色，他人靠左白色
- **😊 表情面板** — 56 个常用表情一键插入
- **↩️ 消息回复** — 支持引用回复，层级清晰
- **🔄 自动轮询** — 每 5 秒拉取新消息，实时同步
- **⏰ 智能时间** — "刚刚"、"N分钟前"、"HH:MM" 自动转换
- **🔗 链接识别** — 消息中的网址自动转为可点击链接
- **👤 头像显示** — 自动加载用户头像
- **📝 消息管理** — 自动裁剪超过 300 条的历史消息，保持流畅
- **🖥️ 跨平台** — 支持 macOS / Windows / Linux

---

## 📸 截图

> 截图待补充，欢迎 PR 提交

---

## 🚀 下载安装

### 系统要求

| 平台 | 最低版本 |
|------|----------|
| macOS | 10.15 (Catalina) |
| Windows | Windows 10 |
| Linux | Ubuntu 18.04+ |

### 方式一：直接下载（推荐）

前往 [Releases 页面](https://github.com/ysanyu/fuba-chat/releases) 下载对应平台的安装包：

| 平台 | 文件 | 说明 |
|------|------|------|
| macOS (Apple Silicon) | `fuliba-chat-1.0.0-arm64.dmg` | M1/M2/M3 芯片 |
| macOS (Intel) | `fuliba-chat-1.0.0-x64.dmg` | Intel 芯片 |
| Windows (安装版) | `fuliba-chat-1.0.0-x64-setup.exe` | 需安装 |
| Windows (便携版) | `fuliba-chat-1.0.0-x64-portable.exe` | 免安装 |
| Linux (AppImage) | `fuliba-chat-1.0.0-x86_64.AppImage` | 直接运行 |
| Linux (deb) | `fuliba-chat-1.0.0-amd64.deb` | Debian/Ubuntu |
| Linux (rpm) | `fuliba-chat-1.0.0-x86_64.rpm` | Fedora/CentOS |

1. 下载对应平台的安装包
2. macOS：打开 `.dmg`，拖动应用到「应用程序」文件夹
3. Windows：双击 `setup.exe` 运行安装程序，或下载 `portable.exe` 免安装直接运行
4. Linux：`chmod +x fuliba-chat-1.0.0-x86_64.AppImage && ./fuliba-chat-1.0.0-x86_64.AppImage`

> **注意**：macOS 首次打开可能提示"无法验证开发者"，右键点击应用 → 选择「打开」即可。

### 方式二：从源码运行

```bash
git clone https://github.com/ysanyu/fuba-chat.git
cd fuba-chat
npm install
npm start
```

---

## 📋 使用说明

### 1. 获取 Cookie

1. 浏览器访问 [fuliba2023.net](https://fuliba2023.net) 并登录
2. 按 `F12` 打开开发者工具
3. 切换到 **Network** 标签
4. 点击任意一个请求
5. 在 **Request Headers** 中找到 `Cookie` 字段，复制完整值

> **⚠️ 重要**：必须从 Network 面板获取 Cookie，因为登录认证 Cookie 是 HttpOnly 的，`document.cookie` 无法读取。

### 2. 进入聊天室

1. 启动应用
2. 将复制的 Cookie 粘贴到输入框
3. 点击「进入聊天室」

### 3. 开始聊天

- **发送消息**：在底部输入框输入文字，按 `Enter` 发送
- **换行**：按 `Shift + Enter`
- **回复消息**：点击消息下方的「回复」
- **插入表情**：点击 😊 按钮打开表情面板
- **自动滚动**：新消息到达时自动滚动到底部

### 快捷键

| 快捷键 | 功能 |
|--------|------|
| `Enter` | 发送消息 |
| `Shift + Enter` | 输入换行 |
| `Ctrl/Cmd + Enter` | 快速登录（登录页） |

---

## 🛠️ 开发指南

### 环境要求

- [Node.js](https://nodejs.org/) 16+
- npm 8+
- Electron 28+

### 开发命令

```bash
# 安装依赖
npm install

# 开发模式运行
npm start

# 打包当前平台
npm run build

# 仅打包不生成安装包（调试用）
npm run pack
```

### 项目结构

```
fuba-chat/
├── main.js           # Electron 主进程（窗口管理、Cookie 注入）
├── preload.js        # 预加载脚本（IPC 桥接）
├── login.html        # 登录界面
├── chatroom.html     # 聊天室主界面
├── package.json      # 项目配置
├── .npmrc            # npm 镜像配置
└── README.md         # 项目文档
```

### 技术栈

| 层级 | 技术 |
|------|------|
| 桌面框架 | Electron 28 |
| 前端 | 原生 HTML / CSS / JavaScript |
| 通信 | Electron IPC + fetch API |
| API | 福利吧聊天室 HTTP 轮询接口 |

### 核心原理

```
登录页 (login.html)                聊天室 (chatroom.html)
     │                                    │
     │ IPC: sendCookies(cookies)          │ fetch() 调用 API
     ▼                                    ▼
  main.js ────────────────────────── Electron 网络层
     │                                    │
     │ session.webRequest                 │ 自动携带 Cookie
     │ .onBeforeSendHeaders               │ (由主进程注入)
     ▼                                    ▼
  注入原始 Cookie 到每个请求 ──────→ fuliba2023.net API
```

**关键设计**：使用 `session.webRequest.onBeforeSendHeaders` 拦截所有请求并注入原始 Cookie 字符串，绕过 Electron Cookie 解析对特殊字符（如 URL 编码的 tab）的限制。

---

## 📦 构建 Release

### 配置 electron-builder

项目已支持 electron-builder，可构建各平台安装包：

```bash
# macOS
npm run build -- --mac

# Windows
npm run build -- --win

# Linux
npm run build -- --linux
```

构建产物在 `dist/` 目录。

### 发布新版本

1. 更新 `package.json` 中的 `version`
2. 提交代码并推送到 main 分支
3. 打 tag 触发自动构建：`git tag -a v1.0.x -m "描述" && git push origin v1.0.x`
4. GitHub Actions 自动构建三平台安装包并创建 Release
5. Release 创建后为 draft 状态，确认无误后在 GitHub 页面点击发布

---

## ❓ FAQ

<details>
<summary><b>为什么提示游客模式？</b></summary>

Cookie 中缺少 `S5r8_2132_auth` 字段。这个字段是 HttpOnly 的，必须从 **Network 面板**获取，不能用 `document.cookie`。

</details>

<details>
<summary><b>Cookie 会过期吗？</b></summary>

会。福利吧的 Cookie 通常有效期 1-7 天，过期后需要重新获取并粘贴。

</details>

<details>
<summary><b>应用启动报错怎么办？</b></summary>

1. 确认 Node.js 版本 ≥ 16
2. 删除 `node_modules` 后重新 `npm install`
3. macOS 如遇 Electron 下载失败，配置镜像：`export ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron/`

</details>

<details>
<summary><b>支持手机端吗？</b></summary>

不支持。本应用是桌面端应用，仅支持 macOS / Windows / Linux。手机端请使用浏览器访问福利吧论坛。

</details>

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

- 提交 PR 前请确保应用能正常启动
- 新功能请先开 Issue 讨论
- 截图、文档改进也欢迎

---

## 📄 许可证

[MIT License](LICENSE) © ysanyu

---

<div align="center">

**⭐ 如果这个项目对你有帮助，欢迎 Star**

[Releases](https://github.com/ysanyu/fuba-chat/releases) · [Issues](https://github.com/ysanyu/fuba-chat/issues) · [Source Code](https://github.com/ysanyu/fuba-chat)

</div>
