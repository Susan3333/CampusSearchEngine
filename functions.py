# coding: utf-8
import requests
import re
import urllib3

# 伪装浏览器头部
kv = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/59.0.3071.115 Safari/537.36"}

depth = 1


def storage_to_local_texts(storage_path, data):
    fileHandle = open(storage_path, "w", encoding='utf-8')
    fileHandle.write(data)
    fileHandle.close()


def get_url_content(href):
    urllib3.disable_warnings()
    r = requests.get(href, headers=kv, verify=False)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    content = r.text
    return content


def delete_lable_for_text(content):
    pre = re.compile('>(.*?)<')
    word = ''.join(pre.findall(content))
    return word


def read_file(path):
    with open(path, 'r', encoding='UTF-8') as f:
        content = f.read()
    return content
