from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

@app.route("/")
def index():
    d = pd.DataFrame(data={'a':[1, 2, 3], 'b': [4, 5 ,6]})
    return render_template('index.html', data=json.loads(d.to_json(orient='records')))

@app.route("/test")
def test():
    return 'Success!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')