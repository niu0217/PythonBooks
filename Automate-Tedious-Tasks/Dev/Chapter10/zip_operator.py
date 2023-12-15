import zipfile
import os

from pathlib import Path

p = Path.cwd()  # 当前路径
exampleZip = zipfile.ZipFile(p / 'example.zip')  # 读取zip文件
print(exampleZip.namelist())  # 打印zip文件中的内容

# exampleZip.extractall()  # 解压全部文件
# exampleZip.extract('spam.txt', p)  # 解压单个文件
exampleZip.close()

# 压缩文件
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
