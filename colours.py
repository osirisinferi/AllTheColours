from itertools import product
from os import path, makedirs

def outputPBM(filename, data):
    if not path.exists("Output"):
        makedirs("Output")
    f = open("Output/" + filename + ".pbm", "w")
    f.write("P1\n4 4\n")
    for pixel in data:
        f.write(str(pixel) + " ")
    f.close()

def main():
    prod = product(range(2), repeat=16)

    for i, content in enumerate(prod):
        outputPBM(str(i), content)

if __name__ == "__main__":
    main()

