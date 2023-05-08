# -*- coding:utf-8 -*-
from utils import parser
from utils import process
import time

top_cat = "finance_money_suda"
top_time = "20230501"
top_show_num = 10

finance_url = 'https://top.finance.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat={}&top_time={}&top_show_num={}&top_order=DESC'

top_cats = [
    'finance_news_0_suda',
    'finance_money_suda'
]

for top_cat in top_cats:
    url = finance_url.format(top_cat, top_time, top_show_num)
    url_lists = parser.parser_urls(url)
    print(url_lists)
    for url_list in url_lists:
        content = parser.parser_html(url_list)
        if len(content['content']) == 0:
            continue
        process.save(content)
        time.sleep(0.5)