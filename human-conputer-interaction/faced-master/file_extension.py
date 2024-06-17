#coding=utf-8
import os

def get_file_extension(file_path):
    # 使用os.path.splitext()函数来获取文件名和扩展名的元组
    _, file_extension = os.path.splitext(file_path)
    
    # 如果你想要去掉扩展名中的点号，可以使用[1:]来获取扩展名的子字符串
    return file_extension[1:]


'''
# 例子
file_path = "/path/to/your/file/example.gif"
extension = get_file_extension(file_path)
print("文件扩展名:", extension)
'''