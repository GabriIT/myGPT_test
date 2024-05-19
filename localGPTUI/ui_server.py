from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# SECONDARY_SERVER_URL = 'http://localhost:5001/process_data'

SECONDARY_SERVER_URL = 'http://localhost:5001//api/prompt_route'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', show_response_modal=False)
    elif request.method == 'POST':
        data = request.json
        name = data.get('name', '')
        user_prompt = name
        print(f"User Prompt: {user_prompt}")
               
        # surname = data.get('surname', '')
        
        response = requests.post(SECONDARY_SERVER_URL, json={'user_prompt': user_prompt})
                                #  json={'name': name, 'surname': surname})
        
        print(user_prompt)

        if response.status_code == 200:
            result = response.json().get('result', '')
            return jsonify({'result': result})
        else:
            return jsonify({'error': 'Failed to process data'})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
