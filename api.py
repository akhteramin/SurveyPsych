from flask import Flask
from flask import request
import json
import time
app = Flask(__name__)

@app.route('/caption/data', methods = ['GET'])

def getData():
    print("data")
    return 'JSON data posted'


@app.route('/caption/data/save/red', methods = ['POST'])

def postJsonDataExtract():
    print(request.is_json)
    content = request.get_json()
    print(content)
    with open('responses/red_'+str(int(round(time.time() * 1000)))+'.json', 'w') as f:
        json.dump(content, f)
    return 'JSON data posted'

@app.route('/caption/data/save/orange', methods = ['POST'])
def postJsonDataExtractOrange():
    print(request.is_json)
    content = request.get_json()
    print(content)
    with open('responses/orange_'+str(int(round(time.time() * 1000)))+'.json', 'w') as f:
        json.dump(content, f)
    return 'JSON data posted'

@app.route('/caption/data/save/purple', methods = ['POST'])
def postJsonDataExtractPurple():
    print(request.is_json)
    content = request.get_json()
    print(content)
    with open('responses/purple_'+str(int(round(time.time() * 1000)))+'.json', 'w') as f:
        json.dump(content, f)
    return 'JSON data posted'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
