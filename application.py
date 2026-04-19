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
        print("Applied Successfully.")
    
    except:
        print("Already Applied.")
    conn.close()


def view_applicants(job_id):
    
    conn=connect()
    cur=conn.cursor()

    cur.execute("SELECT user_id,score FROM applications WHERE job_id=%s",(job_id,))
    data=cur.fetchall()

    top=top_k(data)

    print("\nTop APplications.\n")
    for t in top:
        print(t)
    conn.close()
