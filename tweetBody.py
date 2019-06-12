from tweetscrape.profile_tweets import TweetScrapperProfile



class TweetBody():

    def __init__(self):
        self.private=False

    def to_camel_case(self,snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])

    def getTweetsbyAccount(self,username,pagination=1):
        response=[]
        tweet_scrapper = TweetScrapperProfile(str(username), pages=pagination)
        tweets = tweet_scrapper.get_profile_tweets()
        for tweet in tweets:
            dic = tweet.__dict__
            for key in list(dic.keys()):
                dic[self.to_camel_case(key.replace('__tweet_', ''))] = dic[key]
                del dic[key]
            
            response.append(dic)

        return response



#if __name__ == "__main__":
#    x= TweetBody()
#    print(x.getTweetsbyAccount('elonmusk'))

        