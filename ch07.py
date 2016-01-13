from PIL import Image
import re

picture = Image.open('oxygen/oxygen.png')
mid = picture.size[1]//2

chars = [chr(picture.getpixel((x, mid))[0]) for x in range(0, picture.size[0], 7)]
text = ''.join(chars) 
print(text)

expression = re.compile(r'\d+')
numbers = [int(match) for match in expression.findall(text)]
chars = [chr(number) for number in numbers]
text = ''.join(chars)
print(text)

print(picture.tostring()[108188:110620:28].decode())