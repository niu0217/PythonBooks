import PyPDF2


def combinedpdf():
    """将两个pdf文件合并成一个"""
    pdf1File = open('sources/meetingminutes.pdf', 'rb')
    pdf2File = open('sources/meetingminutes2.pdf', 'rb')
    pdf1Reader = PyPDF2.PdfReader(pdf1File)
    pdf2Reader = PyPDF2.PdfReader(pdf2File)
    pdfWriter = PyPDF2.PdfWriter()

    # 从两个源pdf复制所有的页面，将它们添加到pdfWriter中
    for pageNum in range(len(pdf1Reader.pages)):
        pageObj = pdf1Reader.pages[pageNum]
        pdfWriter.add_page(pageObj)
    for pageNum in range(len(pdf2Reader.pages)):
        pageObj = pdf2Reader.pages[pageNum]
        pdfWriter.add_page(pageObj)

    # 写入
    pdfOutputFile = open('combined.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()


def rotate_page():
    """旋转页面"""
    pdfFile = open('sources/meetingminutes.pdf', 'rb')  # 打开PDF文件
    pdfReader = PyPDF2.PdfReader(pdfFile)  # 创建一个PDF阅读器对象
    page = pdfReader.pages[0]  # 需要旋转的页面
    page.rotate(90)  # 旋转90度

    pdfWriter = PyPDF2.PdfWriter()  # 创建一个PDF写入对象
    pdfWriter.add_page(page)
    resultPdfFile = open('rotatePage.pdf', 'wb')
    pdfWriter.write(resultPdfFile)
    resultPdfFile.close()
    pdfFile.close()


def overlay_page():
    """给pdf的第一页加水印"""
    pdfFile = open('sources/meetingminutes.pdf', 'rb')  # 打开PDF文件
    pdfReader = PyPDF2.PdfReader(pdfFile)  # 创建一个PDF阅读器对象
    pdfFirstPage = pdfReader.pages[0]
    pdfWatermarkReader = PyPDF2.PdfReader(open('sources/watermark.pdf', 'rb'))
    pdfFirstPage.merge_page(pdfWatermarkReader.pages[0])  # 给第一页加水印
    pdfWriter = PyPDF2.PdfWriter()  # 创建一个PDF写入对象
    pdfWriter.add_page(pdfFirstPage)  # 将第一个页面加入到pdfWriter中

    # 将剩余页面也加入到pdfWriter中
    for pageNum in range(1, len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum]
        pdfWriter.add_page(pageObj)

    resultPdfFile = open('watermarkedCover.pdf', 'wb')
    pdfWriter.write(resultPdfFile)  # 将pdfWriter中的内容写入到resultPdfFile中
    pdfFile.close()
    resultPdfFile.close()


def encryption_pdf():
    """加密pdf文件"""
    pdfFile = open('sources/meetingminutes.pdf', 'rb')  # 打开PDF文件
    pdfReader = PyPDF2.PdfReader(pdfFile)  # 创建一个PDF阅读器对象
    pdfWriter = PyPDF2.PdfWriter()  # 创建一个PDF写入对象

    for pageNum in range(len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum]
        pdfWriter.add_page(pageObj)

    pdfWriter.encrypt('niu0217')
    resultPdf = open('encryption.pdf', 'wb')
    pdfWriter.write(resultPdf)

    pdfFile.close()
    resultPdf.close()


if __name__ == '__main__':
    # combinedpdf()
    # rotate_page()
    # overlay_page()
    encryption_pdf()
