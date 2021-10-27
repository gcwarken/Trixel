'''
from PIL import Image

img = Image.open('eggs.png').convert('1')
rawData = img.load()
data = []
for y in range(24):
    for x in range(24):
        data.append(rawData[x,y])

'''

from PIL import Image

img = Image.open('osso_e_patas.png').convert('L')  # convert image to 8-bit grayscale
WIDTH, HEIGHT = img.size

data = list(img.getdata()) # convert image data to a list of integers
# convert that to 2D list (list of lists of integers)
data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]

# At this point the image's pixels are all in memory and can be accessed
# individually using data[row][col].

# For example:
for row in data:
    print(' '.join('{:3}'.format(value) for value in row))


# Here's another more compact representation.
chars = ' 0'  # Change as desired.
scale = (len(chars)-1)/255.
print()
for row in data:
    print(' '.join(chars[int(value*scale)] for value in row))

#input()
