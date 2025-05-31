import sqlite3

class DB_Manager:
    def __init__(self, database):
        self.database = database

    def __executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()

    def __select_data(self, sql, data = tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()
        
    def city_search(self,name):
        sql = 'SELECT CO FROM a1_tablo WHERE City = ? LIMIT 5'
        res = self.__select_data(sql, (name))
        return res
    
    def NO2(self,name):
        sql = 'SELECT CO2 FROM a1_tablo WHERE City = ? LIMIT 5'
        res = self.__select_data(sql, (name))
        return res
    
    def SO2(self,name):
        sql = 'SELECT SO2 FROM a1_tablo WHERE City = ? LIMIT 5'
        res = self.__select_data(sql, (name))
        return res


    def O3(self,name):
        sql = 'SELECT O2 FROM a1_tablo WHERE City = ? LIMIT 5'
        res = self.__select_data(sql, (name))
        return res
    
