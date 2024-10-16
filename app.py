from flask import Flask,request,Response,abort
from flask_cors import CORS
from src.logic import ExtractAddress


app = Flask(__name__)
CORS(app)

API_KEY = "D3$xYp8!nQ4&fJ6v"
def verify_api_key():
    api_key = request.headers.get('Authorization')
    if api_key != API_KEY:
        abort(401, description="Unauthorized: Invalid API key")

@app.after_request
def apply_csp(response: Response):
    response.headers['Content-Security-Policy'] = "upgrade-insecure-requests"
    return response

@app.route('/get_extracted_address', methods=['POST'])
def get_extracted_address():
    try:
        verify_api_key()

        address1 = request.form['address1']
        address2 = request.form['address2']
        pipline = ExtractAddress(address1,address2)
        Information = pipline.get_address_information()
        Information["status"] = "success"


        return Information

    except Exception as e:
        print(e)
        Information = {
            "status": "falied",
            "bulid_no": "",
            "street": "",
            "village": "",  # Not handled as per instructions
            "district": "",
            "gov": "",
            "error": str(e)
        }
        return Information

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)


