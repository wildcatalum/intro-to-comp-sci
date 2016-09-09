# Efren Ibarra, CSC 110, Fall 2016, Section 1B
# programming assignment #2B, 09/08/16

def main():
        diamonds()

def cone():
    for line in range(1, 6):
        for i in range(1, -1*line+7):
                print(" ", end="")
        for i in range(1, line+1):
                print("/", end="")
        print("**", end="")
        for i in range (1, line+1):
                print("\\", end="")
        print()

def diamonds():
        for line in range(1,4):
                print("|")
                for i in range(1, -1*line+4):
                        print(".", end="")
                for i in range(1, line):
                        print("/\\", end="")
                for i in range(1, 5, -2):
                        print(".", end="")
#left off here coding for the upper right part of the two diamonds

def leftuptri():
        for line in range(1,4):
                print("|")
                for i in range(1, -1*line+4):
                        print(".", end="")
                for i in range(1, line):
                        print("/\\", end="")
                for i in range(3, 1, -1):
                        print(".", end="")
                print()
#coded the left upper triangle which apears redundandtly like the downward triangle
#using these triangle we eliminate redundancy but must concantenate leftuptri() and leftdowntri()
#flipping leftuptri() can yield rightuptri()

def leftdowntri():

def line():
    print("+", end="")
    for i in range (1,7):
        print("=*", end="")
    print("+", end="")
    print()

main()
