from flask import Flask, render_template, request, send_from_directory
from weather_fetcher import WeatherFetcher
import os

app = Flask(__name__)
weather_fetcher = WeatherFetcher()
precipitation_img_url = "https://weather.cma.cn/web/channel-339.html"

# 定义城市代码与城市名称的映射
city_codes = {
    "合肥": "101220101",
    "北京": "101010100",
    "上海": "101020100",
    "广州": "101280101",
    "深圳": "101280601"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取用户选择的城市
        selected_city = request.form.get('city')
        if selected_city in city_codes:
            city_code = city_codes[selected_city]
            forecasts = weather_fetcher.get_weather_forecast(city_code)
        else:
            # 若城市代码不存在，默认显示合肥的天气
            forecasts = weather_fetcher.get_weather_forecast("101220101")
    else:
        # 默认显示合肥的天气
        forecasts = weather_fetcher.get_weather_forecast("101220101")

    return render_template('index.html', forecasts=forecasts, precipitation_img_url=precipitation_img_url, city_codes=city_codes)

# 处理 favicon.ico 请求
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(debug=True)