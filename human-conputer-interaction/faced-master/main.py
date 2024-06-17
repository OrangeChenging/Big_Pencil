import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import os
import time

import cv2
from faced import FaceDetector
from faced.utils import annotate_image
from moviepy.editor import VideoFileClip


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=500, height=300)
        self.set_bg_image(self.canvas)
        self.canvas.pack()

    def set_bg_image(self, canvas):
        bg_img_path = "C:\\Users\\denqi\\Desktop\\human-conputer-interaction\\faced-master\\ui\\back1.jpg"  # 背景图片路径
        img = Image.open(bg_img_path)
        img = img.resize((500, 300), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, image=self.bg_img, anchor='nw')

    def run_module1(self):
        subprocess.Popen(["python", "total.py"])
        self.update()

    def run_module2(self):
        subprocess.Popen(["python", "humanfacedet.py"])
        self.update()

    def run_module3(self):
        subprocess.Popen(["python", "feel_em_total.py"])
        self.update()

    def run_module4(self):
        subprocess.Popen(["python", "feel_em_facedet.py"])
        self.update()

    def update(self):
        # 假设子进程会输出一个图片文件，以下代码会读取该图片文件并显示在Tkinter程序中
        try:
            image = Image.open("output.jpg")
            self.photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        except:
            print("Waiting for output from child process...")
        self.master.after(1000, self.update)  # 每隔一秒钟更新一次图片


root = tk.Tk()
root.title('欢迎使用faced-master人脸识别')
root.iconbitmap(
    'C:\\Users\\denqi\\Desktop\\human-conputer-interaction\\faced-master\\ui\\favicon.ico')
root.geometry("500x300")
app = Application(master=root)

btn1 = tk.Button(root, text="文件选择识别", command=app.run_module1)
btn2 = tk.Button(root, text="实时摄像识别", command=app.run_module2)
btn3 = tk.Button(root, text="文件选择情感识别", command=app.run_module3)
btn4 = tk.Button(root, text="实时摄影情感识别", command=app.run_module4)

btn1.config(bg='skyblue')
btn2.config(bg='skyblue')
btn3.config(bg='skyblue')
btn4.config(bg='skyblue')

btn1.place(relx=0.3, rely=0.3, anchor=tk.CENTER)
btn2.place(relx=0.7, rely=0.3, anchor=tk.CENTER)
btn3.place(relx=0.3, rely=0.7, anchor=tk.CENTER)
btn4.place(relx=0.7, rely=0.7, anchor=tk.CENTER)

app.mainloop()


"""
import tkinter as tk
import subprocess

def run_module1():
    subprocess.call(["python", "total.py"])

def run_module2():
    subprocess.call(["python", "humanfacedet.py"])

root = tk.Tk()
root.geometry('300x200')  # 设置窗口大小

# 创建两个按钮，并且设置按钮应用函数及文字
btn1 = tk.Button(root, text="文件选择识别", command=run_module1)
btn2 = tk.Button(root, text="实时摄像识别", command=run_module2)

# 使用place方法设置按钮位置，横向居中显示，并且留有适当间隔
btn1.place(relx=0.3, rely=0.5, anchor=tk.CENTER)  
btn2.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

root.mainloop()"""
