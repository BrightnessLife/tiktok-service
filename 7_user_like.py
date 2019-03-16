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

    # 获取某人喜欢的视频
    print(wrap_api("v1/aweme/favorite",
                   {"user_id": user_id, "max_cursor": 0, "count": 20},
                   device_info=device_info,
                   token=API_TOKEN))
