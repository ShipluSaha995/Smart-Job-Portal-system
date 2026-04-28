import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost", 
        user="root",
        password="!@**Data**1621101##@!",       
        database="job_portal"
    )