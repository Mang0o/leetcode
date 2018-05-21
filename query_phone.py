import requests
import arrow as ar
import hashlib

def get_now_timestamp():
    utc = ar.utcnow()
    return utc.timestamp * 1000

def _generate_url():
    values = {'phone': '15248643899', 'service_type': 'mobile_inverse_call'}
    print(values)
    url = 'https://open.wecash.net/query/v1'
    key = '95263655-787D-49B7-BDB8-3EA56D1B4C57-20170109112720225-100225'
    source = '100225'
    data = {
        'source': source,
        'data_format_type': 'origin',
        'key': key,
    }
    data.update(values)
    data['timestamp'] = str(get_now_timestamp())

    print(data)
    dataStr = ''.join(sorted(data.values()))
    signature = hashlib.md5(dataStr.encode("utf8")).hexdigest().upper()
    query = url + '/{source}?data_format_type=origin&timestamp={timestamp}&signature={signature}'
    result = query.format(source=data['source'], timestamp=data['timestamp'], signature=signature)
    for key, value in values.items():
        result += '&' + key + '=' + value
    return result
#手机号反向联系人查询 mobile_inverse_contact {"success":true,"code":"E000000","message":"请求成功","data":{"mobile_inverse_contact":[{"origin":{"code":"E000001","message":"系统繁忙,请稍后再试"}}]}}
#手机号反向通话信息查询 {"success":true,"code":"E000000","message":"请求成功","data":{"mobile_inverse_call":[{"origin":{"code":"E000001","message":"系统繁忙,请稍后再试"}}]}}
if __name__ == '__main__':
    
    url = _generate_url()
    response = requests.post(url, timeout=10)
    print(response.text)
