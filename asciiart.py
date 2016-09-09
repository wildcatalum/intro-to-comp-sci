# Efren Ibarra, CSC 110, Fall 2016, Section 1B
# programming assignment #2A, 09/03/16
def main():
        antenna()
        top()
        gap()
        eyes()
        gap()
        mouth()
        gap()
        top()
        
def top():
	for i in range(1, 6):
		print("__", end="")
	print()

def eyes():
        print("|+++  +++|")
        for i in range (1, 2):
                print("|+ +  + +|")
        print("|+++  +++|")

def gap():
        for i in range (1,2):
                print("|        |")

def mouth():
        print ("| |||||| |")

def antenna():
        print("    MR     ")
        for i in range(1, 5):
                print("    **    ")
        
main()
