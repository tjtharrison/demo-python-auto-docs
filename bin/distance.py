"""Functions to convert units of distance"""

def convert_meters_to_kilometers(meters):
    """Converts meters to kilometers

    Args:
        meters (float): Distance in meters

    Returns:
        float: Distance in kilometers
    """
    return meters / 1000

def convert_meters_to_miles(meters):
    """Converts meters to miles

    Args:
        meters (float): Distance in meters

    Returns:
        float: Distance in miles
    """
    return meters * 0.000621371

def convert_kilometers_to_meters(kilometers):
    """Converts kilometers to meters

    Args:
        kilometers (float): Distance in kilometers

    Returns:
        float: Distance in meters
    """
    return kilometers * 1000

def convert_kilometers_to_miles(kilometers):
    """Converts kilometers to miles

    Args:
        kilometers (float): Distance in kilometers

    Returns:
        float: Distance in miles
    """
    return kilometers * 0.621371

def convert_miles_to_meters(miles):
    """Converts miles to meters

    Args:
        miles (float): Distance in miles

    Returns:
        float: Distance in meters
    """
    return miles * 1609.34

def convert_miles_to_kilometers(miles):
    """Converts miles to kilometers

    Args:
        miles (float): Distance in miles

    Returns:
        float: Distance in kilometers
    """
    return miles * 1.60934


def convert_inches_to_meters(inches):
    """Converts inches to meters

    Args:
        inches (float): Distance in inches

    Returns:
        float: Distance in meters
    """
    return inches * 0.0254

def convert_inches_to_kilometers(inches):
    """Converts inches to kilometers

    Args:
        inches (float): Distance in inches

    Returns:
        float: Distance in kilometers
    """
    return inches * 0.0000254

def convert_inches_to_miles(inches):
    """Converts inches to miles

    Args:
        inches (float): Distance in inches

    Returns:
        float: Distance in miles
    """
    return inches * 0.000015783

def convert_meters(meters, target):
    """Converts meters to target unit

    Args:
        meters (float): Distance in meters
        target (str): Target unit

    Returns:
        float: Distance in target unit
    """
    if target == 'Kilometers':
        return convert_meters_to_kilometers(meters)
    elif target == 'Miles':
        return convert_meters_to_miles(meters)
    elif target == 'Inches':
        return meters * 39.3701

    return meters

def convert_kilometers(kilometers, target):
    """Converts kilometers to target unit

    Args:
        kilometers (float): Distance in kilometers
        target (str): Target unit

    Returns:
        float: Distance in target unit
    """
    if target == 'Meters':
        return convert_kilometers_to_meters(kilometers)
    elif target == 'Miles':
        return convert_kilometers_to_miles(kilometers)
    elif target == 'Inches':
        return kilometers * 39370.1

    return kilometers

def convert_miles(miles, target):
    """Converts miles to target unit

    Args:
        miles (float): Distance in miles
        target (str): Target unit

    Returns:
        float: Distance in target unit
    """
    if target == 'Meters':
        return convert_miles_to_meters(miles)
    elif target == 'Kilometers':
        return convert_miles_to_kilometers(miles)
    elif target == 'Inches':
        return miles * 63360

    return miles

def convert_inches(inches, target):
    """Converts inches to target unit

    Args:
        inches (float): Distance in inches
        target (str): Target unit

    Returns:
        float: Distance in target unit
    """
    if target == 'Meters':
        return convert_inches_to_meters(inches)
    elif target == 'Kilometers':
        return convert_inches_to_kilometers(inches)
    elif target == 'Miles':
        return convert_inches_to_miles(inches)

    return inches