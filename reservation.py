import mysql.connector
connexion=mysql.connector.connect(host="localhost",user="LQAdmin",password="lqadmin123")
cursor= connexion.cursor()
cursor.execute("CREATE DATABASE lqadmin_reservation_clients")
cursor.execute("CREATE TABLE id INT AUTO_INCREMENT PRIMARY KEY,")

def heure(time):
    cursor= connexion.cursor()
    sql="INSERT INTO reservation_clients (time)VALUES ('%s')" 
    id(time,)
    cursor.execute(sql, (time))
    connexion.commit()
    cursor.close()
    time= input("Entrer une heure de reservation :")
    heure(time)
    connexion.close()