from flask import Flask, render_template, Response, request, json, redirect, url_for
import cv2
from connect.arduino_controller import ArduinoController


app = Flask(__name__)

cap = cv2.VideoCapture(0)
ac = ArduinoController()

def generate():
    while True:
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            (flag, encodeImage) = cv2.imencode(".jpg", frame)

            if not flag:
                continue

            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
            bytearray(encodeImage) + b'\r\n')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/videofeed")
def video_feed():
    return Response(
        generate(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )

@app.route("/send_data", methods=['POST'])
def send_data():
    value =  request.form['group1'];    
    print(value)
    return redirect(url_for("/")) 


python_data = {
    'some_list': [4, 5, 6],
    'nested_dict': {'foo': 7, 'bar': 'a string'}
}


"""@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    print(user, password)
    
    arm_data = [1,2,3,4,5,6,7]
    ac.send_values(arm_data)
    return json.dumps({'status':'OK','user':user,'pass':password});"""

if __name__ == "__main__":
    app.run(debug=True)