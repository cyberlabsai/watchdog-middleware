import psycopg2
import os
from os.path import join, dirname
from dotenv import load_dotenv
 
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
 

def connect():
    conn_cl = psycopg2.connect(
           user=os.getenv('DB_USER'),
           password=os.getenv('DB_PASS'),
           host=os.getenv('DB_HOST'),
           port=os.getenv('DB_PORT'),
           dbname=os.getenv('DB_NAME')
       )
    return conn_cl

def updateTweetRead(tweetId):
    conn = connect()
    cursor = conn.cursor()   

    query =  "UPDATE tweets SET flag = (%s) where id = {tweetId}"
    data = (True)

    cursor.execute(query, data)
    conn.commit()