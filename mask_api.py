import requests

import json

def get_masknum():
    serviceKey = "msYRhJ6JOgdasigGM0PhgnBk3Cgm2oqEwEw90bD4dD9hqTzqMYU8w27FFzW59HzhWPFIuMUwGzA7pRJjqYgMBQ=="
    url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureLIst'
# ------------------------------------------------------- 미세먼지   ---------------------------------------------------------------------------------------------------------------------------
    pm10_params ={'serviceKey' : serviceKey, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'itemCode' : 'PM10', 'dataGubun' : 'HOUR', 'searchCondition' : 'MONTH' }

    pm10_response = requests.get(url, params=pm10_params).content
    pm10_result = json.loads(pm10_response)

    pm10_incheon = pm10_result['response']['body']['items'][0]['incheon']
    pm10_geyonggi = pm10_result['response']['body']['items'][0]['gyeonggi']
    pm10_avg = (int(pm10_incheon) + int(pm10_geyonggi)) / 2
    print(f"미세먼지 인천: {pm10_incheon}, 경기:{pm10_geyonggi}, 평균: {pm10_avg}")
#-------------------------------------------------------  초미세먼지   ---------------------------------------------------------------------------------------------------------------------------
    pm25_params ={'serviceKey' : serviceKey, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'itemCode' : 'PM25', 'dataGubun' : 'HOUR', 'searchCondition' : 'MONTH' }
    pm25_response = requests.get(url, params=pm25_params).content
    pm25_result = json.loads(pm25_response)

    pm25_incheon = pm25_result['response']['body']['items'][0]['incheon']
    pm25_geyonggi = pm25_result['response']['body']['items'][0]['gyeonggi']
    pm25_avg = (int(pm25_incheon) + int(pm25_geyonggi)) / 2
    print(f"초미세먼지 인천: {pm25_incheon}, 경기:{pm25_geyonggi}, 평균: {pm25_avg}")

# -------------------------------------------------------  오존(O3)   ---------------------------------------------------------------------------------------------------------------------------
    O3_params = {'serviceKey' : serviceKey, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'itemCode' : 'O3', 'dataGubun' : 'HOUR', 'searchCondition' : 'MONTH' }

    O3_response = requests.get(url, params=O3_params).content
    O3_result = json.loads(O3_response)

    O3_incheon = O3_result['response']['body']['items'][0]['incheon']
    O3_geyonggi = O3_result['response']['body']['items'][0]['gyeonggi']
    O3_avg = (float(O3_incheon) + float(O3_geyonggi)) / 2
    print(f"초미세먼지 인천: {O3_incheon}, 경기:{O3_geyonggi}, 평균: {O3_avg}")

    return pm10_avg,pm25_avg,O3_avg

if __name__ == "__main__":
    get_masknum()
