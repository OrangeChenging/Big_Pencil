# gui.py
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtGui import QIcon


class PathSelector(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "人脸识别"
        self.width = 600
        self.height = 300
        self.initUI()
        # self.setStyleSheet("background-color: lightblue;")  //设置窗口的背景颜色
        self.selectedPath = ""

        self.status_label = QLabel(self)
        self.status_label.setAlignment(Qt.AlignCenter)  # Center the text

        layout = QVBoxLayout(self)
        layout.addWidget(self.status_label)  # Add the label to the layout

        layout = QVBoxLayout()
        layout.addWidget(self.label_bg)
        self.setLayout(layout)

        # Ensure the label is updated in the UI
        self.setLayout(layout)

    def get_path(self):
        path1, _ = QFileDialog.getOpenFileName(
            self, "请选择文件", "", "All Files (*);;Text Files (*.txt)")
        if path1:
            self.selectedPath = path1
            self.entry_text.setText(self.selectedPath)

    def initUI(self):
        self.setWindowTitle(self.title)

        self.setWindowIcon(QIcon(
            r'C:\\Users\\denqi\\Desktop\\人机交互大作业\\faced-master\\ui\\favicon.ico'))  # 设置图标
        self.setGeometry(100, 100, self.width, self.height)
        self.setGeometry(100, 100, self.width, self.height)

        self.label_bg = QLabel(self)
        self.label = QLabel(self)
        self.label.setText("选择文件：")
        self.label.move(50, 80)

        self.label_bg.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.entry_text = QLineEdit(self)
        self.entry_text.setFixedSize(250, 30)
        self.entry_text.move(150, 80)
        self.entry_text.setReadOnly(True)

        self.button = QPushButton(self)
        self.button.setText('选择路径')
        self.button.move(400, 80)
        self.button.clicked.connect(self.get_path)

        self.submit_button = QPushButton(self)
        self.submit_button.setText('确定(开始执行)')
        self.submit_button.move(155, 150)
        self.submit_button.setFixedSize(200, 50)
        # self.submit_button.clicked.connect(self.close)

        # 以下是设置背景图片的代码
        self.label_bg = QLabel(self)
        # 将路径替换为你想要使用的图片路径

        pixmap = QPixmap(
            "C:\\Users\\denqi\\Desktop\\人机交互大作业\\faced-master\\ui\\back1.jpg")

        self.label_bg.setPixmap(pixmap)
        self.label_bg.setGeometry(0, 0, self.width, self.height)
        self.label_bg.setScaledContents(True)
        self.label_bg.lower()  # 将背景图片设置为最底层
