import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="crud"
)

cursor = db.cursor()

sql = """CREATE TABLE `item` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `category` varchar(100) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `author` varchar(100) DEFAULT NULL,
  `publisher` varchar(100) DEFAULT NULL,
  `production` varchar(100) DEFAULT NULL,
  `copies` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""


cursor.execute(sql)
