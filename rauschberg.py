from bs4 import BeautifulSoup
import requests
import shutil

# Get the website I want to get webcam footage off
html_text = requests.get('https://www.terra-hd.de/rauschberg/').text
soup = BeautifulSoup(html_text, 'lxml')

# Get the actual source of the image and extract it from the div-container
image = soup.find_all('img', class_ = 'webcamimage')

image_source = image[0].attrs['src']
print(image_source)

# Get the full URL of the image

# Combine the image source and the base url

url_base = 'https://www.terra-hd.de/rauschberg/'

url_ext = image_source

full_url = url_base + url_ext

#

r = requests.get(full_url, stream=True)

# Safe the file to the folder /images

if r.status_code == 200:                     
   with open("images/webcam1.jpg", 'wb') as f: 
      r.raw.decode_content = True
      shutil.copyfileobj(r.raw, f)
