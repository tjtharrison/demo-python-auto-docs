"""Small python project to use for converting various units of measurement."""

import inquirer
import sys

from bin import temperature, distance, weight

# Ask user for input
def get_units():
    """
    Ask user for input.

    Raises:
        KeyboardInterrupt: If user presses Ctrl+C.

    Returns:
         dict: Dictionary of user input.
    """
    try:
        unit_type = [
            inquirer.List(
                'unit',
                message='What unit would you like to convert?',
                choices=[
                    'Temperature',
                    'Distance',
                    'Weight'
                ]
        )]

        unit_type = inquirer.prompt(unit_type)["unit"]

        while True:
            if unit_type == 'Temperature':
                source_target = [
                    inquirer.List(
                        'source',
                        message='What unit would you like to convert from?',
                        choices=[
                            'Celsius',
                            'Fahrenheit',
                            'Kelvin'
                        ]
                    ),
                    inquirer.List(
                        'target',
                        message='What unit would you like to convert to?',
                        choices=[
                            'Celsius',
                            'Fahrenheit',
                            'Kelvin'
                        ]
                    )
                ]
            elif unit_type == 'Distance':
                source_target = [
                    inquirer.List(
                        'source',
                        message='What unit would you like to convert from?',
                        choices=[
                            'Meters',
                            'Kilometers',
                            'Miles',
                            'Inches'
                        ]
                    ),
                    inquirer.List(
                        'target',
                        message='What unit would you like to convert to?',
                        choices=[
                            'Meters',
                            'Kilometers',
                            'Miles',
                            'Inches'
                        ]
                    ),
                ]
            elif unit_type == 'Weight':
                source_target = [
                    inquirer.List(
                        'source',
                        message='What unit would you like to convert from?',
                        choices=[
                            'Grams',
                            'Kilograms',
                            'Pounds'
                        ]
                    ),
                    inquirer.List(
                        'target',
                        message='What unit would you like to convert to?',
                        choices=[
                            'Grams',
                            'Kilograms',
                            'Pounds'
                        ]
                    )
                ]

            source_target = inquirer.prompt(source_target)

            if source_target["source"] != source_target["target"]:
                break
            else:
                print('** Please choose different units to convert from and to.**')
                print("")

        response = {"unit_type": unit_type, "source_target": source_target}

        return response
    except KeyboardInterrupt as error_message:
        raise KeyboardInterrupt from error_message


def get_value():
    """
    Ask user for value to convert.

    Raises:
        KeyboardInterrupt: If user presses Ctrl+C.

    Returns:
        int: Value to convert.
    """
    try:

        while True:
            source_value = input('Enter value to convert: ')

            if source_value.isdigit():
                source_value = int(source_value)
                break

        return source_value
    except KeyboardInterrupt as error_message:
        raise KeyboardInterrupt from error_message

def main():
    """Main function for the program."""
    try:
        units = get_units()

        values = get_value()

        print("")
        print("Converting...")
        print("Source: " + str(values) + " " + units["source_target"]["source"])
        print("Target: " + units["source_target"]["target"])

        if units["source_target"]["source"] == "Celsius":
            result = temperature.convert_celsius(values, units["source_target"]["target"])
        elif units["source_target"]["source"] == "Fahrenheit":
            result = temperature.convert_fahrenheit(values, units["source_target"]["target"])
        elif units["source_target"]["source"] == "Kelvin":
            result = temperature.convert_kelvin(values, units["source_target"]["target"])
        elif units["source_target"]["source"] == "Meters":
            result = distance.convert_meters(values, units["source_target"]["target"])
        elif units["source_target"]["source"] == "Kilometers":
            result = distance.convert_kilometers(values, units["source_target"]["target"])
        elif units["source_target"]["source"] == "Miles":
            result = distance.convert_miles(values, units["source_target"]["target"])
        elif units["source_target"]["source"] == "Inches":
            result = distance.convert_inches(values, units["source_target"]["target"])
        elif units["source_target"]["source"] == "Grams":
            result = weight.convert_grams(values, units["source_target"]["target"])
        elif units["source_target"]["source"] == "Kilograms":
            result = weight.convert_kilograms(values, units["source_target"]["target"])
        elif units["source_target"]["source"] == "Pounds":
            result = weight.convert_pounds(values, units["source_target"]["target"])

        print("Answer: " + str(result) + " " + units["source_target"]["target"])


    except KeyboardInterrupt:
        print('\nExiting program...')
        sys.exit(0)


if __name__ == '__main__':
    main()
