import re
import pandas as pd

# Function to convert Western digits to Arabic digits
def convert_to_arabic_digits(number):
    western_to_arabic = {
        '0': '٠', '1': '١', '2': '٢', '3': '٣', '4': '٤',
        '5': '٥', '6': '٦', '7': '٧', '8': '٨', '9': '٩'
    }
    return ''.join(western_to_arabic.get(digit, digit) for digit in number)


# Function to extract the building number from the address
def extract_building_number(address):
    # Remove unwanted characters like '|'
    address = re.sub(r'[|]', '', address)

    # Define pattern to capture the building number (either digits or digits separated by / or other formats)
    building_number_pattern = r"(\d+\s*/\s*\d+|\d+)"  # Capture patterns like '3/21' or '3'

    match = re.search(building_number_pattern, address)
    if match:
        building_number = match.group().strip()
        return convert_to_arabic_digits(building_number)  # Convert to Arabic digits
    return ""  # Return empty if no building number is found


# Function to clean the 'street' part
def clean_street(street, address2):
    if pd.isna(street):  # Skip if the street is NaN
        return street

    # Remove the Address2 from the street
    if address2:
        street = street.replace(address2, '').strip()

    # Remove special characters at the beginning of the text
    street = re.sub(r'^[^\w]+', '', street)  # Remove non-alphanumeric characters from the beginning

    # Remove occurrences of '|'
    street = street.replace('|', '')

    # List of words to remove
    words_to_remove = ['بلوك', 'فيلا', 'ش', 'ع', 'شارع', 'قطعة']

    # Remove specified words from the text
    for word in words_to_remove:
        street = re.sub(r'\b{}\b'.format(word), '', street).strip()

    return street