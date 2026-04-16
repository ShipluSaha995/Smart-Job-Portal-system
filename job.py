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
    conn=connect()
    cur=conn.cursor()
    cur.execute("SELECT * FROM jobs")
    for j in cur.fetchall():
        print(j)
    conn.close()


def search_jobs():
    conn=connect()
    cur=conn.cursor()

    user_loc=input("Your Location: ")
    min_sal=int(input("Minimum Salary: "))

    cur.execute("SELECT job_id, title,location,salary FROM jobs WHERE salary>=%s",(min_sal,))
    jobs=cur.fetchall()

    dist=dijkstra(graph,user_loc)
    ranked=[]
    for j in jobs:
        d=dist.get(j[2],9999)
        priority=d-(j[3]/1000)
        ranked.append(j,priority)

    for i in range(len(ranked)):
        for j in range(i+1, len(ranked)):
            if ranked[j][1]<ranked[i][1]:
                ranked[i],ranked[j]=ranked[j],ranked[i]


    print("\n Best Jobs: ")
    for job, p in ranked:
        print(job, "Priority: ",p)

    conn.close()



def search_by_catagory():
    conn=connect()
    cur=conn.cursor()
    cat=input("Category: ")
    cur.execute("SELECT * FROM jobs WHERE category=%s",(cat,))

    for j in cur.fetchall():
        print(j)
        
    conn.close()
