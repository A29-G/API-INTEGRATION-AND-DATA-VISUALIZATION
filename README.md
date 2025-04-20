# API INTEGRATION AND DATA VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: AISHWARYA VEERANAGOUDA GIRIYAL

*INTERN ID*: CT04WU10

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR


*DESCRIPTION*

This project is a Python-based weather forecast visualization tool that uses the OpenWeatherMap API to retrieve and display a 5-day temperature forecast for a selected city. The main goal is to fetch real-time weather data from a public API and present it visually using line graphs. This project demonstrates the power of API integration, data handling, and visualization using Python, making it both educational and practical.

### Tools and Technologies Used

The project is built entirely in Python and utilizes the following tools:

1. **Requests**: A Python HTTP library used to send requests to the OpenWeatherMap API and fetch weather data in JSON format.
2. **Matplotlib**: A popular data visualization library in Python used to plot the temperature forecast graph.
3. **Datetime**: Python’s built-in module used to convert date-time strings from the API into proper datetime objects.
4. **Visual Studio Code (VS Code)**: A lightweight and versatile code editor used to develop and run the Python script. It includes integrated terminal support and syntax highlighting for efficient development.

### Project Workflow

The project starts by importing required libraries and defining essential configuration variables like the API key, city name (e.g., Delhi), and temperature unit (Celsius). It includes three main functions to divide responsibilities clearly:

1. **`fetch_weather_data(city)`**: This function constructs a URL using the provided city and API key, sends a GET request to OpenWeatherMap, and returns the response data in JSON format if successful.

2. **`process_data(weather_data)`**: This function processes the fetched data by extracting the date-time and temperature from each forecast entry. It stores these values in lists after converting timestamps into Python `datetime` objects.

3. **`visualize(dates, temperatures)`**: This function creates a line graph with time on the x-axis and temperature on the y-axis. The graph includes markers, gridlines, rotated labels, and a title to improve readability.

The main program flow calls these functions in order: it fetches the weather data, processes it, and finally plots the results on a line chart.

### Applications and Use Cases

This project is useful in various real-world situations. Travelers can check upcoming weather to plan trips. Students can study short-term weather trends visually for projects or research. Developers can expand this into a full weather dashboard, integrate it with smart home displays, or build mobile apps. Schools and colleges can use it as a practical project to teach Python, API integration, and data visualization.

### Importance and Skills Gained

This project helps users learn real-world programming skills such as API consumption, working with JSON data, processing time-series data, and visual storytelling with charts. It encourages clean, modular code and improves understanding of how external services interact with Python.

### Conclusion

The Weather Data Visualization Dashboard is a well-rounded mini-project that combines API integration, data processing, and plotting in Python. With simple configuration, users can change the target city or even expand features like humidity or wind tracking. It’s a flexible, educational tool and a great foundation for more advanced data-driven applications.




