# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector


# creating database connection
dataBase = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = 'root',
    port = 3306,
    # auth_plugin='mysql_native_password' - used with (pip install mysql-connector)
)
print(dataBase)
# preprare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE django_blog")
print('database created')

