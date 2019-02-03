import tweepy
import csv
from textblob import TextBlob

consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET_KEY' 

access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_SECRET_ACCESS_TOKEN'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Tamales")

positive = ["Positive"]
negative = ["Negative"]

for tweet in public_tweets:
  analysis = TextBlob(tweet.text)
  value = analysis.sentiment.polarity
  #Si la polaridad es mayor que 0.5 eso indica que es un buen comentario
  if value >= 0.2:
  	positive.append("Porcentaje:" + str(value) +" Tweet: " +tweet.text)
  else:
  	negative.append("Porcentaje:" + str(value) + "Tweet: " + tweet.text )

with open('Analisis.csv', 'a',encoding='utf-8') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerow(positive)
	writer.writerow(negative)


  