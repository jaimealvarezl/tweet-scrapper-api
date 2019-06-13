from flask import Flask
from flask import jsonify
from flask import request
from tweetBody import TweetBody


app = Flask(__name__)


@app.route('/getUserTweets', methods=['POST'])
def get_user_info():
    response=[]
    if request.method == 'POST':
        value = request.get_json()
        username = value['username']
        page_quantity = value['quantity']
        scrapper=TweetBody()
        response=scrapper.getTweetsbyAccount(username,page_quantity)
        
    return jsonify(response)


if __name__ == '__main__':
    app.run()
