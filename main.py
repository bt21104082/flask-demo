import base64
from flask import Flask, send_from_directory, request, jsonify, render_template, send_file
import pandas as pd

app = Flask(__name__)

@app.route('/')
def serve_index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def receive_data():
    try:
        data = request.form['data']
        print("Received data:", data)
        if data == 'men':
            return "you are actually a men"
        else:
            return "you are not a men"
    except Exception as e:
        error_message = "Internal Server Error: " + str(e)
        return error_message, 500

@app.route('/multple-post', methods=['POST'])
def receive_multiple():
    try:
        data = request.form['data']
        print("enter data is : ", data)
        arr = data.split(' ')
        return arr
    except Exception as e:
        error_message = 'Internal server error: ' + str(e)
        return error_message, 500


@app.route('/output-csv', methods=['GET'])
def receive_csv():
    try:

        data = pd.read_csv('data.csv')
        df = pd.DataFrame.to_json(data)
        return df
    except Exception as e:

        error = 'Internal error occurred: ' + str(e)
        return jsonify({'error': error}), 500
    
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.form['data']
    num1, num2, num3 = map(int, data.split(','))  
    if num1 == 1:
        return str(num2 + num3)
    elif num1 == 2:
        return str(num2 - num3)
    elif num1 == 3:
        return str(num2 * num3)
    else:
        return str(num2 / num3)
    
@app.route('/calculate-csv', methods=['POST'])
def calculate_csv():
    data = request.form['data']
    df = pd.read_csv('data.csv')
    result = df
    return result.to_json()


@app.route('/images/<path:filename>')
def get_image(filename):
    return send_from_directory('static/images', filename)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'filename' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['filename']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    file_path = '/home/virendra/' + file.filename
    print("file path is ", file_path)
    file.save(file_path)

    with open(file_path, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')

    return jsonify({'message': 'File uploaded successfully', 'image_data': image_data}), 200


if __name__ == '__main__':
    app.run(debug=True)