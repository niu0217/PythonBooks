import re

# 1. 创建一个Regex对象
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# 2. 向Regex对象的search()方法传入想要查找的字符串，它返回一个Match对象
mo = phoneNumRegex.search('My number is 433-567-8903')
# 3. 调用Match对象的group()方法，返回实际匹配文本的字符串
print('Phone number found: ' + mo.group())
