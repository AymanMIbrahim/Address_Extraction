from flask import Flask,request
from src.logic import ExtractAddress


app = Flask(__name__)

@app.route('/get_extracted_address', methods=['POST'])
def get_extracted_address():
    address1 = request.json['address1']
    address2 = request.json['address2']
    pipline = ExtractAddress(address1,address2)
    Information = pipline.extract_information_from_address()


    return Information

if __name__ == '__main__':
    app.run("0.0.0.0", 7000)


