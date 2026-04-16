from db import connect
from graph import graph
from dijkstra import dijkstra

def post_job(emp_id):
    
    conn=connect()
    cur=conn.cursor()

    title=input("Title: ")
    company=input("Company: ")
    location=input("Location: ")
    salary=int(input("Salary: "))
    skills=input("Skills: ")
    category=input("Catagory: ")

    cur.execute(
        """
        INSERT INTO jobs(title,company,location,salary,required_skills,category,employer_id)
        VALUES(%s,%s,%s,%s,%s,%s,%s)
        """, (title, company,location,salary,skills,category,emp_id)
    )

    conn.commit()
    conn.close()




def view_jobs():
    pass
def search_jobs():
    pass
def search_by_catagory():
    pass
