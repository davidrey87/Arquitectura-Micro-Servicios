# -*- coding: utf-8 -*-
# !/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------
# Archivo: DataBaseSentiments.py
# Tarea: 2 Arquitecturas Micro Servicios.
# Autor(es): David Reyes, Sandy de la Rosa, Jose Rodriguez, Manuel Peralta
# Version: 1 Octubre 2018
# Descripción:
#
#   Este archivo define el rol de base de datos para un servicio. 
#   Su funcion es almacenar la informacion de cada peticion.
#
#
#
#                                        DataBaseSentiments.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Ofrecer un fichero de|- sqlite3               |
#           |Bse de datos de alma-  |    almacenamiento de    |                        |
#           |cenamiento de informa- |    datos.               |                        |
#           |cion.                  |                         |                        |
#           +-----------------------+-------------------------+------------------------+


import sqlite3
from sqlite3 import Error
 
class DataBaseSentiments(object):
    
    DB_LOCATION = ""
    REQUESTS_TABLE = """ CREATE TABLE IF NOT EXISTS requests (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    title text NOT NULL,
                    request_at text NOT NULL,
                    positive text NOT NULL,
                    negative text NOT NULL,
                    neutral text NOT NULL
                    ); """
    
    def __init__(self):
        """Initialize db class variables"""
        conn = self.create_connection()
        if conn is not None:
            self.create_table(conn, DataBaseSentiments.REQUESTS_TABLE)
        else:
            print("Error! cannot create the database connection.")

    def create_connection(self):
        """ create a database connection to a SQLite database """
        try:
            conn = sqlite3.connect("dbsentiment.sqlite")
            return conn
        except Error as e:
            print(e)
    
        return None

    def create_table(self, conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def create_request(self, conn, request):

        """
        Create a new request into the requests table
        :param conn:
        :param request:
        :return: request id
        """
        sql = ''' INSERT INTO requests(title, request_at, positive, negative, neutral)
                VALUES(?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, request)
        conn.commit()
        return cur.lastrowid