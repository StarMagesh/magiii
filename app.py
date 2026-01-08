from flask import Flask, request, jsonify
from flask_cors import CORS
from predictor import predict_temperature
import requests

app = Flask(__name__)
CORS(app)

# Supported cities with coordinates
CITY_COORDS = {
    "vellore": (12.9165, 79.1325),
    "chennai": (13.0827, 80.2707),
    "madurai": (9.9252, 78.1198),
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777)
}

def get_open_meteo_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        res = requests.get(url).json()
        if "current_weather" in res:
            weather = res["current_weather"]
            return {
                "temp": weather["temperature"],
                "wind": weather["windspeed"],
                "condition": f"Wind {weather['windspeed']} km/h"
            }
        else:
            return None
    except:
        return None

@app.route('/weather')
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City name is required"}), 400

    city = city.lower()
    if city in CITY_COORDS:
        lat, lon = CITY_COORDS[city]
        data = get_open_meteo_weather(lat, lon)
        if data:
            return jsonify(data)
        else:
            return jsonify({"error": "Weather data not available"}), 404
    else:
        return jsonify({"error": f"City '{city}' not supported"}), 400

@app.route('/predict')
def predict():
    try:
        day = int(request.args.get('day'))
        predicted_temp = predict_temperature(day)
        if predicted_temp is None:
            return jsonify({"error": "Day must be between 1 and 30"}), 400
        return jsonify({"day": day, "predicted_temp": predicted_temp})
    except:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)