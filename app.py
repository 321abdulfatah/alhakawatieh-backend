from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import logging
import os
import cv2
import base64
from image_processing import count_circles

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Configure the logger
file_handler = logging.FileHandler('server.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

# Configure the upload folder
PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = f'{PROJECT_HOME}/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def get_response_data(num_circles, category):
    # Define a mapping of the number of circles to the response data
    response_map = {
        2: {"1": "2", "2": "22"},
        3: {"1": "3", "2": "33"},
        4: {"1": "4", "2": "44"},
        6: {"1": "6", "2": "66"}
    }

    # Check if the number of circles is in the response map, and return the corresponding data
    if num_circles in response_map:
        return {"name": response_map[num_circles][category]}
    else:
        return {"name": "0"}

@app.route('/')
@cross_origin()
def index():
    response_data = {"message":"Welcome to AlHakawatieh project Backend"}
    return jsonify(response_data), 200

@app.route('/receive_story', methods=['POST'])
@cross_origin()
def receive_story():
    # Create a new folder if it doesn't exist
    create_new_folder(app.config['UPLOAD_FOLDER'])

    # Generate a unique file name for the uploaded image
    img_name = "uploadedImage.png"
    saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)

    # Get the data from the request
    data = request.get_json()
    category = data.get('category')
    image = data.get('image')

    # Decode the base64 image data
    image_bytes = bytes(image, encoding='utf-8')
    with open(saved_path, "wb") as fh:
        fh.write(base64.decodebytes(image_bytes))

    # Count the number of circles in the image
    num_circles = count_circles(saved_path)

    # Get the response data based on the number of circles and the category
    response_data = get_response_data(num_circles, category)

    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)