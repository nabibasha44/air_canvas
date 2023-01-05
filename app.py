from flask import Flask, render_template, url_for, Response
from hand_finger_motion import access_camera

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/video')
def video():
    return Response(access_camera(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
