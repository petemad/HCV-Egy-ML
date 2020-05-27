import requests

url = 'https://www.tutorialspoint.com/downloading-files-from-web-using-python'
r = requests.get(url, allow_redirects=True)

open('HCV-Egy-Data.zip', 'wb').write(r.content)