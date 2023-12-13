"""
输入：My name is AL SWEIGART and I am 4,000 years old.
输出：Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay.
"""
print('Enter the English message to translate into Pig Latin: ')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')  # 元音字母

pigLatin = []  # 保存最后的结果
for word in message.split():
    # 删除每个单词前面的非字母字符
    prefixNonLetters = ''  # 用来保存每个单词前面的非字母字符
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # 删除每个单词后面的非字母字符
    suffixNonLetters = ''  # 用来保存每个单词后面的非字母字符
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # 记住这个单词是全大写还是首字母大写
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()  # 转换为小写方便处理

    # 删除单词开头的所有辅音
    prefixConsonants = ''  # 用来保存每个单词前面的辅音字符
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or title case
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

print(' '.join(pigLatin))

