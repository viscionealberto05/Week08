from database.DB_connect import DBConnect
from model.parola_DTO import Parola

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def recupera_parole():

        results = []
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                       FROM parola"""
            cursor.execute(query)
            for row in cursor:
                parola = Parola(row["id"], row["nome"])
                #print(parola)
                results.append(parola.nome)
            cursor.close()
            cnx.close()
            return results
