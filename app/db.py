import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",        # o 127.0.0.1
        user="root",             # tu usuario de MySQL
        password="root",# reemplazá con tu pass
        database="copa_renault"          # nombre de tu base de datos
    )