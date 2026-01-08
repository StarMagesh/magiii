async function getWeather() {
  const city = document.getElementById("city").value.trim();
  const resultDiv = document.getElementById("weather-result");
  resultDiv.style.opacity = 0;

  if (!city) {
    resultDiv.innerHTML = `<p style="color:red;">Please enter a city name.</p>`;
    resultDiv.style.opacity = 1;
    return;
  }

  try {
    const response = await fetch(`http://localhost:5000/weather?city=${city}`);
    const data = await response.json();

    if (data.error) {
      resultDiv.innerHTML = `<p style="color:red;">${data.error}</p>`;
    } else {
      resultDiv.innerHTML = `
        <p><strong>Temperature:</strong> ${data.temp}°C</p>
        <p><strong>Humidity:</strong> ${data.humidity}%</p>
        <p><strong>Condition:</strong> ${data.condition}</p>
      `;
    }

    resultDiv.style.opacity = 1;
  } catch (error) {
    resultDiv.innerHTML = `<p style="color:red;">Failed to fetch weather data.</p>`;
    resultDiv.style.opacity = 1;
  }
}

async function predictTemp() {
  const day = document.getElementById("day").value.trim();
  const resultDiv = document.getElementById("predict-result");
  resultDiv.style.opacity = 0;

  if (!day || isNaN(day)) {
    resultDiv.innerHTML = `<p style="color:red;">Please enter a valid day number.</p>`;
    resultDiv.style.opacity = 1;
    return;
  }

  try {
    const response = await fetch(`http://localhost:5000/predict?day=${day}`);
    const data = await response.json();

    if (data.error) {
      resultDiv.innerHTML = `<p style="color:red;">${data.error}</p>`;
    } else {
      resultDiv.innerHTML = `<p>Predicted Temperature for Day ${data.day}: <strong>${data.predicted_temp}°C</strong></p>`;
    }

    resultDiv.style.opacity = 1;
  } catch (error) {
    resultDiv.innerHTML = `<p style="color:red;">Prediction failed.</p>`;
    resultDiv.style.opacity = 1;
  }
}