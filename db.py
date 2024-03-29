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
    data = ('True')
    cursor.execute(query, data)

def getTweets(limit = 175):
    conn = connect()
    cursor = conn.cursor()

    query = "SELECT id, tweet_text, image, image_url, user_name FROM tweets  where flag='False' order by created_at asc limit 175"
    cursor.execute(query)
    results = cursor.fetchall()
    return results

