import tweepy
from os import getenv
from dotenv import load_dotenv
import logging

load_dotenv('./.env')

logger = logging.getLogger()

def create_api():
  TWITTER_ACCESS_TOKEN = getenv('TWITTER_ACCESS_TOKEN')
  TWITTER_ACCESS_TOKEN_SECRET = getenv('TWITTER_ACCESS_TOKEN_SECRET')
  CONSUMER_API_KEY = getenv('CONSUMER_API_KEY')
  CONSUMER_API_SECRET_KEY = getenv('CONSUMER_API_SECRET_KEY')

  auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET_KEY)
  auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

  api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True);

  try:
    api.verify_credentials()
  except Exception as e:
    logger.error("Error creating Twitter API", exc_info=True)
    raise e
  logger.info("Successfully created API")
  return api