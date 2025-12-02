import mysql.connector
# pip install mysql-connector-python

conn = mysql.connector.connect(
    host="myMysql",  # nom du container MySQL (DNS local grâce au réseau)
    user="root",
    password="root",
    database="testdb"
)

cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))") # requete SQL => create table
cursor.execute("INSERT INTO users (name) VALUES ('Toto'), ('Tata')") # requete SQL => insert
conn.commit()

cursor.close()
conn.close()
