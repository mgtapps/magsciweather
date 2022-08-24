#gets data from table to csv
def down(current_user):

    import psycopg2
    from psycopg2 import sql
    import csv
    from move_file import move

    connection = psycopg2.connect(user="postgres",password="mdms33!",host="127.0.0.1",port="5432",database="magsci_w4")
    cur = connection.cursor()


    #print("PostgreSQL connection is opened")
    #current_id = current_user.id
    stmt = """COPY(SELECT * FROM magsci_data) WHERE owner_id=%s TO STDOUT WITH CSV HEADER;""",[current_user]


    query = sql.SQL(stmt)

    with open('Database_Query.csv', 'w') as file1:
        cur.copy_expert(query, file1)
        connection.commit()



    connection.close()
    move()

#print("PostgreSQL connection is closed")


