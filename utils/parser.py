# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import re


def parser_urls(url):
    """
    解析获取所有url
    :param url:
    :return:
    """
    url_lists = []
    try:
        response = requests.get(url)
        data_str = response.text[11:-2]
        data_str = eval(data_str, type('Dummy', (dict,), dict(__getitem__=lambda s, n: n))())
        data_str = json.dumps(data_str)
        data_str = json.loads(data_str)
        data_str = data_str['data']
        for data in data_str:
            url = data['url'].replace("\\/", "/")
            url_lists.append(url)
        return url_lists
    except Exception as e:
        print(e)


def parser_html(url):
    """
    解析html获取财经内容
    :param url:
    :return:
    """
    content = {"title": "", "date": "", "source": "", "content": ""}
    try:
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        if soup is None:
            return content
        # 查找标题
        title = soup.h1
        if title is None:
            return content
        title = re.sub(r'\/', '', title.text)
        content["title"] = title

        # 查找时间
        date_attr = {"class": "date"}
        date = soup.find(name='span', attrs=date_attr)
        if date is not None:
            content["date"] = date.text

        # 查找来源
        source_attr = {"class": "source ent-source"}
        source = soup.find(name='a', attrs=source_attr)
        if source is not None:
            content["source"] = source.text

        # 查找内容
        attrs = {"class": "article", "id": "artibody"}
        article_div = soup.find(name='div', attrs=attrs)
        if article_div is None:
            return content
        data = []
        for p in article_div.find_all("p"):
            text = p.text
            text = re.sub(r'\s+', '', text)
            data.append(text)
            # data += p.text + "\n"
        content["content"] = data
        return content
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # url = 'https://finance.sina.com.cn/money/future/agri/2023-04-25/doc-imyrqier4433773.shtml'
    # url = "https://finance.sina.com.cn/money/future/roll/2023-04-25/doc-imyrqyai4423338.shtml"
    url = 'https://finance.sina.com.cn/money/bank/2023-05-01/doc-imysfmex1389245.shtml'
    print(parser_html(url))
