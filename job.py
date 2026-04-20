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
        d = dist.get(j[2], 9999)
        travel_cost = d * 5   #5tk per km 
        priority = (j[3] / 1000) - d
        ranked.append((j, priority, travel_cost, d))

    for i in range(len(ranked)):
        for j in range(i+1, len(ranked)):
            if ranked[j][1] > ranked[i][1]:
                ranked[i],ranked[j]=ranked[j],ranked[i]


    print("\nBest Jobs: ")
    print("__________\n")
    
    for job, p, cost, dist_val in ranked:
        print("Job:", job)
        print("Distance:", dist_val, "km")
        print("Travel Cost:", cost, "taka")
        print("Priority:", p)
    
        print("\n")
        print("____________________________________________________________________________________________________________________________________________________________\n")


    conn.close()



def search_by_category():
    conn = connect(); cur = conn.cursor()

    user_loc = input("Your Location: ")
    cat = input("Category: ")

    cur.execute("SELECT job_id,title,location,salary FROM jobs WHERE category=%s",(cat,))
    jobs = cur.fetchall()

    from dijkstra import dijkstra
    from graph import graph

    dist = dijkstra(graph, user_loc)

    ranked = []

    for j in jobs:
        d = dist.get(j[2], 9999)

        travel_cost = d * 5   # cost per km

        priority = (j[3] / 1000) - d

        ranked.append((j, priority, travel_cost, d))

    # sorting
    for i in range(len(ranked)):
        for j in range(i+1, len(ranked)):
            if ranked[j][1] > ranked[i][1]:
                ranked[i], ranked[j] = ranked[j], ranked[i]

    print("\nFiltered Jobs (by Category):")
    print("____________________________")

    for job, p, cost, dist_val in ranked:
        print("\nJob:", job)
        print("Distance:", dist_val, "km")
        print("Travel Cost:", cost, "taka")
        print("Priority:", p)
        print("\n")
        print("____________________________________________________________________________________________________________________________________________________________\n")


    conn.close()