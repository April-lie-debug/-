from flask import Flask, render_template
from weather_fetcher import WeatherFetcher

app = Flask(__name__)
weather_fetcher = WeatherFetcher()


@app.route('/')
def index():
    forecasts = weather_fetcher.get_weather_forecast("101220101")
    return render_template('index.html', forecasts=forecasts)


if __name__ == '__main__':
    app.run(debug=True)
    