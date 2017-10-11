def starbox(width, height):
    """print a box made up of asterisks.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """
    print("*" * width)  # print top edge of box

    # print sides of box
    # todo: print this line height-2 times, instead of three times
    l= "*" + " " * (width - 2) + "*"
    for i in range(height-2):
        print (l)
    print("*" * width)  # print bottom edge of box


# Test Cases
print("Test 1:")
starbox(5, 5)  # this prints correctly

print("Test 2:")
starbox(2, 3)  # this currently prints two lines too tall - fix it!
