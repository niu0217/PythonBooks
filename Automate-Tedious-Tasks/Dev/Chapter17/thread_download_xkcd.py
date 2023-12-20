#!python3
# -*- coding: utf-8 -*-

"""
thread_download_xkcd.py

用多线程下载xkcd漫画。

思路：
1. 创建线程函数
2. 创建并启动线程
3. 等待所有线程结束

Author: niu0217
Date: 2023-12-20
"""

import requests
import os
import bs4
import threading

# 保存下载的结果
os.makedirs('xkcd', exist_ok=True)
url = 'https://xkcd.com'  # starting url


def download_xkcd(start_comic, end_comic):
    """线程函数：下载start_comic～end_comic漫画页面到xkcd目录下"""
    for urlnumber in range(start_comic, end_comic):
        # Download the page.
        print('Downloading page %s...' % urlnumber)
        response = requests.get(os.path.join(url, str(urlnumber)))
        response.raise_for_status()

        soup = bs4.BeautifulSoup(response.text, 'html.parser')

        # Find the URL of the comic page.
        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('Could not find comic image')
        else:
            comic_url = 'https:' + comic_elem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % comic_url)
            response = requests.get(comic_url)
            response.raise_for_status()

            # Save the image to ./xkcd
            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in response.iter_content(100000):
                image_file.write(chunk)
            image_file.close()


download_threads_list = []  # 保存创建的线程
# 创建14个线程，每个线程下载10个页面
for i in range(0, 140, 10):
    start = i
    end = i + 9
    if start == 0:
        start = 1  # 没有页面为0的漫画
    download_thread = threading.Thread(
        target=download_xkcd,
        args=(start, end)
    )
    download_threads_list.append(download_thread)
    download_thread.start()

# 等待所有线程结束
for downloadthread in download_threads_list:
    downloadthread.join()
print('Done...')
