from pynput.keyboard import Controller

from util.MouseUtil import MouseUtil
import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText

from entity.DaHuaBean import get_flight_flag_info, get_flag_name, save_flight_flag
from util.MouseUtil import MouseUtil
from util.ZuoTianUtil import replenish_piece, fly_destination, click_task

keyboard = Controller()
list1 = ['a979899', 'b979899', 'c979899', 'd979899', 'e979899']
# # 显示桌面
# MouseUtil().right_click(1440, 1080)
# keyboard.press('s')
# keyboard.release('s')
#
# for i in range(5):
#     # 打开大话西游
#     MouseUtil().move_to(36, 44)
#     MouseUtil().click_left_two()
#     time.sleep(6)
#     # 堆叠窗口
#     MouseUtil().right_click(1440 - 100, 900)
#     keyboard.press('e')
#     keyboard.release('e')
#     MouseUtil().left_click((i + 2) * 160 - 29, 880)
#     MouseUtil().left_click((i + 2) * 160 - 29, 880)
# for i in range(5):



for i in list1:
    print(list1.index(i))






# MouseUtil().move_to(51, 880)
# MouseUtil().move_to(211, 880)

# MouseUtil().move_to(212, 880)
# MouseUtil().move_to(212+160, 880)

# MouseUtil().move_to(131, 860)
# MouseUtil().move_to(131, 900)

# MouseUtil().move_to((160 * 1) - 29, 880)





# # 显示桌面
# MouseUtil().right_click(1440, 1080)
# keyboard.press('s')
# keyboard.release('s')
# for i in range(5):
#     MouseUtil().left_click((i+2)*160-29, 880)

#     # 显示桌面
#     MouseUtil().right_click(1440, 1080)
#     keyboard.press('s')
#     keyboard.release('s')
# MouseUtil().left_click((0 + 2) * 160 - 29, 880)


# MouseUtil().move_to(680, 170)
# MouseUtil().move_to(260, 155)
# MouseUtil().move_to(600, 270)
# MouseUtil().move_to(600, 320)