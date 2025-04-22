from flask import Flask, render_template
from weather_fetcher import WeatherFetcher

app = Flask(__name__)
weather_fetcher = WeatherFetcher()
precipitation_img_url = "https://weather.cma.cn/web/channel-339.html"


@app.route('/')
def index():
    forecasts = weather_fetcher.get_weather_forecast("101220101")
    return render_template('index.html', forecasts=forecasts, precipitation_img_url=precipitation_img_url)


if __name__ == '__main__':
    app.run(debug=True)