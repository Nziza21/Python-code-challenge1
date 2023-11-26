# challenge1.py

def convert_to_24_hour(hour, minute, period):
    # Convert 12-hour time to 24-hour time
    if period.lower() == "pm" and hour != 12:
        hour += 12
    elif period.lower() == "am" and hour == 12:
        hour = 0

    # Format the result as a four-digit string
    return f"{hour:02d}{minute:02d}"

# Test examples
print(convert_to_24_hour(8, 30, "am"))  # Output: "0830"
print(convert_to_24_hour(8, 30, "pm"))  # Output: "2030"
