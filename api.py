from flask import Flask, render_template, request
from flask_restful import reqparse, abort, Api, Resource
from werkzeug import secure_filename
import run_inference as inference

app = Flask(__name__)
api = Api(app)
@app.route('/upload')
def render_file():
    return render_template('upload.html')

@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        print(f.filename)
        inference.run_inference_on_image(f.filename)
        return 'uploads 디렉토리 -> 파일 업로드 성공!'


class Api(Resource):
    def get(self):
        if request.method == 'GET':
            return render_template('upload.html')

    def post(self):
        if request.method == 'POST':
            f = request.files['file']
            f.save(secure_filename(f.filename))
            print(f.filename)
            inference.run_inference_on_image(f.filename)
            return 'uploads 디렉토리 -> 파일 업로드 성공!'

api.add_resource(Api,'/upload')
if __name__ == '__main__':
    app.run(debug = True, port = 8080)
