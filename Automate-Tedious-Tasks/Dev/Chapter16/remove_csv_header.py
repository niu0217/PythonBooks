#!python3
# -*- coding: utf-8 -*-

"""
remove_csv_header.py

从CSV文件中删除标题行。

思路：
1. 循环遍历每个CSV文件
2. 读入CSV文件
3. 写入CSV文件，没有第一行

Author: niu0217
Date: 2023-12-20
"""

import csv
import os


def process_current_path(folder):
    """处理所有csv文件(不包括子目录)"""

    # 创建一个文件夹保存最终结果
    os.makedirs('header_removed', exist_ok=True)

    # 遍历并取得folder目录下所有csv文件(不包括子目录)
    for csvfilename in os.listdir(folder):
        if not csvfilename.endswith('.csv'):
            continue

        print(f'Removing header from {folder}/' + csvfilename + '...')

        # 将当前csv文件中的内容读取到csv_rows_list中，除了第一行
        filename_temp = os.path.join(folder, csvfilename)
        csv_rows_list = extract_csv_content_to_list(filename_temp)

        # 将csv_rows_list的内容写入到合适的文件中
        filename_temp = os.path.join('header_removed', csvfilename)
        write_content_to_file(csv_rows_list, filename_temp)


def process_all_path(folder):
    """处理所有csv文件(包括子目录)"""

    # 创建一个文件夹保存最终结果
    os.makedirs('header_removed', exist_ok=True)

    # 遍历并取得folder目录下所有csv文件(包括子目录)
    for foldername, subfoldernames, filenames in os.walk(folder):
        print(f'Current folder:  {foldername}')

        for filename in filenames:
            if not filename.endswith('.csv'):
                continue

            print(f'Removing header from {foldername}/' + filename + '...')

            # 将当前csv文件中的内容读取到csv_rows_list中，除了第一行
            filename_temp = os.path.join(foldername, filename)
            csv_rows_list = extract_csv_content_to_list(filename_temp)

            # 将csv_rows_list的内容写入到合适的文件中
            output_file_path = foldername
            output_file_path = output_file_path.replace('sources', 'header_removed')
            os.makedirs(output_file_path, exist_ok=True)
            filename_temp = os.path.join(output_file_path, filename)
            write_content_to_file(csv_rows_list, filename_temp)

        print('')


def extract_csv_content_to_list(filename):
    """将filename的内容提取到csv_rows_list中保存"""
    csv_rows_list = []
    csv_obj_file = open(filename)
    csv_obj_reader = csv.reader(csv_obj_file)
    for row in csv_obj_reader:
        if csv_obj_reader.line_num == 1:  # 第一行标题数据不要
            continue
        csv_rows_list.append(row)
    csv_obj_file.close()

    return csv_rows_list


def write_content_to_file(csv_rows_list, filename):
    """将csv_rows_list中的内容写入到文件filename中"""
    csv_obj_file = open(filename, 'w', newline='')
    csv_writer = csv.writer(csv_obj_file)
    for row in csv_rows_list:
        csv_writer.writerow(row)
    csv_obj_file.close()


if __name__ == '__main__':
    process_all_path('./sources')
    # process_current_path('./sources')
