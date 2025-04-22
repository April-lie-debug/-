import requests
from bs4 import BeautifulSoup


class WeatherFetcher:
    def __init__(self):
        self.base_url = "https://www.weather.com.cn/weather/"

    def get_weather_forecast(self, city_code):
        try:
            url = self.base_url + city_code + ".shtml"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            soup = BeautifulSoup(response.text, 'html.parser')
            forecasts = []
            ul = soup.find('ul', class_='t clearfix')
            if ul:
                lis = ul.find_all('li')
                for li in lis:
                    date = li.find('h1').text
                    weather = li.find_all('p')[0].text
                    temperatures = li.find_all('p')[1].text
                    wind = li.find_all('p')[2].text
                    if '/' in temperatures:
                        mintemp, maxtemp = temperatures.split('/')
                        mintemp = mintemp.strip()
                        maxtemp = maxtemp.strip()
                    else:
                        mintemp = temperatures.strip()
                        maxtemp = temperatures.strip()
                    forecasts.append({
                        "date": date,
                        "maxtemp": maxtemp,
                        "mintemp": mintemp,
                        "condition": weather,
                        "wind": wind
                    })
            return forecasts
        except requests.RequestException as e:
            print(f"请求出错: {e}")
            return []
        except Exception as e:
            print(f"解析数据出错: {e}")
            return []