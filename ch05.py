import requests, re, pickle

pickle_url = 'http://www.pythonchallenge.com/pc/def/banner.p'

content = requests.get(pickle_url).content
pickle_obj = pickle.loads(content)

for line_list in pickle_obj:
	line = ''
	for char_tuple in line_list:
		line += char_tuple[0] * char_tuple[1]
	print(line)