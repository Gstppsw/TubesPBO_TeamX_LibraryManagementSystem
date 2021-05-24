import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="crud"
)

cursor = db.cursor()

sql ="""CREATE TABLE `borrow` (
  `sub_id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `borrowdate` varchar(100) DEFAULT NULL,
  `itemid` varchar(100) DEFAULT NULL,
  `returndate` varchar(100) DEFAULT NULL,
  `fee` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

cursor.execute(sql)
