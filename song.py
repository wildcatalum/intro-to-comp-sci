# Efren Ibarra, CSC 110, Fall 2016, Section 1B
# programming assignment #1, 08/31/16

def p():
    print("Perhaps she'll die.")

def idk():
    print("I don't know why she swallowed that fly,")

def spiderfly():
    print("She swallowed the spider to catch the fly,")

def birdspider():
    print("She swallowed the bird to catch the spider,")
    spiderfly()
def catbird():
    print("She swallowed the cat to catch the bird,")
    birdspider()

def dogcat():
    print("She swallowed the dog to catch the cat,")
    catbird()

def verse1():
    print("There was an old woman who swallowed a fly.")
    idk()
    p()

def verse2():
    print("There was an old woman who swallowed a spider,")
    print("That wriggled and iggled and jiggled inside her.")
    spiderfly()
    idk()
    p()

def verse3():
    print("There was an old woman who swallowed a bird,")
    print("How absurd to swallow a bird.")
    birdspider()
    idk()
    p()

def verse4():
    print("There was an old woman who swallowed a cat,")
    print("Imagine that to swallow a cat.")
    catbird()
    idk()
    p()

def verse5():
    print("There was an old woman who swallowed a dog,")
    print("What a hog to swallow a dog.")
    dogcat()
    idk()
    p()

def verse6():
    print("There was an old woman who swallowed a bee,")
    print("Cant she just leave it be?")
    print("She swallowed the bee to catch the dog,")
    dogcat()
    idk()
    p()

def verse7():
    print("There was an old woman who swallowed a horse,")
    print("She died of course.")

def main_song():
    verse1()
    print
    verse2()
    print
    verse3()
    print
    verse4()
    print
    verse5()
    print
    verse6()
    print
    verse7()

main_song()
