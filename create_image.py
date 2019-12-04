from PIL import Image
from math import sqrt
from random import randrange

data = input("enter text: ")
imgdim = int(sqrt(len(data))+1)

if imgdim**2 < 1000*1000:
    imgdim = 1000

def str_ascii(data):
    ascii = []

    for i in data:
        ascii.append(ord(i))

    return ascii
    
def modify_pixels(pixels, data):
    ascii_list = str_ascii(data)
    pixels = iter(im.getdata())
    length = len(ascii_list)
    modifed_pixels = []
    counter = 0

    for j in pixels:
        if counter > length - 1:
            break
        
        i = [int(k) for k in j]
        i[0] = ascii_list[counter]
        counter = counter + 1
        i = tuple(i)
        modifed_pixels.append(i)

    return modifed_pixels    

def decode(name):
    im = Image.open(name)
    pixels = iter(im.getdata())

    decoded_string = ''

    for i in pixels:
        if i[0] > 130:
            break
        decoded_string = decoded_string + chr(i[0])
    return decoded_string
im = Image.new(mode = "RGB", size = (imgdim, imgdim))
px = im.load()

for i in range(0,randrange(im.size[0]-1)):
    for j in range(0,randrange(im.size[1]-1)):
        px[j,i] = (randrange(140,250), randrange(140,250), randrange(140,250))

w = im.size[0]
(x, y) = (0, 0)

for pxls in modify_pixels(im, data):
    im.putpixel((x,y),pxls)
    
    if x == w - 1:
        x = 0
        y = y + 1
    else:
        x = x + 1

im.save("output.png")

print(decode('output.png'))
