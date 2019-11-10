# coding: utf-8
from functions import *
import os
from create_index import *


print(os.getcwd())  # 获取当前工作目录路径

num = 0
tittle_list = []
content_list = []
datas_list = []

for num in range(depth * 10 - 1):
    tittle_path = os.path.abspath('tittle_' + str(num) + '.txt')
    tittle_list.append(read_file(tittle_path))
    content_path = os.path.abspath('content_' + str(num) + '.txt')
    content_list.append(read_file(content_path))
for i in range(depth * 10 - 1):
    dummy_dict = {"tittle": tittle_list[i], "content": content_list[i]}
    # dummy_dict = {"tittle": tittle_list[i]}
    datas_list.append(dummy_dict)

# count = 0
for data in datas_list:
    es.index(index='news', doc_type='campus', body=data)
    # count = count + 1
