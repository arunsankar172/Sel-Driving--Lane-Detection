# import the necessary packages
from flask import Flask, render_template, Response
import cv2
app = Flask(__name__)
@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html')

def gen():
    video=cv2.VideoCapture(0)
    while True:
        ret, frame =video.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        op=jpeg.tobytes()
        
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + op + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)

