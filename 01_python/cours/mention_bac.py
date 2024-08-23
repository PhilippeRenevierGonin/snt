
if __name__ == '__main__':
    note = float(input("Entrez la note du bac (0-20) : "))
    if (note >= 16):
        print("c'est une mention TB")
    elif (note >= 14):
        print("c'est une mention B")
    elif (note >= 12):
        print("c'est une mention AB")
    elif (note >= 10):
        print("c'est une mention passable / sans mention")
    else:
        print("malheureusement, le bac n'est pas obtenu")