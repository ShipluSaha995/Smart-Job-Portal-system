from db import connect
from edges import edges
from kruskal import kruskal

def view_all_users():
    conn=connect()
    cur=conn.cursor()
    cur.execute("SELECT user_id,name,email,role FROM users")
    for u in cur.fetchall():
        print(u)
    conn.close()

def view_all_jobs():
    
    conn=connect()
    cur=conn.cursor()

    cur.execute("SELECT * FROM jobs")
    for j in cur.fetchall():
        print(j)
    conn.close()

def view_all_applications():
    conn=connect(); cur=conn.cursor()

    cur.execute("""
    SELECT a.app_id,u.name,j.title,j.company,a.skills,a.experience,a.score
    FROM applications a
    JOIN users u ON a.user_id=u.user_id
    JOIN jobs j ON a.job_id=j.job_id
    """)

    for row in cur.fetchall():
        print(row)

    conn.close()
def dashboard():
    conn=connect()
    cur=conn.cursor()

    cur.execute("SELECT COUNT(*) FROM users")
    u=cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM jobs")
    j=cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM applications")
    a=cur.fetchone()[0]

    print("\n--- DASHBOARD ---")
    print("Users:",u)
    print("Jobs:",j)
    print("Applications:",a)

    conn.close()



def show_mst():
    mst,cost=kruskal(edges)
    print("\nMST:")
    for u,v,w, in mst:
        print(u,"-",v,":",w)
    print("Total Cost: ", cost)
