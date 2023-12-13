# 第7章-模式匹配与正则表达式

## 1. 电话号码与email地址提取

任务：在一篇长的网页或者文章中，找出所有的电话号码和E-mail地址。

步骤：

+ 先全选需要查找的文本到粘贴板上
+ 然后运行程序
+ 最后粘贴结果

思路：

+ 使用pyperclip模块复制和粘贴字符串。
+ 创建两个正则表达式，一个匹配电话号码，一个匹配E-mail地址。
+ 对两个正则表达式，找到所有的匹配，而不是第一次匹配。
+ 将匹配好的字符串整理好格式放在一个字符串中，用于粘贴。
+ 如果文本中没有找到匹配，则显示某种信息。

需要查找的文本：

```
Skip to main content
Home
Search form

Search

GO!
Topics
Arduino
Art & Design
General Computing
Hacking & Computer Security
Hardware / DIY
JavaScript
Kids
LEGO®
LEGO® MINDSTORMS®
Linux & BSD
Skip to main content
Home
Search form

Search

GO!
Catalog
Media
Write for Us
About Us
Topics
Arduino
Art & Design
General Computing
Hacking & Computer Security
Hardware / DIY
JavaScript
Kids
LEGO®
LEGO® MINDSTORMS®
Linux & BSD
Manga
Minecraft
Programming
Python
Science & Math
Scratch
System Administration
Early Access
Gift Certificates
Free ebook edition with every print book purchased from nostarch.com!
Shopping cart
3 Items    Total: $53.48
View cart Checkout
Contact Us

No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103 USA
Phone: 800.420.7240 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST)
Fax: +1 415.863.9950

Reach Us by Email
General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Academic requests: academic@nostarch.com (Please see this page for academic review requests)
Help with your order: info@nostarch.com
Reach Us on Social Media
Twitter
Facebook
Navigation
My account
Log out
Manage your subscription preferences.


About Us  |  ★ Jobs! ★  |  Sales and Distribution  |  Rights  |  Media  |  Academic Requests  |  Conferences  |  Order FAQ  |  Contact Us  |  Write for Us  |  Privacy
Copyright 2018 No Starch Press, Inc

```

代码：

[phone_and_email.py](https://github.com/niu0217/PythonBooks/blob/main/Automate-Tedious-Tasks/Dev/Chapter7/phone_and_email.py)

结果：

```
info@nostarch.com
academic@nostarch.com
415-863-9900
media@nostarch.com
800-420-7240
415-863-9950
```

