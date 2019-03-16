import base64
import json
import random
import uuid
from time import time

import requests

from config import API_TOKEN, ROUTE_CRYPT_TIKTOK
from lib import api_service


def get_new_device_info(token):
    client_uuid = "".join(random.sample("01234567890123456789", 15))
    serial_number = "".join(random.sample("0123456789" + "abcdef", 16))
    openudid = "".join(random.sample("01234567890123456789", 16))
    params = {}
    data = {'_gen_time': str(int(time() * 1000)),
            'header': {'access': 'wifi',
                       'aid': '1233',
                       'app_version': '2.9.0',
                       'appkey': "5559e28267e58eb4c1000012",
                       'build_serial': serial_number,
                       'carrier': 'Lycamobile',
                       'channel': 'wandoujia',
                       'clientudid': client_uuid,
                       'cpu_abi': 'armeabi-v7a',
                       'density_dpi': '420',
                       'device_brand': 'samsung',
                       'device_manufacturer': 'LGE',
                       'device_model': 'Nexus 5X',
                       'display_density': 'mdpi',
                       'display_name': 'Douyin',
                       'google_aid': str(uuid.uuid4()),
                       'language': 'zh',
                       'manifest_version_code': '2018111632',
                       'mc': "2C:59:8A:70:54:{:02x}".format(random.randint(0, 0xFF)),
                       'mcc_mnc': '20820',
                       'not_request_sender': 0,
                       'openudid': openudid,
                       'os': 'Android',
                       'os_api': '27',
                       'os_version': '8.1.0',
                       'package': 'com.zhiliaoapp.musically',
                       # 'package': 'com.ss.android.ugc.aweme',
                       'region': 'US',
                       'release_build': '7f052cf_20181116',
                       'resolution': '1794x1080',
                       'rom': '4948239',
                       'rom_version': 'OPM6.171019.030.K1',
                       'sdk_version': '2.5.6.8',
                       'serial_number': serial_number,
                       'sig_hash': "194326e82c84a639a52e5c023116f12a",
                       'sim_region': 'fr',
                       'sim_serial_number': [],
                       'timezone': '1',
                       'tz_name': 'Europe\\/Madrid',
                       'tz_offset': '3600',
                       'update_version_code': '2018111632',
                       'version_code': '2018111632'},
            'magic_tag': 'ss_app_log'}

    try:
        data = api_service(route=ROUTE_CRYPT_TIKTOK, token=token, method="post", data=json.dumps(data),
                           content_type="application/json")
        data = base64.b64decode(data['base64_data'])
        headers = {
            'Content-Type': 'application/octet-stream;tt-data=a',
            'sdk-version': '1',
            'user-agent': 'okhttp/3.10.0.1',
        }
        resp = requests.post("http://applog.musical.ly/service/2/device_register/", params=params, headers=headers,
                             data=data)
        content = resp.content.decode("utf-8")
        new_device = json.loads(content)
        new_device['openudid'] = openudid
        new_device['android_id'] = serial_number
        new_device['uuid'] = client_uuid
        new_device['iid'] = new_device['install_id']

        return new_device
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    device_info = get_new_device_info(API_TOKEN)
    print(device_info)
