import PyPDF2


def example1():
    """提取第一页的文本 没有加密"""
    pdfFileObj = open('sources/meetingminutes2.pdf', 'rb')  # 打开PDF文件
    pdfReader = PyPDF2.PdfReader(pdfFileObj)  # 创建一个PDF阅读器对象
    pageObj = pdfReader.pages[0]
    page1_text = pageObj.extract_text()
    print(page1_text)


def example2():
    """提取第一页的文本 加密过的pdf"""
    pdfFileObj = open('sources/encrypted.pdf', 'rb')  # 打开PDF文件
    pdfReader = PyPDF2.PdfReader(pdfFileObj)  # 创建一个PDF阅读器对象
    pdfReader.decrypt('rosebud')  # 用密码解密pdf
    page1_text = pdfReader.pages[1].extract_text()  # 提取第一页的文本
    # 将提取出的文本写到一个临时文件中
    textFileObj = open('text.txt', 'w')
    textFileObj.write(page1_text)
    textFileObj.close()


if __name__ == '__main__':
    example2()
