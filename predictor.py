import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model():
    df = pd.read_csv("weather_data.csv")
    X = df[["day"]]
    y = df["temp"]
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_temperature(day):
    if day < 1 or day > 30:
        return None
    model = train_model()
    prediction = model.predict([[day]])
    prediction = max(min(prediction[0], 45), 20)  # Clamp between 20°C and 45°C
    return round(prediction, 2)