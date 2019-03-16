from time import time

from config import API_TOKEN
from lib import wrap_api

if __name__ == '__main__':
    device_info = {'device_id': "6669054101932197381",
                   'install_id': "6669054741999814406",
                   'openudid': '6313442506917502',
                   'uuid': '987632903158726'}

    user_id = "6603395355915993094"
    aweme_id = "6626744652743576838"
    time_now = str(int(time()))

    # 获取某人的粉丝列表
    print(wrap_api("v1/user/follower/list",
                   {"user_id": user_id, "count": 20, "max_time": time_now},
                   device_info=device_info,
                   token=API_TOKEN
                   ))
