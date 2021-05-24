import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="crud"
)

cursor = db.cursor()
sql = "INSERT INTO `item` (`item_id`, `category`, `title`, `author`, `publisher`, `production`, `copies`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = (2, 'Jurnal', 'Asedese Uhuy', 'Babank Tamvan', 'Gramedd', '2000', '2')

cursor.execute(sql, val)

db.commit()