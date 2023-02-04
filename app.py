from flask import Flask, Response
from hand_finger_motion import access_camera
from flask_cors import CORS
import base64, os
from hand_written_rec import detect_hand_written

app = Flask(__name__)
cors = CORS(app)


responses = {}


@app.route("/")
def main():
    return {"path": 'http://127.0.0.1:5000/video'}


@app.route('/video')
def video():
    return Response(access_camera(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/text-response', methods=['POST'])
def ocr_response(request):
    file_body = request.body()
    file_content = file_body.get('buff_data')
    try:
        file_content = base64.b64decode(file_content)
        os.makedirs(os.getcwd() + '/tmp', exist_ok=True)
        localdir = os.getcwd()+'/tmp/'
        temp_files = os.listdir(localdir)
        temp_files = [int(j.lstrip('_').strip('.png')) for j in temp_files]
        temp_version = temp_files[-1]
        localfile = f'{localdir}_{temp_version}.png'
        with open(localfile, "wb") as f:
            f.write(file_content)

        result = detect_hand_written(localfile)
        responses.update({str(temp_version): result})
        return {'status': 'success'}

    except Exception as e:
        print(str(e))
        return {'status': 'fail'}


if __name__ == "__main__":
    app.run(debug=True)
