from zipfile import ZipFile
import re

digits = re.compile(r'([0-9]+)')
file_number = '90052'
comments = []

with ZipFile('zip/channel.zip','r') as zip:
    while True:
        filename = '{}.txt'.format(file_number)
        content = zip.read(filename).decode()

        number_list = digits.findall(content)
        comments.append(zip.getinfo(filename).comment.decode())

        if len(number_list) == 0:
            break
        file_number = number_list[0]

print(content)
print(''.join(comments))