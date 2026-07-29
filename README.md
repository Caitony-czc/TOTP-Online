<div align="center">
  <img src="./totp-online.svg" alt="TOTP Online Logo" width="100" />
  <h1>TOTP Online</h1>
  <p>你的轻量、便捷的 TOTP 验证码生成助手</p>

  [![Python](https://img.shields.io/badge/Python-3.x-blue.svg?style=flat&logo=python)](#)
  [![Tkinter](https://img.shields.io/badge/GUI-Tkinter-9cf.svg?style=flat)](#)
  [![HTML](https://img.shields.io/badge/Web-HTML5-orange.svg?style=flat&logo=html5)](#)

</div>

**TOTP Online** 是一款基于 Python & html 构建的 TOTP (Time-based One-Time Password) 动态验证码生成工具。

在这个注重隐私和安全的时代，越来越多的平台开启了双重验证 (2FA)。本项目旨在提供一个简单、在线&离线可用且跨平台的验证码生成方案。只需输入您的 Secret Key，即可实时生成 6 位动态验证码，告别每次都要拿起手机看验证码的烦恼。

本项目主要提供两个版本：一个是html版本，另一个是专门为 Win 用户准备的exe版本，专门用来对付那些没有电脑端二次验证工具的情况，现在不用移动设备也可以过二次验证。

---

## 核心特性

TOTP验证码生成工具，为用户准备了可以多端访问的网页，用户也可以选择下载html版本或者下载Windows专属的exe版本。

---

## 快速开始

方式一：下载 Windows 桌面端

1. 访问本仓库的 [Releases](../../releases) 页面。
2. 下载最新的 `TOTP Offline vX.X.X.exe`或`TOTP Offline vX.X.X.html` 。
3. 下载后即可运行

### 方式二：免安装体验网页版

打开浏览器，直接访问在线预览：

[TOTP Online体验地址](https://totp-online.pages.dev/)

### 方式三：本地开发与构建

确保您的电脑已安装 Python 3 环境。

1. 安装必要的依赖包：
   
   ```bash
   pip install pyotp
   ```

2. 运行程序：
   
   ```bash
   python totp_gui.py
   ```

---

## 关于作者

**蔡Tony** 走在成长的路上，不断探索

- **我的网站**：[蔡Tony的空间](https://caitony.dpdns.org/)
- **GitHub**: [Caitony-czc](https://github.com/Caitony-czc)

---

## 许可证 (License)

本项目基于 [MIT License](LICENSE) 开源。

允许自由使用、修改和分发，二次开发请保留原作者版权声明。
