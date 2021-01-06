import time

from pynput.keyboard import Controller, Key

from pynput.keyboard import Controller

from util.MouseUtil import MouseUtil
from util.ZuoTianUtil import click_tool_bar, right_goods

keyboard = Controller()
list1 = ['a979899', 'b979899', 'c979899', 'd979899', 'e979899']
screen = [1920, 1080]
# # 显示桌面
# MouseUtil().right_click(screen[0], screen[-1])
# keyboard.press('s')
# keyboard.release('s')
#
# for user in list1:
#     print(list1.index(user))
#     # 打开大话西游
#     MouseUtil().move_to(36, 44)
#     MouseUtil().click_left_two()
#     time.sleep(6)
#     # 堆叠窗口
#     MouseUtil().right_click(1440 - 100, screen[-1])
#     keyboard.press('e')
#     keyboard.release('e')
#
#     MouseUtil().left_click(680, 170)
#     MouseUtil().left_click(260, 155)
#     MouseUtil().left_click(600, 270)
#     time.sleep(1)
#     for i in range(10):
#         keyboard.press(Key.backspace)
#         keyboard.release(Key.backspace)
#     time.sleep(1)
#     for every_char in user:
#         keyboard.press(every_char)
#         keyboard.release(every_char)
#     time.sleep(1)
#     MouseUtil().left_click(600, 320)
#     time.sleep(1)
#     for i in range(10):
#         keyboard.press(Key.backspace)
#         keyboard.release(Key.backspace)
#     time.sleep(1)
#     for every_char in user:
#         keyboard.press(every_char)
#         keyboard.release(every_char)
#     time.sleep(1)
#     MouseUtil().left_click(350, 400)
#     # 选择第一个人物
#     MouseUtil().left_click(200, 290)
#     MouseUtil().left_click(150, 540)
#     MouseUtil().left_click(400, 510)
#     for i in range(3):
#         MouseUtil().left_click(110, 595)
#     click_tool_bar(2)
#     MouseUtil().left_click(410, 300)
#     click_tool_bar(2)
#     MouseUtil().left_click(500, 200)
#     click_tool_bar(2)
#     for i in range(4):
#         MouseUtil().left_click(400, 265)
#         MouseUtil().left_click(315, 425)
#     click_tool_bar(2)
#     click_tool_bar(10)
#     MouseUtil().left_click(350, 425)
#     MouseUtil().left_click(350, 425)
#     click_tool_bar(10)
#     # for i in range(5):
#     #     MouseUtil().left_click(315 + (i * 46), 50)
#     #     if i == 0:
#     #         click_tool_bar(1)
#     #         right_goods(4, 4)
#     #     right_goods(4, 5)
#     #     right_goods(4, 6)
#     MouseUtil().left_click(315, 50)
#     MouseUtil().left_click((list1.index(user) + 3) * 160 - 29, screen[-1] - 20)
# MouseUtil().move_to(760, 240)
# MouseUtil().move_to(760, 400)

#  选择法术
# MouseUtil().move_to(760, 250+(0*20))

#  选择具体哪个法术
# MouseUtil().move_to(570, 227+(2*28))
# 移动到boss上
# MouseUtil().move_to(150, 300)


# MouseUtil().left_click(760, 225+(1*23))
# MouseUtil().left_click(570, 227+(3*28))
# MouseUtil().left_click(150, 300)
#
# MouseUtil().left_click(760, 225+(1*23))
# MouseUtil().left_click(570, 227+(2*28))
# MouseUtil().left_click(150, 300)
#
# MouseUtil().left_click(780, 125)
#
#
# MouseUtil().left_click(760, 225+(1*23))
# MouseUtil().left_click(570, 227+(3*28))
# MouseUtil().left_click(150, 300)
#
# MouseUtil().left_click(760, 225+(1*23))
#
# MouseUtil().left_click(780, 125)


MouseUtil().move_to(150, 300)
