from flask import Flask, Response
from hand_finger_motion import access_camera
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route("/")
def main():
    return {"path": 'http://127.0.0.1:5000/video'}


@app.route('/video')
def video():
    return Response(access_camera(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
