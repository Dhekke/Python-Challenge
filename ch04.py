import requests, re

base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022'
digits = re.compile(r'nothing is ([0-9]+)')

text = requests.get(url).text
match = digits.findall(text)

while len(match) > 0:
    url = base_url % match[0]
    text = requests.get(url).text
    print(text)
    match = digits.findall(text)

