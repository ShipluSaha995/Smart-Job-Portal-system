import mysql.connector
def connect():
    return mysql.connector.connect(
        host="local host",
        user="root",
        passwor="",
        database="job_portal"

    )