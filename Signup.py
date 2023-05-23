import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="LQAdmin",
  passwd="lqadmin123"
)

# Create a cursor object
mycursor = mydb.cursor()

#Creation de la base de donnees
mycursor.execute("CREATE DATABASE lqadmin_form_inscription")


mycursor.execute("CREATE TABLE clients(id INT AUTO_INCREMENT PRIMARY KEY, lastname VARCHAR(25),firstname VARCHAR(25), address VARCHAR(50), zip_code BIGINT(5),city VARCHAR(40), userVARCHAR(30),email VARCHAR(30), passwordVARCHAR(15)")

# Validation HTML
def validate_form(form_inscription):
    errors = []
    if len(form_inscription['name']) == 0:
        errors.append('Le nom est requit')
    if len(form_inscription['lastname']) == 0:
        errors.append('le prenom est requit')
    if len(form_inscription['email']) == 0:
        errors.append('l\'email est requit')
    if len (form_inscription['user']) == 0:
        errors.append('l\'user est requit')
    if len(form_inscription['password'])==0:
        errors.append('le mot de passe est requit')
    return errors

# Insere les donnees dans la table
def insert_data(form_inscription):
    sql = "INSERT INTO clients (lastname,firstname, address, zip_code, city, email, user, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (form_inscription['firstname'], form_inscription['lastname'], form_inscription['adress'], form_inscription['zip_code'],form_inscription['city'], form_inscription['email'], form_inscription['user'], form_inscription['password'])
    mycursor.execute(sql, val)
    mydb.commit()