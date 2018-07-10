import pymysql.cursors
import configparser


class InsertIntoPurchases(object):
    def __init__(self, purchased):
        self.purchased = purchased
        self.insert_into_purchases()

    def insert_into_purchases(self):
        dat = configparser.ConfigParser()
        dat.read('reppi.dat')

        host = dat['Mysql']['Host']
        user = dat['Mysql']['User']
        password = dat['Mysql']['Password']

        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     db='reppi',
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            sql = "INSERT INTO purchases (goods, price, created_at) VALUES (%s, %s, now())"
            cursor.executemany(sql, self.purchased)
            connection.commit()

        connection.close()
