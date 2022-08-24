def mdown_load():
    
    num =len(shelfs)
    data = [[]]
    i=0
    for i in range(num):
        
        row =[]
        rain=shelfs[i].rain
        row.append(float(rain))
        temp=shelfs[i].temperature
        row.append(float(temp))
        month=shelfs[i].month
        row.append(month)
        date_created = shelfs[i].date_created
        row.append(date_created)
        data.append(row)
        i= i+1
    m_dir = os.getcwd()
    my_dir = str(m_dir + '\data_files')
    file_name_o= str("weather_data.csv")
    fname = os.path.join(my_dir, file_name_o)
    file_o = open(fname,'w',encoding='UTF8')
    writer = csv.writer(file_o)
    writer.writerows(data)
    file_o.close()
    d_ss = str(request.args.get('d_ss')).lower()
    if d_ss =="y":
        response= send_file(fname, as_attachment=True)
        return response
    return render_template('input_search', file= fname)
