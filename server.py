from flask import Flask, request
from flask import render_template
import urllib.request
from flask import jsonify


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    username = request.form.get("username")
    
    response = {
        'data': {'username': username },
        'code': '200'
        }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run()
