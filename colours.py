from itertools import product
from os import path, makedirs

def outputPBM(filename, data, x=4, y=4, format="P1", depth=""):
    if not path.exists("Output"):
        makedirs("Output")
    if format =="P1":
        ext = "pbm"
    elif format =="P2":
        ext = "pgm"
    elif format == "P3":
        ext = "ppm"
    else:
        ext = "foo"
    f = open("Output/" + filename + "." + ext, "w")
    f.write("{}\n{} {} {}\n".format(format, x, y, depth))
    for pixel in data:
        f.write(str(pixel) + " ")
    f.close()

def generatePictures(x, y, depth):
    # Possible values for depth:
    #   2 (B&W)
    #   256 (8 bit grey scale)
    #   65536 (16 bit grayscale)
    #   16777216 (24 bit colour scale)

    # chars per pixel is 1 for P1 and P2 formats, so use that as default
    cpp = 1

    if depth == 2:
        format = "P1"
    elif depth == 256 or depth == 65536:
        format = "P2"
    elif depth == 16777216:
        format = "P3"
        # P3 format uses 3 chars per colour channel per pixel with 8 bits per channel
        cpp = 3
        depth = 256
    else:
        raise Exception("Ongeldige kleurendiepte gekozen, mogelijke waarden zijn: "
                        "2, 256, 65536 of 16777216")
    prod = product(range(depth), repeat=x*y*cpp)

    for i, content in enumerate(prod):
        outputPBM(str(i), content, x, y, format, str(depth-1) if depth != 2 else "")

def main():
    generatePictures(1, 1, 16777216)

if __name__ == "__main__":
    main()

