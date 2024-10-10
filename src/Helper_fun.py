import pandas as pd
import re


# Function to clean and remove duplicate words from the end
def remove_duplicates_from_end(standardized_address, address2):
    if pd.isna(address2):  # If Address2 is NaN, skip the operation
        return standardized_address

    # Split Address2 by hyphen to get before and after parts
    parts = [part.strip() for part in address2.split('-')]

    # Check if the last word in Standardized_Address matches any part from Address2
    for part in parts:
        if standardized_address.endswith(part):
            # Remove the part from the end of the standardized address
            standardized_address = standardized_address[:standardized_address.rfind(part)].strip()

    return standardized_address


# Function to convert Western digits to Arabic digits
def convert_to_arabic_digits(number):
    western_to_arabic = {
        '0': '٠', '1': '١', '2': '٢', '3': '٣', '4': '٤',
        '5': '٥', '6': '٦', '7': '٧', '8': '٨', '9': '٩'
    }
    return ''.join(western_to_arabic.get(digit, digit) for digit in number)


# Function to extract the building number from the address
def extract_building_number(address):
    address = re.sub(r'[|]', '', address)  # Remove unwanted characters like '|'
    building_number_pattern = r"(\d+\s*/\s*\d+|\d+)"  # Match patterns like '3/21' or '3'
    match = re.search(building_number_pattern, address)

    if match:
        building_number = match.group().strip()
        return convert_to_arabic_digits(building_number)  # Convert to Arabic digits
    return ""


# Function to remove the building number from the final cleaned address
def remove_building_number_from_address(final_cleaned_address, building_number):
    if building_number and building_number in final_cleaned_address:
        return final_cleaned_address.replace(building_number, '').strip()
    return final_cleaned_address


# Function to clean the 'Street' column based on the given rules
def clean_street(street):
    if pd.isna(street):  # Skip if the street is NaN
        return street
    street = re.sub(r'^[^\w]+', '', street)  # Remove special characters at the beginning
    street = street.replace('|', '')  # Remove '|'
    words_to_remove = ['بلوك', 'فيلا', 'ش', 'ع', 'شارع', 'قطعة']  # List of words to remove
    for word in words_to_remove:
        street = re.sub(r'\b{}\b'.format(word), '', street).strip()
    return street


# Function to update Building_Number if certain words are found
def update_building_number(row):
    address = row['Final_Cleaned_Address']
    building_number = row['Building_Number']
    match = re.search(r"(ع|عمارة|عماره)\s*(\d+)", address)
    if match:
        return convert_to_arabic_digits(match.group(2).strip())  # Convert to Arabic digits
    return building_number


# Function to extract Village, District, and Gov based on common address structure
def extract_village_district_gov(address):
    # Split address based on '-'
    parts = address.split('-')
    village, district, gov = '', '', ''

    if len(parts) >= 3:
        village, district, gov = parts[0].strip(), parts[1].strip(), parts[2].strip()
    elif len(parts) == 2:
        district, gov = parts[0].strip(), parts[1].strip()
    elif len(parts) == 1:
        gov = parts[0].strip()

    return village, district, gov
