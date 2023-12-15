import shutil
import os
import re

# 创建一个美国风格日期的正则表达式：MM-DD-YYYY
datePattern = re.compile(r'''
    ^(.*?)  # all text before the date
    ((0|1)?\d)-  # one or two digits for the month
    ((0|1|2|3)?\d)-  # # one or two digits for the day
    ((19|20)?\d\d)  # four digits for the year
    (.*?)$  # all text after the date
''', re.VERBOSE)

# 遍历文件名查找需要的信息
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # 创建欧洲风格的日期：DD-MM-YYYY
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print(f'Renaing "{amerFilename}" to "{euroFilename}"...')
    # shutil.move(amerFilename, euroFilename)  # uncomment after testing
