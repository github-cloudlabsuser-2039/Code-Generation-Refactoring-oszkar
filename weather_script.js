const fetch = require('node-fetch'); // Ensure you have node-fetch installed (npm install node-fetch)

async function fetchWeather(cityName, apiKey) {
    const baseUrl = "http://api.openweathermap.org/data/2.5/weather";
    const url = `${baseUrl}?q=${cityName}&appid=${apiKey}&units=metric`; // Use "imperial" for Fahrenheit

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const weatherData = await response.json();
        return weatherData;
    } catch (error) {
        return { error: error.message };
    }
}

(async () => {
    const API_KEY = "your_api_key_here"; // Replace with your OpenWeatherMap API key
    const city = "London"; // Replace with the desired city name

    const weatherData = await fetchWeather(city, API_KEY);

    if (weatherData.error) {
        console.log(`Error: ${weatherData.error}`);
    } else {
        console.log(`Weather in ${weatherData.name}:`);
        console.log(`Temperature: ${weatherData.main.temp}°C`);
        console.log(`Weather: ${weatherData.weather[0].description.charAt(0).toUpperCase() + weatherData.weather[0].description.slice(1)}`);
        console.log(`Humidity: ${weatherData.main.humidity}%`);
    }
})();