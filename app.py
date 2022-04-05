from flask import Flask, render_template,request
import os
import csv
import numpy as np
import pickle
import pandas as pd
import re
from flask_ngrok import run_with_ngrok
NON_ALPHANUM = re.compile(r'[\W]')
NON_ASCII = re.compile(r'[^a-z0-1\s]')
def normalize_texts(ts):
    lower = ts.lower()
    no_punctuation = NON_ALPHANUM.sub(r' ',lower)
    ts = NON_ASCII.sub(r'',no_punctuation)
    return ts


app=Flask(__name__)
run_with_ngrok(app)
vectorizer = pickle.load(open("vector.pickel", "rb"))
loaded_model = pickle.load(open("model.pkl", "rb"))


@app.route('/',methods= ['GET','POST'])
def index():
    return render_template('fileenter.html')
@app.route('/data',methods=['GET','POST'])
def data():
    if request.method == 'POST':
        f = request.files['csvfile']
        if not os.path.isdir('static'):
            os.mkdir('static')
        filepath = os.path.join('static', f.filename)
        f.save(filepath)
        data = []
        s = []
        ls = []
        rw = []
        arr = np.array([1])
        with open(filepath, encoding="utf-8") as file:
            csvfile = csv.reader(file)
            i = 0
            for row in csvfile:
                i += 1
                if i == 1:
                    data.append(row[0:7])
                    continue
                ls.append(row[3])
                rw = str(row[2].strip())
                s = (loaded_model.predict(vectorizer.transform([normalize_texts(rw)])))
                if s == arr and (row[3] in {'1', '2'}):
                    row[6] = "Mismatch in star and review"
                    data.append(row[0:7])
            data = pd.DataFrame(data)

        return render_template('data.html', data=data.to_html())

if __name__ == "__main__":
     app.run()
