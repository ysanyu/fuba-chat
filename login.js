// login.js - 登录界面逻辑

function login() {
  const cookies = document.getElementById('cookies').value.trim();
  const statusEl = document.getElementById('status');

  // 验证输入
  if (!cookies) {
    showStatus('请输入 Cookie！', 'error');
    return;
  }

  // 简单验证 Cookie 格式
  if (!cookies.includes('=')) {
    showStatus('Cookie 格式不正确，请检查！', 'error');
    return;
  }

  // 显示加载状态
  showStatus('正在验证并进入聊天室...', 'info');
  document.getElementById('loginBtn').disabled = true;

  // 发送 Cookie 到主进程
  window.electronAPI.sendCookies(cookies);
}

function showStatus(message, type) {
  const statusEl = document.getElementById('status');
  statusEl.textContent = message;
  statusEl.className = 'status ' + type;
}

function toggleHelp() {
  const helpBox = document.getElementById('helpBox');
  helpBox.classList.toggle('show');
}

// 页面加载完成后添加事件监听
document.addEventListener('DOMContentLoaded', () => {
  // 支持按 Ctrl+Enter 或 Cmd+Enter 快速登录
  document.getElementById('cookies').addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      login();
    }
  });
});
