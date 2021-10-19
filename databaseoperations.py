# import psycopg2


def create_table():
    connection = psycopg2.connect(dbname="login", host="localhost", user="postgres", password="mayuresh", port="5432")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE logindata(userid text,password text)''')
    print("Table Created")
    connection.commit()
    connection.close()
    

# def insert_data(userid, password):
    
    # This function adds new data as ID and Password to the database

def searchdata(userid, password):
    connection = psycopg2.connect(dbname="login", host="localhost", user="postgres", password="mayuresh", port="5432")
    cursor = connection.cursor()
    searchquery = '''SELECT * from logindata where userid= %s and password= %s'''
    cursor.execute(searchquery, (userid, password))
    row = cursor.fetchone()
    connection.commit()
    connection.close()
    return row
