from flask import Flask, jsonify
from Lesson2.weather_api import get_weather
app = Flask(__name__) #This creates our app

@app.route('/')
def hello():
    return "Hello World!"


@app.route("/getWeather/<string:city>")
def getWeather(city):
    return (get_weather(city))

if __name__ == '__main__':
    app.run(debug=True)