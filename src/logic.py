from src.Helper_fun import *


class ExtractAddress:
    def __init__(self, address1,address2):
        self.address1 = address1
        self.address2 = address2

    def extract_information_from_address(self):
        # Step 1: Remove Address2 content from Address1 and clean the final address
        cleaned_address = self.address1.replace(self.address2, '').strip()

        # Step 2: Remove duplicates from the end
        final_cleaned_address = remove_duplicates_from_end(cleaned_address,self.address2)

        # Step 3: Extract building number
        building_number = extract_building_number(final_cleaned_address)

        # Step 4: Remove building number from the address to get the street
        street = remove_building_number_from_address(final_cleaned_address, building_number)
        street = clean_street(street)

        # Step 5: Extract Village, District, and Gov from the address
        village, district, gov = extract_village_district_gov(final_cleaned_address)

        # Return the cleaned information as a dictionary
        information = {
            "bulid_no": building_number,
            "street": street,
            "village": village,
            "district": district,
            "gov": gov
        }
        return information
