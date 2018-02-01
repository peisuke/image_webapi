import io
import base64
import numpy as np
from flask import Flask, request, jsonify
from PIL import Image

app = Flask(__name__)

def base64encode(img):
    s = base64.b64encode(img)
    return s.decode('utf-8')

@app.route("/", methods = ["POST"])
def upload():
    data = request.get_data()
    stream = io.BytesIO(data)
    image = np.asarray(Image.open(stream))
   
    # main process
    print(image.shape)

    image = Image.fromarray(image)
    output = io.BytesIO()
    image.save(output, 'jpeg')
    encoded_img = base64encode(output.getvalue())
    json_data =  {'data': encoded_img}

    return jsonify(json_data)

if __name__ == "__main__":
    app.run()
