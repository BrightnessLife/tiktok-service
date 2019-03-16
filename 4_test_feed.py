from config import API_TOKEN
from lib import wrap_api


if __name__ == '__main__':
    device_info = {'device_id': "6669054101932197381",
                   'install_id': "6669054741999814406",
                   'openudid': '6313442506917502',
                   'uuid': '987632903158726'}

    # 获取首页feed
    print(wrap_api("v1/feed",
                   {'count': 6, 'type': 0, 'max_cursor': 0, 'min_cursor': -1, 'pull_type': 2},
                   device_info=device_info,
                   token=API_TOKEN))
