import requests
from bs4 import BeautifulSoup

content = requests.get('form.html')
print(content.content)