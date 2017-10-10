def findOptBmi(weight,height):
    bmi = weight/height**2
    if  bmi > 25:
        weight -= 1
        findOptBmi(weight,height)
    elif bmi < 18.5:
        weight += 1
        findOptBmi(weight,height)
    else:
        print("max weight {},at height {},and bmi {}".format(weight,height, "%.2f" %  bmi ))

findOptBmi(100,1.7)