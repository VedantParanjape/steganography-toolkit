# steganography-toolkit

A toolkit to hide data in an image using steganography techniques

# Usage

```
python3 steganography.py [options] [yada] [yada] [yada]   
usage: -e [input filename] [output filename] [filename with data/string]   
       -d [encoded filename] -f [output_filename(optional)
       -ea [output_filename] [filename with data/string]
       -da [input_filename] -f [output_filename(optional)]

example: python3 steganography.py -e vedant.png encoded.png vedant_rocks
         python3 steganography.py -e vedant.png encoded.png input.txt
         python3 steganography.py -e vedant.png encoded.png input.txt
         python3 steganography.py -d encoded.png
         python3 steganography.py -d encoded.png -f output.txt
         python3 steganography.py -ea encoded.png vedant_rocks
         python3 steganography.py -ea encoded.png input.txt
         python3 steganography.py -da encoded.png
         python3 steganography.py -da encoded.png -f output.txt
         
```

# Requirements
`Python 3.6+`  
`Python PIL`
