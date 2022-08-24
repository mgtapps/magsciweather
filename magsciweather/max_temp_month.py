#finding a max
def month_max(data):
    import datetime
    from date_order import bubble_sort
    def Decimal(n):
            return float(n)
    #data =[(12, Decimal('1.000'), datetime.date(2022, 8, 4), 'july', Decimal('20.000'), 2), (13, Decimal('0.800'), datetime.date(2022, 8, 4), 'august', Decimal('35.200'), 2), (14, Decimal('0.500'), datetime.date(2022, 8, 6), 'august', Decimal('20.000'), 2), (16, Decimal('0.600'), datetime.date(2022, 6, 6), 'june', Decimal('35.000'), 2), (18, Decimal('12.000'), datetime.date(2022, 7, 10), 'july', Decimal('20.000'), 2), (21, Decimal('12.000'), datetime.date(2022, 3, 3), 'march', Decimal('10.000'), 2), (22, Decimal('8.500'), datetime.date(2022, 8, 14), 'august', Decimal('20.000'), 2), (23, Decimal('8.500'), datetime.date(2022, 8, 4), 'august', Decimal('35.500'), 2), (4, Decimal('12.000'), datetime.date(2022, 7, 31), 'july', Decimal('20.000'), 2), (5, Decimal('12.000'), datetime.date(2022, 3, 24), 'march', Decimal('20.000'), 2), (15, Decimal('0.500'), datetime.date(2022, 8, 6), 'august', Decimal('35.000'), 2), (17, Decimal('8.500'), datetime.date(2022, 1, 12), 'january', Decimal('-2.000'), 2), (8, Decimal('8.500'), datetime.date(2022, 7, 1), 'july', Decimal('20.000'), 2), (25, Decimal('5.500'), datetime.date(2022, 8, 4), 'august', Decimal('25.400'), 2), (27, Decimal('0.500'), datetime.date(2022, 8, 5), 'august', Decimal('20.000'), 2)]
    #print(data[0][2])
    #def max_t(data):
        #import datetime
    def Decimal(n):
        return float(n)
    num =len(data)
    data = bubble_sort(data)
    #print("data_s ",data_s)

    d_name = {1:"january", 2:"february", 3:"march", 4:"april", 5:"may", 6:"june", 7:"july", 8:"august", 9:"september", 10:"october", 11:"november", 12:"december"}
    all_months = ['january','february','march','april','may','june','july','august','september','october','november','december']#'january','febuary','april','may','june','july','august','september','october','november','december'
    d = {"january":31, "february":28, "march":31, "april":30, "may":31, "june":30, "july":31, "august":31, "september":30, "october":31, "november":30, "december":31}
    d_num = {"":0,"january":1, "february":2, "march":3, "april":4, "may":5, "june":6, "july":7, "august":8, "september":9, "october":10, "november":11, "december":12}
    d_lp = {"january":31, "february":29, "march":31, "april":30, "may":31, "june":30, "july":31, "august":31, "september":30, "october":31, "november":30, "december":31}
    l_years = [2000,2004,2008,2012,2016,2020,2024,2028,2032,2038,2040,2044,2048]

    year_t = datetime.date.today().year
    this_month= datetime.date.today().month
    date_now= datetime.date.today()
    monthly_max =[]
    data_new_t = []
    data_new = []
    january, february, march, april, may, june, july, august, september = [],[],[],[],[],[],[],[],[]
    october, november, december = [],[],[]
    month_list = [january, february, march, april, may, june, july, august, september,october, november, december ]

    for i in range(num):
        x_a= data[i][2]
        
        x= x_a.month
        y=data[i][4]
        new_row = [x,y]
        data_new.append(new_row)


        i=i+1
        
    for row in data_new:
        if row[0]==1:
            january.append(row[1])
        elif row[0]==2:
            february.append(row[1])
        elif row[0]==3:
            march.append(row[1])
        elif row[0]==4:
            april.append(row[1])
        elif row[0]==5:
            may.append(row[1])
        elif row[0]==6:
            june.append(row[1])
        elif row[0]==7:
            july.append(row[1])
        elif row[0]==8:
            august.append(row[1])
        elif row[0]==9:
            september.append(row[1])
        elif row[0]==10:
            october.append(row[1])
        elif row[0]==11:
            november.append(row[1])
        elif row[0]==12:
            december.append(row[1])

        else:
            print("no data")
    count= 0
    for month in month_list:
        
        count = count+1
        name = d_name[count]
        if month != []:
            max_t = max(month)
        else:
            max_t = 0
        new_row_t = [name, max_t]
        data_new_t.append(new_row_t)
        #print("max temp for  ",name,"",max_t)

    #print("monthly maximum temperatures  ",data_new_t)
    return data_new_t
        



