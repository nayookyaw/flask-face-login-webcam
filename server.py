"""
    Nay Oo Kyaw
    nayookyaw.nok@gmail.com
"""
from flask import *
from flask_socketio import *

import glob
import cv2 as cv
import time
import scipy.misc
import compare_image
import base64

# Init the server
app = Flask(__name__)

app._static_folder = os.path.abspath("templates/static/")

# Send HTML!
@app.route('/')
def root():    
    return render_template('/views/index.html')

# Display the HTML Page & pass in a username parameter
@app.route('/html/<username>')
def html(username):
    return render_template('index.html', username=username)

# Receive image base64
@app.route('/login/with/image', methods=['POST']) 
def get_image():
    data = request.get_json('image_64')

    base64_str = data['image_64']
    base64_str_arr = base64_str.split(",")

    if base64_str_arr[1]:
        base64_img_bytes = base64_str_arr[1].encode('utf-8')
        with open('target_img/target.jpg', 'wb') as fs:
            img_data = base64.decodebytes(base64_img_bytes)
            fs.write(img_data)

        # get target image 
        target_path = glob.glob("target_img/*.jpg")
        for t_img in target_path:
            target = t_img

        response=[]

        # get all images from folder
        path = glob.glob("images/*.jpg")

        for img in path:
            start = time.time()
            distance,result = compare_image.main(target, img)
            end=time.time()

            response_data = {
                'result':str(result),
                'distance':round(distance,2),
                'time_taken':round(end-start,3)
            }
            response.append(response_data)
  
    return jsonify({"result" : response})

# Actually Start the Server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)