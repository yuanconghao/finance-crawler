# -*- coding:utf-8 -*-
from utils import parser
from utils import process
from datetime import datetime
import time

top_cat = "finance_money_suda"
top_time = "20230401"
top_show_num = 1000

finance_url = 'https://top.finance.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat={}&top_time={}&top_show_num={}&top_order=DESC'

finance_roll_url = 'https://finance.sina.com.cn/roll/index.d.html?cid={}&page={}'

page_index_num = 100
gg_date_start = '2023-04-01'
gg_date_end = '2023-05-08'
stock_url = 'https://vip.stock.finance.sina.com.cn/corp/view/vCB_BulletinGather.php?gg_date={}&page_index={}'

top_cats = [
    'finance_news_0_suda',
    'finance_money_suda'
]

# 新闻
for top_cat in top_cats:
    url = finance_url.format(top_cat, top_time, top_show_num)
    url_lists = parser.parser_urls(url)
    print(url_lists)
    for url_list in url_lists:
        content = parser.parser_html(url_list)
        if len(content['content']) == 0:
            continue
        process.save(content, './data/news/')
        # 小心被封
        time.sleep(1)

# 财经新闻


# 股票公告
gg_date_start_ts = int(datetime.strptime(gg_date_start, "%Y-%m-%d").timestamp())
gg_date_end_ts = int(datetime.strptime(gg_date_end, "%Y-%m-%d").timestamp())

while gg_date_start_ts < gg_date_end_ts:
    # 1683475200 -> object
    gg_date_ts = time.localtime(gg_date_start_ts)
    # object -> 2023-05-08
    gg_date = time.strftime("%Y-%m-%d", gg_date_ts)
    # object -> 1683475200.0
    gg_date_start_ts = time.mktime(gg_date_ts) + 86400

    # url
    for page_index in range(1, page_index_num + 1):
        stock_url_format = stock_url.format(gg_date, page_index)
        print(stock_url_format)
        url_lists = parser.parser_stock_urls(stock_url_format)
        print(url_lists)
        for url_list in url_lists:
            content = parser.parser_stock_html(url_list)
            if len(content['content']) == 0:
                continue
            process.save(content, './data/stock/')
            time.sleep(1)