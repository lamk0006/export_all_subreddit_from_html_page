# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:11:34 2022

@author: jlkc1
"""

from bs4 import BeautifulSoup

with open("C:\\Users\\jlkc1\\Desktop\\J\\Subreddit\\subreddits_ subscriber.html", 'r', encoding="utf8") as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    for a in soup.find_all('a', href=True):
        if a['href'] == 'https://www.reddit.com/subreddits/mine#' or a['href'] == 'javascript:void(0)':
            continue
        print(a['href'])
        with open("C:\\Users\\jlkc1\\Desktop\\J\\Subreddit\\subreddits_list.txt","a") as file:
            file.write(a['href'])
            file.write('\n')