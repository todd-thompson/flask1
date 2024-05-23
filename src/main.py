import os
from shutil import copy2

from flask import Flask, send_file
src1 = '/home/user/flask1/src/index.html'
dest1 = '/home/user/flask1/public/index.html'
copy2(src1, dest1)

app = Flask(__name__)

@app.route("/")
def index():
    return send_file(dest1)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
