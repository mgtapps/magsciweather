#finding a max
import datetime
def Decimal(n):
        return float(n)
data =[(12, Decimal('1.000'), datetime.date(2022, 8, 4), 'july', Decimal('20.000'), 2), (13, Decimal('0.800'), datetime.date(2022, 8, 4), 'august', Decimal('35.200'), 2), (14, Decimal('0.500'), datetime.date(2022, 8, 6), 'august', Decimal('20.000'), 2), (16, Decimal('0.600'), datetime.date(2022, 6, 6), 'june', Decimal('35.000'), 2), (18, Decimal('12.000'), datetime.date(2022, 7, 10), 'july', Decimal('20.000'), 2), (21, Decimal('12.000'), datetime.date(2022, 3, 3), 'march', Decimal('10.000'), 2), (22, Decimal('8.500'), datetime.date(2022, 8, 14), 'august', Decimal('20.000'), 2), (23, Decimal('8.500'), datetime.date(2022, 8, 4), 'august', Decimal('35.500'), 2), (4, Decimal('12.000'), datetime.date(2022, 7, 31), 'july', Decimal('20.000'), 2), (5, Decimal('12.000'), datetime.date(2022, 3, 24), 'march', Decimal('20.000'), 2), (15, Decimal('0.500'), datetime.date(2022, 8, 6), 'august', Decimal('35.000'), 2), (17, Decimal('8.500'), datetime.date(2022, 1, 12), 'january', Decimal('-2.000'), 2), (8, Decimal('8.500'), datetime.date(2022, 7, 1), 'july', Decimal('20.000'), 2), (25, Decimal('5.500'), datetime.date(2022, 8, 4), 'august', Decimal('25.400'), 2), (27, Decimal('0.500'), datetime.date(2022, 8, 5), 'august', Decimal('20.000'), 2)]

#def max_t(data):
    #import datetime
def Decimal(n):
    return float(n)
num =len(data)
#date_now= datetime.date.today()
all_months = ['january','february','march','april','may','june','july','august','september','october','november','december']#'january','febuary','april','may','june','july','august','september','october','november','december'
d = {"january":31, "february":28, "march":31, "april":30, "may":31, "june":30, "july":31, "august":31, "september":30, "october":31, "november":30, "december":31}
d_num = {"january":1, "february":2, "march":3, "april":4, "may":5, "june":6, "july":7, "august":8, "september":9, "october":10, "november":11, "december":12}
d_lp = {"january":31, "february":29, "march":31, "april":30, "may":31, "june":30, "july":31, "august":31, "september":30, "october":31, "november":30, "december":31}
l_years = [2000,2004,2008,2012,2016,2020,2024,2028,2032,2038,2040,2044,2048]

year_t = datetime.date.today().year
this_month= datetime.date.today().month
date_now= datetime.date.today()
monthly_max =[]
data_new =[]
for i in range(num):
    data_new.append(data[i][3])
    data_new.append(data[i][4])
    
print(data_new)
