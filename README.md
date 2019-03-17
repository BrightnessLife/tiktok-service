## Tiktok online sign service

> This is based on tiktok version 8.7.2

> Any questions, pls email  [vsdouyin@yandex.com](vsdouyin@yandex.com)

### Step 1
Gen an api token to call our service

+ Just click [http://sign.vsdouyin.com/api/token/gen/](http://sign.vsdouyin.com/api/token/gen/) 
+ Paste to file `config.py` with key `API_TOKEN`
+ Get rest times of token
    + Run `python3 1_info_token.py` get rest times of token
    + or curl request (`b7f5a12b0dfa11f6c1046a2abe65eb94` is a sample token):
```bash
curl "https://sign.vsdouyin.com/api/token/info/b7f5a12b0dfa11f6c1046a2abe65eb94"
``` 

### Step 2
+ Run `python3 2_gen_device.py` to gen device info

### Step 3
+ Run `python3 3_test_as_cp_mas.py`to gen as/cp/mas params
+ Or curl request (`b7f5a12b0dfa11f6c1046a2abe65eb94` is a sample token):
```bash
# delete ts/as/cp/mas params of original url and run:
curl -X "POST" "https://sign.vsdouyin.com/api/e7ae35c/sign/b7f5a12b0dfa11f6c1046a2abe65eb94" \
     -H 'Content-Type: application/json' \
     -d $'{"url": "https://api2-t2.musical.ly/aweme/v1/feed/?type=0&max_cursor=0&min_cursor=-1&count=6&volume=0.0&pull_type=2&req_from=&gaid=4128863a-83f1-491b-b31c-0d7f3cf12e13&ad_user_agent=Dalvik%2F2.1.0+%28Linux%3B+U%3B+Android+7.0%3B+SM-G920F+Build%2FNRD90M%29&app_type=normal&os_api=24&device_type=SM-G920F&ssmix=a&manifest_version_code=2018101602&dpi=640&region=US&carrier_region=FR&carrier_region_v2=208&app_name=musical_ly&version_name=8.7.2&timezone_offset=3600&is_my_cn=0&fp=&ac=wifi&update_version_code=2018101602&channel=googleplay&_rticket=1540184431288&device_platform=android&iid=6612973476225517317&build_number=8.7.2&version_code=872&timezone_name=Europe%2FParis&account_region=FR&openudid=2d439307c172ba73&sys_region=GB&device_id=6575510197157217798&app_language=en&resolution=1440*2464&os_version=7.0&device_brand=samsung&language=en&aid=1233&mcc_mnc=20801"}'
```

## Step 4
+ Run other python files to test tiktok functions.

