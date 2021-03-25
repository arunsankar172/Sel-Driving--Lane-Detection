import numpy as np
import cv2
from mss import mss
from PIL import Image
from flask import Flask, render_template, Response




bounding_box = {'top': 0, 'left': 0, 'width': 1280, 'height': 720}

sct = mss()

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')
def gen():
   while True:
       sct_img = sct.grab(bounding_box)
       frame = np.array(sct_img)
       ret, jpeg = cv2.imencode('.jpg', frame)
       op=jpeg.tobytes()
       yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + op + b'\r\n\r\n')


# In[4]:


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)

