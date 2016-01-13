from PIL import Image
import re

original = Image.open('5808/cave.jpg')
width, height = original.size
even = list()
even_nogap = list()
odd = list()
odd_nogap = list()

data = list(original.getdata())

#Black out pixels where (x + y) is odd, leaving only even coordinates
for line in range(height):
    start = (width * line) + 1 - line % 2
    end = width * (line + 1)
    for position in range(start, end, 2):
        data[position] = (0, 0, 0)

image_even = Image.new('RGB', (640, 480))
image_even.putdata(data)

image_even.save('5808/even.jpg')