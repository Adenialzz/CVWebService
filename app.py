from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
from werkzeug.utils import secure_filename
import os
import cv2
import time
from datetime import timedelta
from CVServiceModels.detection_yolov3 import run, conf
from CVServiceModels.FasterRcnnGeneralDetection import FasterRcnnGeneralDetection
ALLOWED_EXTENSIONS = set([
    "png","jpg","JPG","PNG", "bmp"
])

def is_allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__)

# 静态文件缓存过期时间
app.send_file_max_age_default = timedelta(seconds=1)

cv_model = FasterRcnnGeneralDetection()

@app.route("/upload", methods=['POST', 'GET'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        if not ( f and is_allowed_file(f.filename) ):
            return jsonify({
                "error": 1, 
                "msg": f"Only {list(ALLOWED_EXTENSIONS)} are supported currently. Please check your file format.,"
            })
        user_input = request.form.get("name")

        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, "static/images", secure_filename(f.filename))
        f.save(upload_path)
        
        detected_path = os.path.join(basepath, "static/images", "output_" + secure_filename(f.filename))
        # run(upload_path, conf, detected_path)
        print(detected_path)
        inputs = {
            'thr': 0.70,
            'out_file': detected_path
        }
        result = cv_model.run(upload_path, **inputs)

        path = "/images/" + "output_" + secure_filename(f.filename)
        return render_template("upload_ok.html", path = path, val1 = time.time())
    return render_template("upload.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7100, debug=True)
