#!python3
# -*- coding: utf-8 -*-

"""
simple_operate_csv_file.py

这是一个简单操作csv文件的模块。

该模块包含以下功能：
1. 创建reader对象读取csv数据
2. 在for循环中，从reader对象读取csv数据
3. 创建writer对象写入csv数据
4. 使用delimiter和lineterminator关键字
5. 使用DictReader和DictWriter CSV对象

Author: niu0217
Date: 2023-12-20
"""

import csv


def example1():
    """创建reader对象读取csv数据"""
    example_file = open('sources/example.csv')
    example_reader = csv.reader(example_file)
    example_data_list = list(example_reader)
    print(example_data_list)


def example2():
    """在for循环中，从reader对象读取csv数据"""
    example_file = open('sources/example.csv')
    example_reader = csv.reader(example_file)
    for row in example_reader:
        print('Row #' + str(example_reader.line_num) + ' ' + str(row))


def example3():
    """创建writer对象写入csv数据"""
    output_file = open('output.csv', 'w', newline='')
    output_writer = csv.writer(output_file)
    output_writer.writerow(['nihao', 'niu0217', 'I am', 'a robot'])
    output_writer.writerow(['hello, world', 'niu0217', 'I am', 'a robot'])
    output_file.close()


def example4():
    """使用delimiter和lineterminator关键字"""
    csv_file = open('example.tsv', 'w', newline='')
    csv_writer = csv.writer(csv_file, delimiter='\t', lineterminator='\n\n')
    csv_writer.writerow(['nihao', 'niu0217', 'I am', 'a robot'])
    csv_writer.writerow(['hello, world', 'niu0217', 'I am', 'a robot'])
    csv_file.close()


def example5():
    """使用DictReader和DictWriter CSV对象"""
    example_file = open('sources/exampleWithHeader.csv')
    example_dictreader = csv.DictReader(example_file)
    for row in example_dictreader:
        print(row['Timestamp'], row['Fruit'], row['Quantity'])

    # 如果csv文件没有标题,我们手动给它加上
    print('\n\n')
    example_file = open('sources/example.csv')
    example_dictreader = csv.DictReader(example_file, ['time', 'name', 'account'])
    for row in example_dictreader:
        print(row['time'], row['name'], row['account'])

    # DictWriter对象使用字典来创建CSV文件
    output_file = open('output.csv', 'w', newline='')
    output_dictwriter = csv.DictWriter(output_file, ['Name', 'Pet', 'Phone'])
    output_dictwriter.writeheader()
    output_dictwriter.writerow({
        'Name': 'Alice',
        'Pet': 'cat',
        'Phone': '123-8909'
    })
    output_file.close()


if __name__ == '__main__':
    # example1()
    # example2()
    # example3()
    # example4()
    example5()
