import io
import base64
import requests
import json
from PIL import Image
import numpy as np

# openc image data
img = Image.open('cat.jpg')
img_byte = io.BytesIO()
img.save(img_byte, format='jpeg')
data = img_byte.getvalue()

res = requests.post('http://127.0.0.1:5000/',
                    headers={'Content-Type': 'image/jpeg'},
                    data=data)

json_data = json.loads(res.content.decode('utf8'))

encoded_img = json_data['data']
b_img = base64.b64decode(encoded_img)
stream = io.BytesIO(b_img)
img = np.asarray(Image.open(stream))

print(img.shape)

img = Image.fromarray(img)
img.save('output.jpg')
