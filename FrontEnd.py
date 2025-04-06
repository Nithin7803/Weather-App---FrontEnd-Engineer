// App.js (main logic)
import React, { useState, useEffect } from 'react';
import WeatherCard from './WeatherCard';
import ForecastCard from './ForecastCard';
import './index.css';

const API_KEY = process.env.REACT_APP_WEATHER_API;

function App() {
  const [city, setCity] = useState('');
  const [weather, setWeather] = useState(null);
  const [forecast, setForecast] = useState([]);
  const [error, setError] = useState('');

  const getWeather = async (query) => {
    try {
      const res = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${query}&appid=${API_KEY}&units=metric`);
      if (!res.ok) throw new Error("City not found");
      const data = await res.json();
      setWeather(data);
      getForecast(query);
      setError('');
    } catch (err) {
      setError(err.message);
      setWeather(null);
    }
  };

  const getForecast = async (query) => {
    const res = await fetch(`https://api.openweathermap.org/data/2.5/forecast?q=${query}&appid=${API_KEY}&units=metric`);
    const data = await res.json();
    const daily = data.list.filter(item => item.dt_txt.includes("12:00:00"));
    setForecast(daily);
  };

  return (
    <div className="min-h-screen bg-blue-100 p-6 text-center">
      <h1 className="text-3xl font-bold mb-4">Weather App 🌤️</h1>
      <input
        className="p-2 border rounded"
        value={city}
        onChange={(e) => setCity(e.target.value)}
        placeholder="Enter city"
      />
      <button onClick={() => getWeather(city)} className="ml-2 p-2 bg-blue-500 text-white rounded">Search</button>
      {error && <p className="text-red-600 mt-2">{error}</p>}
      {weather && <WeatherCard weather={weather} />}
      {forecast.length > 0 && <ForecastCard forecast={forecast} />}
    </div>
  );
}

export default App;
