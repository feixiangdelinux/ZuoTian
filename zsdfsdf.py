import time

from entity.DaHuaBean import get_flight_flag_info, get_flag_name, save_flight_flag
from util.MouseUtil import MouseUtil
from util.ZuoTianUtil import replenish_piece, fly_destination, click_task

lis = ['a979899', 'b979899', 'c979899', 'd979899', 'e979899']
monitor = [1920, 1080]


def ling_sha_santou(m_list, monit):
    for i in m_list:
        # 打开客户端
        MouseUtil().left_click((m_list.index(i) + 2) * 160 - 29, monit[-1] - 20)
        lis = get_flight_flag_info('./' + i + '.txt')
        spare_flag = get_flag_name(lis, '备用棋')
        buy_flag = get_flag_name(lis, '长安杂货店(12,11)')
        # 领取做天任务
        task_flag = get_flag_name(lis, '天宫(37,33)')
        fly_destination(task_flag.goods_position_y, task_flag.goods_position_x)
        time.sleep(3)
        # 左键点击npc,领取任务
        MouseUtil().left_click(310, 200)
        click_task(1)
        time.sleep(3)
        MouseUtil().click_left()
        replenish_piece(task_flag, spare_flag, buy_flag)
        # 杀三头魔王
        # 使用指定位置的飞行棋飞到指定位置
        task_flag = get_flag_name(lis, '御马监(10,35)')
        fly_destination(task_flag.goods_position_y, task_flag.goods_position_x)
        # 左键点击npc,领取任务
        time.sleep(3)
        MouseUtil().left_click(190, 300)
        if task_flag.times_left == 1:
            time.sleep(19)
            replenish_piece(task_flag, spare_flag, buy_flag)
        else:
            task_flag.times_left = task_flag.times_left - 1
        save_flight_flag(lis, './' + i + '.txt')
        MouseUtil().left_click((m_list.index(i) + 2) * 160 - 29, monit[-1] - 20)


def sha_heishan(m_list, monit):
    for i in m_list:
        # 打开客户端
        MouseUtil().left_click((m_list.index(i) + 2) * 160 - 29, monit[-1] - 20)
        lis = get_flight_flag_info('./' + i + '.txt')
        spare_flag = get_flag_name(lis, '备用棋')
        buy_flag = get_flag_name(lis, '长安杂货店(12,11)')
        # 杀黑山妖王
        # 使用指定位置的飞行棋飞到指定位置
        task_flag = get_flag_name(lis, '御马监(100,10)')
        fly_destination(task_flag.goods_position_y, task_flag.goods_position_x)
        # 左键点击npc,领取任务
        time.sleep(3)
        MouseUtil().left_click(230, 300)
        if task_flag.times_left == 1:
            time.sleep(19)
            replenish_piece(task_flag, spare_flag, buy_flag)
        else:
            task_flag.times_left = task_flag.times_left - 1
        save_flight_flag(lis, './' + i + '.txt')
        MouseUtil().left_click((m_list.index(i) + 2) * 160 - 29, monit[-1] - 20)


def sha_lanse(m_list, monit):
    for i in m_list:
        # 打开客户端
        MouseUtil().left_click((m_list.index(i) + 2) * 160 - 29, monit[-1] - 20)
        lis = get_flight_flag_info('./' + i + '.txt')
        spare_flag = get_flag_name(lis, '备用棋')
        buy_flag = get_flag_name(lis, '长安杂货店(12,11)')
        # 杀蓝色妖王
        # 使用指定位置的飞行棋飞到指定位置
        task_flag = get_flag_name(lis, '御马监(105,45)')
        fly_destination(task_flag.goods_position_y, task_flag.goods_position_x)
        # 左键点击npc,领取任务
        time.sleep(3)
        MouseUtil().left_click(280, 240)
        if task_flag.times_left == 1:
            time.sleep(19)
            replenish_piece(task_flag, spare_flag, buy_flag)
        else:
            task_flag.times_left = task_flag.times_left - 1
        save_flight_flag(lis, './' + i + '.txt')
        MouseUtil().left_click((m_list.index(i) + 2) * 160 - 29, monit[-1] - 20)


def sha_wannian(m_list, monit):
    for i in m_list:
        # 打开客户端
        MouseUtil().left_click((m_list.index(i) + 2) * 160 - 29, monit[-1] - 20)
        lis = get_flight_flag_info('./' + i + '.txt')
        spare_flag = get_flag_name(lis, '备用棋')
        buy_flag = get_flag_name(lis, '长安杂货店(12,11)')
        # 杀万年熊王
        # 使用指定位置的飞行棋飞到指定位置
        task_flag = get_flag_name(lis, '御马监(110,100)')
        fly_destination(task_flag.goods_position_y, task_flag.goods_position_x)
        # 左键点击npc,领取任务
        time.sleep(3)
        MouseUtil().left_click(480, 580)
        if task_flag.times_left == 1:
            time.sleep(19)
            replenish_piece(task_flag, spare_flag, buy_flag)
        else:
            task_flag.times_left = task_flag.times_left - 1
        save_flight_flag(lis, './' + i + '.txt')
        MouseUtil().left_click((m_list.index(i) + 2) * 160 - 29, monit[-1] - 20)


if __name__ == '__main__':
    for i in range(48):
        ling_sha_santou(lis, monitor)
        sha_heishan(lis, monitor)
        sha_lanse(lis, monitor)
        sha_wannian(lis, monitor)
        print(i)