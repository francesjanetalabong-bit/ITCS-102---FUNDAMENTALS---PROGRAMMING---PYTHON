for i in range(1,7,1):
    for x in range(7, i, -1):
        print("  ",end = " ")
    for y in range(i,0,-1):
        print( y, end= '  ')
    for f in range(2,i + 1,1):
        print(f, end= '  ')
    print()
