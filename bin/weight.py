"""Functions for converting units of weight."""


def convert_grams_to_kilograms(grams):
    """Convert grams to kilograms.

    Args:
        grams (float): Weight in grams

    Returns:
        float: Weight in kilograms
    """
    return grams / 1000


def convert_grams_to_pounds(grams):
    """Convert grams to pounds.

    Args:
        grams (float): Weight in grams

    Returns:
        float: Weight in pounds
    """
    return grams * 0.00220462


def convert_kilograms_to_grams(kilograms):
    """Convert kilograms to grams.

    Args:
        kilograms (float): Weight in kilograms

    Returns:
        float: Weight in grams
    """
    return kilograms * 1000


def convert_kilograms_to_pounds(kilograms):
    """Convert kilograms to pounds.

    Args:
        kilograms (float): Weight in kilograms

    Returns:
        float: Weight in pounds
    """
    return kilograms * 2.20462


def convert_pounds_to_grams(pounds):
    """Convert pounds to grams.

    Args:
        pounds (float): Weight in pounds

    Returns:
        float: Weight in grams
    """
    return pounds * 453.592


def convert_pounds_to_kilograms(pounds):
    """Convert pounds to kilograms.

    Args:
        pounds (float): Weight in pounds

    Returns:
        float: Weight in kilograms
    """
    return pounds * 0.453592


def convert_pounds(value, target):
    """Convert pounds to grams or kilograms.

    Args:
        value (float): Weight in pounds
        target (str): Target unit

    Returns:
        float: Weight in grams or kilograms
    """
    if target == "Grams":
        return convert_pounds_to_grams(value)
    if target == "Kilograms":
        return convert_pounds_to_kilograms(value)
    return value

def convert_grams(value, target):
    """Convert grams to kilograms or pounds.

    Args:
        value (float): Weight in grams
        target (str): Target unit

    Returns:
        float: Weight in kilograms or pounds
    """
    if target == "Kilograms":
        return convert_grams_to_kilograms(value)
    if target == "Pounds":
        return convert_grams_to_pounds(value)
    return value

def convert_kilograms(value, target):
    """Convert kilograms to grams or pounds.

    Args:
        value (float): Weight in kilograms
        target (str): Target unit

    Returns:
        float: Weight in grams or pounds
    """
    if target == "Grams":
        return convert_kilograms_to_grams(value)
    if target == "Pounds":
        return convert_kilograms_to_pounds(value)
    return value
