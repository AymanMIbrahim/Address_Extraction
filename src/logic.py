from fuzzywuzzy import fuzz
from src.download_data import Address1


class ExtractAddress:
    def __init__(self, address1,address2):
        self.address1 = address1
        self.address2 = address2

    def get_address(self):
        Information = {"bulid_no": "", "street": "", "village": "", "district": "", "gov": ""}

        gov,district = self.address2.split("-")[0],self.address2.split("-")[1]
        PureAddress1 = self.address1.replace(self.address2, "")


        return Information