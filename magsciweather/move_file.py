#moving a csv file to a new directory
def move():


    import csv
    import os



    file_name = str("Database_Query.csv")

    file_d = open('Database_Query.csv','r',encoding='UTF8')
    csv_reader = csv.reader(file_d)
    #print(csv_reader)
    data = []
    for line in csv_reader:
        data.append(line)
    #print("data",data)
    m_dir = os.getcwd()
    my_dir = str(m_dir + '\data_files')
    file_name_o= str("Database_Query_o.csv")
    fname = os.path.join(my_dir, file_name_o)
    file_o = open(fname,'w',encoding='UTF8')
    writer = csv.writer(file_o)
    writer.writerows(data)



    file_d.close()
    file_o.close()


