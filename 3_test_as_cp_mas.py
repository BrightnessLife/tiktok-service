from config import API_TOKEN
from lib import sign


def test_sign(token):
    print(sign(
        "https://api2-t2.musical.ly/aweme/v1/feed/?type=0&max_cursor=0&min_cursor=-1&count=6&volume=0.0&pull_type=2&req_from=&gaid=4128863a-83f1-491b-b31c-0d7f3cf12e13&ad_user_agent=Dalvik%2F2.1.0+%28Linux%3B+U%3B+Android+7.0%3B+SM-G920F+Build%2FNRD90M%29&app_type=normal&os_api=24&device_type=SM-G920F&ssmix=a&manifest_version_code=2018101602&dpi=640&region=US&carrier_region=FR&carrier_region_v2=208&app_name=musical_ly&version_name=8.7.2&timezone_offset=3600&is_my_cn=0&fp=&ac=wifi&update_version_code=2018101602&channel=googleplay&_rticket=1540184431288&device_platform=android&iid=6612973476225517317&build_number=8.7.2&version_code=872&timezone_name=Europe%2FParis&account_region=FR&openudid=2d439307c172ba73&sys_region=GB&device_id=6575510197157217798&app_language=en&resolution=1440*2464&os_version=7.0&device_brand=samsung&language=en&aid=1233&mcc_mnc=20801",
        token=token))


if __name__ == '__main__':
    device_info = {'device_id': "66762742687",
                   'install_id': "66088143957",
                   'openudid': '3275465180871399',
                   'uuid': '187604370269819'}

    # 测试签名
    test_sign(API_TOKEN)
