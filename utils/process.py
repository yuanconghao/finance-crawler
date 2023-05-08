# -*- coding: utf-8 -*-
import os


def save(data, path=''):
    """
    将内容写入文件
    :param data:
    :param path:
    :return:
    """
    filename = data['title'] + '.txt'
    date = data['date']
    source = data['source']
    content = data['content']
    if path != '':
        filepath = os.path.join(path, filename)
    else:
        filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = os.path.join(filepath, 'data')

    if not os.path.exists(filepath):
        os.makedirs(filepath)

    file_save_path = os.path.join(filepath, filename)
    print(file_save_path)

    with open(file_save_path, "w") as f:
        f.write(data['title'] + "\n")
        f.write(date + "\n")
        f.write(source + "\n")
        for item in content:
            f.write(item + "\n")

    f.close()


if __name__ == '__main__':
    data = {'title': '今日广西现货市场糖价情况', 'date': '2023年04月25日 11:39', 'source': '云南糖网',
            'content': ['YNTW.COM糖网\xa0 今日（4月25日）早盘郑商所白糖期小幅上涨，上午主力2307合约收盘价6848元，上涨36元，广西现货市场制糖企业、流通商报价如下：',
                        '截至发稿，今日广西现货市场制糖企业报价6890元/吨一线（含税价，提货库点不同），另有商家报价略低，具体情况有待进一步观察。',
                        '截止4月14日，2022/23榨季广西所有开榨糖厂已经结束榨季生产。',
                        '2022/23年榨季截止3月31日广西全区累计入榨甘蔗4121.06万吨，同比减少842.84万吨；产混合糖526.77万吨，同比减少77.85万吨；产糖率12.78%，同比增加0.6个百分点；累计销糖264.93万吨，同比增加37.15万吨；产销率50.29%，同比提高12.62个百分点；工业库存261.84万吨，同比减少115万吨。其中3月份单月产糖22.66万吨，同比减少85.56万吨；销糖50.77万吨，同比减少9.07万吨。',
                        'yntw.com糖网 采编']}

    save(data)
