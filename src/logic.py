from src.Helper_fun import *


class ExtractAddress:
    def __init__(self, address1,address2):
        self.address1 = address1
        self.address2 = address2

    # Main function to extract the address information
    def get_address_information(self):
        Information = {
            "bulid_no": "",
            "street": "",
            "village": "",  # Not handled as per instructions
            "district": "",
            "gov": ""
        }

        # Step 1: Extract district and gov from Address2
        if self.address2:
            address2_parts = self.address2.split('-')
            if len(address2_parts) >= 2:
                Information["district"] = address2_parts[0].strip()
                Information["gov"] = address2_parts[1].strip()

        # Step 2: Extract the building number from Address1
        Information["bulid_no"] = extract_building_number(self.address1)

        # Step 3: Remove the building number from Address1 and clean the street part
        remaining_address = self.address1.replace(Information["bulid_no"], '').strip()
        Information["street"] = clean_street(remaining_address, self.address2)

        return Information
