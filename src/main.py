import datetime
import logging
import sys
import os
import requests
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.database import create_connection, create_table, insert_greeting, fetch_greetings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_greeting(language):
    """
    Returns a greeting based on the current time of day and language.
    """
    current_hour = datetime.datetime.now().hour
    if language == "en":
        if current_hour < 12:
            return "Good morning"
        elif current_hour < 18:
            return "Good afternoon"
        else:
            return "Good evening"
    elif language == "es":
        if current_hour < 12:
            return "Buenos días"
        elif current_hour < 18:
            return "Buenas tardes"
        else:
            return "Buenas noches"
    elif language == "id":
        if current_hour < 12:
            return "Selamat pagi"
        elif current_hour < 18:
            return "Selamat sore"
        else:
            return "Selamat malam"

def get_day_greeting():
    """
    Returns a greeting based on the current day of the week.
    """
    day_of_week = datetime.datetime.now().strftime("%A")
    return f"Happy {day_of_week}!"

def get_weather(api_key, city):
    """
    Fetches the current weather for the given city using the OpenWeatherMap API.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"{weather_description.capitalize()}, {temperature}°C"
    else:
        return "Unable to fetch weather data"

def main():
    """
    Main function to run the greeting program.
    """
    # Connect to the database
    database = "greetings.db"
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
    
    # Get user's name and preferred language
    name = input("Enter your name: ")
    language = input("Enter your preferred language (en/es): ")
    
    # Generate greetings
    greeting = get_greeting(language)
    day_greeting = get_day_greeting()
    
    # Log the generated greetings
    logging.info(f"Day greeting generated: {day_greeting}")
    logging.info(f"Greeting generated: {greeting}")
    
    # Insert greeting into the database
    insert_greeting(conn, name, f"{greeting}, {name}! {day_greeting}")
    
    # Fetch and display all greetings from the database
    rows = fetch_greetings(conn)
    for row in rows:
        print(row)
    
    # Print the greetings
    print(f"{greeting}, {name}! {day_greeting}")

if __name__ == "__main__":
    # Run the main function if this script is executed
    main()