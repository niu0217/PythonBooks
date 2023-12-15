# 第10章-组织文件

## 1. 文件重命名

要求：

+ 检查当前工作目录的所有文件名，寻找美国风格的日期
+ 如果找到，将该文件重命名，交换月份和日期的位置，使之成为欧洲风格的日期

思路：

+ 创建一个正则表达式，可以识别美国风格日期的文本模式
+ 调用`os.listdir()`，找出工作目录中的所有文件
+ 循环遍历每个文件名，利用该正则表达式检查它是否包含日期
+ 如果它包含日期，用`shutil.move()`对该文件重命名

代码：

[renameDates.py](https://github.com/niu0217/PythonBooks/blob/main/Automate-Tedious-Tasks/Dev/Chapter10/renameDates.py)

## 2. 将一个文件夹备份成一个zip文件

代码：

[backupToZip.py](https://github.com/niu0217/PythonBooks/blob/main/Automate-Tedious-Tasks/Dev/Chapter10/backupToZip.py)