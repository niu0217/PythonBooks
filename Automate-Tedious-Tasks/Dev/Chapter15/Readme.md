# 第15章-处理PDF和Word文档

## 操作PDF

文件：[extract_pdf.py](https://github.com/niu0217/PythonBooks/blob/main/Automate-Tedious-Tasks/Dev/Chapter15/extract_pdf.py)

+ 函数：
  + `example2`：提取第一页的文本 没有加密
  + `example2`：提取第一页的文本 加密过的pdf

文件：[create_pdf.py](https://github.com/niu0217/PythonBooks/blob/main/Automate-Tedious-Tasks/Dev/Chapter15/create_pdf.py)

+ 函数：
  + `combinedpdf`：将两个pdf文件合并成一个
  + `rotate_page`：旋转页面
  + `overlay_page`：给pdf的第一页加水印
  + `encryption_pdf`：加密pdf文件

文件：[merge_multiple_pdfs.py](https://github.com/niu0217/PythonBooks/blob/main/Automate-Tedious-Tasks/Dev/Chapter15/merge_multiple_pdfs.py)

+ 功能：合并多个PDF文件

## 操作Word

文件：[deal_word.py](https://github.com/niu0217/PythonBooks/blob/main/Automate-Tedious-Tasks/Dev/Chapter15/deal_word.py)

+ 函数：
  + `readWord`：简单的读取word文档
  + `getText`：获取word中的所有文本
  + `writeWordFirstMethod`：写word的第一种方式
  + `writeWordSecondMethod`：写word的第二种方式
  + `addTitle`：添加标题
  + `addNewline`：换行
  + `addNewpage`：换页
  + `addPicture`：添加图片