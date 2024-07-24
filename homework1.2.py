MyList = [42,69,322,13,0,99,-5,9,8,7,-6,5]
a = 0
while a < len(MyList) :
    if MyList[a] > 0:
        print(MyList[a])
        a += 1
    else:
        break