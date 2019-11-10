# coding: utf-8
from bs4 import BeautifulSoup
from functions import *
from D import love
# site = 'site:qq.com'
site = 'site:usst.edu.cn'


# 获得每页搜索结果
count = 0
for i in range(0, depth):
    url = 'https://www.baidu.com/s?wd=' + site + '&pn=' + str(i * 10)
    print(url)
    text = get_url_content(url)
    soup = BeautifulSoup(text, 'html.parser')
    h3 = soup.find_all('h3')  # 找到所有H3标签的内容
    for dummy_h3 in h3:
        a_in_h3 = dummy_h3.a
        href = a_in_h3.attrs['href']  # 链接
        print(a_in_h3.text, '\n', href)  # h3的内容，即标题
        content = get_url_content(href)
        word = delete_lable_for_text(content)
        storage_content_path = 'content_' + str(count) + '.txt'
        storage_tittle_path = 'tittle_' + str(count) + '.txt'
        storage_to_local_texts(storage_content_path, word)
        storage_to_local_texts(storage_tittle_path, a_in_h3.text)
        count = count + 1
