import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class UsuarioModel:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        self.cursor = self.conn.cursor()

    def crear_usuario(self, nombre, apellido, email, password):
        try:
            query = """
                INSERT INTO usuario (nombre, apellido, email, password)
                VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (nombre, apellido, email, password))
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print("Error:", e)
            return False

    def obtener_usuario(self, email):
        query = "SELECT * FROM usuario WHERE email = %s"
        self.cursor.execute(query, (email,))
        return self.cursor.fetchone()