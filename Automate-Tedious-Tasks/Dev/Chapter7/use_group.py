import re

# example 1
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 433-567-8903')

# example 2
phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search('My number is (433)-567-8903')

print(mo.group(1))
print(mo.group(2))
print(mo.group(3))

print(mo.groups())

