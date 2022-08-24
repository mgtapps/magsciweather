def tots_avgs(data):
    import datetime
    num =len(data)
    date_now= datetime.date.today()
    all_months = ['january','february','march','april','may','june','july','august','september','october','november','december']#'january','febuary','april','may','june','july','august','september','october','november','december'
    d = {"january":31, "february":28, "march":31, "april":30, "may":31, "june":30, "july":31, "august":31, "september":30, "october":31, "november":30, "december":31}
    d_num = {"january":1, "february":2, "march":3, "april":4, "may":5, "june":6, "july":7, "august":8, "september":9, "october":10, "november":11, "december":12}
    d_lp = {"january":31, "february":29, "march":31, "april":30, "may":31, "june":30, "july":31, "august":31, "september":30, "october":31, "november":30, "december":31}
    l_years = [2000,2004,2008,2012,2016,2020,2024,2028,2032,2038,2040,2044,2048]

    year = datetime.date.today().year
    this_month= datetime.date.today().month
    date_now= datetime.date.today()

    result=[]
    for each in all_months:
        i=int(0)
        m_tot=float(0.0)
        for i in range(num):
            date_created =(data[i][2]).year
            #date_created = data[i][2]

            month = data[i][3]
            new_row=[]

            if each == month:
                m_tot= m_tot+ float(data[i][1])

            i=i+1
            if date_created in l_years:
                days= d_lp[each]
            else:
                days = d[each]
            av=m_tot/days
            new_row = [each,m_tot,round(av,2)]


        each_num =d_num[each]
        if each_num <= this_month:
            result.append(new_row)
            
        
    return result, year
