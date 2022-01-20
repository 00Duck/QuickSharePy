from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

HOST = '0.0.0.0'
PORT = 8000
SHARED_DIR = '/path/to/shared/folder'

# From another machine, send a file to this machine (stored in the shared directory)
# Ex: curl -F file=@hello.c 192.168.1.123:8000
@app.route('/', methods = ['POST'])
def upload_file():
   try:
      f = request.files['file']
      f.save(os.path.join(SHARED_DIR, secure_filename( f.filename)))
      return 'File uploaded successfully.'
   except:
      return 'There was a problem uploading the file. Please try again with a valid file.'

# From another machine, ask to download a file by its filename
# Ex: wget 192.168.1.123:8000/hello.c
@app.route('/<path:name>', methods = ['GET', 'PUT'])
def send_file(name):
   if request.method == 'GET':
      return send_from_directory(directory = SHARED_DIR, path = name, as_attachment = True)      

   return 'Unsupported method'

if __name__ == '__main__':
   app.run(host = HOST, port = PORT, debug = False)