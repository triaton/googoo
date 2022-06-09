import sys
import os
from serpapi import GoogleSearch

API_KEY_NAME = 'SERP_API_KEY'

if len(sys.argv) != 2:
  print('Only 1 argument is allowed')
else:
  if not API_KEY_NAME in os.environ:
    print(f'Please set environment variable. {API_KEY_NAME}')
    exit()
  query = sys.argv[1]
  search = GoogleSearch({
    "q": query,
    "api_key": os.environ['SERP_API_KEY']
  })
  data = search.get_dict()
  answer_keys = ['answer', 'snippet']
  for key in answer_keys:
      if key in data['answer_box']:
        answer = data['answer_box'][key]
        print(f'Answer({key}): {answer}\n')

  index = 1
  for organic_result in data['organic_results']:
    keys = ['snippet', 'link']
    for key in keys:
      if key in organic_result:
        value = organic_result[key]
        print(f'{key}: {value}')
    print('\n')
