from flask import Flask
from flask import jsonify
from flask import request
from tweetscrape.profile_tweets import TweetScrapperProfile

app = Flask(__name__)


def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


@app.route('/getInfo', methods=['POST'])
def get_user_info():
    response = []
    if request.method == 'POST':
        value = request.get_json()
        username = value['username']
        page_quantity = value['quantity']
        print(page_quantity)
        tweet_scrapper = TweetScrapperProfile(username, page_quantity)
        tweets = tweet_scrapper.get_profile_tweets()

        for tweet in tweets:
            dic = tweet.__dict__
            # tweetDict = {"author": tweet.__tweet_author__, "text": tweet.__tweet_text__}
            for key in list(dic.keys()):
                dic[to_camel_case(key.replace('__tweet_', ''))] = dic[key]
                del dic[key]

            response.append(dic)

    return jsonify(response)


if __name__ == '__main__':
    app.run()
