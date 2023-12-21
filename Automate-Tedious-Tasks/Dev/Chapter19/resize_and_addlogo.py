#!python3
# -*- coding: utf-8 -*-

"""
resize_and_addlogo.py

项目：添加徽标。

要求：
1. 载入徽标图像
2. 循环遍历工作目标中的所有.png和.jpg文件
3. 检查图片是否宽于或高于300像素
4. 如果是，将宽度或高度中较大的一个减小到300像素，并按比例缩小到另一维度
5. 在角上粘贴徽标图像
6. 将改变的图像存入另一个文件夹

Author: niu0217
Date: 2023-12-21
"""

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logo_image = Image.open('sources/' + LOGO_FILENAME)
logo_width, logo_height = logo_image.size

# Loop over all files in the working directory.
for filename in os.listdir('./sources'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
      or filename == LOGO_FILENAME:
        continue
    image = Image.open('./sources/' + filename)
    width, height = image.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        # Resize the image.
        print('Resizing ./sources/%s...' % filename)
        image = image.resize((width, height))

    # Add the logo.
    print('Adding logo to ./sources/%s...' % filename)
    image.paste(
        logo_image,
        (width - logo_width, height - logo_height),
        logo_image
    )
    # Save changes.
    directory = 'with_logo'
    if not os.path.exists(directory):
        os.makedirs(directory)
    image.save(os.path.join('with_logo', filename))
