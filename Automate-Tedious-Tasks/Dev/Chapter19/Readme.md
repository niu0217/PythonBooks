# 第19章-操作图像

## 简单操作图像

文件：[simple_operate_picture.py](https://github.com/niu0217/PythonBooks/blob/main/Automate-Tedious-Tasks/Dev/Chapter19/simple_operate_picture.py)

函数：

+ `get_image_data_type`：图片的基本信息
+ `copy_paste_cats`：复制粘贴多个猫咪
+ `draw_picture`：画图
+ `write_text`：写字

## 添加徽标

要求：
1. 载入徽标图像
2. 循环遍历工作目标中的所有.png和.jpg文件
3. 检查图片是否宽于或高于300像素
4. 如果是，将宽度或高度中较大的一个减小到300像素，并按比例缩小到另一维度
5. 在角上粘贴徽标图像
6. 将改变的图像存入另一个文件夹

Code：

[resize_and_addlogo.py](https://github.com/niu0217/PythonBooks/blob/main/Automate-Tedious-Tasks/Dev/Chapter19/resize_and_addlogo.py)

