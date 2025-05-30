from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():    
    return render_template('index.html')

app.run(host='10.144.227.137', port=80, debug=True)