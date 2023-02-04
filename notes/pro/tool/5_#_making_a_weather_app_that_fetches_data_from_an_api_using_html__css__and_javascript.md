# making A Weather App that fetches data from an API using HTML, CSS, and JavaScript

Sure, here's an example of a code for making a weather app using HTML, CSS, and JavaScript:

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather App</title>
    <style>
      /* Add your CSS styles here */
      body {
        font-family: Arial, sans-serif;
        background-color: #f2f2f2;
      }

      .container {
        max-width: 600px;
        margin: 0 auto;
        text-align: center;
        padding: 30px;
      }

      h1 {
        font-size: 36px;
        margin-bottom: 20px;
      }

      .weather-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
      }

      .weather-info {
        font-size: 18px;
        margin-top: 20px;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Weather App</h1>
      <div class="weather-card">
        <p class="weather-info">Loading...</p>
      </div>
    </div>

    <!-- Add your JavaScript here -->
    <script>
      const apiKey = "YOUR_API_KEY";
      const weatherCard = document.querySelector(".weather-card");
      const weatherInfo = document.querySelector(".weather-info");

      async function getWeather(city) {
        const response = await fetch(
          `http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`
        );
        const data = await response.json();
        return data;
      }

      async function displayWeather() {
        const city = "San Francisco";
        const weather = await getWeather(city);
        weatherInfo.innerHTML = `
          <p>Temperature: ${weather.main.temp}°F</p>
          <p>Description: ${weather.weather[0].description}</p>
        `;
      }

      displayWeather();
    </script>
  </body>
</html>
```

This code will display a weather app that fetches data from the OpenWeatherMap API and displays the temperature and description of the weather in a city. You will need to replace `YOUR_API_KEY` with your own API key, which you can obtain by signing up for a free account on the OpenWeatherMap website.
