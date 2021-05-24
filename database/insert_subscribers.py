import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="crud"
)

cursor = db.cursor()
sql = "INSERT INTO `subscriber` (`subscriber_id`, `typ`, `name_subscriber`, `address`, `phone`, `email`) VALUES (%s, %s, %s, %s, %s, %s)"
values = [
  (1, 'Reguler', 'Aryow', 'ryacudu st', '12340987', 'aryow@gmail.com'),
  (2, 'Gold', 'Pusda', 'Kedaton st', '085270603244', 'antarez@gmail.com')
]

for val in values:
  cursor.execute(sql, val)
  db.commit()