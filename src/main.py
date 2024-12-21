import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_greeting(language):
    """
    This function returns a greeting message based on the current time of the day."""
    current_hour = datetime.datetime.now().hour
    # Determine the appropriate greeting message based on the current time
    if language == "en":
        if current_hour < 12:
            return "Good morning"
        elif current_hour < 18:
            return "Good afternoon"
        else:
            return "Good evening"
    # Add support for Spanish language
    elif language == "es":
        if current_hour < 12:
            return "Buenos días"
        elif current_hour < 18:
            return "Buenas tardes"
        else:
            return "Buenas noches"


def get_day_greeting():
    """
    This function returns a greeting message based on the current day of the week."""
    day_of_week = datetime.datetime.now().strftime("%A")
    return f"Happy {day_of_week}!"

def main():
    """
    This is the main function that gets the user's name, generates a greeting message, and prints it to the console.
    """
    # Get the user's name
    name = input("Enter your name: ")
    language = input("Enter your language (en/es): ")

    # Generate the greeting message
    greeting = get_greeting(language)
    day_greeting = get_day_greeting()

    # Log the generated greetings
    logging.info(f"Day greeting generated: {day_greeting}")
    logging.info(f"Greeting generated: {greeting}")

    # Print the greeting message
    print(f"{greeting}, {name}! {day_greeting}")

if __name__ == "__main__":
    # Run the main function if the script is executed
    main()