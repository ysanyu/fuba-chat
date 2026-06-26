# releases 目录

打包产物输出目录，运行 `npm run build` 后生成。

## 文件说明

### macOS

| 文件 | 架构 | 说明 |
|------|------|------|
| 福利吧聊天室-1.0.0-arm64.dmg | Apple Silicon | M1/M2/M3 芯片，安装包 |
| 福利吧聊天室-1.0.0.dmg | Intel | Intel 芯片，安装包 |
| 福利吧聊天室-1.0.0-arm64-mac.zip | Apple Silicon | 免安装版 |
| 福利吧聊天室-1.0.0-mac.zip | Intel | 免安装版 |

### Windows

| 文件 | 说明 |
|------|------|
| 福利吧聊天室-Setup-1.0.0.exe | NSIS 安装包 |
| 福利吧聊天室-1.0.0.exe | 免安装便携版 |

### Linux

| 文件 | 说明 |
|------|------|
| 福利吧聊天室-1.0.0.AppImage | AppImage 格式，免安装 |
| 福利吧聊天室-1.0.0.deb | Debian/Ubuntu 安装包 |
| 福利吧聊天室-1.0.0.rpm | Fedora/RedHat 安装包 |

## 使用方法

### macOS
1. 下载 `.dmg` 文件（或 `.zip` 免安装版）
2. 打开 dmg，拖动应用到「应用程序」文件夹
3. 首次打开：右键点击应用 → 选择「打开」

### Windows
1. 下载 `Setup.exe` 安装包（或便携版 `.exe`）
2. 双击运行安装
3. 从开始菜单启动

### Linux
- **AppImage**：`chmod +x 福利吧聊天室-1.0.0.AppImage && ./福利吧聊天室-1.0.0.AppImage`
- **deb**：`sudo dpkg -i 福利吧聊天室-1.0.0.deb`
- **rpm**：`sudo rpm -i 福利吧聊天室-1.0.0.rpm`

## 打包命令

```bash
# 打包所有平台（macOS + Windows + Linux）
npm run build

# 单独打包某个平台
npm run build:mac      # macOS（dmg + zip）
npm run build:win      # Windows（exe + 便携版）
npm run build:linux    # Linux（AppImage + deb + rpm）
```

> **注意**：跨平台打包需要对应系统的环境。例如 Windows 的 `.exe` 最好在 Windows 上打包，Linux 的 `.deb`/`.rpm` 最好在 Linux 上打包。macOS 可以同时打包 dmg 和 zip。
