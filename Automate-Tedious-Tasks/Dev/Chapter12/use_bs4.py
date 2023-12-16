# 简单使用bs4来解析HTML文件

import requests
import bs4

# 使用requests返回一个BeautifulSoup对象
# res = requests.get('https://nostarch.com/')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(type(noStarchSoup))

# 使用File对象返回一个BeautifulSoup对象
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
print(type(exampleSoup))

# 提取元素
# elems = exampleSoup.select('#author')
# elems = exampleSoup.select('p')
# print(f'elems type: {type(elems)}')
# print(f'elems length: {len(elems)}')
# print(f'elems[0] type: {type(elems[0])}')
# print(str(elems[0]))
# print(elems[0].attrs)
# print(elems[0].getText())

# 通过元素的属性获取数据
spanElem = exampleSoup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.attrs)
