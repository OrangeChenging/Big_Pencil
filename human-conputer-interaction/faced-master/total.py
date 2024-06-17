# main.py
import os
import time
from PyQt5.QtCore import QThread, QTimer, Qt
from file_extension import get_file_extension
import videodet
import gifdet
import imgdet
from ui.gui1 import PathSelector
from PyQt5.QtWidgets import QApplication
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import sys
from playsound import playsound


sys.setrecursionlimit(sys.getrecursionlimit() * 5)
val_jpg = "jpg"
val_png = "png"
val_mp4 = "mp4"
val_gif = "gif"


class MyThread(QThread):
    def __init__(self, path, type_file, parent=None):
        super(MyThread, self).__init__(parent)
        self.path = path
        self.type_file = type_file

    def closeEvent(self, event):
        # 检查所有线程是否已结束
        if thread and thread.isRunning():
            # 如果有任何正在运行的线程，忽略这次关闭请求
            event.ignore()
        else:
            # 所有线程都已结束，可以关闭窗口
            event.accept()
            time.stop()  # 停掉时间器
        time.sleep(1)  # 等待一秒，确保线程安全地结束

    def run(self):
        if self.type_file == val_jpg or self.type_file == val_png:
            imgdet.fun(self.path)
        elif self.type_file == val_mp4:
            videodet.fun(self.path)
        elif self.type_file == val_gif:
            gifdet.fun(self.path)
        else:
            print("这个文件什么也不是")
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)

    path_selector = PathSelector()
    path_selector.show()

    thread = None  # create a handle for MyThread object outside the function

    def run_detection():

        global thread
        if thread and thread.isRunning():
            return
        destr = path_selector.selectedPath  # 文件路径

        if destr:
            # Clear the selected path after running the detection
            path_selector.selectedPath = None
            path_selector.hide()  # Hide the main window while running the detector
            new_destr = get_file_extension(destr)
            if thread is None:
                thread = MyThread(destr, new_destr)
                # Show the main window again when the detector finishes
                thread.finished.connect(path_selector.show)
                thread.start()
            elif not thread.isRunning():
                thread = MyThread(destr, new_destr)
                # Show the main window again when the detector finishes
                thread.finished.connect(path_selector.show)
                thread.start()

    def last_window_closed():
        if thread and thread.isRunning():
            path_selector.show()

    app.lastWindowClosed.connect(last_window_closed)
    path_selector.submit_button.clicked.connect(run_detection)

    sys.exit(app.exec_())
