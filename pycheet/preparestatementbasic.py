import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='mycrud',
                                         user='root',
                                         password='')

    cursor = connection.cursor(prepared=True)
    sql_insert_query = """ INSERT INTO User
                       (id, name, fullname, birth) VALUES (%s,%s,%s,%s)"""

    insert_tuple_1 = (100, "Sanogo","Sanogo Souleymane", "2019-03-23")
    insert_tuple_2 = (101, "Koffi","Koffi Serge" ,"2019-05-19")

    cursor.execute(sql_insert_query, insert_tuple_1)
    cursor.execute(sql_insert_query, insert_tuple_2)
    connection.commit()
    print("Data inserted successfully into user table using the prepared statement")

except mysql.connector.Error as error:
    print("parameterized query failed {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")