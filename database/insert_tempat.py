import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="crud"
)

cursor = db.cursor()
sql = "INSERT INTO `tempat` (`id`, `name`) VALUES (%s, %s)"
values = [
   (1, 'Perpustakaan Gedung Eeeeee 10'),
   (3, 'Perpus Nas'),
   (5, 'Pusda2'),
   (6, 'PERPUS GKU')
]

for val in values:
  cursor.execute(sql, val)
  db.commit()
