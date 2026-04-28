from db import connect
from algorithm import calculate_score, top_k

def apply_job(uid):
    conn=connect()
    cur=conn.cursor()

    job_id=int(input("Job ID: "))
    skills=input("Skills: ")
    exp=int(input("Experience: "))

    cur.execute("SELECT required_skills FROM jobs WHERE job_id=%s",(job_id,))
    job=cur.fetchone()

    if not job:
        print("Invalid job.")
        return 
    score=calculate_score(job[0],skills,exp)

    try:
        cur.execute("""
        INSERT INTO applications(user_id,job_id,skills,experience,score)
        VALUE(%s,%s,%s,%s,%s)
        """,(uid,job_id,skills,exp,score))

        conn.commit()
        print("\n\t\t\t\t*****Applied Successfully.******")
        print("____________________________________________________________________________________________________________________________________________________________\n")
    
    except:
        print("\n\t\t\t\t======Already Applied.=========")
        print("____________________________________________________________________________________________________________________________________________________________\n")
    conn.close()


def view_applicants(job_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    SELECT u.name, u.email, a.skills, a.experience, a.score
    FROM applications a
    JOIN users u ON a.user_id = u.user_id
    WHERE a.job_id = %s
    """, (job_id,))

    data = cur.fetchall()

    print("\nTop Applicants:")
    print("_______________\n")


    if not data:
        print("❌ No applicants have applied for this job yet.\n")
        return

    
    data.sort(key=lambda x: x[4], reverse=True)

    for row in data:
        print("Name:", row[0])
        print("Email:", row[1])
        print("Skills:", row[2])
        print("Experience:", row[3])
        print("Score:", row[4])
        print("____________________________________________________________________________________________________________________________________________________________\n")

    conn.close()
