from flask import Flask,request
from flask_cors import CORS
from src.logic import ExtractAddress


app = Flask(__name__)
CORS(app)

@app.route('/get_extracted_address', methods=['POST'])
def get_extracted_address():
    address1 = request.json['address1']
    address2 = request.json['address2']
    pipline = ExtractAddress(address1,address2)
    Information = pipline.get_address_information()


    return Information

if __name__ == '__main__':
    app.run("0.0.0.0", 7000)


