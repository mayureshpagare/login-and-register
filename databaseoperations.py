import psycopg2


# def create_table():
    
    # This function creates a new table in the database


def insert_data(userid, password):
    
    # This function adds new data as ID and Password to the database
    connection = psycopg2.connect(dbname="login", host="localhost", user="postgres", password="mayuresh", port="5432")
    cursor = connection.cursor()
    insert_query = '''INSERT INTO logindata (userid, password) VALUES(%s, %s)'''
    cursor.execute(insert_query, (userid, password))
    connection.commit()
    cursor.close()
    connection.close()

def searchdata(userid, password):
    connection = psycopg2.connect(dbname="login", host="localhost", user="postgres", password="mayuresh", port="5432")
    cursor = connection.cursor()
    searchquery = '''SELECT * from logindata where userid= %s and password= %s'''
    cursor.execute(searchquery, (userid, password))
    row = cursor.fetchone()
    connection.commit()
    connection.close()
    return row
