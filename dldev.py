# 开发者日志版本
# 导入所需的库
import subprocess
import sys
import os
import tkinter as tk
from tkinter import messagebox
from threading import Thread
import time

# 定义一个函数将相对路径转换为绝对路径
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # 如果是使用 PyInstaller 打包的话，这个变量会被设置
    except Exception:
        base_path = os.path.abspath(".")  # 如果没有使用 PyInstaller 打包的话，使用当前目录
    return os.path.join(base_path, relative_path)

# 定义一个函数来执行下载操作
def run_download():
    cookie = cookie_entry.get().strip()  # 获取输入的 cookie
    input_link = link_entry.get().strip()  # 获取输入的链接
    if cookie and input_link:  # 如果输入了 cookie 和 链接
        cmd = f"lux -d -cookie {cookie} {input_link}"  # 使用 lux 命令行工具进行下载
        print("cookie 和 链接都输入了")
        print("cookie:",cookie)
        print("链接:",input_link)
    elif input_link:  # 如果只输入了链接
        cmd = f"lux -d {input_link}"  # 使用 lux 命令行工具进行下载
        print("只输入了链接")
        print("链接:",input_link)
    else:  # 如果没有输入链接
        messagebox.showwarning("警告", "请输入链接")  # 弹出警告框
        print("用户未输入链接")
        return
    try:
        # 使用 subprocess 库执行命令，将输出重定向到 PIPE，这样我们可以读取并显示在 GUI 上
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8', errors='ignore', bufsize=1)
        while True:
            output = process.stdout.readline()  # 读取一行输出
            if output == '' and process.poll() is not None:
                print("输出完毕")
                break
            if output:  # 如果有输出
                log_text.config(state=tk.NORMAL)  # 允许编辑文本框
                if "file already exists, skipping" in output:  # 如果输出表示文件已存在
                    log_text.delete(1.0, tk.END)  # 清空文本框
                    log_text.insert(tk.END, "文件已存在")  # 显示"文件已存在"
                    print("文件已存在")
                    time.sleep(2)  # 等待2秒
                elif "Site" in output and "Title" in output and "Type" in output:  # 如果输出表示开始下载
                    log_text.delete(1.0, tk.END)  # 清空文本框
                    log_text.insert(tk.END, "开始下载")  # 显示"开始下载"
                    print("开始下载")
                    time.sleep(2)  # 等待2秒
                else:
                    log_text.insert(tk.END, output.strip())  # 显示输出
                    print(output.strip())
                log_text.config(state=tk.DISABLED)  # 禁止编辑文本框
                root.update_idletasks()  # 更新 GUI
        log_text.config(state=tk.NORMAL)  # 允许编辑文本框
        log_text.delete(1.0, tk.END)  # 清空文本框
        log_text.insert(tk.END, "下载完成")  # 显示"下载完成"
        print("下载完成")
        log_text.config(state=tk.DISABLED)  # 禁止编辑文本框
        directory = os.getcwd().replace('//', '/')  # 获取当前目录，并将'//'替换为'/'
        print("下载目录:",directory)
        os.startfile(directory)  # 打开当前目录
    except subprocess.CalledProcessError as e:
        messagebox.showerror("错误", f"命令执行出错: {e}")  # 如果执行命令出错，弹出错误框
        print("命令执行出错:",e)
    except Exception as e:
        messagebox.showerror("错误", f"命令执行出错: {e}")  # 如果有其他错误，弹出错误框
        print("命令执行出错:" , e)

# 创建一个 tkinter 窗口
root = tk.Tk()
root.title("哔哩哔哩视频下载程序开发者版")  # 设置窗口标题
root.geometry("500x250")  # 设置窗口大小
cookie_label = tk.Label(root, text="cookie(选填):")  # 创建一个标签
text_label = tk.Label(root, text="填了可下载高清视频")  # 创建一个标签
cookie_entry = tk.Entry(root, width=40)  # 创建一个输入框
link_label = tk.Label(root, text="链接:")  # 创建一个标签
link_entry = tk.Entry(root, width=40)  # 创建一个输入框
download_button = tk.Button(root, text="开始下载", command=lambda: Thread(target=run_download).start())  # 创建一个按钮，点击时会在新的线程中运行 run_download 函数
log_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)  # 创建一个文本框，用于显示日志，初始状态为禁止编辑
cookie_label.pack(pady=10)  # 将标签添加到窗口
text_label.pack()
cookie_entry.pack()
link_label.pack(pady=10)
link_entry.pack()
download_button.pack(pady=10)
log_text.pack(pady=10)  # 将文本框添加到窗口
print("程序运行成功")
root.mainloop()  # 进入 tkinter 的事件循环