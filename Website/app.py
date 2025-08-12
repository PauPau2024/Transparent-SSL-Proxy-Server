from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['comment_database']
comments_collection = db['comments']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_comment', methods=['POST'])
def post_comment():
    if request.method == 'POST':
        data = request.json
        input_text = data.get('inputText')
        # Store the comment in MongoDB
        comments_collection.insert_one({'inputText': input_text})
        return jsonify({'message': 'Comment posted successfully'})

@app.route('/get_comments', methods=['GET'])
def get_comments():
    comments = list(comments_collection.find({}, {'_id': 0}))
    return jsonify(comments)

if __name__ == '__main__':
    app.run(host='192.168.1.2', debug=True)