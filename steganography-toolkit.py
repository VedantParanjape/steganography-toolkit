import os
from PIL import Image
import sys

def convert_to_binary(string_):
    binary = []
    for i in string_:
        binary.append(format(ord(i),'08b'))

    return binary

def modify_pixels(pixels, string):
    binary = convert_to_binary(string)
    length = len(binary)
    pixdata = iter(pixels)
    modified_pixels = []

    for i in range(0,length):
        pix = [pixls for pixls in pixdata.__next__()[:3]+
                                    pixdata.__next__()[:3]+
                                        pixdata.__next__()[:3]]

        for j in range(0,8):
            if binary[i][j] == '0' and pix[j]%2 != 0:
                if pix[j] != 0:
                    pix[j] = pix[j] - 1
                else:
                    pix[j] = pix[j] - 1

            elif binary[i][j] == '1' and pix[j]%2 == 0:
                if pix[j] != 0:
                    pix[j] = pix[j] - 1
                else:
                    pix[j] = pix[j] - 1

        if i == length - 1:
            if pix[-1]%2 == 0:
                pix[-1] = pix[-1] - 1
        else:
            if pix[-1]%2 != 0:
                pix[-1] = pix[-1] -1
        pix = tuple(pix)
        modified_pixels.append(pix[0:3])
        modified_pixels.append(pix[3:6])
        modified_pixels.append(pix[6:9])
    
    return modified_pixels

def encode(pixels, text):
    w = pixels.size[0]
    (x, y) = (0, 0)

    for pxls in modify_pixels(pixels.getdata(), text):
        pixels.putpixel((x,y),pxls)

        if x == w - 1:
            x = 0
            y = y + 1
        else:
            x = x + 1

def decode(pixels):
    pixdata = iter(pixels.getdata())
    str_data = ''
    while 1:
        pix = [pxls for pxls in pixdata.__next__()[:3]+
                                    pixdata.__next__()[:3]+
                                        pixdata.__next__()[:3]]

        binstr = ''

        for i in pix[:8]:
            if i%2 == 0:
                binstr = binstr + '0'
            else:
                binstr = binstr + '1'
        
        str_data = str_data + chr(int(binstr,2))

        if pix[-1]%2 != 0:
            return str_data


# im = Image.open('vedant.png')
# px = im.load()
# str_in = input("enter a string: ")

def main():
    if sys.argv[1] == '-e':
        im = Image.open(sys.argv[2])
        output_name = sys.argv[3]
        string = sys.argv[4]
        
        if sys.argv[4].find('.') >=0:
            if sys.argv[4].split('.')[1] == 'txt':
                file = open(sys.argv[4],'r')
                string = file.read()
                file.close()
                print("read from file: ", sys.argv[4])

        encode(im,string)
        im.save(output_name)

    elif sys.argv[1] == '-d':
        im = Image.open(sys.argv[2])
        if sys.argv[3] == '-f':
            file = open(sys.argv[4],'a+')
            file.truncate(0)
            file.write(decode(im))
            file.close()
        else:
            print(decode(im))

    else:
        for i in sys.argv:
            print(i)

        print('usage: -e [file_name] [out_filename] [string]')
        print('       -d [file_name]')

if __name__ == '__main__':
    main()