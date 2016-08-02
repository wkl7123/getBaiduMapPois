mysql> desc info;
+-----------+---------------+------+-----+---------+-------+
| Field     | Type          | Null | Key | Default | Extra |
+-----------+---------------+------+-----+---------+-------+
| city_code | varchar(1000) | YES  |     | NULL    |       |
| name      | varchar(1000) | YES  |     | NULL    |       |
| address   | varchar(1000) | YES  |     | NULL    |       |
| phone     | varchar(1000) | YES  |     | NULL    |       |
| x         | varchar(1000) | YES  |     | NULL    |       |
| y         | varchar(1000) | YES  |     | NULL    |       |
+-----------+---------------+------+-----+---------+-------+
6 rows in set (0.00 sec)

mysql> desc city;
+-------+---------------+------+-----+---------+-------+
| Field | Type          | Null | Key | Default | Extra |
+-------+---------------+------+-----+---------+-------+
| name  | varchar(1000) | YES  |     | NULL    |       |
| code  | varchar(1000) | YES  |     | NULL    |       |
+-------+---------------+------+-----+---------+-------+
