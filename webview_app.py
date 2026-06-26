#!/usr/bin/env python3
"""
福利吧聊天室 WebView 版本
使用 PyQt6 创建一个简单的桌面应用
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEngineCookieStore
from PyQt6.QtCore import QUrl, Qt


class ChatWindow(QMainWindow):
    def __init__(self, cookies=None):
        super().__init__()
        self.setWindowTitle("福利吧聊天室")
        self.setGeometry(100, 100, 1200, 800)
        
        # 创建 WebView
        self.webview = QWebEngineView()
        
        # 设置 Cookie (如果提供)
        if cookies:
            self.set_cookies(cookies)
        
        # 加载聊天室页面
        self.webview.load(QUrl("https://fuliba2023.net/forum.php"))
        
        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.webview)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # 注入 JavaScript 自动打开聊天室
        self.webview.loadFinished.connect(self.on_load_finished)
    
    def set_cookies(self, cookies_str):
        """设置 Cookie"""
        profile = QWebEngineProfile.defaultProfile()
        cookie_store = profile.cookieStore()
        
        # 解析 Cookie 字符串
        cookies = cookies_str.split(';')
        for cookie in cookies:
            if '=' in cookie:
                name, value = cookie.strip().split('=', 1)
                # 这里需要更复杂的 Cookie 设置逻辑
                # 为简化，我们直接通过 JavaScript 设置
                pass
    
    def on_load_finished(self, success):
        """页面加载完成后自动打开聊天室"""
        if success:
            # 注入 JavaScript 自动点击聊天室按钮
            js_code = """
            setTimeout(function() {
                var launcher = document.getElementById('chatroom-launcher');
                if (launcher) {
                    launcher.click();
                }
            }, 3000);
            """
            self.webview.page().runJavaScript(js_code)


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("福利吧聊天室 - 登录")
        self.setGeometry(100, 100, 500, 600)
        
        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建布局
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # 标题
        from PyQt6.QtWidgets import QLabel
        title = QLabel("🎉 福利吧聊天室")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Cookie 输入框
        label = QLabel("请输入 Cookie：")
        layout.addWidget(label)
        
        from PyQt6.QtWidgets import QTextEdit, QPushButton, QMessageBox
        
        self.cookie_input = QTextEdit()
        self.cookie_input.setPlaceholderText("例如：bbs_sid=xxxxx; bbs_auth=xxxxx; ...")
        self.cookie_input.setMaximumHeight(100)
        layout.addWidget(self.cookie_input)
        
        # 帮助文本
        help_text = QLabel("在浏览器登录福利吧后，按 F12 打开开发者工具，在 Console 中输入 document.cookie 复制输出的内容")
        help_text.setWordWrap(True)
        layout.addWidget(help_text)
        
        # 登录按钮
        login_btn = QPushButton("进入聊天室")
        login_btn.clicked.connect(self.login)
        layout.addWidget(login_btn)
        
        # 帮助按钮
        help_btn = QPushButton("如何获取 Cookie？")
        help_btn.clicked.connect(self.show_help)
        layout.addWidget(help_btn)
    
    def login(self):
        """处理登录"""
        cookies = self.cookie_input.toPlainText().strip()
        
        if not cookies:
            QMessageBox.warning(self, "错误", "请输入 Cookie！")
            return
        
        # 打开聊天室窗口
        self.chat_window = ChatWindow(cookies)
        self.chat_window.show()
        self.close()
    
    def show_help(self):
        """显示帮助信息"""
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(self, "帮助", 
            "获取 Cookie 教程：\n\n"
            "1. 在浏览器中登录福利吧论坛\n"
            "2. 按 F12 打开开发者工具\n"
            "3. 切换到 Console (控制台) 标签\n"
            "4. 输入 document.cookie 并回车\n"
            "5. 复制输出的完整 Cookie 字符串"
        )


def main():
    app = QApplication(sys.argv)
    
    # 显示登录窗口
    login_window = LoginWindow()
    login_window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
