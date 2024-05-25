import requests

from logger import logger


def get_weather_data(city: list[str]):
    """
    回傳臺灣各縣市未來七天內多個時段的天氣預報
    台中、台北等要轉換成臺中、臺北
    輸入需自動對應到以下縣市:
    ["臺北市","新北市","桃園市","臺中市","臺南市","高雄市","基隆市","新竹市","嘉義市","宜蘭縣","新竹縣","苗栗縣","彰化縣","南投縣","雲林縣","嘉義縣","屏東縣","花蓮縣","臺東縣","澎湖縣","金門縣","連江縣"]
    """

    logger.info(f"get weather data of {city}")

    apikey = "CWA-C87D7630-0DDC-46F4-B546-E063D3533CFF"
    dataid = "F-D0047-091"
    url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/{dataid}?Authorization={apikey}&format=JSON"
    res = requests.get(url)

    raw_data = res.json()
    raw_data = raw_data["records"]["locations"][0]

    data = raw_data["location"]

    temps = []
    for i in data:
        temp = {}
        temp["locationName"] = i["locationName"]
        for j in i["weatherElement"]:
            if j["elementName"] == "WeatherDescription":
                temp["time"] = j["time"]
        if temp["locationName"] in city:
            temps.append(temp)

    return temps
