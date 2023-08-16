"""Functions to convert units of temperature"""

def convert_celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32

def convert_celsius_to_kelvin(celsius):
    """Converts Celsius to Kelvin

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Kelvin
    """
    return celsius + 273.15

def convert_fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5/9

def convert_fahrenheit_to_kelvin(fahrenheit):
    """Converts Fahrenheit to Kelvin

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Kelvin
    """
    return (fahrenheit + 459.67) * 5/9

def convert_kelvin_to_celsius(kelvin):
    """Converts Kelvin to Celsius

    Args:
        kelvin (float): Temperature in Kelvin

    Returns:
        float: Temperature in Celsius
    """
    return kelvin - 273.15



def convert_kelvin_to_fahrenheit(kelvin):
    """Converts Kelvin to Fahrenheit

    Args:
        kelvin (float): Temperature in Kelvin

    Returns:
        float: Temperature in Fahrenheit
    """
    return (kelvin * 9/5) - 459.67


def convert_celsus(value, target):
    """Converts Celsius to target unit

    Args:
        value (float): Temperature in Celsius
        target (str): Target unit

    Returns:
        float: Temperature in target unit
    """
    if target == 'Fahrenheit':
        return convert_celsius_to_fahrenheit(value)
    elif target == 'Kelvin':
        return convert_celsius_to_kelvin(value)
    else:
        return value


def convert_fahrenheit(value, target):
    """Converts Fahrenheit to target unit

    Args:
        value (float): Temperature in Fahrenheit
        target (str): Target unit

    Returns:
        float: Temperature in target unit
    """
    if target == 'Celsius':
        return convert_fahrenheit_to_celsius(value)
    elif target == 'Kelvin':
        return convert_fahrenheit_to_kelvin(value)
    else:
        return value


def convert_kelvin(value, target):
    """Converts Kelvin to target unit

    Args:
        value (float): Temperature in Kelvin
        target (str): Target unit

    Returns:
        float: Temperature in target unit
    """
    if target == 'Celsius':
        return convert_kelvin_to_celsius(value)
    elif target == 'Fahrenheit':
        return convert_kelvin_to_fahrenheit(value)
    else:
        return value
