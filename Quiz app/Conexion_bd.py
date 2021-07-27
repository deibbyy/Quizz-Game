import sqlite3 
from sqlite3.dbapi2 import connect

class preguntas:
    def leerPreguntas(self):
        # Hacemos la conexion
        conexion=sqlite3.connect('BD_Preguntas.s3db')
        # Le decimos que los caracteres extraños que marquen errores los ignore
        conexion.text_factory=lambda b: b.decode(errors='ignore')
        #print("Conexion lograda")
        # Creamos el cursor
        cursorObj = conexion.cursor()
        cursorObj.execute('SELECT * FROM Preguntas')
        return cursorObj.fetchall()


