import mysql.connector
from config import * 
def connect_db():
    connection = mysql.connector.connect(
      host = HOST,
      port = PORT,
      user = USER,
      password = PASSWORD,
      database = DATABASE

    )

    return connection