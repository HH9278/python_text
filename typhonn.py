import requests

def get_geo_info_by_zip(api_key, zip_code, country_code):
    url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={api_key}"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        lat = data['lat']
        lon = data['lon']
        print(f"郵便番号: {zip_code}")
        print(f"国コード: {country_code}")
        print(f"緯度: {lat}")
        print(f"経度: {lon}")
        return lat, lon  # 緯度と経度を返す
    else:
        print(f"エラーコード: {response.status_code}")
        print(f"エラーメッセージ: {response.json()}")
        return None, None

def get_weather_info(api_key, lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&lang=ja"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temp = data['main']['temp'] - 273.15  # ケルビンから摂氏に変換
        wind_speed = data['wind']['speed']

        print(f"天気: {weather_description}")
        print(f"温度: {temp:.2f}°C")
        print(f"風速: {wind_speed} m/s")
    else:
        print(f"エラーコード: {response.status_code}")
        print(f"エラーメッセージ: {response.json()}")

# 入力する情報
zip_code = "E14"        # ロンドンE14の郵便番号
country_code = "GB"     # イギリスの国コード
api_key = "a15b2264eb4de376e70a3325a6048156"  # ここにAPIキーを入力してください

# 緯度と経度を取得
lat, lon = get_geo_info_by_zip(api_key, zip_code, country_code)

# 緯度と経度が取得できた場合、天気情報を取得
if lat is not None and lon is not None:
    get_weather_info(api_key, lat, lon)