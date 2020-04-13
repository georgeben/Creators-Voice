"""
Retrieves bible verses for tweeting
"""
import requests
from requests.exceptions import HTTPError
import logging

logger = logging.getLogger()
api_url = "https://labs.bible.org/api/?passage=random&type=json"

def get_random_verse():
  try:
    response = requests.get(api_url)
    response.raise_for_status
    response_json = response.json()
    verse = f'{response_json[0]["text"]} {response_json[0]["bookname"]} {response_json[0]["chapter"]}:{response_json[0]["verse"]}'
    return verse
  except HTTPError as e:
    logger.error("Failed to fetch bible verse")
    logger.error(e)
