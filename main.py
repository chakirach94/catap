from typing import Union
#importing the libraries we will be needing
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sentiment = SentimentIntensityAnalyzer()
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: str, q: Union[str, None] = None):
    sent_1 = sentiment.polarity_scores(item_id)
    print(sent_1)
    response="https://cdn.pixabay.com/download/audio/2022/03/24/audio_a8fa663998.mp3?filename=cat-call-meow-102607.mp3"

    if sent_1['compound']>0.6:
      #lot of love
      response="https://cdn.pixabay.com/download/audio/2022/03/15/audio_ee7c253ac0.mp3?filename=purring-cat-75673.mp3"
   
    if sent_1['compound']>0.5:
      response="https://cdn.pixabay.com/download/audio/2022/03/15/audio_ee7c253ac0.mp3?filename=purring-cat-75673.mp3"
   #normal love

    if sent_1['compound']<-0.4:
      response="https://cdn.pixabay.com/download/audio/2022/03/15/audio_83db82aaab.mp3?filename=angry-cat-meow-82091.mp3"
    #angry cat
    
    if sent_1['compound']<-0.6:
      response="https://cdn.pixabay.com/download/audio/2022/02/07/audio_519e8d4d29.mp3?filename=funny-cat-always-grumpy-kitty-17840.mp3"
    #angry cat

    return {response}
