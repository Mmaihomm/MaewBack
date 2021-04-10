from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


classArr = ['Maincoon', 'Persian', 'Exotic']
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


@app.route('/', methods=['GET'])
def home():
    message = json.dumps({"message": "Backend"})
    return message, 200


@app.route('/cat', methods=['POST'])
def cat():
    data = dict(request.files)
    print(data['image'])
    message = json.dumps({"message": "Backend"})
    return message,200


if __name__ == '__main__':
    app.run(debug=True)
