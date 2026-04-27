from db import connect
from graph import graph
from dijkstra import dijkstra


def post_job(emp_id):
    conn = connect()
    cur = conn.cursor()

    title = input("Title: ")
    company = input("Company: ")
    location = input("Location: ").strip().title()   # ✅ FIXED
    salary = int(input("Salary: "))
    skills = input("Skills: ")
    category = input("Category: ")

    print("____________________________________________________________________________________________________________________________________________________________\n")

    cur.execute("""
        INSERT INTO jobs(title,company,location,salary,required_skills,category,employer_id)
        VALUES(%s,%s,%s,%s,%s,%s,%s)
    """, (title, company, location, salary, skills, category, emp_id))

    conn.commit()
    conn.close()


def view_jobs():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM jobs")

    print("\nPosted Jobs:")
    print("____________\n")

    for j in cur.fetchall():
        print(j, "\n")

    conn.close()



def search_jobs():
    conn = connect()
    cur = conn.cursor()

    user_loc = input("Your Location: ").strip().title()   # ✅ FIXED

    # ✅ Validate location
    if user_loc not in graph:
        print("❌ Invalid location! Use: Dhaka, Gazipur, Narayanganj, Comilla")
        return

    min_sal = int(input("Minimum Salary: "))

    cur.execute("SELECT job_id, title, location, salary FROM jobs WHERE salary >= %s", (min_sal,))
    jobs = cur.fetchall()

    dist = dijkstra(graph, user_loc)

    ranked = []

    for j in jobs:
        job_location = j[2].strip().title()   # ✅ FIXED

        d = dist.get(job_location, 9999)

        travel_cost = d * 5
        priority = (j[3] / 1000) - d

        ranked.append((j, priority, travel_cost, d))


    for i in range(len(ranked)):
        for j in range(i + 1, len(ranked)):
            if ranked[j][1] > ranked[i][1]:
                ranked[i], ranked[j] = ranked[j], ranked[i]

    print("\nBest Jobs:")
    print("__________\n")

    for job, p, cost, dist_val in ranked:
        print("Job:", job)
        print("Distance:", dist_val, "km")
        print("Travel Cost:", cost, "taka")
        print("Priority:", p)
        print("____________________________________________________________________________________________________________________________________________________________\n")

    conn.close()


def search_by_category():
    conn = connect()
    cur = conn.cursor()

    user_loc = input("Your Location: ").strip().title()   # ✅ FIXED

    # ✅ Validate location
    if user_loc not in graph:
        print("❌ Invalid location! Use: Dhaka, Gazipur, Narayanganj, Comilla")
        return

    cat = input("Category: ")

    cur.execute("SELECT job_id, title, location, salary FROM jobs WHERE category = %s", (cat,))
    jobs = cur.fetchall()

    dist = dijkstra(graph, user_loc)

    ranked = []

    for j in jobs:
        job_location = j[2].strip().title()   # ✅ FIXED

        d = dist.get(job_location, 9999)

        travel_cost = d * 5
        priority = (j[3] / 1000) - d

        ranked.append((j, priority, travel_cost, d))

    
    for i in range(len(ranked)):
        for j in range(i + 1, len(ranked)):
            if ranked[j][1] > ranked[i][1]:
                ranked[i], ranked[j] = ranked[j], ranked[i]

    print("\nFiltered Jobs (by Category):")
    print("____________________________\n")

    for job, p, cost, dist_val in ranked:
        print("Job:", job)
        print("Distance:", dist_val, "km")
        print("Travel Cost:", cost, "taka")
        print("Priority:", p)
        print("____________________________________________________________________________________________________________________________________________________________\n")

    conn.close()