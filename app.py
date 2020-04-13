#!/usr/bin/env python3

import tweepy
from config import create_api
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def tweet(api, message):
  api.update_status(message)
  logger.info("Successfully posted status")

def main():
  api = create_api()
  msg = "Hello"
  while True:
    msg+="!"
    tweet(api, msg)
    time.sleep(60)

if (__name__ == "__main__"):
  main()