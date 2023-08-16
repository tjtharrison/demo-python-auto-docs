"""Functions to convert units of temperature."""


def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9 / 5) + 32


def convert_celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin.

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Kelvin
    """
    return celsius + 273.15


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5 / 9


def convert_fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin.

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Kelvin
    """
    return (fahrenheit + 459.67) * 5 / 9


def convert_kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius.

    Args:
        kelvin (float): Temperature in Kelvin

    Returns:
        float: Temperature in Celsius
    """
    return kelvin - 273.15


def convert_kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit.

    Args:
        kelvin (float): Temperature in Kelvin

    Returns:
        float: Temperature in Fahrenheit
    """
    return (kelvin * 9 / 5) - 459.67


def convert_celsius(value, target):
    """Convert Celsius to target unit.

    Args:
        value (float): Temperature in Celsius
        target (str): Target unit

    Returns:
        float: Temperature in target unit
    """
    if target == "Fahrenheit":
        return convert_celsius_to_fahrenheit(value)
    if target == "Kelvin":
        return convert_celsius_to_kelvin(value)
    return value


def convert_fahrenheit(value, target):
    """Convert Fahrenheit to target unit.

    Args:
        value (float): Temperature in Fahrenheit
        target (str): Target unit

    Returns:
        float: Temperature in target unit
    """
    if target == "Celsius":
        return convert_fahrenheit_to_celsius(value)
    if target == "Kelvin":
        return convert_fahrenheit_to_kelvin(value)
    return value


def convert_kelvin(value, target):
    """Convert Kelvin to target unit.

    Args:
        value (float): Temperature in Kelvin
        target (str): Target unit

    Returns:
        float: Temperature in target unit
    """
    if target == "Celsius":
        return convert_kelvin_to_celsius(value)
    if target == "Fahrenheit":
        return convert_kelvin_to_fahrenheit(value)
    return value
