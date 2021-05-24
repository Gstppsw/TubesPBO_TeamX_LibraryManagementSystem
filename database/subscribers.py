import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="crud"
)

cursor = db.cursor()

sql = """CREATE TABLE `subscriber` (
  `subscriber_id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `typ` varchar(100) DEFAULT NULL,
  `name_subscriber` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""


cursor.execute(sql)
