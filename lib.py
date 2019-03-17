#!/usr/bin/env python3
# encoding: utf-8
import json
from time import time
from urllib.parse import unquote_plus

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from config import API_EP_TIKTOK, ROUTE_SIGN_TIKTOK

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_original_url(action, args_dict, ts, device_info):
    install_id = device_info['install_id']
    device_id = device_info['device_id']
    uuid = device_info['uuid']
    openudid = device_info['openudid']

    args = ""
    # print(args_dict)
    for (idx, val) in args_dict.items():
        args += "&{0}={1}".format(idx, val)

    url = 'https://api2.musical.ly/aweme/' + action + "/?" \
          + args \
          + '&retry_type=no_retry' \
          + '&iid=' + str(install_id) \
          + '&device_id=' + str(device_id) \
          + "&openudid=" + str(openudid) \
          + "&ts=" + str(ts) \
          + '&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=872&version_name=8.7.2&device_platform=android&ab_version=8.7.2&ssmix=a&device_type=ONEPLUS+A5000&device_brand=OnePlus&os_api=27&os_version=8.1.0&app_language=zh-Hant&language=zh&region=JP&sys_region=JP&carrier_region=JP&build_number=8.7.2&timezone_offset=28800&timezone_name=Asia%2FShanghai&mcc_mnc=46001&is_my_cn=0&fp=PrT_c2LZLMwbFlqMFlU1LSFIJzQZ&account_region=HK&pass-region=1&pass-route=1&manifest_version_code=2018101602&resolution=1080*1920&dpi=420&update_version_code=2018101602&_rticket=1543507053287';
    return url


def get_signed_url(action, args, ts, device_info, token=""):
    original_url = get_original_url(action, args, ts, device_info)
    # print(original_url)

    return sign(original_url, token=token)


def sign(original_url, token=""):
    data = {"url": original_url}
    try:
        data = api_service(token=token, route=ROUTE_SIGN_TIKTOK, method="post", data=json.dumps(data))
        # print(data)
        # data = json.loads(content)
        return data.get("url")
    except Exception as e:
        print(e)


def api_douyin(action, args, ts, device_info, token=""):
    try:
        url = get_signed_url(action, args, ts, device_info, token=token)
        resp = requests.get(url=url,
                            headers={
                                "User-Agent": "com.zhiliaoapp.musically/2018101602 (Linux; U; Android 9; zh_CN; ONEPLUS A5000; Build/PKQ1.180716.001; Cronet/58.0.2991.0)"},
                            verify=False,
                            cookies={'install_id': str(device_info['install_id'])})
        content = resp.content.decode("utf-8")
        # print("ssss", url, resp.content, resp.status_code)
        d = json.loads(content)
        return d
    except Exception as e:
        print(e)


def api_service(route, token="", method="get", data=None, content_type="application/json"):
    resp = requests.request(method=method, url="{0}/{1}/{2}".format(API_EP_TIKTOK, route,token), data=data,
                            headers={"Content-Type": content_type}, verify=False)

    # print(resp.content)
    if token != "" and resp.headers.get("x-token") != token:
        raise Exception(resp.headers.get("x-token"))
    elif resp.headers.get("x-token-times") == "0":
        raise Exception(resp.content.decode("utf-8"))
    data = resp.content.decode("utf-8")
    return json.loads(data)


# ————————————————————  APIs  ——————————————————————


def wrap_api(action, args, device_info={}, token=""):
    try:
        ts = str(int(time()))
        data = api_douyin(action, args, ts, device_info, token=token)
        return data
    except Exception as e:
        print(e)


def request_dict(req):
    params = req.split("?")[1]
    lp = params.split('&')
    di = {}
    for e in lp:
        k, v = e.split('=')
        di[k] = unquote_plus(v)

    return dict(di)
