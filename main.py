import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText

from entity.DaHuaBean import get_flight_flag_info, get_flag_name, save_flight_flag
from util.MouseUtil import MouseUtil
from util.ZuoTianUtil import replenish_piece, fly_destination, click_task


def zuo_tian(path, four, nineteen):
    lis = get_flight_flag_info(path)
    spare_flag = get_flag_name(lis, '备用棋')
    buy_flag = get_flag_name(lis, '长安杂货店(12,11)')
    # 领取做天任务
    task_flag = get_flag_name(lis, '天宫(37,33)')
    fly_destination(task_flag.goods_position_y, task_flag.goods_position_x)
    time.sleep(four)
    # 左键点击npc,领取任务
    MouseUtil().left_click(310, 200)
    click_task(1)
    time.sleep(four)
    MouseUtil().click_left()
    replenish_piece(task_flag, spare_flag, buy_flag)
    # 杀三头魔王
    # 使用指定位置的飞行棋飞到指定位置
    task_flag = get_flag_name(lis, '御马监(10,35)')
    fly_destination(task_flag.goods_position_y, task_flag.goods_position_x)
    # 左键点击npc,领取任务
    time.sleep(four)
    MouseUtil().left_click(190, 300)
    time.sleep(nineteen)
    replenish_piece(task_flag, spare_flag, buy_flag)
    # 杀黑山妖王
    # 使用指定位置的飞行棋飞到指定位置
    task_flag = get_flag_name(lis, '御马监(100,10)')
    fly_destination(task_flag.goods_position_y, task_flag.goods_position_x)
    # 左键点击npc,领取任务
    time.sleep(four)
    MouseUtil().left_click(230, 300)
    time.sleep(nineteen)
    replenish_piece(task_flag, spare_flag, buy_flag)
    # 杀蓝色妖王
    # 使用指定位置的飞行棋飞到指定位置
    task_flag = get_flag_name(lis, '御马监(105,45)')
    fly_destination(task_flag.goods_position_y, task_flag.goods_position_x)
    # 左键点击npc,领取任务
    time.sleep(four)
    MouseUtil().left_click(280, 240)
    time.sleep(nineteen)
    replenish_piece(task_flag, spare_flag, buy_flag)
    # 杀万年熊王
    # 使用指定位置的飞行棋飞到指定位置
    task_flag = get_flag_name(lis, '御马监(110,100)')
    fly_destination(task_flag.goods_position_y, task_flag.goods_position_x)
    # 左键点击npc,领取任务
    time.sleep(four)
    MouseUtil().left_click(480, 580)
    time.sleep(nineteen)
    replenish_piece(task_flag, spare_flag, buy_flag)
    save_flight_flag(lis, path)


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
    msg['Subject'] = Header('大话西游', 'utf-8')
    smtp.sendmail('957493412@qq.com', '1421760774@qq.com', msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    t = time.time()
    for i in range(9):
        # 再世情缘
        zuo_tian('./a979899.txt', 3, 19)
        # 大闹天宫
        # zuo_tian('./b979899.txt', 3, 19)
        # 二阶堂红丸
        # zuo_tian('./c979899.txt', 3, 19)
        # 拉尔夫
        # zuo_tian('./d979899.txt', 3, 19)
        # 拉尔夫
        # zuo_tian('./f979899.txt', 3, 19)
        print(i + 1)
    a = time.time()
    print(int(a) - int(t))
    send_mail('大话西游完成')
