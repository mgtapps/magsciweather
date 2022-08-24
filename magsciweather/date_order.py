def bubble_sort(MyList):
    import numpy as np
    import datetime
    def Decimal(n):
       return float(n)
    
    MaxIndex = len(MyList)
    
    n = MaxIndex - 1
    for i in range(n):
        for j in range(n):
            if MyList[j][2] > MyList[j+1][2]:
                temp = MyList[j]
                MyList[j] = MyList[j+1]
                MyList[j+1] = temp
        n = n-1
    return MyList
