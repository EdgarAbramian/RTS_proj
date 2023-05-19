import mysql.connector
import config
# Create the connection object
myconn = mysql.connector.connect(host="localhost", user=config.user, passwd=config.password, database = config.db_name)
# creating the cursor object
cur = myconn.cursor()
sql = "insert into data.game(id,XP) values(%s, %s)"

# The row values are provided in the form of tuple
val = (3,123)

try:
    # inserting the values into the table
    cur.execute(sql, val)

    # commit the transaction
    myconn.commit()

except:
    myconn.rollback()

print(cur.rowcount, "record inserted!")
myconn.close()
