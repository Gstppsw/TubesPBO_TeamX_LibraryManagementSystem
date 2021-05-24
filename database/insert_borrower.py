import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="crud"
)

cursor = db.cursor()
sql = "INSERT INTO `borrow` (`sub_id`, `borrowdate`, `itemid`, `returndate`, `fee`) VALUES (%s, %s, %s, %s, %s)"
val = (1, '2021-05-10', '1', '2021-05-23', '3000')

cursor.execute(sql, val)

db.commit()