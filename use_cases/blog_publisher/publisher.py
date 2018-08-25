from flask import Flask, render_template, request
import os
from werkzeug import secure_filename

UPLOAD_FOLDER = '/app/files'
ALLOWED_EXTENSIONS = set(['html'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_file():
   return render_template('index.html')
	
@app.route('/publisher',methods = ['POST', 'GET'])
def publisher():
   if request.method == 'POST':
       file = request.files['file']
       blog_name =  request.files['blogname']
       if file and allowed_file(file.filename):
           filename = secure_filename(file.filename)
           file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           out = "Blog created at /" + blog_name 
           return out
		
if __name__ == '__main__':
   app.run("0.0.0.0",80,debug = True)
