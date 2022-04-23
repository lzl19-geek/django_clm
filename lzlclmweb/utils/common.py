from django.conf import settings
def get_lng_lat(address):
    """将地址解析为经纬度"""
    import json
    from urllib.request import urlopen, quote

    url = settings.BAIDU_LNG_LAT_URL
    output = 'json'
    ak = settings.BAIDU_AK
    address = quote(address)  # 为防止乱码用quote进行编码
    uri = url + '?' + 'address=' + address + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode()
    temp = json.loads(res)
    lat = temp['result']['location']['lat']
    lng = temp['result']['location']['lng']

    # get_distance_duration({'lat': 45.979928, 'lng': 122.434658}, {'lat': lat, 'lng': lng})

    return {'lat': lat, 'lng': lng}  # 纬度:latitude,经度:longitude


def get_distance_duration(origin, destination):
    """计算起点到达终点距离（米）、时间（秒），以及配送费"""
    import json
    from urllib.request import urlopen, quote

    url = settings.BAIDU_RIDING_URL
    ak = settings.BAIDU_AK
    # 起点经纬度，格式为：纬度,经度；小数点后不超过6位，40.056878,116.30815
    origin_lng = str(origin['lng'])
    origin_lat = str(origin['lat'])
    destination_lng = str(destination['lng'])
    destination_lat = str(destination['lat'])
    uri = url + '?' + 'origin=' + origin_lat + ',' + origin_lng + '&' + 'destination=' + destination_lat + ',' + destination_lng + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode()
    temp = json.loads(res)
    if temp['status'] == 0:
        distance = temp['result']['routes'][0]['distance']
        duration = temp['result']['routes'][0]['duration']
    else:
        distance, duration = 0, 0
    return {'distance': distance, 'duration': duration}


def verify_exist(request, name, value):
    """校验是否重复"""
    from apps.user.models import User

    try:
        user = User.objects.get(**{name:value})
    except User.DoesNotExist:
        user = None
    if user:
        return True
    else:
        return False
