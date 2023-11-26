
# Challenge 1: Converting 12-hour time to 24-hour time

## Description

Given a 12-hour time in the format "hour:minute period," the task is to convert it to a 24-hour time format. For example, "8:30 am" should be converted to "0830," and "8:30 pm" should be converted to "2030."

## Function Signature

```python
def convert_to_24_hour(hour, minute, period):
    """
    Converts a 12-hour time to 24-hour time.

    Args:
    - hour (int): The hour (1 to 12).
    - minute (int): The minute (0 to 59).
    - period (str): The period, either "am" or "pm".

    Returns:
    - str: The 24-hour time as a four-digit string.
    """
    # implementation