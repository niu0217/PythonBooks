#! python3
# merge_multiple_pdfs.py
# Combines all PDFS in the current working directory into a single PDF.

import PyPDF2
import os

# Get all the PDF filenames
pdfFiles = []  # 保存所有的文件名字
for filename in os.listdir('./sources'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)  # 将文件名字从小到大排序

pdfWriter = PyPDF2.PdfWriter()  # 创建一个PDF写入对象

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open('./sources/' + filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    # 对加密文件进行处理
    if pdfReader.is_encrypted:
        pdfReader.decrypt('rosebud')

    # Loop through all the pages (except the first) and add them.
    for pageNum in range(1, len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum]
        pdfWriter.add_page(pageObj)

    pdfFileObj.close()

# Save the resulting PDF to a file.
resultPdf = open('resultFile.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
