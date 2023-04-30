#!/usr/bin/python
# coding=utf-8


##############################################################################
__author__ = "Jason A. Arter"
__date__ = "2023-04-28"
__copyright__ = ""
__credits__ = ["Jason A. Arter"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Jason A. Arter"
__email__ = "jason.arter@gmail.com"
__status__ = "Prototype"
__updated__ = "2023-04-28"
__python_version__ = "3.11"
##############################################################################


from dotenv import dotenv_values
import pymysql as ms


def create_db():
    config = dotenv_values(".env")
    conn = ms.connect(host='localhost',
                      user=config["DB_USER"],
                      password=config["DB_PASSWORD"],
                      autocommit=True)
    my_cursor = conn.cursor()
    statement = f""