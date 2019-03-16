## Tiktok在线签名服务

> This is based on tiktok version 8.7.2

> Any questions, pls email  [vsdouyin@yandex.com](vsdouyin@yandex.com)

### Step 1
Gen an api token to call our service

+ Just click [http://sign.vsdouyin.com/api/token/gen/](http://sign.vsdouyin.com/api/token/gen/) 
+ Paste to file `config.py` with key `API_TOKEN`
+ Run `python3 1_info_token.py` get rest times of token 

### Step 2
+ Run `python3 2_gen_device.py` to gen device info

### Step 3
+ Run `python3 3_test_as_cp_mas.py`to gen as/cp/mas params

## Step 4
+ Run other python fileS to test tiktok functions.

