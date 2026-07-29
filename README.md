<div align="center">
  <h1>TOTP Online</h1>
  <p>你的轻量、便捷的 TOTP 验证码生成助手</p>

  [![Python](https://img.shields.io/badge/Python-3.x-blue.svg?style=flat&logo=python)](#)
  [![Tkinter](https://img.shields.io/badge/GUI-Tkinter-9cf.svg?style=flat)](#)
  [![HTML](https://img.shields.io/badge/Web-HTML5-orange.svg?style=flat&logo=html5)](#)
</div>

## 项目简介

**TOTP Online** 是一款基于 Python 与 Web 构建的 TOTP (Time-based One-Time Password) 动态验证码生成工具。

在这个注重隐私和安全的时代，越来越多的平台开启了双重验证 (2FA)。本项目旨在提供一个简单、离线可用且跨平台的验证码生成方案。只需输入您的 Secret Key，即可实时生成 6 位动态验证码，告别每次都要拿起手机看验证码的烦恼。

本项目主要提供两个版本：一个是网页版，另一个是专门为 Win 用户准备的离线版（TOTP Offline），专门用来对付那些没有电脑端二次验证工具的情况，满足不同场景下的使用需求。

---

## 核心特性

- **多平台支持**：提供本地 Python 桌面端版本以及纯前端 Web 网页版本。
- **实时生成与读秒**：基于标准 TOTP 算法，界面自带 30 秒倒计时进度条，自动刷新。
- **一键便捷复制**：点击按钮即可快速复制当前验证码，无缝粘贴到系统登录界面。
- **现代化 UI 设计**：简约卡片式设计，支持不同系统的分辨率与 DPI 自动缩放适配。

---

## 快速开始

### 方式一：Web 网页版体验

直接使用浏览器打开项目中的 `index.html`，即可使用纯前端处理的验证码功能，数据完全在本地计算，安全可靠。

### 方式二：Python 桌面端

1. 确保您的电脑已安装 Python 3 环境。
2. 安装必要的依赖包：
   ```bash
   pip install pyotp
   ```
3. 运行程序：
   ```bash
   python totp_gui.py
   ```

-----

## 关于作者

**蔡Tony**
走在成长的路上，不断探索

- **我的网站**：[蔡Tony的空间](https://caitony.dpdns.org/)
- **GitHub**: [Caitony-czc](https://github.com/Caitony-czc)

-----

## 许可证 (License)

本项目基于 [MIT License](LICENSE) 开源。

允许自由使用、修改和分发，二次开发请保留原作者版权声明。
