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

    # Define pattern for building number after "عمارة", "عماره", or "ع"
    # This will capture both single numbers and patterns like 12/1
    building_number_with_label_pattern = r"(?:عماره|عمارة|ع)\s*(\d+(?:\s*/\s*\d+)?)"

    # First, check for building number after "عماره", "عمارة", or "ع"
    match = re.search(building_number_with_label_pattern, address)
    if match:
        building_number = match.group(1).strip()  # Get the number after the label
        return convert_to_arabic_digits(building_number)  # Convert to Arabic digits

    # If not found, fall back to the general pattern for building numbers
    building_number_general_pattern = r"(\d+\s*/\s*\d+|\d+)"  # Capture patterns like '3/21' or '3'
    match = re.search(building_number_general_pattern, address)
    if match:
        building_number = match.group().strip()
        return convert_to_arabic_digits(building_number)  # Convert to Arabic digits

    return ""  # Return empty if no building number is found


#Function to extract village name from the street column
def extract_village(street):
    # Check if the street contains 'قرية' or 'قريه'
    match = re.search(r"(قرية|قريه)\s+(.+)", street)
    if match:
        # Return the text after 'قرية' or 'قريه'
        return match.group(2).strip()
    return ""  # Return empty string if no match


# Function to clean the 'street' part
def clean_street(street, address2):
    if pd.isna(street):  # Skip if the street is NaN
        return street


    # Remove the Address2 from the street
    if address2:
        street = street.replace(address2, '').strip()

    # Extract the village and remove it from the street
    village_name = extract_village(street)
    if village_name:
        street = street.replace(village_name, '').strip()

    # Remove special characters at the beginning of the text
    # Remove non-alphanumeric characters from the beginning
    street = re.sub(r'^[^\w]+', '', street)

    # Remove occurrences of '|','-' from the text
    street = street.replace('|', ' ')
    street = street.replace('-', ' ')
    # List of words to remove
    words_to_remove = ["عمارة",'بلوك', 'فيلا',"قرية","قريه", 'ش', 'ع', 'شارع', 'قطعة']

    # Remove specified words from the text
    for word in words_to_remove:
        street = re.sub(r'\b{}\b'.format(word), '', street).strip()

    # Remove extra spaces (replace 2 or more spaces with 1 space)
    street = re.sub(r'\s{2,}', ' ', street)

    return village_name ,street


