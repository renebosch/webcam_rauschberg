from bs4 import BeautifulSoup
import requests
import shutil
import dropbox

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
      
      
# Take the file and upload it to Dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
 
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
 
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
 
def main():
    access_token = 'H4YI9GLvXcYAAAAAAAAAAdNkasNTmlKLKqzSI997hxrDCx5OpzUzFIG3CJiHhJv4'
    transferData = TransferData(access_token)
 
    file_from = 'images/webcam1.jpg' # This is name of the file to be uploaded
    file_to = '/rauschberg/webcam1.jpg'  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.
 
    # API v2
    transferData.upload_file(file_from, file_to)
 
if __name__ == '__main__':
    main()
