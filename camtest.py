#!/usr/bin/env python

from flask import Flask, render_template, request
from base64 import b64encode

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def photo():
    img = request.files['cameraInput']
    return render_template('photo.html',
            mime=img.mimetype, b64data=b64encode(img.read()))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
