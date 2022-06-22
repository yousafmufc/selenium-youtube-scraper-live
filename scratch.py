import requests
from bs4 import BeautifulSoup
import selenium

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'

#Remember: requests does not execute Javascript. So can't fetch information from
#dynamic web pages.
response = requests.get(YOUTUBE_TRENDING_URL)

#getting status code from URL retrieval
print('Status code',response.status_code)

#writing output to file to see text
with open('trending.html','w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text,'html.parser')

print('Page Title:',doc.title.text)

#Find all video divs
video_divs = doc.find_all('div', class_='style-scope ytd-video-renderer')

print(f'Found {len(video_divs)} videos')
