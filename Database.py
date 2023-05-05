
import mysql.connector
import configparser


class Connection:
    def __init__(self):
       config = configparser.ConfigParser()
       config.read('config.ini')
       self.cnx = mysql.connector.connect(user=config['mysql']['user'], password=config['mysql']['password'],
                                host=config['mysql']['host'],
                                database=config['mysql']['database'])

       self.cursor = self.cnx.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.cnx.commit()
        self.cnx.close()

    @staticmethod
    def get_all_cars():
        query = "SELECT matricule,v_model,v_image,voiture_cat FROM voiture WHERE v_flag = 0"
        with Connection() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result
    
    @staticmethod
    def get_car_price(matricule):
        query = "SELECT prix_jour FROM voiture_categorie WHERE voiture_cat = (SELECT voiture_cat FROM voiture WHERE matricule = %s)"
        with Connection() as cursor:
            cursor.execute(query, (matricule,))
            result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
        
    @staticmethod
    def get_reserved_cars():
        query = "SELECT matricule,v_model,v_image,voiture_cat FROM voiture WHERE v_flag = 1"
        with Connection() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result
    
    @staticmethod
    def set_car_reserved(matricule):
        query = "UPDATE voiture SET v_flag = 1 WHERE matricule = %s"
        with Connection() as cursor:
            cursor.execute(query, (matricule,))