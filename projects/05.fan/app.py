from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.li8phsg.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    return jsonify({'msg': 'POST 연결 완료!'})

@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5001, debug=True)