# Tweet-Scrapper-Api

Web Api based on project: https://github.com/5hirish/tweet_scrapper

This wrapper contains easy way to get information data of public Tweets.
This API are tested for Python3.


### Requeriments(Could get using pip)

```
pip install tweetscrape
pip install Flask
```


### How to use?

Once that you has install dependecies, you can run next terminal command

```
FLASK_APP=app.py flask run
```
Next Step is consume API that * Running on http://localhost:5000/getInfo.
Method is a Post and expected this body:

```json
{"username":"here Name account"}
```
Response Body has this structure: 

```json
   {
       "author": "",
       "authorId": "0123445667",
       "authorName": "tweettest",
       "conversationId": "012345677",
       "favoriteCount": "01234566",
       "hasParent": false,
       "hashtags": [
           "#testing"
       ],
       "id": "010291291929121",
       "links": [
           "https://t.co/U5jKSGWQWW8Pfo"
       ],
       "mentions": [],
       "repliesCount": "66",
       "retweetCount": "45",
       "text": "Testing",
       "timeMs": "",
       "type": ""
   }
```




