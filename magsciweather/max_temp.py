#finding a max
def max_t(data):
    
    import datetime

    #data = [3.0,4.5,2,1,3,6,1.7]
    maxNumb = float(0.0)
    valid = False
    def Decimal(n):
           return float(n)
    
    data_t=[]

        

    for each in data:
        item = each[4]
        data_t.append(item)
        
    #print("numbers are  ", data_t)

    pos = 0
    len_array = len(data_t)
    while pos < (len_array):
        if float(data_t[pos]) > maxNumb:
            maxNumb = data_t[pos]
            pos = pos + 1
        else:
            pos = pos + 1

    #print("maximum value is  ", maxNumb)
    return maxNumb
