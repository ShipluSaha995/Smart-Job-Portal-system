import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",   # ✅ no space
        user="root",
        password="!@**Data**1621101##@!",        # ✅ correct spelling
        database="job_portal"
    )