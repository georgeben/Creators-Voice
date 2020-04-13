#!/usr/bin/env python3

import tweepy, logging, time, sched
from config import create_api
from bible import get_random_verse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

s = sched.scheduler(time.time, time.sleep)
INTERVAL = 60 * 60 * 8  #8 hours
TEST_INTERVAL = 60

def tweet(api, message):
  api.update_status(message)
  logger.info("Successfully posted status")

def main(scheduler):
  api = create_api()
  bible_verse = get_random_verse()
  tweet(api, bible_verse)
  scheduler.enter(TEST_INTERVAL, 1, main, (scheduler,))

if (__name__ == "__main__"):
  s.enter(TEST_INTERVAL, 1, main, (s,))
  s.run()