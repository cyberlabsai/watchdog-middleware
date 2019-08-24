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

def updateTweetRead(tweetIds):
    conn = connect()
    cursor = conn.cursor()   
    query =  "UPDATE tweets SET read = true where id in ({ids})".format(ids=', '.join(tweetIds))
    cursor.execute(query)
    conn.commit()
    conn.close()

def getTweets():
    conn = connect()
    cursor = conn.cursor()

    query = "SELECT id, tweet_text, image_status, image_base64, user_name, url FROM tweets  where read='False' order by created_at asc limit 175"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

