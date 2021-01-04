import datetime
import json
import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText
from urllib.request import urlopen

from apscheduler.schedulers.blocking import BlockingScheduler
from numpy import *


class Employee:
    def __init__(self):
        self.name = ''
        self.current_price_list = []
        self.total_volume_list = []


def first_save_data():
    """
    第一次运行保存所有数据到BtcPrice
    :return:
    """
    ss = int(round(time.time() * 1000))
    url = 'http://py.btc126.com/json/markets.json?t=' + str(ss)
    # 获取虚拟货币价格
    cybermoney_list = json.loads(urlopen(url).read().decode())
    final_data = []
    for i in cybermoney_list:
        aa = Employee()
        aa.name = i['symbol']
        aa.current_price_list.append(i['current_price'])
        aa.total_volume_list.append(i['total_volume'])
        final_data.append(aa.__dict__)
    json_str = json.dumps(final_data, ensure_ascii=False)
    with open('./BtcPrice.txt', "w") as f:
        f.write(json_str)


def send_mail(message):
    """
    发送邮件
    :param message:
    :return:
    """
    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login('957493412@qq.com', 'pdtsanllybzwbdgg')
    # 编写HTML类型的邮件正文
    msg = MIMEText(message, 'html', 'utf-8')
    msg['Subject'] = Header('低价提醒', 'utf-8')
    smtp.sendmail('957493412@qq.com', '1421760774@qq.com', msg.as_string())
    smtp.quit()


def remind_one(lis):
    """
    如果当前价格达到最低则发送邮件提示投资者
    :param lis:
    :return:
    """
    grade_down_data(lis)
    temp_str = '<html>'
    for i in lis:
        for j in allPrice:
            if j['name'] == i['symbol']:
                temp_str += '<h1> 币种:&nbsp&nbsp<font color="red">' + str(i['symbol']) + '</font>&nbsp&nbsp当前价格:' + str(
                    i['current_price']) + '&nbsp&nbsp最高价格:' + str(
                    max(j['current_price_list'])) + '&nbsp&nbsp平均价格:' + str(
                    round(mean(j['current_price_list']), 2)) + '</h1>' + '<br/>'
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print(ts + '   ' + '可投资数量：  ' + str(len(lis)))
    if len(lis) > 0:
        send_mail(temp_str + '<html>')


def is_minimum(current_price, all_price):
    """
    当前价格是否是最低价格
    :param current_price:
    :param all_price:
    :return:
    """
    if current_price <= min(all_price):
        return True
    else:
        return False


def data_processing(lis):
    """
    对数据进行处理
    :param lis:
    :return:
    """
    final_data = []
    for i in lis:
        for j in allPrice:
            if j['name'] == i['symbol']:
                if is_minimum(i['current_price'], j['current_price_list']):
                    final_data.append(i)
                if len(j['current_price_list']) >= 100:
                    del (j['current_price_list'][0])
                j['current_price_list'].append(i['current_price'])
                if len(j['total_volume_list']) >= 100:
                    del (j['total_volume_list'][0])
                j['total_volume_list'].append(i['total_volume'])
    remind_one(final_data)
    json_str = json.dumps(allPrice, ensure_ascii=False)
    with open('./BtcPrice.txt', "w") as f:
        f.write(json_str)


def grade_down_data(cybermoney_list):
    """
    根据24小时的成交额对数据进行降序处理
    :param cybermoney_list:
    :return:
    """
    n = len(cybermoney_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if cybermoney_list[j]['total_volume'] < cybermoney_list[j + 1]['total_volume']:
                cybermoney_list[j], cybermoney_list[j + 1] = cybermoney_list[j + 1], cybermoney_list[j]


def get_price():
    """
    获取当前时间虚拟货币价格
    :return:
    """
    ss = int(round(time.time() * 1000))
    url = 'http://py.btc126.com/json/markets.json?t=' + str(ss)
    print(url)
    # 获取虚拟货币价格
    cybermoney_list = json.loads(urlopen(url).read().decode())
    # 按24小时的成交额进行排序
    grade_down_data(cybermoney_list)
    # 选取成交额最高的前50支
    excellent_list = cybermoney_list[:20]
    for i in excellent_list[::-1]:
        if i['symbol'] == 'usdt' or i['symbol'] == 'usdc' or i['symbol'] == 'busd'or i['symbol'] == 'dai':
            excellent_list.remove(i)
    for i in excellent_list:
        print(i['symbol'] + '    ' + str(i['price_change_percentage_24h']))
    # 进行判断
    data_processing(excellent_list)


def dojob():
    """
    定时任务,每900秒执行一次get_price()
    :return:
    """
    scheduler = BlockingScheduler()
    scheduler.add_job(get_price, 'interval', seconds=900, id='test_job1')
    scheduler.start()


if __name__ == '__main__':
    f = open('./BtcPrice.txt')
    st = f.read()
    allPrice = json.loads(st)
    dojob()

    # first_save_data()

    # get_price()
