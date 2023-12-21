#!python3
# -*- coding: utf-8 -*-

"""
simple_operate_picture.py

这是一个简单操作图像的模块。

该模块包含以下功能：
1. 图片的基本信息
2. 复制粘贴多个猫咪
3. 画图
4. 写字

Author: niu0217
Date: 2023-12-21
"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import os


def get_image_data_type():
    """图片的基本信息"""
    cat_image = Image.open('./sources/zophie.png')
    print(f'filename: {cat_image.filename}')
    print(f'format: {cat_image.format}')
    print(f'format description: {cat_image.format_description}')
    print(f'size: {cat_image.size}')
    width, height = cat_image.size
    print(f'width: {width}\nheight: {height}')


def copy_paste_cats():
    """复制粘贴多个猫咪"""
    cat_image = Image.open('sources/zophie.png')
    face_image = cat_image.crop((355, 345, 565, 560))  # 截取猫咪的脸
    cat_image_width, cat_image_height = cat_image.size
    face_image_width, face_image_height = face_image.size
    cat_copy_image = cat_image.copy()
    for left in range(0, cat_image_width, face_image_width):
        for top in range(0, cat_image_height, face_image_height):
            print(left, top)
            cat_copy_image.paste(face_image, (left, top))
    cat_copy_image.save('multicats.png')


def draw_picture():
    """画图"""
    obj_image = Image.new('RGBA', (200, 200), 'white')
    obj_drawimage = ImageDraw.Draw(obj_image)
    obj_drawimage.line([(0, 0), (199, 0), (0, 199), (0, 0)], fill='black')
    obj_drawimage.rectangle((20, 30, 60, 60), fill='blue')
    obj_drawimage.ellipse((120, 30, 160, 60), fill='red')
    obj_drawimage.polygon(
        ((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)),
        fill='brown'
    )
    for i in range(100, 200, 10):
        obj_drawimage.line([(i, 0), (200, i - 100)], fill='green')
    obj_image.save('drawing.png')


def write_text():
    """写字"""
    obj_image = Image.new('RGBA', (200, 200), 'white')
    obj_drawimage = ImageDraw.Draw(obj_image)
    obj_drawimage.text((20, 150), 'Hello', fill='purple')
    fonts_folder = '/Library/Fonts'
    arial_font = ImageFont.truetype(
        os.path.join(fonts_folder, 'Arial Unicode.ttf'),
        32
    )
    obj_drawimage.text((100, 150), 'Howdy', fill='gray', font=arial_font)
    obj_image.save('text.png')


if __name__ == '__main__':
    # get_image_data_type()
    # copy_paste_cats()
    # draw_picture()
    write_text()
