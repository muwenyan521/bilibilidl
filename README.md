# 哔哩哔哩视频下载程序

## 项目介绍

本项目是一个基于 Python 的哔哩哔哩视频下载程序，用户只需输入视频链接，便可自动下载视频。同时，程序提供了输入cookie的选项，用户输入自己的cookie后，可以下载高清视频。在下载过程中，程序会实时显示下载进度。

## 项目结构

* 主程序：`dlmain.py`
* 依赖库：`subprocess`, `sys`, `os`, `tkinter`, `threading`, `time`

## 使用说明

1. 打开程序，你将看到两个输入框和一个按钮。

2. 在 "链接:" 输入框中输入你想要下载的哔哩哔哩视频链接。

3. （可选）在 "cookie(选填):" 输入框中输入你的哔哩哔哩账号的 cookie。这可以让你下载高清视频。

4. 点击 "开始下载" 按钮，程序将开始下载视频。

5. 在下载过程中，你可以在下方的文本框中看到当前进程。

6. 下载完成后，程序会自动打开包含下载视频的文件夹。

## 注意事项

* 本程序仅供个人学习使用，严禁用于任何商业用途。
* 使用本程序下载的视频，版权归原作者所有，请尊重原创，不得用于任何商业用途。

## 更新日志

* V1.0.0：实现了基本的视频下载功能

## 开源许可

本项目采用 MIT 开源许可证。

## Cookie获取教程：

1. 打开浏览器，进入哔哩哔哩官网，确保你已经登录你的账号。
  ![显示哔哩哔哩官网首页，用户已登录。](https://8aa5534c.telegraph-image-9ah.pages.dev/file/4d4e2c274ab90833b0dab.png)
2. 在浏览器中按 F12 打开开发者工具。
  ![显示打开的开发者工具窗口。](https://8aa5534c.telegraph-image-9ah.pages.dev/file/77a6950fa4a45b48000d6.png)
3. 在开发者工具的顶部菜单中，选择 Network（网络）选项。
  ![开发者工具顶部菜单，Network选项被选中。](https://8aa5534c.telegraph-image-9ah.pages.dev/file/342ba10006dbd394c6fcb.png)
4. 开启录制,并在浏览器中刷新哔哩哔哩的页面。
  ![在浏览器中，哔哩哔哩页面被刷新。](https://8aa5534c.telegraph-image-9ah.pages.dev/file/dc9fc823119af5ac59014.png)
5. 在开发者工具的 Network 面板中，会显示所有的网络请求。搜索名为 nav 的请求，点击它。
  ![在开发者工具 Network 面板中，显示了一系列网络请求，nav 的请求被选中。](https://8aa5534c.telegraph-image-9ah.pages.dev/file/4a1a661bdf64ff4d228c7.png)
6. 在右侧面板中，选择 Headers（头部）选项。在 Request Headers（请求头部）部分，找到名为 Cookie 的字段，这就是你的哔哩哔哩 Cookie。
  ![在开发者工具 Headers 面板中，显示了一系列头部信息，Cookie 字段被选中](https://8aa5534c.telegraph-image-9ah.pages.dev/file/7ba72269666ef0097f046.png)
7.只需复制 Cookie 中 SESSDATA 的值，并粘贴到本程序的 "cookie(选填):" 输入框中，就可以使用你的哔哩哔哩账号下载高清视频了。
  ![复制SESSDATA](https://8aa5534c.telegraph-image-9ah.pages.dev/file/7c2777bd9837fc77771a4.png)
  ![SESSDATA被粘贴至输入框中](https://8aa5534c.telegraph-image-9ah.pages.dev/file/fa13adc077e7720261d01.png)

注意：Cookie 包含了你的登录信息，请不要将其泄露给他人。
