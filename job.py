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
    print("____________________________________________________________________________________________________________________________________________________________\n")

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
    print("\n")
    print("Posted Jobs: ")
    print("____________\n")
    for j in cur.fetchall():
        print(j)
        print("\n")
    print("\n")
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
        priority = (j[3] / 1000) - d
        ranked.append((j, priority))

    for i in range(len(ranked)):
        for j in range(i+1, len(ranked)):
            if ranked[j][1] > ranked[i][1]:
                ranked[i],ranked[j]=ranked[j],ranked[i]


    print("\nBest Jobs: ")
    print("__________\n")
    
    for job, p in ranked:
        print(job, "Priority: ",p)
    
    print("\n")

    conn.close()



def search_by_catagory():
    conn=connect()
    cur=conn.cursor()
    cat=input("Category: ")
    print("_________\n")
    cur.execute("SELECT * FROM jobs WHERE category=%s",(cat,))

    for j in cur.fetchall():
        print(j)
    print("\n")
        
    conn.close()
