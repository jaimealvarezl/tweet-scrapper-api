# Tweet-Scrapper-Api

Web Api based on: https://github.com/5hirish/tweet_scrapper

This wrapper contains an easy way to get information of public Tweeter profiles.
This API was tested with Python3.


### Requeriments(Could get using pip)

```
pip install tweetscraper
pip install Flask
```


### How to use?

Once installed dependecies, run next commands on the terminal

```
FLASK_APP=app.py flask run
```
Next Step is to consume API which is * Running on http://localhost:5000/getInfo.
Method is a Post and expects a body as this:

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




